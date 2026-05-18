import json
import shutil
from pathlib import Path
from fuzz_cookiecutter.agent.core.config import FuzzerConfig
from fuzz_cookiecutter.agent.models import BatchRunResult, TestResult
from fuzz_cookiecutter.agent.utils.coverage_utils import (
    combine_and_export_coverage,
    summarize_coverage,
)
from fuzz_cookiecutter.agent.utils.grammarinator_utils import generate_cases, process_grammar
from fuzz_cookiecutter.agent.utils.monitoring import trace
from fuzz_cookiecutter.agent.utils.report_utils import (
    results_to_markdown,
    write_json,
    write_text,
)
from fuzz_cookiecutter.agent.utils.sandbox_utils import execute_case


def run_batch(
    config: FuzzerConfig,
    *,
    label: str,
    grammar_text: str | None = None,
) -> BatchRunResult:
    trace("batch", "starting batch run", label=label, override_grammar=grammar_text is not None)
    config.ensure_directories()
    run_dir = config.run_cache_dir / label
    if run_dir.exists():
        shutil.rmtree(run_dir)
        trace("batch", "removed previous run directory", path=run_dir)
    run_dir.mkdir(parents=True, exist_ok=True)
    trace("batch", "created run directory", path=run_dir)
    generator_dir = run_dir / "generator"
    cases_dir = run_dir / "cases"
    workspaces_dir = run_dir / "workspaces"
    results_dir = run_dir / "results"
    coverage_dir = run_dir / "coverage"
    workspaces_dir.mkdir(parents=True, exist_ok=True)
    results_dir.mkdir(parents=True, exist_ok=True)
    trace("batch", "created batch subdirectories", generator_dir=generator_dir, cases_dir=cases_dir, workspaces_dir=workspaces_dir, results_dir=results_dir, coverage_dir=coverage_dir)

    original_grammar = config.grammar_path.read_text(encoding="utf-8")
    active_grammar = grammar_text or original_grammar
    if grammar_text is not None:
        config.grammar_path.write_text(grammar_text, encoding="utf-8")
        trace("batch", "wrote temporary candidate grammar", path=config.grammar_path)

    try:
        trace("batch", "processing grammar", grammar_path=config.grammar_path)
        generator = process_grammar(config, config.grammar_path, generator_dir)
        trace("batch", "grammar processed", generator=generator)
        trace("batch", "generating manifests", case_count=config.batch_size, depth=config.generation_depth)
        manifests = generate_cases(
            config,
            generator,
            case_count=config.batch_size,
            depth=config.generation_depth,
            output_dir=cases_dir,
        )
        trace("batch", "generated manifests", count=len(manifests), cases_dir=cases_dir)
        results: list[TestResult] = []
        for index, manifest_path in enumerate(manifests):
            case_id = f"case_{index:03d}"
            workspace_dir = workspaces_dir / case_id
            trace("batch", "starting case", case_id=case_id, manifest=manifest_path)
            
            try:
                raw_data = json.loads(manifest_path.read_text(encoding="utf-8"))
            except Exception as e:
                trace("batch", "manifest validation failed (invalid JSON)", case_id=case_id, error=e)
                results.append(
                    TestResult(
                        case_id=case_id,
                        status="ERROR",
                        manifest_path=str(manifest_path),
                        execution_mode="unknown",
                        exit_code=None,
                        exception_type=type(e).__name__,
                        exception_message=str(e),
                        stdout_excerpt="",
                        stderr_excerpt="",
                        hook_phase_reached=None,
                        materialization_status="FAILED",
                        generated_project_path=None,
                        file_count_created=0,
                        duration_ms=0,
                    )
                )
                continue
            
            raw_data["case_id"] = case_id
            raw_data["manifest_path"] = str(manifest_path)
            # Create a mock spec that works with execute_case
            class MockSpec:
                def __init__(self, d):
                    self.case_id = d.get("case_id")
                    self.mode = d.get("mode")
                    self.manifest_path = d.get("manifest_path")
                    self.workspace_dir = workspace_dir
                    self.d = d
                def to_payload(self):
                    return self.d
            
            spec = MockSpec(raw_data)
            
            trace("batch", "executing case", case_id=case_id)
            results.append(
                execute_case(
                    config,
                    spec,
                    coverage_dir=coverage_dir,
                    result_dir=results_dir,
                )
            )
            trace(
                "batch",
                "case execution finished",
                case_id=case_id,
                status=results[-1].status,
                exit_code=results[-1].exit_code,
                phase=results[-1].hook_phase_reached,
            )

        trace("batch", "combining coverage data", coverage_dir=coverage_dir)
        coverage_json = combine_and_export_coverage(
            config, coverage_dir, run_dir / "coverage.json"
        )
        trace("batch", "coverage export complete", coverage_json=coverage_json)
        coverage_summary = summarize_coverage(coverage_json)
        trace(
            "batch",
            "coverage summary computed",
            percent=coverage_summary.percent_covered,
            covered_lines=coverage_summary.covered_lines,
            branches=coverage_summary.covered_branches,
        )
        results_json = write_json(
            run_dir / "results.json",
            [result.to_dict() for result in results],
        )
        trace("batch", "wrote results json", path=results_json)
        results_markdown = write_text(
            run_dir / "results.md",
            results_to_markdown(results, coverage_summary),
        )
        trace("batch", "wrote results markdown", path=results_markdown)
        return BatchRunResult(
            label=label,
            run_dir=run_dir,
            grammar_text=active_grammar,
            manifests=manifests,
            results=results,
            coverage_json=coverage_json,
            coverage_summary=coverage_summary,
            results_json=results_json,
            results_markdown=results_markdown,
            notes={"generator": str(generator)},
        )
    finally:
        if grammar_text is not None:
            config.grammar_path.write_text(original_grammar, encoding="utf-8")
            trace("batch", "restored original grammar", path=config.grammar_path)
