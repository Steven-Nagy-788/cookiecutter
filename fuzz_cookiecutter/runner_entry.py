import argparse
import json
import shlex
import time
from pathlib import Path
from typing import Any

from click.testing import CliRunner
from cookiecutter.cli import main as cli_main
from cookiecutter.prompt import prompt_for_config
from fuzz_cookiecutter.agent.models import TestResult
from fuzz_cookiecutter.agent.utils.cli_utils import excerpt


def _run_cli(command: str) -> tuple[int, str, str | None]:
    args = shlex.split(command)
    runner = CliRunner()
    result = runner.invoke(cli_main, args, catch_exceptions=True)
    exception_name = None if result.exception is None else type(result.exception).__name__
    return result.exit_code, result.output, exception_name


def _run_json(payload: dict[str, Any]) -> tuple[int, str, str | None]:
    context = {"cookiecutter": payload}
    try:
        prompt_for_config(context, no_input=True)
        return 0, "OK", None
    except Exception as exc:
        return 1, str(exc), type(exc).__name__


def execute(spec: dict[str, Any]) -> TestResult:
    start = time.perf_counter()
    mode = spec.get("mode")
    
    try:
        if mode == "cli":
            command = spec.get("command", "")
            exit_code, stdout, exception_type = _run_cli(command)
        elif mode == "json":
            payload = spec.get("json_payload", {})
            exit_code, stdout, exception_type = _run_json(payload)
        else:
            raise ValueError(f"Unknown mode: {mode}")

        status = "SUCCESS" if exit_code == 0 else "WARNING"
        return TestResult(
            case_id=spec.get("case_id", "unknown"),
            status=status,
            manifest_path=str(spec.get("manifest_path", "")),
            execution_mode=mode,
            exit_code=exit_code,
            exception_type=exception_type,
            exception_message=None,
            stdout_excerpt=excerpt(stdout),
            stderr_excerpt="",
            hook_phase_reached=None,
            materialization_status="OK",
            generated_project_path=None,
            file_count_created=0,
            duration_ms=int((time.perf_counter() - start) * 1000),
        )
    except Exception as exc:
        return TestResult(
            case_id=spec.get("case_id", "unknown"),
            status="CRASH",
            manifest_path=str(spec.get("manifest_path", "")),
            execution_mode=mode,
            exit_code=1,
            exception_type=type(exc).__name__,
            exception_message=str(exc),
            stdout_excerpt="",
            stderr_excerpt="",
            hook_phase_reached=None,
            materialization_status="OK",
            generated_project_path=None,
            file_count_created=0,
            duration_ms=int((time.perf_counter() - start) * 1000),
        )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--spec", required=True)
    parser.add_argument("--result", required=True)
    args = parser.parse_args()

    spec = json.loads(Path(args.spec).read_text(encoding="utf-8"))
    
    # Pass along case_id and manifest_path from spec wrapping
    result = execute(spec)
    
    Path(args.result).write_text(
        json.dumps(result.to_dict(), indent=2, sort_keys=True), encoding="utf-8"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
