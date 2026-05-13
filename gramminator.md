# Grammarinator QA Report for Cookiecutter

This document records the Grammarinator-based fuzzing work done for the Cookiecutter repository, with a focus on `cookiecutter.json` parsing and the SSTI regression case you provided.

## What Was Built

Two ANTLR grammars were added under [fuzzer](fuzzer):

- [fuzzer/CookiecutterJSON.g4](fuzzer/CookiecutterJSON.g4)
- [fuzzer/CookiecutterSSTI.g4](fuzzer/CookiecutterSSTI.g4)

These are used to generate fuzz inputs with Grammarinator for:

- normal Cookiecutter-style JSON contexts
- SSTI-focused payloads that exercise the Jinja rendering path

Two runner scripts were also added:

- [fuzzer/execute_cookiecutter_json.py](fuzzer/execute_cookiecutter_json.py)
- [fuzzer/run_gramminator_cases.py](fuzzer/run_gramminator_cases.py)

The runner executes each generated sample in an isolated subprocess so payloads such as `os.abort()` are captured as crashes instead of killing the entire fuzz session.

## What Was Verified

The full Grammarinator flow was executed successfully in the project virtual environment:

1. Grammars were processed with `grammarinator-process`.
2. Sample corpora were generated for both grammars.
3. The generated samples were run through the Cookiecutter prompt/render pipeline.
4. A pytest was added to make the generated-corpus execution repeatable.
5. Coverage was computed with `pytest --cov`.

The new regression test is:

- [tests/test_grammarinator_generated_samples.py](tests/test_grammarinator_generated_samples.py)

## Commands Used

Process the grammars:

```bash
source .venv/bin/activate
grammarinator-process fuzzer/CookiecutterJSON.g4 -o fuzzer/gen/json
grammarinator-process fuzzer/CookiecutterSSTI.g4 -o fuzzer/gen/ssti
```

Generate samples:

```bash
mkdir -p fuzzer/samples/json fuzzer/samples/ssti

grammarinator-generate --sys-path fuzzer/gen/json \
  CookiecutterJSONGenerator.CookiecutterJSONGenerator \
  -r start -n 300 -d 15 \
  -o fuzzer/samples/json/sample_%d.json

grammarinator-generate --sys-path fuzzer/gen/ssti \
  CookiecutterSSTIGenerator.CookiecutterSSTIGenerator \
  -r start -n 100 -d 8 \
  -o fuzzer/samples/ssti/sample_%d.json
```

Run the generated samples:

```bash
/media/steven/MaD/projects/cookiecutter/.venv/bin/python fuzzer/run_gramminator_cases.py --samples "fuzzer/samples/json/*.json" --timeout 5
/media/steven/MaD/projects/cookiecutter/.venv/bin/python fuzzer/run_gramminator_cases.py --samples "fuzzer/samples/ssti/*.json" --timeout 5
```

Run the regression test with coverage:

```bash
/media/steven/MaD/projects/cookiecutter/.venv/bin/python -m pytest tests/test_grammarinator_generated_samples.py -q --cov=cookiecutter --cov-report=term-missing
```

## Results

The new pytest passed:

- `2 passed in 87.20s`

Coverage from that run was:

- overall: `20%`
- `cookiecutter/environment.py`: `83%`
- `cookiecutter/extensions.py`: `57%`
- `cookiecutter/prompt.py`: `50%`
- `cookiecutter/utils.py`: `45%`
- `cookiecutter/config.py`: `26%`

The other major modules remain at `0%` in this run because the generated-sample test does not call into the full CLI or repository download/generation pipeline.

## What Features This Fuzzing Hits

The fuzzing currently exercises the following behavior:

- `cookiecutter.generate_context` style JSON loading through the worker harness
- Jinja rendering of prompt defaults and nested values
- `create_env_with_context` and `StrictEnvironment` setup
- built-in extension loading and environment configuration paths
- `prompt_for_config` handling for strings, lists, dicts, booleans, and undefined-variable cases
- crash handling for SSTI payloads such as `os.abort()`

The sample runs surfaced expected edge conditions such as:

- malformed JSON samples
- undefined Jinja variables in generated values
- empty choice lists
- template syntax errors from aggressive SSTI payloads

Those failures are useful fuzz findings because they show the harness is reaching the intended render and error-handling code paths instead of only generating no-op inputs.

## Practical Interpretation

This setup is strongest for regression testing the prompt/render layer and SSTI exposure. It is not yet a full end-to-end CLI coverage suite, so modules like `cookiecutter.cli`, `cookiecutter.generate`, `cookiecutter.repository`, and `cookiecutter.hooks` remain mostly untouched by this particular corpus.

If you want broader feature coverage, the next step would be to add a second grammar or test harness that drives the CLI entry point and template download/generation pipeline as well.

## LLM Update: Coverage Boost Grammar

Using LLM to update the grammar, I added a new CLI-focused corpus in [fuzzer/coverage_boost](fuzzer/coverage_boost) to drive more of the Cookiecutter entrypoint than the original prompt/render-only samples.

### What Was Added

- [fuzzer/coverage_boost/CookiecutterCLIExpanded.g4](fuzzer/coverage_boost/CookiecutterCLIExpanded.g4)
- [fuzzer/coverage_boost/run_cli_corpus.py](fuzzer/coverage_boost/run_cli_corpus.py)
- [tests/test_grammarinator_cli_coverage_boost.py](tests/test_grammarinator_cli_coverage_boost.py)

This new grammar targets:

- `cookiecutter.cli.main`
- `cookiecutter.main.cookiecutter`
- `cookiecutter.config.get_user_config`
- `cookiecutter.repository.determine_repo_dir`
- `cookiecutter.generate.generate_context`
- `cookiecutter.generate.generate_files`
- `cookiecutter.main` replay and list-installed branches

### Commands Used

Process the new grammar:

```bash
mkdir -p fuzzer/coverage_boost/gen
/media/steven/MaD/projects/cookiecutter/.venv/bin/grammarinator-process fuzzer/coverage_boost/CookiecutterCLIExpanded.g4 -o fuzzer/coverage_boost/gen -v
```

Generate the new corpus:

```bash
mkdir -p fuzzer/coverage_boost/samples
/media/steven/MaD/projects/cookiecutter/.venv/bin/grammarinator-generate --sys-path fuzzer/coverage_boost/gen CookiecutterCLIExpandedGenerator.CookiecutterCLIExpandedGenerator -r start -n 40 -d 10 -o fuzzer/coverage_boost/samples/sample_%d.txt
```

Run the new corpus and compute coverage:

```bash
/media/steven/MaD/projects/cookiecutter/.venv/bin/python -m pytest tests/test_grammarinator_cli_coverage_boost.py -q --cov=cookiecutter --cov-report=term-missing
```

### New Result

This CLI-focused corpus passed and raised total package coverage from `20%` to `60%` in the dedicated run.

Key module coverage improvements from the new corpus:

- `cookiecutter/cli.py`: `77%`
- `cookiecutter/config.py`: `80%`
- `cookiecutter/generate.py`: `56%`
- `cookiecutter/hooks.py`: `42%`
- `cookiecutter/main.py`: `93%`
- `cookiecutter/prompt.py`: `53%`
- `cookiecutter/replay.py`: `84%`
- `cookiecutter/repository.py`: `74%`
- `cookiecutter/utils.py`: `68%`

### Interpretation

The original grammar set was good for prompt/render and SSTI regression behavior. The LLM-updated grammar expands the corpus into the real CLI and generation path, which is why the coverage jumped substantially.