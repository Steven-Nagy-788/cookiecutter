# Cookiecutter Testing Plan

## 1. Functionality Overview

The Cookiecutter codebase is a robust templating utility designed to ingest configurations, fetch template repositories, prompt users, and render directory structures. The core functionalities identified in the codebase are:

1. **CLI & User Interaction (`cli.py`, `prompt.py`)**: 
   - Parses CLI arguments (`--no-input`, `--checkout`, `--directory`, etc.).
   - Reads global config and project-specific `cookiecutter.json`.
   - Prompts the user interactively via terminal for context values, supporting strings, booleans, and dictionaries.
2. **State & Configuration (`config.py`, `replay.py`)**: 
   - Merges default settings with a user's `~/.cookiecutterrc`.
   - Caches completed contexts and replays them to bypass prompts on subsequent runs.
3. **Template Discovery & Fetching (`repository.py`, `vcs.py`, `zipfile.py`, `find.py`)**: 
   - Downloads/Clones templates from Github, Gitlab, or Bitbucket.
   - Handles password authentication for remote cloning.
   - Extracts ZIP archives.
   - Navigates nested directory structures to find the actual `cookiecutter.json` boundary.
4. **Generation & Templating (`generate.py`, `environment.py`, `extensions.py`)**: 
   - Integrates Jinja2 to render directories and files.
   - Provides text extensions (e.g. `jsonify`, `slugify`).
5. **Hooks & Events (`hooks.py`)**: 
   - Executes user-defined Python or Shell scripts before and after directory rendering.

## 2. Existing Test Coverage Analysis

A thorough audit of the `/tests` directory reveals that Cookiecutter maintains a healthy, established test suite utilizing `pytest`:

**What is well tested:**
- **Nominal Workflows**: Rendering contexts (`test_generate_files.py`, `test_main.py`).
- **CLI Flags**: Behavior toggles via arg parsing (`test_cli.py`).
- **Hooks**: Error handling and abort sequences on Python and Shell scripts (`test_hooks.py`, `test_abort_generate_on_hook_error.py`).
- **Inputs**: Extensive test isolation on reading different variable types via shell (`test_prompt.py`, `test_read_user_yes_no.py`).
- **File System Handling**: File permissions, nested templates, and line endings.

**Critical Gaps (Lacking coverage):**
- **Fuzzing & Malformed Constructs**: Lack of unstructured automated mutation inputs. The suite assumes largely 'correct' or 'slightly incorrect' JSON structures in templates.
- **Race conditions & concurrency**: Edge cases involving git clones on high-latency networks or colliding temp-directories.
- **Static Analysis Flow Isolation**: Testing intermediate states of parsed Jinja macros and definitions prior to actual rendering.

## 3. White Box Testing Strategy

Applying structural testing at the source code level to evaluate the internal logic pathways.

### 3.1 Reaching Definitions & Data Flow
When a variable is assigned a value (definition), we want to test every path that uses this variable. 
- **Context Generation Flow**: Trace the generation of the `context` dictionary.
  - **Start**: `config.py` definitions.
  - **Intermediate**: `prompt.py` mutates context values based on default values vs user inputs vs replay configurations. 
  - **Sink**: `generate.generate_files()` consumes this variable.
  - **Test Objective**: Write data-flow specific tests asserting that if a value is defined in `~/.cookiecutterrc`, but overridden in `.json`, and *then* overridden by user input, the output reflects the precise final re-definition.
- **Hook Paths Context**: Ensure variables injected into `hooks.py` execution environment strictly match the post-prompt final definitions.

### 3.2 Available Expressions & Optimization Validation
Jinja2 extensions (`environment.py`) implement macros and formatting expressions across huge templates.
- **Test Objective**: Create structural unit tests verifying that standard regex expressions or text manipulation elements (`slugify` filters) correctly cache or process massive text blobs without failing recursively. Check that templates with heavily duplicated variables only compile/fetch those expressions efficiently.

## 4. Black Box & ISP (Input Space Partitioning) Strategy

Testing against the domain boundaries without knowledge of internal paths.

### 4.1 Equivalence Partitioning (Partitioning User Inputs)
The prompt inputs (`prompt.py`) accept various data structures. 
- **Partition 1 (Primitive)**: Strings, numerics, unicode strings.
- **Partition 2 (Boolean)**: Y, y, N, n, true, false variations.
- **Partition 3 (Dictionaries/Choices)**: Numbered array selections.
- **Test Objective**: Ensure exactly one test targets the inner boundary of each of these equivalence partitions.

### 4.2 Boundary Value Analysis
- **Filenames**: Max OS filename characters.
- **Recursion**: Provide nested directories exactly at the Windows maximum path limit edge cases (260 characters).
- **Template Context Depth**: Providing deeply nested JSON dictionaries in `cookiecutter.json` (e.g., nesting level 10, 50, 100). Check where recursive limit boundary fails.

### 4.3 Domain Modeling (System Context Tests)
- Create a test matrix that targets combinations of:
  - Repository Type (Local / Github Git / Gitlab Hg / ZIP Archive)
  - Output Target (Local Mount / Network Drive / Symlink Dir)
  - Config Method (Replay / CLI Args / Interactive shell)
  - *Goal*: Test combinations that don't logically contradict (e.g. Git clone onto a symlink using Replay configuration).

## 5. Fuzzing Strategy

Automating input generation to discover obscure programmatic crashes, specifically focused on external dependencies (Jinja & JSON parser) and input limits.

### 5.1 Tools Proposed
- **Hypothesis**: For property-based Python testing.
- **Atheris**: For coverage-guided mutation fuzzing.

### 5.2 Targets for Fuzzing
1. **JSON Parser Fuzzing (`cookiecutter.json`)**:
   - Provide heavily mutated malformed `.json` configurations (corrupted keys, mismatched brackets, infinite self-referencing values).
   - Ensure the application fails gracefully using custom `exceptions.py` rather than hard core-dumps or raw exceptions.
2. **Template Compilation Fuzzing (`generate.py`)**:
   - Insert thousands of randomized Jinja2 tags (`{% ... %}`, `{{ ... }}`) containing invalid, nested, or recursive filters into a fake template text file.
   - Assert that `environment.py` safely yields `UndefinedVariableInTemplate` rather than hanging the server and consuming 100% CPU (ReDoS).
3. **CLI Arguments Fuzzing**:
   - Supply randomly generated UTF-16, emojis, or massive byte arrays to the `--checkout` or `--directory` flags. Limit length out-of-bounds validations.

## 6. Execution Timeline & CI/CD Integration

To rollout this complete plan:
1. Initialize **Hypothesis** in the `pyproject.toml` and write property-based tests for `prompt.py`.
2. Map data flow (White box) explicitly missing in `generate.py` via standard PyTest runs.
3. Integrate Atheris fuzzing templates into GitHub Actions on a weekly schedule (given fuzzing computationally is expensive to run on every commit).
