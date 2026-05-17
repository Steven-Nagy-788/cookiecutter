from __future__ import annotations

from dataclasses import dataclass

from fuzz_cookiecutter.agent.models import CoverageSummary


@dataclass(slots=True)
class CoverageDelta:
    line_delta: int
    branch_delta: int
    percent_delta: float
    candidate_is_at_least_as_good: bool


def compare_coverage(
    baseline: CoverageSummary, candidate: CoverageSummary
) -> CoverageDelta:
    line_delta = candidate.covered_lines - baseline.covered_lines
    branch_delta = candidate.covered_branches - baseline.covered_branches
    percent_delta = candidate.percent_covered - baseline.percent_covered
    at_least_as_good = (
        candidate.covered_lines,
        candidate.covered_branches,
        candidate.percent_covered,
    ) >= (
        baseline.covered_lines,
        baseline.covered_branches,
        baseline.percent_covered,
    )
    return CoverageDelta(
        line_delta=line_delta,
        branch_delta=branch_delta,
        percent_delta=percent_delta,
        candidate_is_at_least_as_good=at_least_as_good,
    )

