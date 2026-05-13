from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


def run_one(worker: Path, sample: Path, timeout: int) -> tuple[int, str]:
    proc = subprocess.run(
        [sys.executable, str(worker), "--json", str(sample)],
        capture_output=True,
        text=True,
        timeout=timeout,
    )
    output = (proc.stdout + proc.stderr).strip()
    return proc.returncode, output


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Run generated cookiecutter.json samples in isolated subprocesses."
    )
    parser.add_argument("--samples", required=True, help="Glob for generated JSON files")
    parser.add_argument("--timeout", type=int, default=5, help="Timeout per sample")
    args = parser.parse_args()

    root = Path(__file__).resolve().parent
    worker = root / "execute_cookiecutter_json.py"
    samples = sorted(Path.cwd().glob(args.samples))

    if not samples:
        print("no samples found")
        return 2

    passed = 0
    failed = 0
    crashed = 0

    for sample in samples:
        try:
            code, output = run_one(worker, sample, args.timeout)
        except subprocess.TimeoutExpired:
            crashed += 1
            print(f"TIMEOUT {sample}")
            continue

        if code == 0:
            passed += 1
            print(f"PASS {sample}")
            continue

        if code < 0:
            crashed += 1
            print(f"CRASH signal={-code} file={sample}")
            if output:
                print(output)
            continue

        failed += 1
        print(f"FAIL code={code} file={sample}")
        if output:
            print(output)

    print(f"summary: pass={passed} fail={failed} crash={crashed} total={len(samples)}")
    return 0 if failed == 0 and crashed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
