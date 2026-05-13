from __future__ import annotations

import argparse
import shlex
from pathlib import Path

from click.testing import CliRunner

from cookiecutter.cli import main


def run_one(sample: Path, output_root: Path) -> tuple[int, str]:
    command_text = sample.read_text(encoding='utf-8').strip()
    args = shlex.split(command_text)

    if '-o' not in args and '--output-dir' not in args:
        sample_output_dir = output_root / sample.stem
        sample_output_dir.mkdir(parents=True, exist_ok=True)
        args.extend(['-o', str(sample_output_dir)])

    result = CliRunner().invoke(main, args)
    return result.exit_code, result.output


def main_runner() -> int:
    parser = argparse.ArgumentParser(
        description='Run Grammarinator-generated Cookiecutter CLI samples.'
    )
    parser.add_argument('--samples', required=True, help='Glob for generated command files')
    parser.add_argument('--output-root', required=True, help='Directory for per-sample outputs')
    args = parser.parse_args()

    samples = sorted(Path.cwd().glob(args.samples))
    if not samples:
        print('no samples found')
        return 2

    output_root = Path(args.output_root)
    output_root.mkdir(parents=True, exist_ok=True)

    passed = 0
    failed = 0

    for sample in samples:
        code, output = run_one(sample, output_root)
        if code == 0:
            passed += 1
            print(f'PASS {sample}')
        else:
            failed += 1
            print(f'FAIL code={code} file={sample}')
            if output:
                print(output)

    print(f'summary: pass={passed} fail={failed} total={len(samples)}')
    return 0 if failed == 0 else 1


if __name__ == '__main__':
    raise SystemExit(main_runner())