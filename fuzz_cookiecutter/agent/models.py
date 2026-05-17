from __future__ import annotations

from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any


@dataclass(slots=True)
class InvocationConfig:
    no_input: bool
    extra_context: dict[str, Any]
    replay: dict[str, Any] | None
    overwrite_if_exists: bool
    skip_if_file_exists: bool
    accept_hooks: bool
    keep_project_on_failure: bool
    output_dir_state: str


@dataclass(slots=True)
class ManifestExecutionSpec:
    case_id: str
    manifest_path: Path
    workspace_dir: Path
    template_repo_dir: Path
    output_dir: Path
    predicted_project_dir: Path
    mode: str
    template_source: str
    invocation: InvocationConfig
    replay_file: Path | None = None
    notes: dict[str, Any] = field(default_factory=dict)

    def to_payload(self) -> dict[str, Any]:
        payload = asdict(self)
        for key in (
            "manifest_path",
            "workspace_dir",
            "template_repo_dir",
            "output_dir",
            "predicted_project_dir",
            "replay_file",
        ):
            value = payload[key]
            payload[key] = None if value is None else str(value)
        return payload


@dataclass(slots=True)
class TestResult:
    __test__ = False

    case_id: str
    status: str
    manifest_path: str
    execution_mode: str
    exit_code: int | None
    exception_type: str | None
    exception_message: str | None
    stdout_excerpt: str
    stderr_excerpt: str
    hook_phase_reached: str | None
    materialization_status: str
    generated_project_path: str | None
    file_count_created: int
    duration_ms: int
    details: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(slots=True)
class FileCoverageSummary:
    path: str
    covered_lines: int
    num_statements: int
    missing_lines: list[int]
    percent_covered: float


@dataclass(slots=True)
class CoverageSummary:
    covered_lines: int
    num_statements: int
    covered_branches: int
    num_branches: int
    percent_covered: float
    files: list[FileCoverageSummary] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return {
            "covered_lines": self.covered_lines,
            "num_statements": self.num_statements,
            "covered_branches": self.covered_branches,
            "num_branches": self.num_branches,
            "percent_covered": self.percent_covered,
            "files": [asdict(item) for item in self.files],
        }


@dataclass(slots=True)
class BatchRunResult:
    label: str
    run_dir: Path
    grammar_text: str
    manifests: list[Path]
    results: list[TestResult]
    coverage_json: Path | None
    coverage_summary: CoverageSummary
    results_json: Path
    results_markdown: Path
    notes: dict[str, Any] = field(default_factory=dict)


@dataclass(slots=True)
class RuleUpdate:
    rule: str
    replacement: str


@dataclass(slots=True)
class PlannerOutput:
    analysis: str
    overrepresented_responses: list[str]
    underexplored_scenario_families: list[str]
    reachable_by_grammar: list[str]
    reachable_by_harness_only: list[str]
    unreachable_harness_limits: list[str]
    line_target_hints: list[dict[str, Any]]
    recommended_rule_edits: list[dict[str, str]]

    @classmethod
    def from_dict(cls, payload: dict[str, Any]) -> "PlannerOutput":
        return cls(
            analysis=payload.get("analysis", ""),
            overrepresented_responses=list(payload.get("overrepresented_responses", [])),
            underexplored_scenario_families=list(
                payload.get("underexplored_scenario_families", [])
            ),
            reachable_by_grammar=list(payload.get("reachable_by_grammar", [])),
            reachable_by_harness_only=list(payload.get("reachable_by_harness_only", [])),
            unreachable_harness_limits=list(payload.get("unreachable_harness_limits", [])),
            line_target_hints=list(payload.get("line_target_hints", [])),
            recommended_rule_edits=list(payload.get("recommended_rule_edits", [])),
        )


@dataclass(slots=True)
class MutationPlan:
    rationale: str
    updates: list[RuleUpdate]

    @classmethod
    def from_dict(cls, payload: dict[str, Any]) -> "MutationPlan":
        updates = [
            RuleUpdate(rule=item["rule"], replacement=item["replacement"])
            for item in payload.get("updates", [])
        ]
        return cls(rationale=payload.get("rationale", ""), updates=updates)


@dataclass(slots=True)
class LLMCallResult:
    prompt_path: Path
    output_path: Path
    raw_text: str
    parsed_json: dict[str, Any]
    provider: str


@dataclass(slots=True)
class ValidationResult:
    ok: bool
    feedback: str
    candidate_grammar: str | None = None
