from __future__ import annotations

import subprocess
import os
import sys
from pathlib import Path


def run_command(
    args: list[str],
    *,
    cwd: Path,
    timeout: int | None = None,
    env: dict[str, str] | None = None,
) -> subprocess.CompletedProcess[str]:
    merged_env = {**os.environ, **(env or {})}
    venv_bin = str(Path(sys.executable).parent)
    path_val = merged_env.get("PATH", "")
    if path_val:
        merged_env["PATH"] = f"{venv_bin}{os.pathsep}{path_val}"
    else:
        merged_env["PATH"] = venv_bin

    return subprocess.run(
        args,
        cwd=cwd,
        capture_output=True,
        text=True,
        timeout=timeout,
        env=merged_env,
        check=False,
    )


def excerpt(text: str, limit: int = 800) -> str:
    if len(text) <= limit:
        return text
    return text[: limit - 3] + "..."
