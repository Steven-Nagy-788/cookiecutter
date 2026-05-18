from __future__ import annotations

import json
import os
import subprocess
from pathlib import Path

from fuzz_cookiecutter.agent.core.config import FuzzerConfig
from fuzz_cookiecutter.agent.models import ManifestExecutionSpec, TestResult
from fuzz_cookiecutter.agent.utils.cli_utils import excerpt
from fuzz_cookiecutter.agent.utils.monitoring import trace


def execute_case(
    config: FuzzerConfig,
    spec: ManifestExecutionSpec,
    *,
    coverage_dir: Path,
    result_dir: Path,
) -> TestResult:
    trace("sandbox", "preparing case execution", case_id=spec.case_id, mode=spec.mode)
    result_dir.mkdir(parents=True, exist_ok=True)
    coverage_dir.mkdir(parents=True, exist_ok=True)
    spec_path = result_dir / f"{spec.case_id}.spec.json"
    result_path = result_dir / f"{spec.case_id}.result.json"
    stdout_path = result_dir / f"{spec.case_id}.stdout.log"
    stderr_path = result_dir / f"{spec.case_id}.stderr.log"
    spec_path.write_text(json.dumps(spec.to_payload(), indent=2), encoding="utf-8")
    trace("sandbox", "wrote execution spec", case_id=spec.case_id, spec_path=spec_path)
    env = os.environ.copy()
    env["PYTHONPATH"] = str(config.repo_root)
    env["COVERAGE_FILE"] = str(coverage_dir / ".coverage")
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    env["TMPDIR"] = str(spec.workspace_dir)
    env["TEMP"] = str(spec.workspace_dir)
    env["TMP"] = str(spec.workspace_dir)
    import sys
    venv_bin = str(Path(sys.executable).parent)
    path_val = env.get("PATH", "")
    if path_val:
        env["PATH"] = f"{venv_bin}{os.pathsep}{path_val}"
    else:
        env["PATH"] = venv_bin

    command = [
        sys.executable,
        "-m",
        "coverage",
        "run",
        "--branch",
        "--parallel-mode",
        "--source=cookiecutter",
        "fuzz_cookiecutter/runner_entry.py",
        "--spec",
        str(spec_path),
        "--result",
        str(result_path),
    ]
    trace("sandbox", "launching runner subprocess", case_id=spec.case_id, timeout=config.per_case_timeout_seconds)

    try:
        proc = subprocess.run(
            command,
            cwd=config.repo_root,
            env=env,
            capture_output=True,
            text=True,
            timeout=config.per_case_timeout_seconds,
            check=False,
        )
    except subprocess.TimeoutExpired as exc:
        trace("sandbox", "runner subprocess timed out", case_id=spec.case_id)
        return TestResult(
            case_id=spec.case_id,
            status="ERROR",
            manifest_path=str(spec.manifest_path),
            execution_mode=spec.mode,
            exit_code=None,
            exception_type="TimeoutExpired",
            exception_message=f"Timed out after {config.per_case_timeout_seconds}s",
            stdout_excerpt=excerpt((exc.stdout or "") if isinstance(exc.stdout, str) else ""),
            stderr_excerpt=excerpt((exc.stderr or "") if isinstance(exc.stderr, str) else ""),
            hook_phase_reached=None,
            materialization_status="OK",
            generated_project_path=None,
            file_count_created=0,
            duration_ms=config.per_case_timeout_seconds * 1000,
        )

    stdout_path.write_text(proc.stdout, encoding="utf-8")
    stderr_path.write_text(proc.stderr, encoding="utf-8")
    trace("sandbox", "runner subprocess finished", case_id=spec.case_id, returncode=proc.returncode)

    if result_path.exists():
        payload = json.loads(result_path.read_text(encoding="utf-8"))
        trace(
            "sandbox",
            "loaded structured case result",
            case_id=spec.case_id,
            status=payload.get("status"),
            exception=payload.get("exception_type"),
        )
        return TestResult(**payload)

    status = "CRASH" if proc.returncode < 0 else "ERROR"
    trace("sandbox", "runner exited without structured result", case_id=spec.case_id, status=status)
    return TestResult(
        case_id=spec.case_id,
        status=status,
        manifest_path=str(spec.manifest_path),
        execution_mode=spec.mode,
        exit_code=proc.returncode,
        exception_type="ProcessTerminated",
        exception_message="Runner exited before producing a result payload",
        stdout_excerpt=excerpt(proc.stdout),
        stderr_excerpt=excerpt(proc.stderr),
        hook_phase_reached=None,
        materialization_status="OK",
        generated_project_path=None,
        file_count_created=0,
        duration_ms=0,
    )
