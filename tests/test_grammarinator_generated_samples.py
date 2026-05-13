from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

import pytest


REPO_ROOT = Path(__file__).resolve().parents[1]
FUZZER_RUNNER = REPO_ROOT / 'fuzzer' / 'run_gramminator_cases.py'


def _run_corpus(sample_glob: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [
            sys.executable,
            str(FUZZER_RUNNER),
            '--samples',
            sample_glob,
            '--timeout',
            '5',
        ],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        check=False,
    )


def _parse_summary(output: str) -> dict[str, int]:
    match = re.search(
        r'summary: pass=(\d+) fail=(\d+) crash=(\d+) total=(\d+)',
        output,
    )
    if not match:
        pytest.fail(f'Missing summary line in output:\n{output}')

    return {
        'pass': int(match.group(1)),
        'fail': int(match.group(2)),
        'crash': int(match.group(3)),
        'total': int(match.group(4)),
    }


@pytest.mark.parametrize(
    ('sample_glob', 'expected_behavior'),
    [
        ('fuzzer/samples/json/*.json', 'json'),
        ('fuzzer/samples/ssti/*.json', 'ssti'),
    ],
)
def test_generated_gramminator_samples(sample_glob: str, expected_behavior: str) -> None:
    result = _run_corpus(sample_glob)

    assert result.returncode in {0, 1}
    assert 'summary:' in result.stdout

    summary = _parse_summary(result.stdout)
    assert summary['total'] > 0
    assert summary['pass'] + summary['fail'] + summary['crash'] == summary['total']

    if expected_behavior == 'json':
        assert summary['pass'] > 0
    else:
        assert summary['crash'] > 0 or summary['fail'] > 0