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

PlannerOutput(analysis='The current corpus heavily exercises the CLI/API mode selection and the pre_prompt hook failure, but most branches in generate.py (handling of deep dictionary overwrites and list merging), prompt.py (choice-to-bool conversion), zipfile.py (URL handling), vcs.py (repo URL parsing) and config.py (path expansion) remain untouched. The grammar already covers many template fields, but lacks constructs that trigger those missing lines, such as nested dictionary variables, list‑type context values, boolean choice prompts, and URL‑based template sources.', overrepresented_responses=['mode=api', 'pre_prompt hook raising SystemExit', 'no_input=true with empty extra_context'], underexplored_scenario_families=['deep dictionary variable overwrites in generate.py', 'list‑type context merging in generate.py', 'yes/no choice conversion in prompt.py', 'template source as a remote zip URL', "VCS repo URL parsing with '+' separator", 'environment‑variable/user‑home expansion in config paths'], reachable_by_grammar=['deep dictionary variable overwrites (via extra_context_object with nested dicts)', 'list‑type context values (extra_context_object with arrays)', 'yes/no choice prompts (adding a prompt that expects a boolean)', 'hooks that succeed or fail (hook_script alternatives already present)', 'nested_templates variations (already in grammar)'], reachable_by_harness_only=['remote zip URL template source (requires harness to supply a URL and a cached zip file)', 'VCS repo URL parsing (requires harness to mock a VCS checkout)', 'config path expansion with env vars (requires harness to set env vars and invoke config helpers)'], unreachable_harness_limits=['The harness cannot fabricate a real remote zip or VCS repo without external resources; such cases must be simulated via mocks, which the current harness does not provide.'], line_target_hints=[{'target': 'cookiecutter/generate.py:72', 'delivery': 'grammar', 'code_signal': 'assigning a new value to a deep dictionary variable when in_dictionary_variable is true', 'required_inputs': '"extra_context" object containing a nested dictionary, e.g. { "project_name": { "sub": "value" } } and a template that references {{ cookiecutter.project_name.sub }}', 'grammar_implication': 'Add a rule allowing extra_context_object to contain arbitrary nested JSON objects (e.g., a new rule nested_json_object) and allow path_expr / text_contents to reference those nested keys.'}, {'target': 'cookiecutter/generate.py:76', 'delivery': 'grammar', 'code_signal': 'handling a list value in the context when in_dictionary_variable is true', 'required_inputs': '"extra_context" object with a list value, e.g. { "features": ["a", "b"] } and a template that uses {{ cookiecutter.features }}', 'grammar_implication': 'Extend extra_context_object to allow array literals (choice_array or a new list_literal rule) as values.'}, {'target': 'cookiecutter/prompt.py:53', 'delivery': 'grammar', 'code_signal': 'conversion of a user answer string to a boolean via yes_choices/no_choices', 'required_inputs': 'A prompt entry of type "confirm" (or a boolean prompt) that receives a string answer like "yes" or "no"; the harness must feed the answer via extra_context or replay payload.', 'grammar_implication': 'Introduce a new prompts_object variant that includes a "confirm" field, e.g., "use_docker": "[yes/no]", and allow extra_context to supply the raw string answer.'}, {'target': 'cookiecutter/zipfile.py:38', 'delivery': 'harness', 'code_signal': "expansion of a user‑provided clone_to_dir path that contains '~' or env vars", 'required_inputs': 'Invocation with output_dir_state pointing to a path like "~/tmp/{{cookiecutter.repo_name}}" and the harness sets an environment variable used in the path.', 'grammar_implication': 'No grammar change needed; harness must set env vars and pass a path containing them.'}, {'target': 'cookiecutter/vcs.py:41', 'delivery': 'harness', 'code_signal': "splitting a repo URL on '+' to separate VCS type from URL", 'required_inputs': 'Template source set to a remote VCS URL such as "git+https://example.com/repo.git"; harness must mock the VCS checkout routine.', 'grammar_implication': 'Add a new alternative to template_source allowing a string literal that matches the VCS URL pattern.'}, {'target': 'cookiecutter/config.py:38', 'delivery': 'harness', 'code_signal': 'os.path.expandvars and expanduser on a configuration path', 'required_inputs': 'A configuration file path in the manifest that includes "$HOME" or "~"; harness must set the corresponding environment variable.', 'grammar_implication': 'No grammar edit; just ensure harness can inject env vars.'}], recommended_rule_edits=[{'rule': 'extra_context_object', 'rationale': 'Current definition only allows empty object or single‑key objects with scalar values. To hit deep dictionary overwrites and list handling, broaden it to accept nested JSON objects and arrays.'}, {'rule': 'template_source', 'rationale': 'Add an alternative that matches a remote URL string (e.g., \'"git+https://example.com/repo.git"\') so that generate.py and vcs.py code paths for remote templates become reachable.'}, {'rule': 'prompts_object', 'rationale': 'Introduce a confirm‑style prompt (e.g., "use_docker": "[yes/no]") to exercise the yes/no conversion logic in prompt.py.'}, {'rule': 'nested_json_object', 'rationale': 'Create a reusable rule for arbitrary JSON objects (key/value pairs where values can be strings, numbers, booleans, arrays, or other objects) and reference it from extra_context_object.'}, {'rule': 'list_literal', 'rationale': "Define a rule for JSON arrays (e.g., '[' choice_array ']') to allow list values in extra_context."}])

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

