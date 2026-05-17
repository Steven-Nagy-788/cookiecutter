from __future__ import annotations

from datetime import datetime


def trace(scope: str, message: str, /, **fields: object) -> None:
    timestamp = datetime.now().strftime("%H:%M:%S")
    suffix = ""
    if fields:
        rendered = " ".join(f"{key}={value}" for key, value in fields.items())
        suffix = f" | {rendered}"
    print(f"[{timestamp}] [{scope}] {message}{suffix}", flush=True)

