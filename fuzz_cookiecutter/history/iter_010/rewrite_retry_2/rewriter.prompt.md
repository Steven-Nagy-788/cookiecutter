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

PlannerOutput(analysis='The current grammar covers many typical manifest fields but the fuzzing results show most cases hitting early validation errors (NonTemplatedInputDirException) and a few hook failures. Coverage gaps are concentrated in generate.py (handling of dictionary/list overwrites), prompt.py (choice parsing), zipfile.py (path handling), vcs.py (repo URL parsing) and config.py (path expansion). These code paths are not exercised because the grammar never produces inputs that trigger deep context merging, list overwrites, boolean choice conversion, URL‑based template sources, or environment‑variable paths.', overrepresented_responses=["mode=api with default template_source='local' and no_input=true", 'extra_context empty or trivial', 'hooks either null or a simple success script'], underexplored_scenario_families=['no_input=false with populated extra_context and replay payloads', 'template_source variations (e.g., remote git/hg URLs)', 'output_dir_state collisions combined with overwrite_if_exists / skip_if_file_exists toggles', 'hooks that raise exceptions in pre_gen_project or post_gen_project', 'binary file handling with custom binary_path_expr and binary_contents', 'choice prompts that require boolean conversion (yes/no) and default handling'], reachable_by_grammar=['no_input=false + extra_context overrides', 'replay payloads with partial context', 'nested_templates with multiple entries', 'hooks scripts that raise SystemExit', 'binary file entries', 'copy_without_render patterns'], reachable_by_harness_only=['template_source as a remote git+https URL (requires VCS handling)', "output_dir_state='project_exists' with pre‑existing files on disk", 'environment‑variable paths for config expansion', 'zipfile extraction of a remote archive'], unreachable_harness_limits=["The harness currently only creates a temporary empty directory for the template; it cannot simulate an existing project directory to hit output_dir_state='project_exists'.", 'It does not clone remote repositories, so VCS and zipfile code remain unreachable.'], line_target_hints=[{'target': 'cookiecutter/generate.py:72', 'delivery': 'grammar', 'code_signal': 'Assigning an overwritten scalar value inside a nested dictionary variable', 'required_inputs': 'template_object.cookiecutter_json containing a nested dict variable (e.g., a new key under a dict) and invocation_object.extra_context providing a different value for the same key, with overwrite_if_exists=true', 'grammar_implication': 'Add a rule to allow extra_context_object to contain arbitrary nested key/value pairs (not just flat keys). For example, allow \'{ "project_name": { "sub": "value" } }\' and ensure json_bool can be true to trigger the overwrite path.'}, {'target': 'cookiecutter/generate.py:76', 'delivery': 'grammar', 'code_signal': 'Handling list values when merging context variables', 'required_inputs': 'extra_context_object with a list for a key that also appears in cookiecutter_json (e.g., "license": ["MIT", "GPL"]). overwrite_if_exists must be true and in_dictionary_variable flag set by having the key inside a dict variable.', 'grammar_implication': 'Extend extra_context_object to allow list literals (e.g., \'[\' \'"MIT"\' \',\' \'"GPL"\' \']\' ).'}, {'target': 'cookiecutter/prompt.py:53', 'delivery': 'grammar', 'code_signal': 'Conversion of user input string to boolean for yes/no choices', 'required_inputs': 'invocation_object.no_input=false, prompts_object containing a boolean choice prompt, and extra_context providing a string like "yes" or "no" for that prompt.', 'grammar_implication': 'Introduce a new rule boolean_input_string with alternatives like \'"yes"\', \'"no"\', \'"y"\', \'"n"\' and allow extra_context to map a prompt key to such a string.'}, {'target': 'cookiecutter/zipfile.py:38', 'delivery': 'harness', 'code_signal': 'Path expansion for a user‑home shortcut or env var', 'required_inputs': "template_source set to a remote zip URL (requires VCS/zip harness support) and output_dir_state pointing to a path containing '~' or '$HOME'.", 'grammar_implication': 'If harness is extended, grammar could add a rule template_source_url allowing strings like \'"git+https://example.com/repo.git"\' which forces zipfile handling.'}, {'target': 'cookiecutter/vcs.py:41', 'delivery': 'harness', 'code_signal': "Parsing of repo_url with a '+' separator to select VCS type", 'required_inputs': 'template_source value of the form \'"git+https://example.com/repo.git"\' or \'"hg+https://example.com/repo.hg"\'.', 'grammar_implication': 'Add an alternative to template_source rule: template_source_url : \'"git+https://example.com/repo.git"\' | \'"hg+https://example.com/repo.hg"\'.'}, {'target': 'cookiecutter/config.py:38', 'delivery': 'grammar', 'code_signal': 'Expansion of environment variables in a path string', 'required_inputs': 'Any path field (e.g., copy_without_render entries) containing a placeholder like \'"$HOME/project"\' or \'~/.config\' .', 'grammar_implication': "Add a rule env_path_literal allowing strings with '$' or '~' characters, and use it in copy_without_render_array or path_expr."}], recommended_rule_edits=[{'rule': 'extra_context_object', 'rationale': 'Currently only flat key/value pairs are allowed. Extending it to support nested objects, list literals, and boolean strings will let us hit generate.py overwrite logic and prompt boolean conversion.'}, {'rule': 'template_source', 'rationale': 'Add alternatives for remote VCS URLs (git+..., hg+...) so that vcs.py and zipfile.py paths become reachable.'}, {'rule': 'copy_without_render_array', 'rationale': 'Allow entries with env‑var or home‑dir expansions (e.g., \'"$HOME/assets/*"\') to exercise config.path expansion.'}, {'rule': 'hook_script', 'rationale': 'Introduce a variant that raises a custom exception (e.g., \'"raise ValueError(\'hook fail\')\\n"\') to explore different failure modes in hooks handling.'}, {'rule': 'newline_value', 'rationale': 'Add a non‑standard newline literal (e.g., \'"\\r"\') to test edge cases in generate.py line handling.'}])

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

