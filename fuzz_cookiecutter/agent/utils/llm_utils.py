from __future__ import annotations

from collections import Counter
from pathlib import Path

from fuzz_cookiecutter.agent.models import BatchRunResult, CoverageSummary, TestResult
from fuzz_cookiecutter.agent.utils.coverage_utils import top_missing_hotspots


COOKIECUTTER_REACHABILITY_GUIDE = """
cookiecutter/prompt.py
- Reach with string, bool, choice-list, dict, __prompts__, and nested templates.
- Favor cases that mix no_input=False with default-driven answers.

cookiecutter/generate.py
- Reach with _copy_without_render, _new_lines, binary files, rendered paths, and output collisions.
- Favor cases that vary overwrite_if_exists and skip_if_file_exists.

cookiecutter/hooks.py
- Reach with no hooks, successful hooks, and failing hooks.
- Favor pre_gen_project and post_gen_project scripts.

cookiecutter/main.py and cookiecutter/cli.py
- Reach with both cli and api modes, replay-driven runs, and keep_project_on_failure.

cookiecutter/replay.py
- Reach with replay payloads that partially satisfy the current template context.
""".strip()


def format_results_summary(results: list[TestResult]) -> str:
    counts = Counter(result.status for result in results)
    lines = ["Result counts:"]
    for status, count in sorted(counts.items()):
        lines.append(f"- {status}: {count}")
    interesting = [
        result
        for result in results
        if result.status != "SUCCESS" or result.exception_type
    ][:5]
    if interesting:
        lines.append("Representative cases:")
        for result in interesting:
            lines.append(
                f"- {result.case_id}: {result.status} mode={result.execution_mode} "
                f"exception={result.exception_type or 'none'} phase={result.hook_phase_reached or 'n/a'}"
            )
    return "\n".join(lines)


def format_coverage_summary(summary: CoverageSummary) -> str:
    return (
        f"Coverage totals: {summary.covered_lines}/{summary.num_statements} lines, "
        f"{summary.covered_branches}/{summary.num_branches} branches, "
        f"{summary.percent_covered:.2f}% overall."
    )


def format_missing_hotspots(summary: CoverageSummary, *, limit: int = 5) -> str:
    hotspots = top_missing_hotspots(summary, limit=limit)
    if not hotspots:
        return "No missing-line hotspots were captured."
    lines = ["Top hotspots:"]
    for file_summary in hotspots:
        preview = ", ".join(str(line) for line in file_summary.missing_lines[:8])
        lines.append(
            f"- {file_summary.path}: {len(file_summary.missing_lines)} missing lines "
            f"({preview})"
        )
    return "\n".join(lines)


def format_missing_line_context(
    repo_root: Path, summary: CoverageSummary, *, limit: int = 5
) -> str:
    snippets: list[str] = []
    for file_summary in top_missing_hotspots(summary, limit=limit):
        source_path = Path(file_summary.path)
        if not source_path.is_absolute():
            candidate = (repo_root / source_path).resolve()
            if candidate.exists():
                source_path = candidate
        if not source_path.exists() or not file_summary.missing_lines:
            continue
        source_lines = source_path.read_text(encoding="utf-8").splitlines()
        for missing_line in file_summary.missing_lines[:3]:
            start = max(1, missing_line - 1)
            end = min(len(source_lines), missing_line + 1)
            excerpt = "\n".join(
                f"{line_no}: {source_lines[line_no - 1]}"
                for line_no in range(start, end + 1)
            )
            snippets.append(f"{file_summary.path}:{missing_line}\n{excerpt}")
    return "\n\n".join(snippets) if snippets else "No source excerpts available."


def format_iteration_history(history: list[BatchRunResult]) -> str:
    if not history:
        return "No prior iterations."
    lines = []
    for batch in history:
        lines.append(
            f"- {batch.label}: {batch.coverage_summary.percent_covered:.2f}% "
            f"({len(batch.results)} cases)"
        )
    return "\n".join(lines)

