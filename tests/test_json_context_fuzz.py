"""
Grammar and property-based fuzz tests for cookiecutter.json loading and parsing.

Tests the JSON loading, parsing, and context dictionary conversion pipeline.
"""

from __future__ import annotations

import json
import os
import tempfile
from pathlib import Path
from unittest.mock import patch

import pytest
from hypothesis import HealthCheck, given, settings, strategies as st
from hypothesis.extra.lark import from_lark
from lark import Lark

from cookiecutter.generate import generate_context, apply_overwrites_to_context
from cookiecutter.exceptions import ContextDecodingException


# Property-based test: Generate valid JSON context structures
@st.composite
def json_context_strategy(draw):
    """Generate valid cookiecutter context structures."""
    # Generate simple key-value pairs
    keys = draw(
        st.lists(
            st.text(
                alphabet='abcdefghijklmnopqrstuvwxyz_',
                min_size=1,
                max_size=20
            ),
            min_size=1,
            max_size=10,
            unique=True
        )
    )
    
    values = []
    for _ in keys:
        value_choice = draw(st.integers(0, 2))
        if value_choice == 0:
            # String value
            values.append(draw(st.text(max_size=50)))
        elif value_choice == 1:
            # Integer value
            values.append(draw(st.integers(min_value=0, max_value=9999)))
        else:
            # Boolean value
            values.append(draw(st.booleans()))
    
    return dict(zip(keys, values))


FUZZ_MAX_EXAMPLES = int(os.getenv('CC_FUZZ_MAX_EXAMPLES', '100'))
FUZZ_DEADLINE_MS = int(os.getenv('CC_FUZZ_DEADLINE_MS', '500'))


# Grammar for JSON context structures
JSON_CONTEXT_GRAMMAR = r"""
start: json_object

json_object: "{" json_pair ("," json_pair)* "}"
           | "{" "}"

json_pair: json_string ":" json_value

json_string: "\"" /[a-z_]+/ "\""

json_value: json_string
          | json_number
          | json_boolean
          | json_array

json_array: "[" json_value ("," json_value)* "]"
          | "[" "]"

json_number: /[0-9]+/

json_boolean: "true" | "false"

%import common.WS
%ignore WS
"""


def _json_grammar_strategy():
    """Generate JSON-like strings from grammar."""
    parser = Lark(JSON_CONTEXT_GRAMMAR, start='start', parser='lalr')
    return from_lark(parser)


@settings(
    max_examples=FUZZ_MAX_EXAMPLES,
    deadline=FUZZ_DEADLINE_MS,
    suppress_health_check=[HealthCheck.too_slow],
)
@given(context=json_context_strategy())
def test_generate_context_with_valid_json_property(context):
    """Property test: generate_context handles valid context dicts."""
    with tempfile.TemporaryDirectory() as tmpdir:
        context_file = Path(tmpdir) / 'cookiecutter.json'
        
        # Write context as JSON
        with open(context_file, 'w', encoding='utf-8') as f:
            json.dump(context, f)
        
        # Should not crash and should load successfully
        result = generate_context(str(context_file))
        
        # Assertions
        assert result is not None
        assert 'cookiecutter' in result
        assert isinstance(result['cookiecutter'], dict)
        # All original keys should be present
        for key in context:
            assert key in result['cookiecutter']


@settings(
    max_examples=FUZZ_MAX_EXAMPLES,
    deadline=FUZZ_DEADLINE_MS,
    suppress_health_check=[HealthCheck.too_slow],
)
@given(json_str=_json_grammar_strategy())
def test_generate_context_with_grammar_fuzzed_json(json_str):
    """Grammar test: generate_context handles grammar-generated JSON strings."""
    with tempfile.TemporaryDirectory() as tmpdir:
        context_file = Path(tmpdir) / 'cookiecutter.json'
        
        # Write grammar-generated content
        with open(context_file, 'w', encoding='utf-8') as f:
            f.write(json_str)
        
        try:
            # Attempt to load
            result = generate_context(str(context_file))
            
            # If successful, validate structure
            assert result is not None
            assert 'cookiecutter' in result
            assert isinstance(result['cookiecutter'], dict)
            
        except (json.JSONDecodeError, ContextDecodingException, ValueError):
            # Expected for some edge-case grammar outputs
            # (e.g., unterminated strings, trailing commas)
            pass
        except Exception as e:
            # Unexpected exceptions should not occur
            # File not found or similar I/O is expected
            if 'No such file' not in str(e):
                raise


@settings(
    max_examples=50,
    deadline=FUZZ_DEADLINE_MS,
    suppress_health_check=[HealthCheck.too_slow],
)
@given(
    context=json_context_strategy(),
    default_context=json_context_strategy(),
)
def test_apply_overwrites_to_context_property(context, default_context):
    """Property test: apply_overwrites_to_context merges contexts safely."""
    # Make a copy to track mutations
    original_context = context.copy()
    
    try:
        # Apply overwrites
        apply_overwrites_to_context(context, default_context)
        
        # After overwrite, context should still contain original keys
        # (unless they were overwritten)
        for key in original_context:
            assert key in context
            
    except (ValueError, KeyError, TypeError):
        # Expected for some edge cases (e.g., type mismatches)
        pass


@settings(
    max_examples=30,
    deadline=FUZZ_DEADLINE_MS,
    suppress_health_check=[HealthCheck.too_slow],
)
@given(
    malformed_json=st.text(
        alphabet='{""\':[]0123456789,\\n\t ',
        min_size=1,
        max_size=100
    )
)
def test_generate_context_with_malformed_json(malformed_json):
    """Test that malformed JSON raises appropriate exceptions."""
    with tempfile.TemporaryDirectory() as tmpdir:
        context_file = Path(tmpdir) / 'cookiecutter.json'
        
        with open(context_file, 'w', encoding='utf-8') as f:
            f.write(malformed_json)
        
        try:
            result = generate_context(str(context_file))
            # If it parses, should have cookiecutter key
            if result:
                assert 'cookiecutter' in result
        except (json.JSONDecodeError, ContextDecodingException, ValueError):
            # Expected for malformed JSON
            pass


def test_generate_context_with_nested_deeply_nested_context():
    """Test that deeply nested JSON contexts are handled."""
    deep_context = {'cookiecutter': {'a': 1}}
    # Build a deeply nested structure
    current = deep_context['cookiecutter']
    for i in range(10):
        current[f'level_{i}'] = {'nested': i}
        current = current[f'level_{i}']
    
    with tempfile.TemporaryDirectory() as tmpdir:
        context_file = Path(tmpdir) / 'cookiecutter.json'
        
        with open(context_file, 'w', encoding='utf-8') as f:
            json.dump(deep_context['cookiecutter'], f)
        
        # Should handle deep nesting without crashing
        result = generate_context(str(context_file))
        assert result is not None
        assert 'cookiecutter' in result


def test_generate_context_missing_file():
    """Test that missing file raises appropriate error."""
    with pytest.raises((FileNotFoundError, OSError)):
        generate_context('/nonexistent/path/cookiecutter.json')


def test_generate_context_with_extra_context():
    """Test context generation with extra_context parameter."""
    with tempfile.TemporaryDirectory() as tmpdir:
        context_file = Path(tmpdir) / 'cookiecutter.json'
        
        base_context = {'project_name': 'myproject', 'version': '1.0.0'}
        with open(context_file, 'w', encoding='utf-8') as f:
            json.dump(base_context, f)
        
        extra = {'project_name': 'override_project'}
        
        result = generate_context(
            str(context_file),
            extra_context=extra
        )
        
        assert result is not None
        assert result['cookiecutter']['project_name'] == 'override_project'
        assert result['cookiecutter']['version'] == '1.0.0'


def test_generate_context_with_special_keys():
    """Test that special keys (starting with _) are handled."""
    with tempfile.TemporaryDirectory() as tmpdir:
        context_file = Path(tmpdir) / 'cookiecutter.json'
        
        context = {
            'project_name': 'test',
            '_private': 'hidden',
            '_copy_without_render': ['*.txt'],
        }
        
        with open(context_file, 'w', encoding='utf-8') as f:
            json.dump(context, f)
        
        result = generate_context(str(context_file))
        
        assert result is not None
        assert '_private' in result['cookiecutter']
        assert '_copy_without_render' in result['cookiecutter']
