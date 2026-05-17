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

PlannerOutput(analysis='The current corpus heavily exercises the CLI/API mode selection and the replay/no_input branches, but many internal paths remain untouched: handling of dictionary variable overwrites in generate.py, boolean conversion in prompt.py, zipfile extraction, VCS cloning, and config path expansion. Most failures are NonTemplatedInputDirException, indicating the template source is always "local" and never triggers remote‑repo handling. Hooks are only exercised for success/failure, but not for missing hook scripts. The grammar already covers many literals but lacks ways to provoke the missing lines (e.g., providing extra_context that creates nested dictionary variables, using copy_without_render with binary files, varying new_lines, and forcing zipfile/VCS paths).', overrepresented_responses=['mode=api', 'mode=cli', 'no_input=true', 'no_input=false with empty extra_context', 'hooks=pre_prompt success/failure'], underexplored_scenario_families=['remote template source (git/hg URL) to hit vcs.py and zipfile.py', 'extra_context that creates nested dictionary variables causing generate.py overwrite logic', 'boolean prompt conversion (yes/no choices) to hit prompt.py lines 53‑58', 'config path expansion with environment variables and user home shortcuts', 'copy_without_render with binary files and new_lines variations', 'output_dir_state collisions with overwrite_if_exists / skip_if_file_exists combos'], reachable_by_grammar=['extra_context_object (add nested dict entries)', 'copy_without_render_array (add more patterns)', 'newline_value (add other escape sequences)', 'json_bool (already present)', 'hooks_object (add null or script variants)', 'output_dir_state (already present)', 'replay_value (extend with partial dicts)', 'choice_array (add more licenses)', 'path_expr / binary_path_expr (add deeper templated paths)'], reachable_by_harness_only=['template_source = remote URL (requires harness to supply a git/hg repo)', 'environment variable expansion in config paths (needs harness to set env vars)', 'zipfile extraction of a remote archive (requires harness to host a zip)', 'VCS cloning logic (needs harness to provide a repo URL)', 'prompt boolean conversion (needs harness to feed interactive answers)'], unreachable_harness_limits=['The harness cannot simulate interactive stdin for prompt conversion without modifying the grammar to embed answer strings.', 'Remote repository fetching cannot be forced purely by grammar; the harness must host a repo or mock network calls.'], line_target_hints=[{'target': 'cookiecutter/generate.py:72', 'delivery': 'grammar', 'code_signal': 'assigning a new variable in a nested dictionary when in_dictionary_variable is true', 'required_inputs': 'extra_context_object must contain a nested dict like {"nested": {"var": "value"}} and invocation.no_input must be false so the generator walks the context merging logic', 'grammar_implication': 'Add a new alternative to extra_context_object that yields a nested dictionary with at least two levels, e.g., \'{ "nested": { "inner": "val" } }\''}, {'target': 'cookiecutter/generate.py:76', 'delivery': 'grammar', 'code_signal': 'handling list values inside a dictionary variable during context merging', 'required_inputs': 'extra_context_object must provide a list under a key that already exists in the template context (e.g., "license": ["MIT", "GPL"]). Also set overwrite_if_exists true to force the branch.', 'grammar_implication': 'Extend extra_context_object with a case that includes a list literal, e.g., \'{ "license": ["MIT", "GPL"] }\''}, {'target': 'cookiecutter/prompt.py:53', 'delivery': 'harness', 'code_signal': 'value.strip().lower() and membership checks in yes_choices/no_choices', 'required_inputs': 'During a prompt, supply answer strings such as "YES", "y", "No", "n" via the harness\'s simulated stdin or by setting no_input=false and providing a replay payload that contains these strings.', 'grammar_implication': 'N/A – requires harness to feed prompt answers; alternatively, embed a replay_value that contains pre‑filled answers matching yes/no choices.'}, {'target': 'cookiecutter/zipfile.py:38', 'delivery': 'harness', 'code_signal': 'Path expansion of clone_to_dir for a remote zip download', '~required_inputs': 'template_source must be a remote URL (e.g., "https://example.com/template.zip") and the harness must provide a reachable zip file; output_dir_state can be "missing" to trigger extraction.', 'grammar_implication': 'Introduce a new rule template_source_remote that allows a string literal matching a URL; mark it as editable.'}, {'target': 'cookiecutter/vcs.py:41', 'delivery': 'harness', 'code_signal': "splitting repo_url on '+' and handling git/hg types", 'required_inputs': 'template_source set to a VCS URL like "git+https://github.com/user/repo.git"; harness must mock or provide the repo.', 'grammar_implication': 'Add an alternative to template_source that matches a VCS URL pattern.'}, {'target': 'cookiecutter/config.py:38', 'delivery': 'harness', 'code_signal': 'os.path.expandvars and expanduser on a path string', 'required_inputs': 'Provide a path containing environment variables (e.g., "${HOME}/.cookiecutter") and set an env var in the harness; also test a tilde path "~/template".', 'grammar_implication': 'Add a rule for template_source that can be a path string with ${VAR} or ~, or let harness inject such a string directly.'}], recommended_rule_edits=[{'rule': 'extra_context_object', 'rationale': 'Add nested dictionary and list alternatives to trigger generate.py overwrite and list handling branches.'}, {'rule': 'template_source', 'rationale': 'Introduce a remote URL alternative (e.g., "https://example.com/template.zip") and a VCS URL alternative (e.g., "git+https://github.com/user/repo.git") to reach zipfile.py and vcs.py.'}, {'rule': 'newline_value', 'rationale': 'Add a Windows‑style CRLF literal "\\r\\n" already present, but also include "\\r" to vary line‑ending handling.'}, {'rule': 'copy_without_render_array', 'rationale': 'Add a case with multiple glob patterns and a mix of binary and text paths to exercise binary handling and copy_without_render logic.'}, {'rule': 'hooks_object', 'rationale': 'Add a variant where one of the hook scripts is null while others are valid, to test partial hook presence.'}, {'rule': 'replay_value', 'rationale': 'Add a replay payload that omits some keys (e.g., only "project_name") to test partial replay handling.'}])

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

