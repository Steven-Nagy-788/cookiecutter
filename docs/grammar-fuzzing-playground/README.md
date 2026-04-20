# Grammar-Based Fuzzing for Cookiecutter CLI

This folder is a practical walkthrough for adding and using a grammar-based fuzzer in this repository.

It is intentionally written as plain Markdown notes, not in the Sphinx/reStructuredText style used in the rest of the docs.

## What we wanted

- Choose a grammar-based fuzzer that fits this Python project.
- Run it against Cookiecutter CLI behavior.
- Understand generated input and observed output.
- Tune fuzzing configuration.
- Check coverage.
- Integrate fuzzing into an existing CLI-oriented workflow.

## Why this fuzzer choice

We chose Hypothesis + Lark.

- Hypothesis integrates directly with pytest.
- Lark gives readable grammars for CLI argument generation.
- Hypothesis can replay failures with a seed and shrinking.
- This keeps everything in Python and inside the existing test toolchain.

## What was added in the repo

- Test dependencies added in `pyproject.toml`: `hypothesis`, `lark`.
- Grammar fuzz smoke test: `tests/test_cli_grammar_fuzz.py`.
- Task integration:
  - `make fuzz-cli`
  - `just fuzz-cli` (if `just` is installed)

## First simple grammar (integration smoke)

The first grammar is intentionally small and conservative. It starts from one known template path and generates combinations of CLI flags:

- `--no-input`
- `--replay`
- `-v`
- `-f`
- `--overwrite-if-exists`
- `--default-config`
- `--accept-hooks=yes`
- `--accept-hooks=no`
- `-o tests/tmp-fuzz`
- `--output-dir tests/tmp-fuzz`
- `--replay-file tests/test-replay/valid_replay.json`

This is enough to verify that grammar generation and CLI invocation are wired together correctly.

## What the fuzz test asserts

The smoke test is designed to detect crashes and unstable behavior first:

- Accepts expected CLI exit codes: `0`, `1`, or `2`.
- Rejects Python tracebacks in output.
- If exit is `0`, verifies the CLI reached the call into `cookiecutter.cli.cookiecutter`.

## How to run

Run with Make (works on this machine):

```bash
make fuzz-cli
```

Run directly with pytest:

```bash
/home/seif/VV/cookiecutter/.venv/bin/python -m pytest \
  tests/test_cli_grammar_fuzz.py -q --hypothesis-show-statistics
```

## How to read results quickly

Hypothesis statistics tell you:

- passing examples: generated inputs that satisfy assertions
- invalid examples: generated inputs rejected by assumptions/strategy path constraints
- stop reason: usually `settings.max_examples`

A healthy smoke run here looked like:

- `200` passing examples
- `0` failures
- `40` invalid examples

## Coverage check

To focus on CLI coverage while fuzzing:

```bash
CC_FUZZ_MAX_EXAMPLES=300 CC_FUZZ_DEADLINE_MS=400 HYPOTHESIS_SEED=7 \
/home/seif/VV/cookiecutter/.venv/bin/python -m pytest \
  tests/test_cli_grammar_fuzz.py -q --hypothesis-show-statistics \
  --cov=cookiecutter.cli --cov-report=term-missing
```

A representative run reached around `69%` for `cookiecutter/cli.py` with the starter grammar.

## What to do next

1. Expand grammar options to include more mutually-exclusive and edge-case flag combinations.
2. Add extra-context tokens once a safe generation format is defined.
3. Add a CI job for `make fuzz-cli` as a non-blocking stage first.
4. Promote it to blocking once runtime and stability are comfortable.

See `configs-and-recipes.md` for tuning knobs and repeatable recipes.
