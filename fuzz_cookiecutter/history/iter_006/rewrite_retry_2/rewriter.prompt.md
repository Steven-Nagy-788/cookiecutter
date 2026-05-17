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

PlannerOutput(analysis='The current grammar exercises many branches but still misses large blocks in generate.py (list handling and deep dict overwrites), prompt.py (choice parsing), zipfile.py (URL handling), vcs.py (repo URL parsing) and config.py (path expansion). Most failures are NonTemplatedInputDirException from generate_files, indicating the template source is never treated as a real directory. Hook failures are only exercised via the existing hook_script alternatives. The harness currently only toggles mode, no_input, and replay, leaving many combinations of json_bool flags, extra_context, copy_without_render, new_lines, nested templates, and hook scripts unexplored.', overrepresented_responses=['mode=api with no_input=true and extra_context empty (produces NonTemplatedInputDirException)', "hook_script='null' (no hook execution)", 'json_bool always true/false but not combined with conflicting overwrite/skip flags'], underexplored_scenario_families=['overwrite_if_exists vs skip_if_file_exists interactions when output_dir_state=project_exists', 'pre_prompt and post_gen_project hook scripts that succeed or raise SystemExit', 'nested_templates with both entries present and varying key/path/title/description values', 'copy_without_render patterns that include both asset glob and rendered glob together', "new_lines values other than '\\n' (i.e., '\\r\\n' and null) affecting file writing", 'extra_context providing non‑string values (e.g., boolean, list) to trigger generate.py list handling', 'replay payloads that partially fill the template (missing some keys) to hit generate.py missing‑key branches', 'choice_array variations combined with boolean prompts to hit prompt.py conversion logic'], reachable_by_grammar=['All missing lines in generate.py related to list handling and deep dict overwrites can be reached by adding extra_context entries that are lists or nested dicts.', 'prompt.py yes/no parsing can be exercised by providing extra_context values that are strings like "YES", "no", etc., and by adding choice_array with different casing.', 'zipfile.py URL handling can be reached by setting template_source to a remote URL (currently only "local"), requiring a new rule.', 'vcs.py repo URL parsing can be reached by allowing template_source to be a VCS URL (e.g., "git+https://example.com/repo.git").', 'config.py path expansion can be exercised by adding a rule for template_source that yields a path containing environment variables (e.g., "$HOME/template").'], reachable_by_harness_only=['Scenarios that require the harness to set internal flags such as keep_project_on_failure without changing the manifest (already possible).', 'Simulating file‑system collisions for output_dir_state=project_exists while varying overwrite_if_exists/skip_if_file_exists – the harness can pre‑create a dummy project directory.'], unreachable_harness_limits=['The harness cannot create a real remote git repository, so full VCS cloning paths remain unreachable unless the grammar supplies a mock URL that the code treats as local.', 'The harness cannot inject malformed JSON into the manifest; all inputs must be syntactically valid according to the grammar.'], line_target_hints=[{'target': 'cookiecutter/generate.py:72', 'delivery': 'grammar', 'code_signal': 'Assigning a new value to a variable inside a deep dictionary when in_dictionary_variable is true', 'required_inputs': 'extra_context_object must contain a nested dict, e.g., { "project_name": { "sub": "value" } } and invocation_object.no_input=false so that extra_context is merged', 'grammar_implication': 'Add a rule extra_context_object that can produce nested dictionary literals (key: value pairs where value may be another object) instead of only flat string entries.'}, {'target': 'cookiecutter/generate.py:76', 'delivery': 'grammar', 'code_signal': 'When a context value is a list and in_dictionary_variable is true, the list is overwritten', 'required_inputs': 'extra_context_object must include a list value, e.g., { "license": ["MIT","GPL"] }', 'grammar_implication': 'Extend extra_context_object to allow list literals with string elements (reuse choice_array syntax).'}, {'target': 'cookiecutter/prompt.py:53', 'delivery': 'grammar', 'code_signal': 'User input string is stripped and lower‑cased before yes/no choice check', 'required_inputs': 'Provide a prompt answer via extra_context that is a string with mixed case and surrounding whitespace, e.g., "  YeS  " for a boolean prompt', 'grammar_implication': 'Allow extra_context_object values to be arbitrary strings (currently only specific literals).'}, {'target': 'cookiecutter/zipfile.py:38', 'delivery': 'grammar', 'code_signal': 'Path expansion for a clone_to_dir that contains environment variables', 'required_inputs': 'template_source rule should permit a value like "${HOME}/my_template"', 'grammar_implication': 'Replace template_source rule with alternatives: \'"local"\' | env_path, where env_path matches a string containing "$" and alphanumerics.'}, {'target': 'cookiecutter/vcs.py:41', 'delivery': 'grammar', 'code_signal': "Splitting repo_url on '+' to detect VCS type", 'required_inputs': 'template_source must be a VCS URL such as "git+https://example.com/repo.git"', 'grammar_implication': 'Add a new rule vcs_url and extend template_source to include vcs_url alternatives.'}, {'target': 'cookiecutter/config.py:38', 'delivery': 'grammar', 'code_signal': 'os.path.expandvars and expanduser are called on a path string', 'required_inputs': 'template_source path containing both a user‑home shortcut and an env var, e.g., "~/{{cookiecutter.repo_name}}" or "$HOME/{{cookiecutter.repo_name}}"', 'grammar_implication': "Allow template_source to accept interpolated paths with '~' and '$' characters."}], recommended_rule_edits=[{'rule': 'extra_context_object', 'rationale': 'Current rule only yields empty object or single flat key/value pairs. To hit generate.py list and deep‑dict branches we need nested objects and list literals. Expand the rule to allow arbitrary JSON objects and arrays, reusing existing choice_array and adding a generic array rule.'}, {'rule': 'template_source', 'rationale': 'Only "local" is allowed, preventing zipfile and vcs code paths. Add alternatives for env_path, vcs_url, and remote zip URLs so that path expansion and repo URL parsing are exercised.'}, {'rule': 'hook_script', 'rationale': 'Only three alternatives exist; add a script that writes a file and then exits with non‑zero code after writing, to differentiate pre_prompt vs post_gen_project failure handling.'}, {'rule': 'nested_templates_value', 'rationale': 'Currently either null or exactly two entries. Add a single‑entry alternative and allow three entries to vary the loop count and hit more branches.'}, {'rule': 'copy_without_render_array', 'rationale': 'Only single glob patterns are allowed. Add a combination array with both asset and rendered globs to trigger multiple copy‑without‑render paths.'}, {'rule': 'newline_value', 'rationale': "Null and '\\n' are covered; include '\\r\\n' and also an empty string to test line‑ending handling in generate.py."}])

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

