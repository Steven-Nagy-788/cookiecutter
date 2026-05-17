from __future__ import annotations

import json
from pathlib import Path

from fuzz_cookiecutter.agent.core.config import FuzzerConfig
from fuzz_cookiecutter.agent.models import CoverageSummary, FileCoverageSummary
from fuzz_cookiecutter.agent.utils.cli_utils import run_command


def combine_and_export_coverage(
    config: FuzzerConfig, coverage_dir: Path, output_json: Path
) -> Path | None:
    coverage_files = list(coverage_dir.glob(".coverage*"))
    if not coverage_files:
        return None
    combine = run_command(
        ["python", "-m", "coverage", "combine", str(coverage_dir)],
        cwd=config.repo_root,
        env={"COVERAGE_FILE": str(coverage_dir / ".coverage")},
    )
    if combine.returncode != 0:
        msg = combine.stderr.strip() or combine.stdout.strip() or "unknown error"
        raise RuntimeError(f"coverage combine failed: {msg}")
    export = run_command(
        ["python", "-m", "coverage", "json", "-o", str(output_json)],
        cwd=config.repo_root,
        env={"COVERAGE_FILE": str(coverage_dir / ".coverage")},
    )
    if export.returncode != 0:
        msg = export.stderr.strip() or export.stdout.strip() or "unknown error"
        raise RuntimeError(f"coverage json export failed: {msg}")
    return output_json


def summarize_coverage(coverage_json: Path | None) -> CoverageSummary:
    if coverage_json is None or not coverage_json.exists():
        return CoverageSummary(
            covered_lines=0,
            num_statements=0,
            covered_branches=0,
            num_branches=0,
            percent_covered=0.0,
            files=[],
        )

    payload = json.loads(coverage_json.read_text(encoding="utf-8"))
    files: list[FileCoverageSummary] = []
    for path, details in sorted(payload.get("files", {}).items()):
        summary = details.get("summary", {})
        files.append(
            FileCoverageSummary(
                path=path,
                covered_lines=int(summary.get("covered_lines", 0)),
                num_statements=int(summary.get("num_statements", 0)),
                missing_lines=list(details.get("missing_lines", [])),
                percent_covered=float(summary.get("percent_covered", 0.0)),
            )
        )

    totals = payload.get("totals", {})
    return CoverageSummary(
        covered_lines=int(totals.get("covered_lines", 0)),
        num_statements=int(totals.get("num_statements", 0)),
        covered_branches=int(totals.get("covered_branches", 0)),
        num_branches=int(totals.get("num_branches", 0)),
        percent_covered=float(totals.get("percent_covered", 0.0)),
        files=files,
    )


def top_missing_hotspots(summary: CoverageSummary, *, limit: int = 5) -> list[FileCoverageSummary]:
    ordered = sorted(summary.files, key=lambda item: (-len(item.missing_lines), item.path))
    return ordered[:limit]
