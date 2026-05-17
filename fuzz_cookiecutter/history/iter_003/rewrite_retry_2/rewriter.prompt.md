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

PlannerOutput(analysis='The current corpus heavily exercises the CLI/API mode selection and the pre_prompt hook failure, but almost never reaches the deeper generate logic (dictionary variable overwrites, list handling) or the prompt boolean conversion paths. Most failures are NonTemplatedInputDirException, indicating the template source is always "local" with no VCS/zip handling. Coverage gaps cluster in generate.py (variable overwrites), prompt.py (yes/no choice parsing), zipfile.py (URL handling), vcs.py (repo URL parsing), and config.py (path expansion). The grammar does not currently provide any constructs to trigger VCS/zip paths, URL‑based template sources, or to supply unusual boolean inputs that would exercise prompt conversion. Moreover, the extra_context and replay objects are limited, preventing exploration of nested replay payloads that could hit generate.py\'s dictionary merge logic.', overrepresented_responses=['mode="cli" or "api" with default template_source="local"', 'pre_prompt hook raising SystemExit', 'no_input=true paths'], underexplored_scenario_families=['template_source via VCS or zip URL', 'extra_context/replay payloads that contain nested dictionaries or lists', 'boolean prompt answers that trigger yes/no conversion logic', 'overwrite_if_exists / skip_if_file_exists combinations that cause file‑collision handling', 'hooks that succeed (pre_gen_project / post_gen_project) and hooks that raise other exceptions'], reachable_by_grammar=['template_source (currently only "local")', 'execution_mode', 'nested_templates', 'hooks scripts', 'extra_context objects', 'replay payloads'], reachable_by_harness_only=['VCS/zip URL handling (requires external resources)', "filesystem path expansion edge cases (e.g., '~' or env vars)", 'network failures in zipfile download'], unreachable_harness_limits=['Cannot simulate remote git/hg repositories without network access', 'Cannot create actual zip files on the fly for zipfile path handling'], line_target_hints=[{'target': 'cookiecutter/generate.py:72', 'delivery': 'grammar', 'code_signal': 'Assigning a new variable in a deeper dictionary level during context merging', 'required_inputs': 'A replay payload or extra_context that contains a nested dictionary key not present in the base cookiecutter_json, e.g., extra_context: { "new_section": { "subkey": "value" } }', 'grammar_implication': 'Add a new alternative to extra_context_object that allows arbitrary nested JSON objects (e.g., using a generic json_object rule) so the manifest can inject a new dictionary variable.'}, {'target': 'cookiecutter/generate.py:76', 'delivery': 'grammar', 'code_signal': 'Handling a list value inside a dictionary variable during merge', 'required_inputs': 'extra_context or replay containing a list, e.g., { "features": ["a", "b"] }', 'grammar_implication': 'Extend extra_context_object (and possibly replay_value) with a rule that can produce list literals (choice_array or a new list_literal rule).'}, {'target': 'cookiecutter/prompt.py:53', 'delivery': 'grammar', 'code_signal': 'Conversion of raw user input string to boolean via yes/no choice sets', 'required_inputs': 'A prompt that expects a boolean and an extra_context entry that supplies a non‑standard string such as "Y" or "n" (mixed case, whitespace)', 'grammar_implication': 'Introduce a new rule boolean_input_string with alternatives like "Y", "yes", "No", " n " etc., and allow extra_context values to be these raw strings instead of json_bool.'}, {'target': 'cookiecutter/zipfile.py:38', 'delivery': 'harness', 'code_signal': "Path expansion for a clone_to_dir that contains '~' or environment variables", 'required_inputs': 'Set the output_dir_state to a path like "~/tmp/{{cookiecutter.repo_name}}" via a new manifest field (requires harness support).', 'grammar_implication': 'N/A – this line is exercised by the harness configuring the output directory.'}, {'target': 'cookiecutter/vcs.py:41', 'delivery': 'harness', 'code_signal': 'Parsing a repo URL with a VCS scheme (e.g., "git+https://example.com/repo.git")', 'required_inputs': 'template_source must be a URL (e.g., "git+https://example.com/repo.git") which is currently not allowed by the grammar.', 'grammar_implication': 'Replace the template_source rule with alternatives for "git+...", "hg+...", and zip URLs, or add a new rule template_source_url that matches a URL string.'}, {'target': 'cookiecutter/config.py:38', 'delivery': 'harness', 'code_signal': 'Expansion of environment variables in a path string', 'required_inputs': 'Provide an output_dir_state that includes "$HOME" or "%USERPROFILE%"; this is controlled by the test harness rather than the manifest.', 'grammar_implication': 'N/A'}], recommended_rule_edits=[{'rule': 'template_source', 'rationale': 'Add alternatives for VCS and zip URLs to reach vcs.py and zipfile.py logic.'}, {'rule': 'extra_context_object', 'rationale': "Allow nested dictionary and list literals (e.g., using a generic json_value rule) so generate.py's dictionary/list merge paths are exercised."}, {'rule': 'replay_value', 'rationale': 'Extend to accept nested structures and list values, mirroring the extra_context enhancements.'}, {'rule': 'hook_script', 'rationale': 'Add a successful hook variant that writes a file without raising, and a variant that raises a non‑SystemExit exception to explore different hook failure modes.'}, {'rule': 'json_bool', 'rationale': 'Introduce a rule raw_bool_string with values like "Y", "yes", "No", " n " to feed prompt conversion paths.'}])

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

