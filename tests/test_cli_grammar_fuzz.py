"""Grammar-based fuzz tests for cookiecutter CLI argument parsing."""

from __future__ import annotations

import os
import shlex
from unittest.mock import patch

import pytest
from click.testing import CliRunner
from hypothesis import HealthCheck, given, settings
from hypothesis.extra.lark import from_lark
from lark import Lark

from cookiecutter.cli import main


GRAMMAR = r"""
start: template options
template: "tests/fake-repo-pre/"
options: (WS option)*

option: "--no-input"
      | "--replay"
      | "-v"
      | "-f"
      | "--overwrite-if-exists"
      | "--default-config"
      | "--accept-hooks=yes"
      | "--accept-hooks=no"
      | "-o tests/tmp-fuzz"
      | "--output-dir tests/tmp-fuzz"
      | "--replay-file tests/test-replay/valid_replay.json"

%import common.WS
"""


def _command_strategy():
    parser = Lark(GRAMMAR, start='start', parser='lalr')
    return from_lark(parser).map(shlex.split)


FUZZ_MAX_EXAMPLES = int(os.getenv('CC_FUZZ_MAX_EXAMPLES', '100'))
FUZZ_DEADLINE_MS = int(os.getenv('CC_FUZZ_DEADLINE_MS', '200'))


@pytest.fixture(scope='session')
def cli_runner():
    """Fixture that returns a helper function to run the cookiecutter cli."""
    runner = CliRunner()

    def cli_main(*cli_args, **cli_kwargs):
        """Run cookiecutter cli main with the given args."""
        return runner.invoke(main, cli_args, **cli_kwargs)

    return cli_main


@settings(
    max_examples=FUZZ_MAX_EXAMPLES,
    deadline=FUZZ_DEADLINE_MS,
    suppress_health_check=[HealthCheck.too_slow],
)
@given(cli_args=_command_strategy())
def test_cli_grammar_fuzz_smoke(cli_runner, cli_args):
    """Fuzz CLI args from a small grammar and assert stable behavior."""
    with patch('cookiecutter.cli.cookiecutter') as mock_cookiecutter:
        result = cli_runner(*cli_args)

        # We allow expected CLI errors, but never a Python traceback crash.
        assert result.exit_code in {0, 1, 2}
        assert 'Traceback (most recent call last)' not in result.output

        # Successful parsing and execution path should call into cookiecutter.
        if result.exit_code == 0:
            assert mock_cookiecutter.call_count == 1
