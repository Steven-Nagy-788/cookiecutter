# Grammarinator grammars for cookiecutter.json fuzzing

This folder contains ANTLR grammars and runners for fuzzing `cookiecutter.json` inputs.

## Files

- `CookiecutterJSON.g4`: General cookiecutter-like JSON object grammar.
- `CookiecutterSSTI.g4`: Focused grammar for SSTI payload regression cases.
- `execute_cookiecutter_json.py`: Worker that loads and renders one JSON input.
- `run_gramminator_cases.py`: Batch runner with per-sample subprocess isolation.

## 1) Install tools

```bash
source .venv/bin/activate
pip install grammarinator antlr4-tools
```

## 2) Build generators from ANTLR

```bash
antlr4 -Dlanguage=Python3 -visitor fuzzer/CookiecutterJSON.g4
antlr4 -Dlanguage=Python3 -visitor fuzzer/CookiecutterSSTI.g4

# Convert ANTLR grammars into Grammarinator generators
grammarinator-process fuzzer/CookiecutterJSON.g4 -o fuzzer/gen/json
grammarinator-process fuzzer/CookiecutterSSTI.g4 -o fuzzer/gen/ssti
```

## 3) Generate fuzz samples

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

## 4) Execute samples against Cookiecutter context/prompt pipeline

/media/steven/MaD/projects/cookiecutter/.venv/bin/python fuzzer/run_gramminator_cases.py --samples "fuzzer/samples/json/*.json" --timeout 5
/media/steven/MaD/projects/cookiecutter/.venv/bin/python fuzzer/run_gramminator_cases.py --samples "fuzzer/samples/ssti/*.json" --timeout 5

If a payload terminates the process (for example `os.abort()`), the batch runner reports it as `CRASH signal=...`.
