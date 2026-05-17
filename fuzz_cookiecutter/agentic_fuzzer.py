from __future__ import annotations

import argparse
import sys
from pathlib import Path

if __package__ in {None, ""}:
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from fuzz_cookiecutter.agent.core.config import FuzzerConfig
from fuzz_cookiecutter.agent.core.llm_client import load_dotenv_files
from fuzz_cookiecutter.agent.orchestrator import run_fuzzer
from fuzz_cookiecutter.agent.utils.monitoring import trace


def main() -> int:
    repo_root = Path(__file__).resolve().parents[1]
    trace("entry", "starting agentic fuzzer entrypoint", repo_root=repo_root)
    load_dotenv_files(repo_root / "fuzz_cookiecutter" / ".env", repo_root / ".env")
    trace("entry", "loaded dotenv files")
    parser = argparse.ArgumentParser(description="Run the Cookiecutter agentic fuzzer.")
    parser.add_argument("--batch-size", type=int, default=None)
    parser.add_argument("--iterations", type=int, default=None)
    parser.add_argument("--timeout", type=int, default=None)
    args = parser.parse_args()
    trace(
        "entry",
        "parsed command line arguments",
        batch_size=args.batch_size,
        iterations=args.iterations,
        timeout=args.timeout,
    )

    config = FuzzerConfig.discover(repo_root=repo_root)
    trace("entry", "discovered fuzzer config", batch_size=config.batch_size, iterations=config.max_iterations)
    if args.batch_size is not None:
        config.batch_size = args.batch_size
        trace("entry", "overrode batch size from CLI", batch_size=config.batch_size)
    if args.iterations is not None:
        config.max_iterations = args.iterations
        trace("entry", "overrode iteration count from CLI", iterations=config.max_iterations)
    if args.timeout is not None:
        config.per_case_timeout_seconds = args.timeout
        trace("entry", "overrode per-case timeout from CLI", timeout=config.per_case_timeout_seconds)
    trace(
        "entry",
        "launching orchestrator",
        batch_size=config.batch_size,
        iterations=config.max_iterations,
        timeout=config.per_case_timeout_seconds,
    )
    return run_fuzzer(config)


if __name__ == "__main__":
    raise SystemExit(main())
