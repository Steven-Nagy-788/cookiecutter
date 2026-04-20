# How to Use Cookiecutter

## Overview

Cookiecutter is a command-line tool that **rapidly generates project templates** from pre-configured "cookiecutters" (template directories). It's commonly used to create Python packages, but works for any project type.

---

## How Cookiecutter Works

### High-Level Workflow

1. **Load Config** → Read user settings from `~/.cookiecutterrc`
2. **Find Template** → Locate local template or clone from GitHub/GitLab/Bitbucket
3. **Read Template** → Parse `cookiecutter.json` to extract configuration variables
4. **Run Pre-Prompt Hook** → Execute custom setup logic if defined
5. **Prompt User** → Ask interactive questions to fill template variables
6. **Run Pre-Generation Hook** → Execute custom logic before rendering
7. **Render Files** → Use Jinja2 to substitute variables in file names and content
8. **Run Post-Generation Hook** → Execute cleanup/finalization scripts
9. **Clean Up** → Remove temporary directories

### Key Modules

| Module | Purpose |
|--------|---------|
| **cli.py** | Click-based command-line interface with options like `--no-input`, `--replay`, `--checkout` |
| **main.py** | Core orchestrator that coordinates the entire workflow |
| **generate.py** | Renders templates: loads context, generates files with Jinja2, handles binary vs text files |
| **prompt.py** | Interactive user prompts for string, choice, and boolean variables |
| **repository.py** | Locates/fetches templates (local, GitHub, GitLab, Bitbucket, ZIP files) |
| **config.py** | Loads and merges user configuration from `~/.cookiecutterrc` |
| **hooks.py** | Executes pre/post-generation scripts (Python or shell) |
| **environment.py** | Sets up Jinja2 with custom extensions (jsonify, slugify, uuid, datetime, random) |
| **utils.py** | Helper utilities (file operations, directory creation, cleanup) |

### Architecture

Cookiecutter follows a **pipeline architecture** with clear separation of concerns:

```
┌─────────────────────────────────────────────────────────────┐
│                      CLI Layer (cli.py)                     │
│              Click-based command parsing                    │
└──────────────────────┬──────────────────────────────────────┘
                       │
┌──────────────────────▼──────────────────────────────────────┐
│                Orchestration Layer (main.py)                │
│          Coordinates the entire workflow                    │
└─────────┬────────────┬────────────┬────────────┬────────────┘
          │            │            │            │
    ┌─────▼──┐   ┌─────▼──┐   ┌────▼────┐   ┌──▼──────┐
    │ Config │   │ Repo   │   │ Context │   │ Prompt  │
    │(config)│   │(repo.py)   │(generate)   │(prompt) │
    └────────┘   └────────┘   └─────┬──┘   └────┬────┘
                                     │           │
                    ┌────────────────▼─────┬─────▼──────┐
                    │    File Generation   │   Hooks    │
                    │   (generate.py)      │ (hooks.py) │
                    └─────────────────────┬────────────┘
                                          │
                    ┌─────────────────────▼────────────┐
                    │    Jinja2 Environment            │
                    │   (environment.py)               │
                    └────────────────────────────────┘
```

### Execution Flow

```
┌─ __main__.py (root)
   │
   └─→ cookiecutter.cli:main()
       │
       ├─→ [Parse CLI arguments using Click]
       │
       └─→ cookiecutter.main:cookiecutter()
           │
           ├─→ get_user_config()
           ├─→ determine_repo_dir()
           │   ├─→ is_repo_url() / is_zip_file()
           │   ├─→ expand_abbreviations()
           │   ├─→ clone() OR use local dir
           │   └─→ repository_has_cookiecutter_json()
           │
           ├─→ run_pre_prompt_hook() [if accept_hooks]
           │
           ├─→ generate_context()
           │   └─→ Load and parse cookiecutter.json
           │
           ├─→ prompt_for_config() [unless --no-input or --replay]
           │
           ├─→ generate_files()
           │   ├─→ create_env_with_context()
           │   ├─→ find_template()
           │   ├─→ render_and_create_dir() [render output dir name]
           │   ├─→ run_hook_from_repo_dir('pre_gen_project')
           │   ├─→ Walk template tree:
           │   │   ├─→ generate_file() for each file
           │   │   └─→ Handle binary vs. text rendering
           │   └─→ run_hook_from_repo_dir('post_gen_project')
           │
           ├─→ dump() [Save replay data]
           │
           └─→ rmtree() [Cleanup temporary directories if needed]
```

---

## How to Run Cookiecutter

### Prerequisites

The project uses a virtual environment (`.venv`). Ensure it's activated:

```bash
source .venv/bin/activate
```

**Important**: Before using the CLI, install the project in editable mode:

```bash
python -m pip install -e .
```

This installs cookiecutter as a CLI tool in your environment, making the `cookiecutter` command available.

### Using as a CLI Tool

#### Use a GitHub-hosted template with interactive prompts

```bash
cookiecutter gh:audreyfeldroy/cookiecutter-pypackage
```

#### Use a local template

```bash
cookiecutter path/to/template/
```

#### Skip prompts and use defaults

```bash
cookiecutter --no-input gh:audreyfeldroy/cookiecutter-pypackage
```

#### Reuse previous answers

```bash
cookiecutter --replay gh:audreyfeldroy/cookiecutter-pypackage
```

#### Output to specific directory

```bash
cookiecutter --output-dir ~/Projects/ gh:audreyfeldroy/cookiecutter-pypackage
```

#### Common CLI Options

- `--no-input` → Skip all prompts and use default values
- `--replay` → Reuse answers from previous runs (stored in `~/.cookiecutter_replay/`)
- `--output-dir DIR` → Specify output directory (default: current directory)
- `--overwrite-if-exists` → Overwrite existing project directory
- `--skip-if-file-exists` → Skip files that already exist
- `--checkout BRANCH` → Check out a specific git branch/tag/commit
- `--config-file FILE` → Use a custom config file instead of `~/.cookiecutterrc`
- `--directory DIR` → Directory within repository to use as template

### Using Programmatically (in Python)

```python
from cookiecutter.main import cookiecutter

# Generate from local template
cookiecutter('path/to/cookiecutter-template/')

# Generate from GitHub
cookiecutter('gh:audreyfeldroy/cookiecutter-pypackage')

# With custom options
cookiecutter(
    'gh:audreyfeldroy/cookiecutter-pypackage',
    no_input=True,
    output_dir='~/Projects/',
    extra_context={'project_name': 'my_project'}
)
```

---

## How to Run Tests

The test suite uses **pytest** with coverage reporting.

### Prerequisites

Ensure dependencies are installed:

```bash
python -m pip install -e ".[test]"
```

Or use `uv` (recommended):

```bash
uv sync --group test
```

### Quick Test Run (Current Python Version)

Run all tests with verbose output and coverage:

```bash
pytest
```

Run a specific test file:

```bash
pytest tests/test_cli.py
```

Run a specific test:

```bash
pytest tests/test_cli.py::test_click_version
```

Run with coverage report:

```bash
pytest --cov-report=html
```

### Using Justfile (Recommended)

The project includes a `justfile` with helpful shortcuts:

```bash
# Run tests for current Python version (3.13) with coverage
just coverage

# Run tests for all supported Python versions (3.10-3.14)
just test-all

# Run linting
just lint

# View all available commands
just list
```

### Using UV Directly

Run tests with a specific Python version:

```bash
# Run with Python 3.13
uv run --python=3.13 --isolated --group test -- pytest

# Run with Python 3.12
uv run --python=3.12 --isolated --group test -- pytest

# Run with coverage report (HTML)
uv run --python=3.13 --isolated --group test -- pytest --cov-report=html --cov-report=xml --cov-branch
```

### Test Organization

Key test files in `tests/`:

| Test File | Purpose |
|-----------|---------|
| `test_cli.py` | CLI argument parsing and options |
| `test_main.py` | Core workflow orchestration |
| `test_generate_files.py` | File rendering and template generation |
| `test_prompt.py` | User input prompts |
| `test_hooks.py` | Hook execution (pre/post generation) |
| `test_cookiecutter_local_with_input.py` | End-to-end local template with prompts |
| `test_environment.py` | Jinja2 environment and extensions |
| `test_abort_generate_on_hook_error.py` | Error handling and hook failures |
| `test_read_user_*.py` | Various input prompt types |

### Coverage Requirements

The project enforces **100% test coverage**. When running coverage checks, the build will fail if coverage drops below 100%:

```bash
pytest --cov=cookiecutter --cov-report=term-missing --cov-fail-under=100
```

---

## Project Dependencies

| Dependency | Version | Purpose |
|-----------|---------|---------|
| **Jinja2** | ≥2.7, <4.0 | Template rendering engine |
| **Click** | ≥7.0, <9.0 | CLI framework for commands/options |
| **binaryornot** | ≥0.4.4 | Detect binary vs. text files |
| **pyyaml** | ≥5.3.1 | Parse YAML config files |
| **python-slugify** | ≥4.0.0 | Generate URL-safe slugs from strings |
| **requests** | ≥2.23.0 | HTTP library for repository access |
| **arrow** | Latest | Date/time utilities for templates |
| **rich** | Latest | Terminal output formatting (prompts, colors) |

**Dev Dependencies:**
- `pytest` → Test runner
- `pytest-cov` → Coverage reporting
- `pytest-mock` → Mocking utilities
- `freezegun` → Time mocking for tests
- `ruff` → Linting and formatting

---

## Troubleshooting

### `PackageNotFoundError: cookiecutter` when running CLI

This occurs because `cookiecutter/__init__.py` reads the package version using `importlib.metadata`. 

**Solution**: Install the package in editable mode:

```bash
python -m pip install -e .
```

### Tests fail with import errors

Ensure test dependencies are installed:

```bash
python -m pip install -e ".[test]"
```

### Want to develop with editable install + dependencies

```bash
python -m pip install -e ".[dev,test]"
```

---

## Key Takeaways

- **CLI tool**: Create projects from templates interactively or programmatically
- **Jinja2-powered**: Render any text-based files with variables  
- **Extensible**: Pre/post-generation hooks for custom logic
- **Config-driven**: `cookiecutter.json` defines the template interface
- **Well-tested**: 100% test coverage requirement enforced
- **Multi-language**: Templates work with any language or markup format
- **Cross-platform**: Works on Windows, Mac, and Linux
