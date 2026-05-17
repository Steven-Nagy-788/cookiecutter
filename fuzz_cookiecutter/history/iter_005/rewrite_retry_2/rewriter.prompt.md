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

PlannerOutput(analysis='The current corpus heavily exercises the CLI/API mode selection and the pre_prompt hook failure, but almost never reaches the deeper generation logic (copy_without_render handling, newline handling, binary file rendering, and the dictionary‑variable overwrite path in generate.py). The missing lines are mostly in generate.py, prompt.py, zipfile.py, vcs.py and config.py, indicating that the harness never triggers URL‑based template fetching, VCS cloning, or the complex context‑merge branches. The grammar currently fixes many fields to static literals, limiting the ability to vary boolean flags, extra_context, replay payloads, and nested template structures that would drive those uncovered branches.', overrepresented_responses=['"mode": "api"', '"no_input": true', 'hook_script = null or raising SystemExit', 'default copy_without_render and new_lines values'], underexplored_scenario_families=['no_input = false with non‑empty extra_context and replay payloads', 'overwrite_if_exists / skip_if_file_exists combinations', 'hooks that succeed (pre_gen_project / post_gen_project) and that write files', 'binary file entries with custom binary_path_expr and contents', 'nested_templates with more than two entries and varied keys/paths', 'choice_array variations and missing license entries', 'prompt conversion of yes/no strings (triggering prompt._convert_to_bool)', 'zipfile download path (is_url true) and VCS repo_url parsing'], reachable_by_grammar=['execution_mode', 'template_source', 'template_object (root_name, cookiecutter_json, prompts, copy_without_render, new_lines, files, hooks, nested_templates)', 'invocation_object (no_input, extra_context, replay, json_bool flags, output_dir_state)', 'binary_contents, binary_path_expr, text_contents, hook_script'], reachable_by_harness_only=['is_url flag in zipfile handling (requires a remote URL in template_source)', 'repo_url parsing in vcs (requires a VCS URL in template_source)', 'environment variable expansion in config (requires path strings with $HOME or ~)', 'deep dictionary variable overwrite logic in generate.py (needs extra_context keys that map to existing context variables)', 'prompt._convert_to_bool branches (needs yes/no string answers in prompts)'], unreachable_harness_limits=['The harness currently only supplies a local template source; it cannot produce a URL for zipfile or a VCS URL, so those branches stay uncovered.', 'Prompt answers are not simulated; the harness does not feed user input, so the yes/no conversion path is never taken.'], line_target_hints=[{'target': 'cookiecutter/generate.py:72', 'delivery': 'grammar', 'code_signal': 'assigning overwrite value to a new dictionary variable during deep context merge', 'required_inputs': '"extra_context" object containing a key that matches a nested variable name (e.g., {"project_name": "NewName"}) while no_input is false and replay is null', 'grammar_implication': 'Add alternatives to extra_context_object that include arbitrary key/value pairs (string literals) and allow extra_context to be a non‑empty dict with keys that exist in the template context.'}, {'target': 'cookiecutter/generate.py:76-78', 'delivery': 'grammar', 'code_signal': 'handling list‑type context variables with in_dictionary_variable flag', 'required_inputs': '"extra_context" with a list value for a known list variable (e.g., {"license": ["MIT", "GPL"]}) and set in_dictionary_variable true via a new flag in the manifest (e.g., "_in_dict_var": true)', 'grammar_implication': 'Introduce a new optional field in invocation_object (e.g., "_in_dict_var") that the harness interprets to set the internal flag, and expand extra_context_object to allow list literals.'}, {'target': 'cookiecutter/prompt.py:53-57', 'delivery': 'grammar', 'code_signal': 'conversion of user answer strings to bool for yes/no prompts', 'required_inputs': 'A prompts_object that includes a yes/no question and a corresponding entry in extra_context (or replay) providing a string answer like "yes" or "no"', 'grammar_implication': 'Allow prompts_object to specify a "type": "bool" field and permit extra_context values that are plain strings (e.g., {"use_docker": "yes"}).'}, {'target': 'cookiecutter/zipfile.py:38-42', 'delivery': 'harness', 'code_signal': 'is_url flag true triggers path expansion and download logic', 'required_inputs': 'template_source set to a URL string (e.g., "https://example.com/template.zip") instead of "local"', 'grammar_implication': 'Replace the fixed rule template_source : \'"local"\' with an alternative that accepts a URL literal.'}, {'target': 'cookiecutter/vcs.py:41-44', 'delivery': 'harness', 'code_signal': "repo_url split on '+' and handling of git/hg prefixes", 'required_inputs': 'template_source set to a VCS URL like "git+https://github.com/user/repo.git"', 'grammar_implication': 'Extend template_source to include a VCS URL literal alternative.'}, {'target': 'cookiecutter/config.py:38-39', 'delivery': 'grammar', 'code_signal': 'path expansion of environment variables and user home', 'required_inputs': 'Any path field (e.g., output_dir_state) containing "~" or "$HOME"', 'grammar_implication': 'Allow string literals in relevant fields (e.g., output_dir_state) to contain tilde or $VAR patterns.'}], recommended_rule_edits=[{'rule': 'template_source', 'rationale': 'Add a URL alternative so zipfile and VCS branches can be exercised.'}, {'rule': 'extra_context_object', 'rationale': 'Permit arbitrary key/value pairs and list literals to trigger deep context merge and list handling in generate.py.'}, {'rule': 'invocation_object', 'rationale': 'Introduce an optional boolean flag (e.g., "_in_dict_var") that the harness can map to the internal in_dictionary_variable flag, enabling coverage of lines 76‑78.'}, {'rule': 'prompts_object', 'rationale': 'Add a variant that includes a "type": "bool" entry and allow corresponding extra_context strings, so prompt._convert_to_bool is exercised.'}, {'rule': 'hook_script', 'rationale': 'Add a successful hook variant that writes a file (already present) but also a variant that returns a non‑exception string, to diversify hook outcomes.'}, {'rule': 'nested_templates_value', 'rationale': 'Allow three or more nested_template_entry items to increase nested‑template handling depth.'}])

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

