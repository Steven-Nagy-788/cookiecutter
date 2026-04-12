# Cookiecutter Architecture

Cookiecutter is a command-line utility that creates projects from project templates (cookiecutters). 

## Core Concepts

1. **Input**: A template directory (either local or cloned from a VCS like git/hg, or a zip archive). The template contains:
   - A `cookiecutter.json` file defining prompts and default values.
   - A parameterized directory (e.g., `{{ cookiecutter.project_name }}/`) containing the template files.
   - Optional hooks (pre-gen and post-gen scripts), executed prior to or after generation.
2. **Context Generation**: Cookiecutter reads the configuration, prompts the user for contextual inputs, or retrieves context from a replay file for reproducibility without prompting. It also merges this against user defaults from `.cookiecutterrc`.
3. **Output Generation**: Using the compiled user context, it applies a templating engine (Jinja2) to copy files and resolve template variables, producing a finalized output directory structure.

## Key Modules

### Entrypoints
- `cli.py`: The command-line entrypoint. Parses arguments using `click` and triggers the main application logic.
- `main.py`: Exposes the main `cookiecutter()` function. It coordinates downloading the template, constructing the context, prompting the user, and generating the files.
- `__main__.py` & `__init__.py`: Package initialization and execution wrapper for module-level runs (`python -m cookiecutter`).

### Configuration & Context
- `config.py`: Handles loading user configuration (like `~/.cookiecutterrc`) and merging it into a settings dictionary. 
- `prompt.py`: Parses `cookiecutter.json` and optionally prompts the user interactively (e.g., using `click`) for template variables, allowing dynamic contextual configuration.
- `replay.py`: Caches user input selections into a JSON file, providing functionality to identically execute past generic runs seamlessly without reprompting.

### Repositories & Fetching
- `repository.py`: Determines if the template is local or remote, and delegates to the appropriate fetcher module.
- `vcs.py`: Handles cloning of remote templates from version control systems (Git or Mercurial).
- `zipfile.py`: Handles unzipping and staging zip-based template archives.
- `find.py`: Helper functionality navigating through a resolved template repo to locate the actual project template folder and `cookiecutter.json`.

### Generation & Rendering
- `generate.py`: Handles rendering the templated paths and file contents. It parses files within the template relying on Jinja2, handling context merges and directory setup.
- `environment.py`: Configuration and initialization of the Jinja2 rendering environment (e.g., setting StrictUndefined policies).
- `extensions.py`: Custom Jinja2 extensions (like `jsonify` or `slugify`) exposed during the templating process.
- `hooks.py`: Executes user-provided `pre_gen_project` and `post_gen_project` hook scripts allowing extensible validation, dependency resolution, or cleanup.

### Utilities
- `exceptions.py`: Defines all custom Cookiecutter exceptions internally (e.g., `NonTemplatedInputDirException`, `RepositoryNotFound`).
- `log.py`: Configures standard logging formatting and handlers based on user flags.
- `utils.py`: General system utilities utilized across modules (e.g., safe filesystem path creation, removing directories securely).

## Process Flow

1. **Invoke**: User runs `cookiecutter <template>` via CLI (`cli.py`).
2. **Configure**: User-level configuration is loaded (`config.py`).
3. **Resolve**: `main.py` employs `repository.py` (delegating to `vcs.py` or `zipfile.py`) to identify, conditionally download/clone, and cache the project source template locally. `find.py` finds the template folder within the repo.
4. **Contextualize**: A working context is formed from default configurations merged with `cookiecutter.json`.
5. **Prompting**: `prompt.py` iteratively queries the user for their respective configuration overrides. If cached values are needed, `replay.py` provides inputs instead.
6. **Pre-generation Hooks**: Contextually triggered, `hooks.py` evaluates pre-gen scripts executing extensible programmatic validations.
7. **Generation**: `generate.py` builds the requisite files/directories and dynamically injects Jinja2 templated arguments leveraging `environment.py` and `extensions.py` to formulate the outputs.
8. **Post-generation Hooks**: Post-operation shell/python scripts run via `hooks.py` completing any system scaffolding (like initializing remote git logs).
