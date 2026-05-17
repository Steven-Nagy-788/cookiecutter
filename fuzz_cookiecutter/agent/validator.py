from __future__ import annotations

import json
import re
from dataclasses import dataclass

from fuzz_cookiecutter.agent.core.config import FuzzerConfig
from fuzz_cookiecutter.agent.models import MutationPlan, ValidationResult
from fuzz_cookiecutter.agent.utils.grammarinator_utils import compile_candidate_smoke
from fuzz_cookiecutter.agent.utils.monitoring import trace

PROTECTED_RULES = [
    "case_file",
    "case_object",
    "execution_mode",
    "template_source",
    "template_object",
    "invocation_object",
]


@dataclass(slots=True)
class RuleSpan:
    name: str
    start: int
    end: int
    text: str


def _strip_fences(text: str) -> str:
    fenced = re.search(r"```(?:json)?\s*(.*?)```", text, re.DOTALL)
    return fenced.group(1).strip() if fenced else text.strip()


def parse_json_response(raw_text: str) -> dict:
    trace("validator", "parsing JSON response")
    cleaned = _strip_fences(raw_text)
    start = cleaned.find("{")
    end = cleaned.rfind("}")
    if start == -1 or end == -1 or end < start:
        raise ValueError("Response did not contain a JSON object")
    return json.loads(cleaned[start : end + 1])


def extract_grammar_declaration(grammar_text: str) -> str:
    trace("validator", "extracting grammar declaration")
    match = re.search(r"grammar\s+([A-Za-z_][A-Za-z0-9_]*)\s*;", grammar_text)
    if not match:
        raise ValueError("Grammar declaration not found")
    return match.group(0)


def extract_rule_spans(grammar_text: str) -> dict[str, RuleSpan]:
    trace("validator", "extracting rule spans from grammar")
    lines = grammar_text.splitlines(keepends=True)
    offsets: list[int] = []
    current_offset = 0
    for line in lines:
        offsets.append(current_offset)
        current_offset += len(line)

    spans: dict[str, RuleSpan] = {}
    index = 0
    while index < len(lines):
        stripped = lines[index].strip()
        if re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*", stripped):
            if index + 1 < len(lines) and lines[index + 1].lstrip().startswith(":"):
                start = offsets[index]
                name = stripped
                end_index = index + 1
                while end_index < len(lines) and lines[end_index].strip() != ";":
                    end_index += 1
                if end_index >= len(lines):
                    raise ValueError(f"Rule {name} did not terminate with ';'")
                end = offsets[end_index] + len(lines[end_index])
                spans[name] = RuleSpan(
                    name=name,
                    start=start,
                    end=end,
                    text=grammar_text[start:end],
                )
                index = end_index + 1
                continue
        index += 1
    return spans


def editable_rules(grammar_text: str) -> list[str]:
    trace("validator", "listing editable rules")
    rules = [
        name
        for name in extract_rule_spans(grammar_text)
        if name not in PROTECTED_RULES
    ]
    return sorted(rules)


def protected_rule_context(grammar_text: str) -> str:
    trace("validator", "building protected rule context")
    spans = extract_rule_spans(grammar_text)
    return "\n\n".join(spans[name].text.rstrip() for name in PROTECTED_RULES if name in spans)


def _replacement_rule_name(replacement: str) -> str | None:
    for line in replacement.splitlines():
        stripped = line.strip()
        if stripped:
            return stripped if re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*", stripped) else None
    return None


def apply_mutation_plan(grammar_text: str, plan: MutationPlan) -> str:
    trace("validator", "applying mutation plan", update_count=len(plan.updates))
    spans = extract_rule_spans(grammar_text)
    updated_text = grammar_text
    ordered_spans = sorted(
        (spans[update.rule] for update in plan.updates),
        key=lambda item: item.start,
        reverse=True,
    )
    replacements = {update.rule: update.replacement.rstrip() + "\n" for update in plan.updates}
    for span in ordered_spans:
        updated_text = (
            updated_text[: span.start]
            + replacements[span.name]
            + updated_text[span.end :]
        )
    return updated_text


def validate_mutation_response(
    config: FuzzerConfig, grammar_text: str, raw_text: str
) -> ValidationResult:
    trace("validator", "validating mutation response")
    try:
        payload = parse_json_response(raw_text)
        plan = MutationPlan.from_dict(payload)
    except Exception as exc:  # noqa: BLE001
        trace("validator", "mutation response JSON parsing failed", error=exc)
        return ValidationResult(ok=False, feedback=f"Could not parse mutation plan JSON: {exc}")

    if not plan.updates:
        trace("validator", "mutation response contained no updates")
        return ValidationResult(ok=False, feedback="Mutation plan did not include any rule updates")
    if len(plan.updates) > 3:
        trace("validator", "mutation response exceeded update limit", update_count=len(plan.updates))
        return ValidationResult(ok=False, feedback="Mutation plan updated more than 3 rules")

    seen: set[str] = set()
    spans = extract_rule_spans(grammar_text)
    for update in plan.updates:
        if update.rule in seen:
            trace("validator", "duplicate rule update rejected", rule=update.rule)
            return ValidationResult(ok=False, feedback=f"Duplicate update for rule {update.rule}")
        seen.add(update.rule)
        if update.rule not in spans:
            trace("validator", "unknown rule update rejected", rule=update.rule)
            return ValidationResult(ok=False, feedback=f"Unknown rule {update.rule}")
        if update.rule in PROTECTED_RULES:
            trace("validator", "protected rule update rejected", rule=update.rule)
            return ValidationResult(ok=False, feedback=f"Protected rule {update.rule} cannot be modified")
        if ";" not in update.replacement:
            trace("validator", "unterminated replacement rejected", rule=update.rule)
            return ValidationResult(ok=False, feedback=f"Replacement for {update.rule} did not terminate with ';'")
        replacement_name = _replacement_rule_name(update.replacement)
        if replacement_name != update.rule:
            trace("validator", "replacement header mismatch rejected", rule=update.rule, replacement_name=replacement_name)
            return ValidationResult(
                ok=False,
                feedback=f"Replacement block for {update.rule} must start with the same rule name",
            )

    candidate = apply_mutation_plan(grammar_text, plan)
    if extract_grammar_declaration(candidate) != extract_grammar_declaration(grammar_text):
        trace("validator", "grammar declaration changed unexpectedly")
        return ValidationResult(ok=False, feedback="Grammar declaration changed unexpectedly")

    smoke_ok, smoke_feedback = compile_candidate_smoke(config, candidate)
    if not smoke_ok:
        trace("validator", "candidate smoke validation failed", feedback=smoke_feedback)
        return ValidationResult(ok=False, feedback=smoke_feedback)
    trace("validator", "mutation response accepted")
    return ValidationResult(ok=True, feedback="ok", candidate_grammar=candidate)
