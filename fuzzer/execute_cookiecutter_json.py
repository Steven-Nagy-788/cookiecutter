from __future__ import annotations

import argparse
import json
from pathlib import Path

from cookiecutter.prompt import prompt_for_config


def run_case(json_path: Path) -> int:
    with open(json_path, encoding="utf-8") as handle:
        context = {"cookiecutter": json.load(handle)}
    rendered = prompt_for_config(context, no_input=True)
    json.dumps(rendered)
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Load and render a cookiecutter.json file through prompt logic."
    )
    parser.add_argument("--json", dest="json_path", required=True)
    args = parser.parse_args()

    path = Path(args.json_path)
    if not path.is_file():
        print(f"missing file: {path}")
        return 2

    return run_case(path)


if __name__ == "__main__":
    raise SystemExit(main())
