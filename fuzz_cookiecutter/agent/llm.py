from __future__ import annotations

from pathlib import Path

from fuzz_cookiecutter.agent.core.config import FuzzerConfig
from fuzz_cookiecutter.agent.core.llm_client import BaseLLMClient
from fuzz_cookiecutter.agent.models import (
    BatchRunResult,
    LLMCallResult,
    MutationPlan,
    PlannerOutput,
)
from fuzz_cookiecutter.agent.prompts.prompt import load_prompt
from fuzz_cookiecutter.agent.utils.llm_utils import (
    COOKIECUTTER_REACHABILITY_GUIDE,
    format_coverage_summary,
    format_iteration_history,
    format_missing_hotspots,
    format_missing_line_context,
    format_results_summary,
)
from fuzz_cookiecutter.agent.utils.monitoring import trace
from fuzz_cookiecutter.agent.validator import (
    PROTECTED_RULES,
    editable_rules,
    extract_grammar_declaration,
    parse_json_response,
    protected_rule_context,
)


def _render_prompt(template: str, values: dict[str, object]) -> str:
    trace("llm", "rendering prompt template", placeholder_count=len(values))
    rendered = template
    for key, value in values.items():
        rendered = rendered.replace("{" + key + "}", str(value))
    trace("llm", "prompt template rendered")
    return rendered


def _write_prompt_and_output(
    run_dir: Path,
    *,
    prompt_name: str,
    prompt_text: str,
    raw_output: str,
    provider: str,
) -> LLMCallResult:
    run_dir.mkdir(parents=True, exist_ok=True)
    trace("llm", "writing prompt and raw output artifacts", run_dir=run_dir, prompt_name=prompt_name, provider=provider)
    prompt_path = run_dir / f"{prompt_name}.prompt.md"
    output_path = run_dir / f"{prompt_name}.output.json"
    prompt_path.write_text(prompt_text, encoding="utf-8")
    output_path.write_text(raw_output, encoding="utf-8")
    parsed = parse_json_response(raw_output)
    trace("llm", "parsed llm JSON output", prompt_name=prompt_name, output_path=output_path)
    return LLMCallResult(
        prompt_path=prompt_path,
        output_path=output_path,
        raw_text=raw_output,
        parsed_json=parsed,
        provider=provider,
    )


def run_planner(
    config: FuzzerConfig,
    client: BaseLLMClient,
    *,
    run_dir: Path,
    grammar_text: str,
    champion: BatchRunResult,
    validation_feedback: str,
    history: list[BatchRunResult],
) -> tuple[PlannerOutput, LLMCallResult]:
    trace("llm", "starting planner call", run_dir=run_dir)
    prompt_template = load_prompt("planner_agent.md")
    prompt_text = _render_prompt(
        prompt_template,
        {
            "grammar_declaration": extract_grammar_declaration(grammar_text),
            "protected_rules": ", ".join(PROTECTED_RULES),
            "protected_rule_context": protected_rule_context(grammar_text),
            "editable_rules": ", ".join(editable_rules(grammar_text)),
            "current_grammar": grammar_text,
            "codebase_reachability_guide": COOKIECUTTER_REACHABILITY_GUIDE,
            "results_summary": format_results_summary(champion.results),
            "coverage_summary": format_coverage_summary(champion.coverage_summary),
            "missing_hotspots": format_missing_hotspots(champion.coverage_summary),
            "missing_line_context": format_missing_line_context(
                config.repo_root, champion.coverage_summary
            ),
            "validation_feedback": validation_feedback or "None",
            "iteration_history": format_iteration_history(history),
        },
    )
    response = client.complete(prompt_text, "planner")
    trace("llm", "planner response received", provider=response.provider, response_length=len(response.text))
    call_result = _write_prompt_and_output(
        run_dir,
        prompt_name="planner",
        prompt_text=prompt_text,
        raw_output=response.text,
        provider=response.provider,
    )
    trace("llm", "planner output structured", recommendations=len(call_result.parsed_json.get("recommended_rule_edits", [])))
    return PlannerOutput.from_dict(call_result.parsed_json), call_result


def run_rewriter(
    client: BaseLLMClient,
    *,
    run_dir: Path,
    grammar_text: str,
    planner_output: PlannerOutput,
) -> tuple[MutationPlan, LLMCallResult]:
    trace("llm", "starting rewriter call", run_dir=run_dir)
    prompt_template = load_prompt("coder_agent.md")
    prompt_text = _render_prompt(
        prompt_template,
        {
            "grammar_declaration": extract_grammar_declaration(grammar_text),
            "protected_rules": ", ".join(PROTECTED_RULES),
            "protected_rule_context": protected_rule_context(grammar_text),
            "editable_rules": ", ".join(editable_rules(grammar_text)),
            "current_grammar": grammar_text,
            "codebase_reachability_guide": COOKIECUTTER_REACHABILITY_GUIDE,
            "planner_output": planner_output,
        },
    )
    response = client.complete(prompt_text, "rewriter")
    trace("llm", "rewriter response received", provider=response.provider, response_length=len(response.text))
    call_result = _write_prompt_and_output(
        run_dir,
        prompt_name="rewriter",
        prompt_text=prompt_text,
        raw_output=response.text,
        provider=response.provider,
    )
    trace("llm", "rewriter output structured", updates=len(call_result.parsed_json.get("updates", [])))
    return MutationPlan.from_dict(call_result.parsed_json), call_result
