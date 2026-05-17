from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from fuzz_cookiecutter.agent.models import CoverageSummary, TestResult


def write_json(path: Path, payload: Any) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")
    return path


def write_text(path: Path, contents: str) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(contents, encoding="utf-8")
    return path


def results_to_markdown(results: list[TestResult], coverage: CoverageSummary) -> str:
    lines = [
        "# Batch Results",
        "",
        f"- Cases: {len(results)}",
        f"- Coverage: {coverage.percent_covered:.2f}%",
        f"- Covered lines: {coverage.covered_lines}/{coverage.num_statements}",
        f"- Covered branches: {coverage.covered_branches}/{coverage.num_branches}",
        "",
        "| Case | Status | Mode | Exit | Exception | Phase | Files |",
        "| --- | --- | --- | --- | --- | --- | --- |",
    ]
    for result in results:
        lines.append(
            "| {case} | {status} | {mode} | {exit_code} | {exc} | {phase} | {files} |".format(
                case=result.case_id,
                status=result.status,
                mode=result.execution_mode,
                exit_code=result.exit_code if result.exit_code is not None else "",
                exc=result.exception_type or "",
                phase=result.hook_phase_reached or "",
                files=result.file_count_created,
            )
        )
    return "\n".join(lines) + "\n"


def write_finding(path: Path, title: str, details: dict[str, Any]) -> Path:
    payload = {"title": title, "details": details}
    return write_json(path, payload)

