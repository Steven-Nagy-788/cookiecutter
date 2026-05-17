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

PlannerOutput(analysis='The current corpus heavily exercises the API mode with non‑templated input directories, yielding many WARNINGs, but it barely touches the prompt conversion logic, the VCS/ZIP handling, and the deep‑merge code in generate.py. Hook scripts, overwrite/skip flags, and replay payloads are under‑used. Consequently, large blocks of generate.py, prompt.py, zipfile.py, vcs.py and config.py remain uncovered.', overrepresented_responses=['NonTemplatedInputDirException in generate_files (API mode)', 'SystemExit from pre_prompt hook'], underexplored_scenario_families=['Successful and failing hook scripts (pre_gen_project, post_gen_project)', 'Binary file handling with copy_without_render patterns', 'new_lines variations (\\n vs \\r\\n vs null)', 'overwrite_if_exists / skip_if_file_exists flag combinations', 'Replay‑driven runs with partial context', 'CLI mode with no_input=false and default‑driven answers', 'Nested template processing (nested_templates non‑null)', 'Path expansion via config.expand_path and zipfile.clone_to_dir handling'], reachable_by_grammar=['execution_mode (cli/api)', 'template_source (local)', 'template_object (all sub‑objects)', 'invocation_object (both branches)', 'extra_context_object (including custom keys)', 'replay_value (null or full dict)', 'hooks_object (null / success / failure scripts)', 'copy_without_render_array (different glob patterns)', 'newline_value (both newline strings and null)', 'json_bool (true/false)', 'nested_templates_value (null or list of entries)', 'choice_array (different license lists)', 'binary_path_expr / text_contents variations'], reachable_by_harness_only=['zipfile.clone_to_dir path expansion (requires a real filesystem path)', 'vcs.repo_url parsing (needs a URL string supplied by the harness)', 'config.expand_path handling of environment variables and ~ (requires harness to set env vars)', 'generate.py deep‑merge of dictionary variables that are only created when extra_context contains nested dicts not expressed in the current grammar'], unreachable_harness_limits=['The harness cannot create actual files on disk, so binary file write‑out paths cannot be verified beyond grammar generation.', 'Network‑based VCS cloning cannot be performed in the sandbox, limiting coverage of vcs.clone_repo.'], line_target_hints=[{'target': 'cookiecutter/generate.py:72', 'delivery': 'grammar', 'code_signal': 'assigning a new key into a nested context dictionary when a variable is a dictionary variable', 'required_inputs': 'extra_context_object must contain a nested dict, e.g. { "project_name": { "sub": "value" } } and invocation_object.no_input = false so the generator walks the dict.', 'grammar_implication': 'Add an alternative to extra_context_object that yields a nested dictionary structure (e.g., \'{ "project_name": { "sub": "value" } }\').'}, {'target': 'cookiecutter/generate.py:76-78', 'delivery': 'grammar', 'code_signal': 'handling list values inside a dictionary variable during deep‑merge', 'required_inputs': 'extra_context_object with a list value for a known variable, e.g. { "license": ["MIT", "GPL"] } and a matching variable in cookiecutter_json_object.', 'grammar_implication': 'Extend extra_context_object with a case that includes a list literal (JSON array) for a key.'}, {'target': 'cookiecutter/prompt.py:53-58', 'delivery': 'grammar', 'code_signal': 'conversion of user input strings to boolean choices (yes/no)', 'required_inputs': 'invocation_object.no_input = false and prompts_object must contain a boolean‑type prompt (e.g., "use_docker"), then extra_context_object supplies values like "yes", "no", "y", "n".', 'grammar_implication': 'Add a new rule extra_context_object_bool that can emit boolean‑style strings ("yes", "no", "y", "n", "true", "false") for boolean prompts.'}, {'target': 'cookiecutter/zipfile.py:38-39', 'delivery': 'harness', 'code_signal': 'expanding a user‑provided clone_to_dir path with Path.expanduser', 'required_inputs': 'A manifest that sets a top‑level field (e.g., "zip_clone_dir": "~/tmp/template") which the harness passes to zipfile.clone_to_dir(). The grammar does not currently expose such a field.', 'grammar_implication': 'Introduce a top‑level optional field (e.g., "zip_clone_dir") in the case manifest and map it to the harness call.'}, {'target': 'cookiecutter/vcs.py:41-44', 'delivery': 'harness', 'code_signal': 'splitting a repo URL of the form "git+https://example.com/repo.git"', 'required_inputs': 'A manifest that includes a field "repo_url": "git+https://example.com/repo.git" passed to the harness when invoking the template source loader.', 'grammar_implication': "Add a rule repo_url_literal that can produce strings with a '+' separator (git+, hg+)."}, {'target': 'cookiecutter/config.py:38-39', 'delivery': 'harness', 'code_signal': 'os.path.expandvars and expanduser on a path containing $HOME or ~', 'required_inputs': 'A manifest field "config_path": "~/{{cookiecutter.repo_name}}"" with an environment variable set (e.g., $HOME).', 'grammar_implication': "Add a rule config_path_expr that can embed '~' or '${HOME}' placeholders."}, {'target': 'cookiecutter/config.py:48-49', 'delivery': 'grammar', 'code_signal': 'deep copy of default configuration and merging overrides', 'required_inputs': 'extra_context_object that supplies a top‑level key matching a config option (e.g., "default_context": { "project_slug": "myproj" })', 'grammar_implication': 'Add an extra_context variant that includes a nested dict named "default_context" to trigger the deep‑copy/merge path.'}], recommended_rule_edits=[{'rule': 'extra_context_object', 'rationale': "Current alternatives only provide flat string values. Adding a nested dictionary alternative and a list‑value alternative will allow the generator's deep‑merge logic (lines 72‑78) to be exercised."}, {'rule': 'extra_context_object', 'rationale': 'Introduce a boolean‑style string alternative ("yes", "no", "y", "n") so that prompt._convert_to_bool() (prompt.py lines 53‑58) is exercised when no_input=false.'}, {'rule': 'hooks_object', 'rationale': 'Add a fourth alternative where one of the hook scripts raises an exception after a successful pre_prompt, to hit failure paths in cookiecutter/hooks.py.'}, {'rule': 'invocation_object', 'rationale': 'Create a third alternative that mixes overwrite_if_exists=true with skip_if_file_exists=false (and vice‑versa) to explore all flag combinations in generate.py.'}, {'rule': 'nested_templates_value', 'rationale': 'Add a single‑element list alternative (one nested_template_entry) to trigger the loop that processes nested templates without requiring a second entry.'}, {'rule': 'newline_value', 'rationale': 'Add an explicit \'"\\r"\' alternative to increase line‑break handling coverage.'}, {'rule': 'repo_url_literal', 'rationale': "New rule (top‑level) to emit repo URLs with a '+' separator, enabling vcs.py parsing."}, {'rule': 'config_path_expr', 'rationale': "New rule (top‑level) to emit paths containing '~' or '${HOME}' so config.expand_path is exercised."}])

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

