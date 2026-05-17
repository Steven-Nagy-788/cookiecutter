from __future__ import annotations

import argparse
import json
import time
from contextlib import contextmanager
from pathlib import Path
from typing import Any, Iterator
from unittest.mock import patch

from click.testing import CliRunner

from cookiecutter.cli import main as cli_main
from cookiecutter.exceptions import (
    ContextDecodingException,
    EmptyDirNameException,
    FailedHookException,
    InvalidModeException,
    InvalidZipRepository,
    NonTemplatedInputDirException,
    OutputDirExistsException,
    RepositoryCloneFailed,
    RepositoryNotFound,
    UndefinedVariableInTemplate,
    UnknownExtension,
)
from cookiecutter.main import cookiecutter as cookiecutter_api
from fuzz_cookiecutter.agent.models import InvocationConfig, TestResult


KNOWN_WARNING_EXCEPTIONS = (
    ContextDecodingException,
    EmptyDirNameException,
    FailedHookException,
    InvalidModeException,
    InvalidZipRepository,
    NonTemplatedInputDirException,
    OutputDirExistsException,
    RepositoryCloneFailed,
    RepositoryNotFound,
    UndefinedVariableInTemplate,
    UnknownExtension,
    ValueError,
)


def _count_created_files(project_dir: Path) -> int:
    if not project_dir.exists():
        return 0
    return sum(1 for path in project_dir.rglob("*") if path.is_file())


def _classify_exception(exc: BaseException) -> str:
    if isinstance(exc, KNOWN_WARNING_EXCEPTIONS):
        return "WARNING"
    return "CRASH"


@contextmanager
def _track_phases() -> Iterator[dict[str, str | None]]:
    state: dict[str, str | None] = {"phase": None}

    def wrapper(phase: str, func):
        def inner(*args, **kwargs):
            state["phase"] = phase
            return func(*args, **kwargs)

        return inner

    from cookiecutter import generate as generate_module
    from cookiecutter import hooks as hooks_module
    from cookiecutter import main as main_module
    from cookiecutter import prompt as prompt_module

    with (
        patch.object(
            main_module, "run_pre_prompt_hook", wrapper("pre_prompt", main_module.run_pre_prompt_hook)
        ),
        patch.object(
            main_module, "generate_context", wrapper("context_generation", main_module.generate_context)
        ),
        patch.object(
            main_module, "prompt_for_config", wrapper("prompt", main_module.prompt_for_config)
        ),
        patch.object(
            main_module, "generate_files", wrapper("generate_files", main_module.generate_files)
        ),
        patch.object(
            generate_module,
            "render_and_create_dir",
            wrapper("render_path", generate_module.render_and_create_dir),
        ),
        patch.object(
            generate_module, "generate_file", wrapper("render_file", generate_module.generate_file)
        ),
        patch.object(
            generate_module,
            "run_hook_from_repo_dir",
            wrapper("hook_dispatch", generate_module.run_hook_from_repo_dir),
        ),
        patch.object(
            hooks_module, "run_hook", wrapper("hook_run", hooks_module.run_hook)
        ),
        patch.object(
            hooks_module,
            "run_script_with_context",
            wrapper("hook_script_render", hooks_module.run_script_with_context),
        ),
    ):
        yield state


@contextmanager
def _auto_default_prompts(enabled: bool) -> Iterator[None]:
    if not enabled:
        yield
        return

    from cookiecutter import prompt as prompt_module

    with (
        patch.object(
            prompt_module.Prompt,
            "ask",
            side_effect=lambda _prompt, **kwargs: kwargs.get("default", ""),
        ),
        patch.object(
            prompt_module.YesNoPrompt,
            "ask",
            side_effect=lambda _prompt, **kwargs: kwargs.get("default", True),
        ),
        patch.object(
            prompt_module.JsonPrompt,
            "ask",
            side_effect=lambda _prompt, **kwargs: kwargs.get("default", {}),
        ),
    ):
        yield


def _run_cli(spec: dict[str, Any]) -> tuple[int, str, str | None]:
    args = [
        str(spec["template_repo_dir"]),
        "--default-config",
        "--output-dir",
        str(spec["output_dir"]),
    ]
    invocation = InvocationConfig(**spec["invocation"])
    if invocation.no_input:
        args.append("--no-input")
    if invocation.overwrite_if_exists:
        args.append("--overwrite-if-exists")
    if invocation.skip_if_file_exists:
        args.append("--skip-if-file-exists")
    if not invocation.accept_hooks:
        args.extend(["--accept-hooks", "no"])
    if invocation.keep_project_on_failure:
        args.append("--keep-project-on-failure")
    if spec["replay_file"]:
        args.extend(["--replay-file", str(spec["replay_file"])])
    for key, value in invocation.extra_context.items():
        args.append(f"{key}={value}")

    runner = CliRunner()
    result = runner.invoke(cli_main, args, catch_exceptions=True)
    exception_name = None if result.exception is None else type(result.exception).__name__
    return result.exit_code, result.output, exception_name


def _run_api(spec: dict[str, Any]) -> tuple[int, str, str | None]:
    invocation = InvocationConfig(**spec["invocation"])
    kwargs = {
        "template": str(spec["template_repo_dir"]),
        "no_input": invocation.no_input,
        "extra_context": invocation.extra_context or None,
        "replay": str(spec["replay_file"]) if spec["replay_file"] else None,
        "overwrite_if_exists": invocation.overwrite_if_exists,
        "output_dir": str(spec["output_dir"]),
        "default_config": True,
        "skip_if_file_exists": invocation.skip_if_file_exists,
        "accept_hooks": invocation.accept_hooks,
        "keep_project_on_failure": invocation.keep_project_on_failure,
    }
    cookiecutter_api(**kwargs)
    return 0, "", None


def execute(spec: dict[str, Any]) -> TestResult:
    start = time.perf_counter()
    generated_project_path = str(spec["predicted_project_dir"])
    with _track_phases() as tracker, _auto_default_prompts(
        not spec["invocation"]["no_input"]
    ):
        try:
            if spec["mode"] == "cli":
                exit_code, stdout, cli_exception = _run_cli(spec)
                status = "SUCCESS" if exit_code == 0 else "WARNING"
                return TestResult(
                    case_id=spec["case_id"],
                    status=status,
                    manifest_path=str(spec["manifest_path"]),
                    execution_mode="cli",
                    exit_code=exit_code,
                    exception_type=cli_exception,
                    exception_message=None,
                    stdout_excerpt=stdout[:800],
                    stderr_excerpt="",
                    hook_phase_reached=tracker["phase"],
                    materialization_status="OK",
                    generated_project_path=generated_project_path if Path(generated_project_path).exists() else None,
                    file_count_created=_count_created_files(Path(generated_project_path)),
                    duration_ms=int((time.perf_counter() - start) * 1000),
                )

            exit_code, stdout, _ = _run_api(spec)
            return TestResult(
                case_id=spec["case_id"],
                status="SUCCESS",
                manifest_path=str(spec["manifest_path"]),
                execution_mode="api",
                exit_code=exit_code,
                exception_type=None,
                exception_message=None,
                stdout_excerpt=stdout[:800],
                stderr_excerpt="",
                hook_phase_reached=tracker["phase"],
                materialization_status="OK",
                generated_project_path=generated_project_path if Path(generated_project_path).exists() else None,
                file_count_created=_count_created_files(Path(generated_project_path)),
                duration_ms=int((time.perf_counter() - start) * 1000),
            )
        except Exception as exc:  # noqa: BLE001
            return TestResult(
                case_id=spec["case_id"],
                status=_classify_exception(exc),
                manifest_path=str(spec["manifest_path"]),
                execution_mode=spec["mode"],
                exit_code=1,
                exception_type=type(exc).__name__,
                exception_message=str(exc),
                stdout_excerpt="",
                stderr_excerpt="",
                hook_phase_reached=tracker["phase"],
                materialization_status="OK",
                generated_project_path=generated_project_path if Path(generated_project_path).exists() else None,
                file_count_created=_count_created_files(Path(generated_project_path)),
                duration_ms=int((time.perf_counter() - start) * 1000),
                details={"exception_repr": repr(exc)},
            )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--spec", required=True)
    parser.add_argument("--result", required=True)
    args = parser.parse_args()

    spec = json.loads(Path(args.spec).read_text(encoding="utf-8"))
    result = execute(spec)
    Path(args.result).write_text(
        json.dumps(result.to_dict(), indent=2, sort_keys=True), encoding="utf-8"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
