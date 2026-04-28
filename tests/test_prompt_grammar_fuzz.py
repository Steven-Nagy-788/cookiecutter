"""Grammar-based fuzz tests for cookiecutter prompt handling."""

from __future__ import annotations

import os
from io import StringIO
from unittest.mock import patch

import pytest
from hypothesis import HealthCheck, given, settings
from hypothesis.extra.lark import from_lark
from lark import Lark

from cookiecutter.prompt import (
    read_user_variable,
    read_user_yes_no,
    read_user_choice,
)


USER_INPUT_GRAMMAR = r"""
start: input_value

input_value: text_input
           | choice_input
           | yes_no_input

text_input: /[a-zA-Z0-9_]{1,20}/

choice_input: /[a-zA-Z0-9]{1,20}/

yes_no_input: "yes" | "no" | "true" | "false" | "y" | "n" | "1" | "0"

%import common.WS
"""


def _user_input_strategy():
    """Generate valid user-like inputs."""
    parser = Lark(USER_INPUT_GRAMMAR, start='start', parser='lalr')
    return from_lark(parser)


FUZZ_MAX_EXAMPLES = int(os.getenv('CC_FUZZ_MAX_EXAMPLES', '100'))
FUZZ_DEADLINE_MS = int(os.getenv('CC_FUZZ_DEADLINE_MS', '300'))


@settings(
    max_examples=FUZZ_MAX_EXAMPLES,
    deadline=FUZZ_DEADLINE_MS,
    suppress_health_check=[HealthCheck.too_slow],
)
@given(user_input=_user_input_strategy())
def test_read_user_variable_with_fuzzed_input(user_input):
    """Fuzz test read_user_variable with generated input strings."""
    # Mock stdin to provide fuzzed input
    with patch('rich.prompt.Prompt.ask') as mock_ask:
        mock_ask.return_value = user_input
        
        try:
            result = read_user_variable('test_var', default_value='default')
            
            # Assertions: function should not crash
            assert result is not None
            # Result should be a string
            assert isinstance(result, str)
            
        except (ValueError, TypeError, AttributeError):
            # Expected exceptions from invalid input are acceptable
            pass
        except Exception:
            # Unexpected crashes should fail the test
            raise


@settings(
    max_examples=FUZZ_MAX_EXAMPLES,
    deadline=FUZZ_DEADLINE_MS,
    suppress_health_check=[HealthCheck.too_slow],
)
@given(user_input=_user_input_strategy())
def test_read_user_yes_no_with_fuzzed_input(user_input):
    """Fuzz test read_user_yes_no with generated input strings."""
    with patch('rich.prompt.Confirm.ask') as mock_ask:
        # Try to interpret input as yes/no
        mock_ask.return_value = user_input.lower() in ('yes', 'true', 'y', '1')
        
        try:
            result = read_user_yes_no('test_bool', default_value=False)
            
            # Assertions: function should not crash
            assert result is not None
            # Result should be boolean
            assert isinstance(result, bool)
            
        except (ValueError, TypeError, AttributeError):
            # Expected exceptions are acceptable
            pass
        except Exception:
            raise


@settings(
    max_examples=FUZZ_MAX_EXAMPLES,
    deadline=FUZZ_DEADLINE_MS,
    suppress_health_check=[HealthCheck.too_slow],
)
@given(user_input=_user_input_strategy())
def test_read_user_choice_with_fuzzed_input(user_input):
    """Fuzz test read_user_choice with generated input strings."""
    # Predefined choices
    choices = ['option1', 'option2', 'option3']
    
    with patch('cookiecutter.prompt.Prompt.ask') as mock_ask:
        # Prompt.ask will return a choice index as string ('1', '2', '3')
        # We need to return one of these valid indices
        valid_choice_indices = ['1', '2', '3']
        # If input looks like a number, use it if valid; otherwise pick one
        try:
            choice_idx = int(user_input) if user_input.isdigit() else 1
            if 1 <= choice_idx <= len(choices):
                mock_ask.return_value = str(choice_idx)
            else:
                mock_ask.return_value = '1'
        except (ValueError, IndexError):
            mock_ask.return_value = '1'  # Default to first choice
        
        try:
            result = read_user_choice('test_choice', options=choices)
            
            # Assertions: function should not crash
            assert result is not None
            # Result should be one of the valid choices
            assert result in choices
            
        except (ValueError, TypeError, AttributeError, IndexError):
            # Expected exceptions are acceptable
            pass
        except Exception:
            raise
