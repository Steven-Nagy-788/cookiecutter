from __future__ import annotations

import subprocess
import os
from pathlib import Path


def run_command(
    args: list[str],
    *,
    cwd: Path,
    timeout: int | None = None,
    env: dict[str, str] | None = None,
) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        args,
        cwd=cwd,
        capture_output=True,
        text=True,
        timeout=timeout,
        env={**os.environ, **(env or {})},
        check=False,
    )


def excerpt(text: str, limit: int = 800) -> str:
    if len(text) <= limit:
        return text
    return text[: limit - 3] + "..."
