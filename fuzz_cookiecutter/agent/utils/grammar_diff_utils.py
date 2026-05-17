from __future__ import annotations

from difflib import unified_diff


def diff_grammars(before: str, after: str, *, from_name: str = "before", to_name: str = "after") -> str:
    return "".join(
        unified_diff(
            before.splitlines(keepends=True),
            after.splitlines(keepends=True),
            fromfile=from_name,
            tofile=to_name,
        )
    )

