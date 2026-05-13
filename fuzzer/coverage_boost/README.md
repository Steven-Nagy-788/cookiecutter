# Coverage boost corpus

This directory was added by an LLM update to broaden the Grammarinator-based fuzzing surface beyond the original prompt/render corpus.

It focuses on the real Cookiecutter CLI entrypoint so the generated inputs can hit more of:

- `cookiecutter.cli`
- `cookiecutter.main`
- `cookiecutter.config`
- `cookiecutter.repository`
- `cookiecutter.generate`

## Workflow

1. Process the grammar with Grammarinator.
2. Generate command samples into this directory.
3. Run the samples through the CLI runner.
4. Compute coverage with `pytest --cov`.

## Grammar

- [CookiecutterCLIExpanded.g4](CookiecutterCLIExpanded.g4)

## Runner

- [run_cli_corpus.py](run_cli_corpus.py)