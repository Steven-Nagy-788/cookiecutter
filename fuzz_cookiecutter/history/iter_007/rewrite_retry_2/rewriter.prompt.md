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

PlannerOutput(analysis='The current corpus heavily exercises the CLI/API mode selection and the pre_prompt hook failure, but most of the generate, prompt, zipfile, vcs and config logic remains untouched. Missing lines are in deep dictionary handling, choice parsing, path expansion, and VCS URL parsing. The grammar does not yet expose variations needed to trigger those branches (e.g., non‑boolean yes/no inputs, custom repo URLs, environment‑variable paths, nested dictionary overwrites, and replay payloads with missing keys).', overrepresented_responses=['mode = "api"', 'pre_prompt hook raising SystemExit', 'no_input = true'], underexplored_scenario_families=['no_input = false with replay payloads', 'hooks that succeed (pre_gen_project / post_gen_project)', 'overwrite_if_exists / skip_if_file_exists combinations', 'choice prompts receiving varied yes/no strings', 'binary vs text file handling with copy_without_render', 'nested template entries with different keys/paths', 'repo URLs that include a VCS scheme (git+https://...)'], reachable_by_grammar=['choice parsing in prompt.py (yes/no strings)', 'nested dictionary overwrites in generate.py', 'binary vs text file handling', 'copy_without_render patterns', 'replay payload structures', 'output_dir_state variations'], reachable_by_harness_only=['environment variable expansion in config.py', 'URL handling in zipfile.py and vcs.py (requires real filesystem or network paths)', 'exception paths that need a non‑existent input directory'], unreachable_harness_limits=["The harness currently only creates in‑memory manifests; it cannot simulate a real filesystem path containing '~' or $HOME expansions, nor can it host a remote zip URL or VCS repo.", 'Replay payloads that reference keys not present in the template require the template to be rendered, which the harness does not execute.'], line_target_hints=[{'target': 'cookiecutter/generate.py:72', 'delivery': 'grammar', 'code_signal': 'Assigning a new value to a variable inside a nested dictionary (overwrite flag)', 'required_inputs': 'template.cookiecutter_json with a nested dict variable (e.g., a custom key) and invocation.extra_context providing that key with a different value; also set "no_input": false to allow context merging.', 'grammar_implication': 'Add a new rule for extra_context_object that can include arbitrary key/value pairs (e.g., "custom_key": "new_value") and extend cookiecutter_json_object with a nested dict field (e.g., "custom": { "sub": "val" }).'}, {'target': 'cookiecutter/generate.py:76', 'delivery': 'grammar', 'code_signal': 'Handling list values inside a nested dictionary during context merging.', 'required_inputs': 'extra_context_object containing a list for an existing key (e.g., "license": ["MIT", "GPL"]).', 'grammar_implication': 'Allow extra_context_object to map keys to list literals; introduce a list_literal rule used inside extra_context_object.'}, {'target': 'cookiecutter/prompt.py:53', 'delivery': 'grammar', 'code_signal': 'Parsing yes/no choices after stripping and lower‑casing the input string.', 'required_inputs': 'prompts_object with a boolean prompt (e.g., "use_docker") and extra_context providing a non‑standard yes/no string such as "Y" or "nO".', 'grammar_implication': 'Extend extra_context_object to allow string values that are not strict "true"/"false" and add a rule for yes_no_string with alternatives like "y", "Y", "yes", "n", "N", "no".'}, {'target': 'cookiecutter/zipfile.py:38', 'delivery': 'harness', 'code_signal': 'Path expansion of a user‑home shortcut.', 'required_inputs': "A manifest that sets a custom template_source path containing '~' (requires harness to write to a temporary directory and pass that path to the generator).", 'grammar_implication': 'N/A – cannot be reached by grammar alone.'}, {'target': 'cookiecutter/vcs.py:41', 'delivery': 'harness', 'code_signal': 'Parsing a repo URL with a VCS scheme (e.g., "git+https://example.com/repo.git").', 'required_inputs': 'template_source set to a remote URL string; the harness must invoke the VCS fetch routine.', 'grammar_implication': 'N/A – requires external resource handling.'}, {'target': 'cookiecutter/config.py:38', 'delivery': 'harness', 'code_signal': 'Expansion of environment variables in a path.', 'required_inputs': 'A template_source path containing "$HOME" or "%USERPROFILE%"; harness must set the env var.', 'grammar_implication': 'N/A – path expansion is outside manifest grammar.'}], recommended_rule_edits=[{'rule': 'extra_context_object', 'rationale': 'Current rule only allows empty object or two single‑key objects. To hit nested dict and list handling in generate.py we need arbitrary key/value pairs, including strings, booleans, lists, and nested objects.'}, {'rule': 'extra_context_object', 'rationale': 'Introduce a new alternative that permits a list literal (e.g., \'[\' \'"MIT"\' \',\' \'"GPL"\' \']\') as a value, enabling list‑merge branches.'}, {'rule': 'extra_context_object', 'rationale': 'Add a yes_no_string rule and allow it as a value for boolean prompts, exercising the case‑insensitive yes/no parsing in prompt.py.'}, {'rule': 'hook_script', 'rationale': 'Add a successful hook variant that writes a file without raising, to cover the success path of pre_gen_project and post_gen_project.'}, {'rule': 'json_bool', 'rationale': 'Keep as is; but ensure both true and false are used in combination with overwrite_if_exists and skip_if_file_exists to explore all four permutations.'}, {'rule': 'nested_templates_value', 'rationale': 'Add a third entry option (single entry) and allow empty objects for nested_key/path/title/description to hit deeper branches in generate.py handling of nested templates.'}])

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

