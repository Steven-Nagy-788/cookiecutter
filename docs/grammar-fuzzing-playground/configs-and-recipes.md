# Fuzz Configs and Recipes

This page is a practical cheat sheet for tuning runs and understanding behavior.

## Environment knobs

The grammar fuzz test reads these environment variables:

- `CC_FUZZ_MAX_EXAMPLES`
  - Number of generated test inputs.
  - Higher value explores more combinations but takes longer.
- `CC_FUZZ_DEADLINE_MS`
  - Per-example runtime budget in milliseconds.
  - Increase if slow environments cause deadline noise.
- `HYPOTHESIS_SEED`
  - Makes data generation deterministic for replay.

## Fast local smoke

```bash
CC_FUZZ_MAX_EXAMPLES=50 CC_FUZZ_DEADLINE_MS=200 make fuzz-cli
```

Use this during active editing.

## Medium exploratory run

```bash
CC_FUZZ_MAX_EXAMPLES=300 CC_FUZZ_DEADLINE_MS=400 make fuzz-cli
```

Good balance of speed and behavior exploration.

## Reproducible run (seeded)

```bash
CC_FUZZ_MAX_EXAMPLES=300 CC_FUZZ_DEADLINE_MS=400 HYPOTHESIS_SEED=7 make fuzz-cli
```

Use this when discussing a result with teammates.

## Coverage-focused run

```bash
CC_FUZZ_MAX_EXAMPLES=300 CC_FUZZ_DEADLINE_MS=400 HYPOTHESIS_SEED=7 \
/home/seif/VV/cookiecutter/.venv/bin/python -m pytest \
  tests/test_cli_grammar_fuzz.py -q --hypothesis-show-statistics \
  --cov=cookiecutter.cli --cov-report=term-missing
```

## Understanding input vs output

The generated input is a list of CLI args derived from the grammar. For example:

```text
['tests/fake-repo-pre/', '--no-input']
['tests/fake-repo-pre/', '-f']
['tests/fake-repo-pre/', '--replay-file', 'tests/test-replay/valid_replay.json']
```

Observed output can vary by mode:

- exit `0`: valid non-interactive path
- exit `1`: runtime-level expected CLI error or interactive path interruption
- exit `2`: usage/argument parsing issue from click

The test treats these as expected classes of outcomes and mainly guards against Python-level crashes.

## Integrating with CLI scripts

Current integration points:

- Make target: `make fuzz-cli`
- Just recipe: `just fuzz-cli` (if `just` exists)

If your shell scripts already call Make targets, adding `make fuzz-cli` is the simplest integration path.

## Troubleshooting quick notes

- If pip is missing in the venv, bootstrap it first:

```bash
/home/seif/VV/cookiecutter/.venv/bin/python -m ensurepip --upgrade
```

- If `just` is missing, use Make target instead.
- If many examples are invalid, refine grammar structure or option compatibility rules.

copying assets... 