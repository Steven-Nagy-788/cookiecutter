# Grammar Rewriter

You are an expert ANTLR4 grammar engineer. Your job is to execute a mutation plan provided by the analysis planner.

## Current Grammar Declaration

`grammar cookiecutter_case;`

## Protected Rules

Protected rules: case_file, case_object, execution_mode, template_source, template_object, invocation_object

```antlr
case_file
    : case_object EOF
    ;

case_object
    : '{'
      '"mode"' ':' execution_mode ','
      '"template_source"' ':' template_source ','
      '"template"' ':' template_object ','
      '"invocation"' ':' invocation_object
      '}'
    ;

execution_mode
    : '"cli"'
    | '"api"'
    ;

template_source
    : '"local"'
    ;

template_object
    : '{'
      '"root_name"' ':' root_name ','
      '"cookiecutter_json"' ':' cookiecutter_json_object ','
      '"prompts"' ':' prompts_object ','
      '"copy_without_render"' ':' copy_without_render_array ','
      '"new_lines"' ':' newline_value ','
      '"files"' ':' files_array ','
      '"hooks"' ':' hooks_object ','
      '"nested_templates"' ':' nested_templates_value
      '}'
    ;

invocation_object
    : '{'
      '"no_input"' ':' 'true' ','
      '"extra_context"' ':' extra_context_object ','
      '"replay"' ':' 'null' ','
      '"overwrite_if_exists"' ':' json_bool ','
      '"skip_if_file_exists"' ':' json_bool ','
      '"accept_hooks"' ':' json_bool ','
      '"keep_project_on_failure"' ':' json_bool ','
      '"output_dir_state"' ':' output_dir_state
      '}'
    | '{'
      '"no_input"' ':' 'false' ','
      '"extra_context"' ':' '{}' ','
      '"replay"' ':' replay_value ','
      '"overwrite_if_exists"' ':' json_bool ','
      '"skip_if_file_exists"' ':' json_bool ','
      '"accept_hooks"' ':' json_bool ','
      '"keep_project_on_failure"' ':' json_bool ','
      '"output_dir_state"' ':' output_dir_state
      '}'
    ;
```

## Editable Existing Rules

binary_contents, binary_path_expr, choice_array, cookiecutter_json_object, copy_without_render_array, database_object, extra_context_object, feature_flag_dict, file_entry, files_array, hook_script, hooks_object, json_bool, nested_description, nested_key, nested_path, nested_template_entry, nested_templates_value, nested_title, newline_value, output_dir_state, owner_object, path_expr, project_name_value, prompts_object, replay_value, repo_name_value, root_name, text_contents

## Current Grammar

```antlr
grammar cookiecutter_case;

case_file
    : case_object EOF
    ;

case_object
    : '{'
      '"mode"' ':' execution_mode ','
      '"template_source"' ':' template_source ','
      '"template"' ':' template_object ','
      '"invocation"' ':' invocation_object
      '}'
    ;

execution_mode
    : '"cli"'
    | '"api"'
    ;

template_source
    : '"local"'
    ;

template_object
    : '{'
      '"root_name"' ':' root_name ','
      '"cookiecutter_json"' ':' cookiecutter_json_object ','
      '"prompts"' ':' prompts_object ','
      '"copy_without_render"' ':' copy_without_render_array ','
      '"new_lines"' ':' newline_value ','
      '"files"' ':' files_array ','
      '"hooks"' ':' hooks_object ','
      '"nested_templates"' ':' nested_templates_value
      '}'
    ;

root_name
    : '"{{cookiecutter.repo_name}}"'
    | '"{{cookiecutter.project_name}}"'
    ;

cookiecutter_json_object
    : '{'
      '"project_name"' ':' project_name_value ','
      '"repo_name"' ':' repo_name_value ','
      '"use_docker"' ':' json_bool ','
      '"license"' ':' choice_array ','
      '"database"' ':' database_object
      '}'
    | '{'
      '"project_name"' ':' project_name_value ','
      '"repo_name"' ':' repo_name_value ','
      '"feature_flags"' ':' feature_flag_dict ','
      '"owner"' ':' owner_object
      '}'
    ;

project_name_value
    : '"Example Project"'
    | '"Cookie Lab"'
    | '"Replay Project"'
    | '"Broken Value"'
    ;

repo_name_value
    : '"{{ cookiecutter.project_name|lower }}"'
    | '"{{ cookiecutter.project_name }}_pkg"'
    ;

database_object
    : '{'
      '"engine"' ':' '"sqlite"' ','
      '"port"' ':' '"5432"'
      '}'
    | '{'
      '"engine"' ':' '"postgres"' ','
      '"port"' ':' '"5432"'
      '}'
    ;

feature_flag_dict
    : '{'
      '"docs"' ':' json_bool ','
      '"ci"' ':' json_bool
      '}'
    ;

owner_object
    : '{'
      '"team"' ':' '"platform"' ','
      '"email"' ':' '"team@example.com"'
      '}'
    ;

prompts_object
    : '{}'
    | '{'
      '"project_name"' ':' '"Project name?"' ','
      '"use_docker"' ':' '"Use Docker?"' ','
      '"license"' ':' '"Choose a license"' ','
      '"database"' ':' '"Database settings"'
      '}'
    | '{'
      '"project_name"' ':' '"Name of the generated package"' ','
      '"owner"' ':' '"Owner metadata"'
      '}'
    ;

copy_without_render_array
    : '[]'
    | '[' '"{{cookiecutter.repo_name}}/assets/*"' ']'
    | '[' '"{{cookiecutter.repo_name}}/rendered/*.yml"' ']'
    ;

newline_value
    : '"\\n"'
    | '"\\r\\n"'
    | 'null'
    ;

files_array
    : '[' file_entry ']'
    | '[' file_entry ',' file_entry ']'
    | '[' file_entry ',' file_entry ',' file_entry ']'
    ;

file_entry
    : '{'
      '"path"' ':' path_expr ','
      '"kind"' ':' '"text"' ','
      '"contents"' ':' text_contents
      '}'
    | '{'
      '"path"' ':' binary_path_expr ','
      '"kind"' ':' '"binary"' ','
      '"contents"' ':' binary_contents
      '}'
    ;

path_expr
    : '"README.md"'
    | '"docs/guide.md"'
    | '"rendered/config.yml"'
    | '"{{cookiecutter.repo_name}}/README.md"'
    | '"{{cookiecutter.repo_name}}/pyproject.toml"'
    | '"{{cookiecutter.repo_name}}/src/{{cookiecutter.repo_name}}/__init__.py"'
    | '"{{cookiecutter.repo_name}}/templates/report.txt"'
    ;

binary_path_expr
    : '"assets/logo.bin"'
    | '"{{cookiecutter.repo_name}}/assets/logo.bin"'
    ;

text_contents
    : '"# {{ cookiecutter.project_name }}\\n"'
    | '"package = {{ cookiecutter.repo_name }}\\n"'
    | '"docs_enabled={{ cookiecutter.feature_flags.docs }}\\n"'
    | '"engine={{ cookiecutter.database.engine }}\\n"'
    | '"{{ cookiecutter.missing_value }}\\n"'
    ;

binary_contents
    : '"AAECAwQ="' 
    | '"c29tZS1iaW5hcnktYnl0ZXM="' 
    ;

hooks_object
    : '{'
      '"pre_prompt"' ':' hook_script ','
      '"pre_gen_project"' ':' hook_script ','
      '"post_gen_project"' ':' hook_script
      '}'
    ;

hook_script
    : 'null'
    | '"from pathlib import Path\\nPath(\'HOOK_OK\').write_text(\'ok\', encoding=\'utf-8\')\\n"'
    | '"raise SystemExit(1)\\n"'
    ;

nested_templates_value
    : 'null'
    | '[' nested_template_entry ',' nested_template_entry ']'
    ;

nested_template_entry
    : '{'
      '"key"' ':' nested_key ','
      '"path"' ':' nested_path ','
      '"title"' ':' nested_title ','
      '"description"' ':' nested_description
      '}'
    ;

nested_key
    : '"core"'
    | '"service"'
    ;

nested_path
    : '"nested_core"'
    | '"nested_service"'
    ;

nested_title
    : '"Core Template"'
    | '"Service Template"'
    ;

nested_description
    : '"Minimal local template"'
    | '"Template with a nested prompt path"'
    ;

invocation_object
    : '{'
      '"no_input"' ':' 'true' ','
      '"extra_context"' ':' extra_context_object ','
      '"replay"' ':' 'null' ','
      '"overwrite_if_exists"' ':' json_bool ','
      '"skip_if_file_exists"' ':' json_bool ','
      '"accept_hooks"' ':' json_bool ','
      '"keep_project_on_failure"' ':' json_bool ','
      '"output_dir_state"' ':' output_dir_state
      '}'
    | '{'
      '"no_input"' ':' 'false' ','
      '"extra_context"' ':' '{}' ','
      '"replay"' ':' replay_value ','
      '"overwrite_if_exists"' ':' json_bool ','
      '"skip_if_file_exists"' ':' json_bool ','
      '"accept_hooks"' ':' json_bool ','
      '"keep_project_on_failure"' ':' json_bool ','
      '"output_dir_state"' ':' output_dir_state
      '}'
    ;

extra_context_object
    : '{}'
    | '{'
      '"project_name"' ':' '"Overwritten Project"'
      '}'
    | '{'
      '"use_docker"' ':' '"true"'
      '}'
    ;

replay_value
    : 'null'
    | '{'
      '"cookiecutter"' ':' '{'
         '"project_name"' ':' '"Replay Project"' ','
         '"repo_name"' ':' '"replay_project"' ','
         '"use_docker"' ':' 'true'
      '}'
      '}'
    ;

choice_array
    : '[' '"MIT"' ',' '"GPL"' ',' '"Apache"' ']'
    | '[' '"BSD"' ',' '"MIT"' ']'
    ;

output_dir_state
    : '"missing"'
    | '"existing_empty"'
    | '"project_exists"'
    ;

json_bool
    : 'true'
    | 'false'
    ;

```

## Codebase Reachability Reference

cookiecutter/prompt.py
- Reach with string, bool, choice-list, dict, __prompts__, and nested templates.
- Favor cases that mix no_input=False with default-driven answers.

cookiecutter/generate.py
- Reach with _copy_without_render, _new_lines, binary files, rendered paths, and output collisions.
- Favor cases that vary overwrite_if_exists and skip_if_file_exists.

cookiecutter/hooks.py
- Reach with no hooks, successful hooks, and failing hooks.
- Favor pre_gen_project and post_gen_project scripts.

cookiecutter/main.py and cookiecutter/cli.py
- Reach with both cli and api modes, replay-driven runs, and keep_project_on_failure.

cookiecutter/replay.py
- Reach with replay payloads that partially satisfy the current template context.

## Planner Analysis And Mutation Plan

PlannerOutput(analysis='The current corpus heavily exercises the CLI/API mode selection and the pre_prompt hook failure, but most branches in generate.py (handling of nested dictionary overwrites), prompt.py (choice parsing), zipfile.py (URL handling), vcs.py (repo URL parsing) and config.py (path expansion) remain untouched. The grammar already covers many template fields, but lacks constructs to trigger deeper dictionary variable handling, choice‑to‑bool conversion, URL‑based template sources, VCS repo types, and path expansion via environment variables. Additionally, replay payloads are only exercised with a simple static dict; more complex partial replays could hit missing branches.', overrepresented_responses=['mode=api', 'pre_prompt hook raising SystemExit', 'no_input=true with empty extra_context'], underexplored_scenario_families=['nested dictionary variable overwrites in generate.py', 'boolean conversion of user choices in prompt.py', 'template_source as a remote URL (git/hg) to hit zipfile/vcs logic', 'environment variable expansion in config paths', 'partial replay payloads with missing keys'], reachable_by_grammar=['nested dictionary overwrites (via extra_context_object with nested dicts)', 'choice‑to‑bool conversion (via prompts_object with choice lists and extra_context providing raw strings)', 'partial replay payloads (by extending replay_value with incomplete cookiecutter dict)', 'hooks success/failure (already reachable)', 'overwrite_if_exists / skip_if_file_exists variations (already reachable)'], reachable_by_harness_only=['remote template_source (requires actual git/hg URL, not representable in current grammar)', 'environment variable expansion in config paths (requires harness to set env vars before invocation)', 'zipfile extraction of remote archives (needs network/file system setup)'], unreachable_harness_limits=['The harness cannot simulate a VCS repository without providing a real URL; the grammar would need a new rule for template_source to accept a URL string.', 'Path expansion via os.path.expandvars requires external environment variables; the harness would need to set them, which is outside the manifest scope.'], line_target_hints=[{'target': 'cookiecutter/generate.py:72', 'delivery': 'grammar', 'code_signal': 'Assigning a new value to a variable inside a nested dictionary (context[variable] = overwrite) when in_dictionary_variable is true.', 'required_inputs': 'extra_context_object must contain a nested dict, e.g. { "project_name": { "sub": "value" } } and the template must reference {{ cookiecutter.project_name.sub }} in a prompt or file.', 'grammar_implication': 'Add a rule allowing extra_context_object to contain arbitrary nested JSON objects (key: string, value: string or object) instead of the current flat literals.'}, {'target': 'cookiecutter/generate.py:76-78', 'delivery': 'grammar', 'code_signal': 'Handling list values inside a nested dictionary variable (context[variable] = overwrite) and then continuing the loop.', 'required_inputs': 'extra_context_object with a list value inside a nested dict, e.g. { "features": ["a", "b"] } and a template reference {{ cookiecutter.features }}.', 'grammar_implication': "Extend extra_context_object to allow list literals (e.g. '[' string (',' string)* ']') as values."}, {'target': 'cookiecutter/prompt.py:53-58', 'delivery': 'grammar', 'code_signal': 'Conversion of raw user input strings to boolean via yes_choices/no_choices.', 'required_inputs': 'prompts_object must include a boolean‑type prompt (e.g., "use_docker": "Use Docker?"), and extra_context_object must supply a raw string like "yes" or "no" (case‑insensitive).', 'grammar_implication': 'Allow extra_context_object values to be raw strings (not only quoted literals) that are not wrapped in {{ }} so that the prompt parser receives them directly.'}, {'target': 'cookiecutter/zipfile.py:38-42', 'delivery': 'harness', 'code_signal': 'Path expansion and URL detection for remote zip downloads.', 'required_inputs': 'template_source set to a URL string (e.g., "https://example.com/template.zip") and harness must provide a reachable zip file.', 'grammar_implication': 'Introduce a new rule template_source_url : \'"https://"\' ... to allow URL literals.'}, {'target': 'cookiecutter/vcs.py:41-44', 'delivery': 'harness', 'code_signal': "Parsing repo_url with a '+' separator to determine VCS type (git/hg).", 'required_inputs': 'template_source set to a VCS URL like "git+https://github.com/user/repo.git".', 'grammar_implication': 'Add an alternative to template_source that matches VCS URL patterns.'}, {'target': 'cookiecutter/config.py:38-39', 'delivery': 'harness', 'code_signal': 'Expansion of environment variables in a path string.', 'required_inputs': 'An environment variable (e.g., $HOME) used inside a path field such as "${HOME}/templates" passed to the harness before execution.', 'grammar_implication': 'No grammar change needed; harness must set env vars.'}], recommended_rule_edits=[{'rule': 'extra_context_object', 'rationale': 'Current definition only allows empty object or single‑key flat literals. To hit nested dictionary overwrites and list handling in generate.py, broaden it to accept arbitrary JSON objects with nested dicts and arrays.'}, {'rule': 'template_source', 'rationale': 'Only "local" is allowed, preventing coverage of zipfile and vcs branches. Add alternatives for URL strings (http/https) and VCS URLs (git+..., hg+...).'}, {'rule': 'prompts_object', 'rationale': 'Include a variant where prompt values are raw strings that the prompt parser will treat as user input, enabling boolean conversion logic.'}, {'rule': 'replay_value', 'rationale': 'Allow partial cookiecutter dicts (omit some keys) to exercise missing‑key handling in replay processing.'}, {'rule': 'json_bool', 'rationale': 'Add a variant that is a string "true"/"false" (unquoted) to simulate raw user input for boolean prompts.'}])

## Response Format

Return JSON only. Use this exact shape:

{
  "rationale": "one short sentence",
  "updates": [
    {
      "rule": "existingRuleName",
      "replacement": "existingRuleName\n    : ...\n    ;"
    }
  ]
}

