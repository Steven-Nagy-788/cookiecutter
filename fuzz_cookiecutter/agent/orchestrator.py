from __future__ import annotations

import shutil
from pathlib import Path

from fuzz_cookiecutter.agent.core.config import FuzzerConfig
from fuzz_cookiecutter.agent.core.llm_client import build_llm_client
from fuzz_cookiecutter.agent.llm import run_planner, run_rewriter
from fuzz_cookiecutter.agent.test_runner import run_batch
from fuzz_cookiecutter.agent.utils.coverage_diff_utils import compare_coverage
from fuzz_cookiecutter.agent.utils.grammar_diff_utils import diff_grammars
from fuzz_cookiecutter.agent.utils.monitoring import trace
from fuzz_cookiecutter.agent.utils.report_utils import write_finding, write_json, write_text
from fuzz_cookiecutter.agent.validator import validate_mutation_response


def _copy_batch_artifacts(destination_root: Path, label: str, run_dir: Path) -> Path:
    trace("orchestrator", "copying batch artifacts", label=label, source=run_dir, destination_root=destination_root)
    destination = destination_root / label
    if destination.exists():
        shutil.rmtree(destination)
    shutil.copytree(run_dir, destination)
    trace("orchestrator", "copied batch artifacts", destination=destination)
    return destination


def _write_final_summary(
    config: FuzzerConfig,
    *,
    champion_label: str,
    champion_coverage: float,
    history: list[str],
) -> Path:
    lines = [
        "# Cookiecutter Agentic Fuzzer Summary",
        "",
        f"- Champion batch: {champion_label}",
        f"- Champion coverage: {champion_coverage:.2f}%",
        "- History:",
    ]
    lines.extend(f"  - {entry}" for entry in history)
    summary_path = write_text(config.reports_dir / "final_summary.md", "\n".join(lines) + "\n")
    trace("orchestrator", "wrote final summary", path=summary_path)
    return summary_path


def run_fuzzer(config: FuzzerConfig) -> int:
    trace("orchestrator", "starting fuzzer run")
    config.ensure_directories()
    trace("orchestrator", "ensured fuzzer directories")
    for path in config.run_cache_dir.glob("*"):
        if path.is_dir():
            shutil.rmtree(path)
        else:
            path.unlink()
    trace("orchestrator", "cleared run cache", path=config.run_cache_dir)
    for path in config.history_dir.glob("iter_*"):
        if path.is_dir():
            shutil.rmtree(path)
        else:
            path.unlink()
    trace("orchestrator", "cleared iteration history", path=config.history_dir)
    for path in config.findings_dir.glob("iter_*"):
        if path.is_dir():
            shutil.rmtree(path)
        else:
            path.unlink()
    trace("orchestrator", "cleared findings", path=config.findings_dir)
    llm_client = build_llm_client(
        base_url=config.llm_base_url,
        api_key=config.llm_api_key,
        model_name=config.llm_model_name,
        timeout_seconds=config.llm_timeout_seconds,
    )
    trace(
        "orchestrator",
        "constructed llm client",
        model=config.llm_model_name,
        base_url=config.llm_base_url or "heuristic-fallback",
        timeout=config.llm_timeout_seconds,
    )

    trace("orchestrator", "running baseline batch")
    baseline = run_batch(config, label="baseline")
    trace(
        "orchestrator",
        "baseline batch completed",
        coverage=baseline.coverage_summary.percent_covered,
        cases=len(baseline.results),
    )
    _copy_batch_artifacts(config.baselines_dir, "baseline", baseline.run_dir)
    history_batches = [baseline]
    history_labels = [
        f"baseline {baseline.coverage_summary.percent_covered:.2f}%"
    ]
    champion_batch = baseline
    champion_grammar = baseline.grammar_text
    validation_feedback = ""

    for iteration in range(1, config.max_iterations + 1):
        trace("orchestrator", "starting iteration", iteration=iteration)
        iteration_dir = config.history_dir / f"iter_{iteration:03d}"
        iteration_dir.mkdir(parents=True, exist_ok=True)
        trace("orchestrator", "created iteration directory", path=iteration_dir)

        trace("orchestrator", "running planner", iteration=iteration)
        planner_output, planner_call = run_planner(
            config,
            llm_client,
            run_dir=iteration_dir,
            grammar_text=champion_grammar,
            champion=champion_batch,
            validation_feedback=validation_feedback,
            history=history_batches,
        )
        trace(
            "orchestrator",
            "planner completed",
            iteration=iteration,
            provider=planner_call.provider,
            recommendations=len(planner_output.recommended_rule_edits),
        )
        write_json(iteration_dir / "planner.parsed.json", planner_call.parsed_json)
        trace("orchestrator", "wrote parsed planner output", path=iteration_dir / "planner.parsed.json")

        validated = None
        for retry in range(1, config.mutation_retry_limit + 1):
            trace("orchestrator", "running rewriter", iteration=iteration, retry=retry)
            mutation_plan, rewriter_call = run_rewriter(
                llm_client,
                run_dir=iteration_dir / f"rewrite_retry_{retry}",
                grammar_text=champion_grammar,
                planner_output=planner_output,
            )
            trace(
                "orchestrator",
                "rewriter completed",
                iteration=iteration,
                retry=retry,
                provider=rewriter_call.provider,
                updates=len(mutation_plan.updates),
            )
            write_json(
                iteration_dir / f"rewriter_retry_{retry}.parsed.json",
                rewriter_call.parsed_json,
            )
            trace(
                "orchestrator",
                "wrote parsed rewriter output",
                path=iteration_dir / f"rewriter_retry_{retry}.parsed.json",
            )
            validated = validate_mutation_response(
                config, champion_grammar, rewriter_call.raw_text
            )
            trace(
                "orchestrator",
                "validated candidate mutation",
                iteration=iteration,
                retry=retry,
                ok=validated.ok,
                feedback=validated.feedback,
            )
            if validated.ok:
                break
            validation_feedback = validated.feedback

        if not validated or not validated.ok or not validated.candidate_grammar:
            trace("orchestrator", "candidate rejected during validation", iteration=iteration)
            write_finding(
                config.findings_dir / f"iter_{iteration:03d}_invalid_candidate.json",
                "invalid_candidate_grammar",
                {"feedback": validation_feedback or "validation failed"},
            )
            trace(
                "orchestrator",
                "wrote invalid candidate finding",
                path=config.findings_dir / f"iter_{iteration:03d}_invalid_candidate.json",
            )
            history_labels.append(f"iter_{iteration:03d} rejected during validation")
            continue

        candidate_grammar = validated.candidate_grammar
        trace("orchestrator", "running candidate batch", iteration=iteration)
        candidate_batch = run_batch(
            config,
            label=f"iter_{iteration:03d}_candidate",
            grammar_text=candidate_grammar,
        )
        trace(
            "orchestrator",
            "candidate batch completed",
            iteration=iteration,
            coverage=candidate_batch.coverage_summary.percent_covered,
            cases=len(candidate_batch.results),
        )
        history_batches.append(candidate_batch)
        delta = compare_coverage(champion_batch.coverage_summary, candidate_batch.coverage_summary)
        trace(
            "orchestrator",
            "computed coverage delta",
            iteration=iteration,
            line_delta=delta.line_delta,
            branch_delta=delta.branch_delta,
            percent_delta=delta.percent_delta,
            promoted=delta.candidate_is_at_least_as_good,
        )

        write_text(
            iteration_dir / "grammar.diff",
            diff_grammars(champion_grammar, candidate_grammar),
        )
        trace("orchestrator", "wrote grammar diff", path=iteration_dir / "grammar.diff")
        write_json(
            iteration_dir / "coverage.diff.json",
            {
                "line_delta": delta.line_delta,
                "branch_delta": delta.branch_delta,
                "percent_delta": delta.percent_delta,
                "candidate_is_at_least_as_good": delta.candidate_is_at_least_as_good,
            },
        )
        trace("orchestrator", "wrote coverage diff", path=iteration_dir / "coverage.diff.json")

        if delta.candidate_is_at_least_as_good:
            config.grammar_path.write_text(candidate_grammar, encoding="utf-8")
            trace("orchestrator", "updated champion grammar on disk", path=config.grammar_path)
            champion_grammar = candidate_grammar
            champion_batch = candidate_batch
            _copy_batch_artifacts(
                config.history_dir, f"iter_{iteration:03d}_promoted", candidate_batch.run_dir
            )
            trace("orchestrator", "candidate promoted", iteration=iteration, coverage=champion_batch.coverage_summary.percent_covered)
            history_labels.append(
                f"iter_{iteration:03d} promoted {candidate_batch.coverage_summary.percent_covered:.2f}%"
            )
            validation_feedback = ""
        else:
            trace("orchestrator", "candidate rejected after coverage comparison", iteration=iteration)
            write_finding(
                config.findings_dir / f"iter_{iteration:03d}_candidate_regression.json",
                "candidate_regression",
                {
                    "line_delta": delta.line_delta,
                    "branch_delta": delta.branch_delta,
                    "percent_delta": delta.percent_delta,
                },
            )
            trace(
                "orchestrator",
                "wrote candidate regression finding",
                path=config.findings_dir / f"iter_{iteration:03d}_candidate_regression.json",
            )
            history_labels.append(
                f"iter_{iteration:03d} rejected {candidate_batch.coverage_summary.percent_covered:.2f}%"
            )
            validation_feedback = "Candidate regressed coverage versus champion."

    trace("orchestrator", "writing final summary")
    _write_final_summary(
        config,
        champion_label=champion_batch.label,
        champion_coverage=champion_batch.coverage_summary.percent_covered,
        history=history_labels,
    )
    trace("orchestrator", "fuzzer run complete", champion=champion_batch.label, coverage=champion_batch.coverage_summary.percent_covered)
    return 0
