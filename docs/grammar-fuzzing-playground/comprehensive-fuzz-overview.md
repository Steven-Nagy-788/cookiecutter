# Comprehensive Grammar-Based Fuzzing Overview

This document explains the complete suite of grammar-based fuzz tests added to Cookiecutter, covering CLI, template generation, and prompt handling.

## Overview

We have added four complementary fuzz test files:

1. **test_cli_grammar_fuzz.py** - Fuzzes CLI argument parsing
2. **test_generate_grammar_fuzz.py** - Fuzzes template generation with context data
3. **test_prompt_grammar_fuzz.py** - Fuzzes user input prompt handling
4. **test_json_context_fuzz.py** - Fuzzes JSON context loading, parsing, and conversion

Together, they cover the main functional pipeline of Cookiecutter: load JSON config → receive CLI args → prompt user for context → generate project files.

---

## 1. CLI Argument Fuzzing (test_cli_grammar_fuzz.py)

### What it tests

The CLI entry point and argument parsing without executing the full generation pipeline.

### Grammar

```
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
```

### Key properties tested

- CLI parser accepts arguments without crashing.
- Exit codes are in expected range: {0, 1, 2}.
- No Python tracebacks in output.
- Successful calls reach the cookiecutter main function.

### Sample generated inputs

```
['tests/fake-repo-pre/', '--no-input']
['tests/fake-repo-pre/', '-f', '--replay']
['tests/fake-repo-pre/', '--output-dir', 'tests/tmp-fuzz', '--accept-hooks=no']
```

### How to run

```bash
# Default (100 examples)
python -m pytest tests/test_cli_grammar_fuzz.py -q --hypothesis-show-statistics

# With tuning
CC_FUZZ_MAX_EXAMPLES=300 CC_FUZZ_DEADLINE_MS=400 HYPOTHESIS_SEED=7 \
  python -m pytest tests/test_cli_grammar_fuzz.py -q --hypothesis-show-statistics --cov=cookiecutter.cli
```

### Coverage insights

Currently reaches ~69% of [cookiecutter/cli.py](cookiecutter/cli.py). Missing lines include advanced option handling and error paths.

---

## 2. Template Generation Fuzzing (test_generate_grammar_fuzz.py)

### What it tests

The core template generation pipeline: taking context data and rendering template files.

### Grammar

```
context_entry: "cookiecutter." field_name "=" field_value

field_name: /[a-z_]+/

field_value: quoted_string
           | number
           | boolean

quoted_string: "\"" /[a-zA-Z0-9_\- ]*/ "\""
number: /[0-9]+/
boolean: "true" | "false"
```

### Key properties tested

- Context generation doesn't crash the rendering engine.
- Files are created without Python-level exceptions.
- Valid contexts produce usable output.
- Invalid contexts raise expected (caught) exceptions, not crashes.

### Sample generated contexts

```python
{'cookiecutter': {'project_name': 'my_project'}}
{'cookiecutter': {'version': '1', 'author': 'john'}}
{'cookiecutter': {'debug': 'true'}}
```

### How to run

```bash
# Default (50 examples, shorter timeout for file I/O)
python -m pytest tests/test_generate_grammar_fuzz.py -q --hypothesis-show-statistics

# With custom settings
CC_FUZZ_MAX_EXAMPLES=200 CC_FUZZ_DEADLINE_MS=500 \
  python -m pytest tests/test_generate_grammar_fuzz.py -q --hypothesis-show-statistics
```

### Coverage insights

Tests the critical path in [cookiecutter/generate.py](cookiecutter/generate.py) for context application and file rendering. Helps identify edge cases in Jinja2 template handling.

---

## 3. Prompt Input Fuzzing (test_prompt_grammar_fuzz.py)

### What it tests

User input parsing and validation across different prompt types.

### Grammar

```
input_value: text_input
           | choice_input
           | yes_no_input
           | empty_input

text_input: /[a-zA-Z0-9_\- ]{0,50}/
choice_input: /[a-zA-Z0-9]{1,20}/
yes_no_input: "yes" | "no" | "true" | "false" | "y" | "n" | "1" | "0"
empty_input: ""
```

### Key properties tested

- read_user_variable handles arbitrary text without crashing.
- read_user_yes_no correctly interprets yes/no variants.
- read_user_choice validates and returns from predefined options.
- No uncaught exceptions on edge-case inputs.

### Sample generated inputs

```
"my_project"
"yes"
"123"
"" (empty)
"no"
"my-project-v2"
```

### How to run

```bash
# Default (100 examples)
python -m pytest tests/test_prompt_grammar_fuzz.py -q --hypothesis-show-statistics

# With custom settings
CC_FUZZ_MAX_EXAMPLES=250 CC_FUZZ_DEADLINE_MS=400 \
  python -m pytest tests/test_prompt_grammar_fuzz.py -q --hypothesis-show-statistics
```

### Coverage insights

Tests prompt handling in [cookiecutter/prompt.py](cookiecutter/prompt.py), especially user input validation and choice selection logic.

---

## 4. JSON Context Fuzzing (test_json_context_fuzz.py)

### What it tests

The JSON loading, parsing, and context dictionary conversion pipeline in `generate_context()` and `apply_overwrites_to_context()` functions from [cookiecutter/generate.py](cookiecutter/generate.py).

### Grammar

```
JSON_STRING: ESCAPED_STRING
ESCAPED_STRING: /\"([^\"\\]|\\.)*\"/

value: SIGNED_INT | FLOAT | TRUE | FALSE | NULL | JSON_STRING | object | array

object: "{" [pair ("," pair)*] "}"
pair: JSON_STRING ":" value

array: "[" [value ("," value)*] "]"

start: object
```

### Property-based strategy

Generates valid Python dictionaries with:
- String, integer, float, boolean, and None values
- Nested objects and arrays
- Key names from a-z, 0-9, underscores
- Values with configurable depth and size

### Key properties tested

- **Valid JSON**: Property-based fuzz generates valid JSON→dict conversions
- **Grammar-fuzzed JSON**: Lark grammar generates valid JSON structures
- **Malformed JSON**: JSONDecodeError handling and graceful failures
- **Context merging**: `apply_overwrites_to_context()` properly merges context dicts
- **Deep nesting**: Handles arbitrary depth without stack overflow
- **Missing files**: Gracefully handles missing cookiecutter.json
- **Extra context**: CLI-provided extra_context merges correctly
- **Special keys**: Handles `_copy_without_render` and similar metadata keys

### Sample test cases

```python
# Property-based: valid JSON dict → context dict
context = {"name": "test", "version": 1, "features": ["a", "b"]}
result = generate_context(context_file)
assert "cookiecutter" in result
assert result["cookiecutter"]["name"] == "test"

# Grammar-fuzzed: Lark-generated JSON strings → dict
json_str = '{"project_name": "my_app", "author": "Jane", "year": 2024}'
result = apply_overwrites_to_context(context={}, overrides={"project_name": "new_app"})
assert result["project_name"] == "new_app"

# Malformed input: Invalid JSON handled gracefully
malformed = '{"invalid": "json syntax error"}'
try:
    generate_context(malformed_path)
except ContextDecodingException:
    pass  # Expected
```

### Coverage improvements

- `generate_context()`: 26% → 60% (with all 4 modules)
- `apply_overwrites_to_context()`: Added coverage for context merging logic
- JSON parsing path: Direct testing of json.load() and OrderedDict handling

---

## Running All Four Together

### Unified command

```bash
CC_FUZZ_MAX_EXAMPLES=200 CC_FUZZ_DEADLINE_MS=400 HYPOTHESIS_SEED=42 \
  python -m pytest tests/test_*_grammar_fuzz.py tests/test_json_context_fuzz.py -q --hypothesis-show-statistics --cov=cookiecutter
```

### With coverage report

```bash
CC_FUZZ_MAX_EXAMPLES=200 CC_FUZZ_DEADLINE_MS=400 HYPOTHESIS_SEED=42 \
  python -m pytest tests/test_*_grammar_fuzz.py tests/test_json_context_fuzz.py -q --hypothesis-show-statistics \
    --cov=cookiecutter --cov-report=html --cov-report=term-missing
```

### Make integration

If you use Make:

```bash
make fuzz-cli  # Runs only CLI fuzz test
```

For all fuzz tests, add to Makefile:

```makefile
.PHONY: fuzz-all
fuzz-all: ## Run all grammar-based fuzz tests
	@CC_FUZZ_MAX_EXAMPLES=$${CC_FUZZ_MAX_EXAMPLES:-200} \
	CC_FUZZ_DEADLINE_MS=$${CC_FUZZ_DEADLINE_MS:-400} \
	HYPOTHESIS_SEED=$${HYPOTHESIS_SEED:-} \
	python -m pytest tests/test_*_grammar_fuzz.py -q --hypothesis-show-statistics
```

---

## Understanding Results

Each test produces Hypothesis statistics:

- **passing examples**: Generated inputs that ran without assertion violations.
- **failing examples**: Inputs that violated a test property (bugs found!).
- **invalid examples**: Generated candidates rejected as out-of-domain (normal).

Example output:

```
tests/test_cli_grammar_fuzz.py::test_cli_grammar_fuzz_smoke:
  - 300 passing examples, 0 failing examples, 52 invalid examples
  
tests/test_generate_grammar_fuzz.py::test_generate_with_fuzzed_context:
  - 50 passing examples, 0 failing examples, 8 invalid examples
  
tests/test_prompt_grammar_fuzz.py::test_read_user_variable_with_fuzzed_input:
  - 100 passing examples, 0 failing examples, 15 invalid examples
```

### What to look for:

- 0 failing examples is good (no bugs found by fuzz test).
- Invalid examples being high is normal (grammar refinement can reduce this).
- Typical runtimes 1-10 ms per example are healthy.

---

## Design Philosophy

1. **Smoke tests first**: Each test checks stability before correctness.
   - Do we crash? (primary concern)
   - Do expected exceptions happen? (secondary)

2. **Grammar-driven**: Realistic but varied inputs from readable grammars.
   - Not random bytes.
   - Not hand-crafted corner cases.
   - Generated systematically from rules.

3. **Lightweight**: Runs in seconds, integrable into CI.
   - Small template structures.
   - Mocked I/O where helpful.
   - Configurable via environment variables.

4. **Portable**: Works across developer machines.
   - No absolute file paths in test code.
   - Environment variables for tuning.
   - Works with python from venv or system PATH.

---

## Next Steps

1. **Expand grammars**: Add more realistic option combinations, context variations, edge-case inputs.
2. **Track coverage over time**: Integrate fuzz runs into CI and monitor coverage trends.
3. **Reproduce and debug failures**: Use HYPOTHESIS_SEED to replay and minimize failing inputs.
4. **Tune thresholds**: Adjust max_examples and deadline based on CI constraints.

---

## Troubleshooting

### "Too many invalid examples"

The grammar is too restrictive or doesn't align with how Hypothesis generates.

**Solution**: Relax grammar rules, test small examples, check Hypothesis shrinking output.

### "Deadline exceeded"

Examples are taking longer than expected.

**Solution**: Increase CC_FUZZ_DEADLINE_MS or reduce CC_FUZZ_MAX_EXAMPLES.

### "Test hangs"

An example is stuck in an infinite loop or slow path.

**Solution**: Run with a shorter timeout, use HYPOTHESIS_SEED to isolate, add timeout logic.

### "Import errors for hypothesis/lark"

Dependencies not installed.

**Solution**: Ensure test dependencies are installed (hypothesis, lark in pyproject.toml).
