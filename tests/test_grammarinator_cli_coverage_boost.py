from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

import pytest


REPO_ROOT = Path(__file__).resolve().parents[1]
RUNNER = REPO_ROOT / 'fuzzer' / 'coverage_boost' / 'run_cli_corpus.py'
SAMPLES = 'fuzzer/coverage_boost/samples/*.txt'


def _run_corpus(output_root: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [
            sys.executable,
            str(RUNNER),
            '--samples',
            SAMPLES,
            '--output-root',
            str(output_root),
        ],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        check=False,
    )


def _parse_summary(output: str) -> dict[str, int]:
    match = re.search(r'summary: pass=(\d+) fail=(\d+) total=(\d+)', output)
    if not match:
        pytest.fail(f'Missing summary line in output:\n{output}')

    return {
        'pass': int(match.group(1)),
        'fail': int(match.group(2)),
        'total': int(match.group(3)),
    }


def test_cli_coverage_boost_corpus(tmp_path: Path) -> None:
    result = _run_corpus(tmp_path / 'cli-output')

    assert result.returncode in {0, 1}
    assert 'summary:' in result.stdout

    summary = _parse_summary(result.stdout)
    assert summary['total'] > 0
    assert summary['pass'] + summary['fail'] == summary['total']
    assert summary['pass'] > 0