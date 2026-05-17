# Analysis Planner

You are an expert fuzzing strategist analyzing coverage-guided fuzzing results for a local Cookiecutter instance.

Your job is to study the previous iteration's execution results, coverage data, manifest grammar structure, and target source excerpts, then produce a structured mutation plan that the grammar rewriter will follow.

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

## Previous Run Results

Result counts:
- SUCCESS: 4
- WARNING: 8
Representative cases:
- case_000: WARNING mode=api exception=NonTemplatedInputDirException phase=generate_files
- case_001: WARNING mode=api exception=NonTemplatedInputDirException phase=generate_files
- case_002: WARNING mode=api exception=NonTemplatedInputDirException phase=generate_files
- case_004: WARNING mode=cli exception=SystemExit phase=pre_prompt
- case_007: WARNING mode=api exception=NonTemplatedInputDirException phase=generate_files

## Coverage Data

Coverage totals: 735/1101 lines, 131/294 branches, 62.08% overall.

## Missing-Line Hotspots

Top hotspots:
- cookiecutter\generate.py: 66 missing lines (72, 76, 77, 78, 79, 82, 83, 85)
- cookiecutter\prompt.py: 54 missing lines (53, 54, 55, 56, 57, 58, 75, 80)
- cookiecutter\zipfile.py: 54 missing lines (38, 39, 41, 44, 45, 47, 48, 50)
- cookiecutter\vcs.py: 48 missing lines (41, 42, 43, 44, 45, 46, 47, 48)
- cookiecutter\config.py: 41 missing lines (38, 39, 48, 50, 53, 54, 56, 58)

## Missing-Line Source Context

cookiecutter\generate.py:72
71:             # We are dealing with a new dictionary variable in a deeper level
72:             context[variable] = overwrite
73: 

cookiecutter\generate.py:76
75:         if isinstance(context_value, list):
76:             if in_dictionary_variable:
77:                 context[variable] = overwrite

cookiecutter\generate.py:77
76:             if in_dictionary_variable:
77:                 context[variable] = overwrite
78:                 continue

cookiecutter\prompt.py:53
52:         """Convert choices to a bool."""
53:         value = value.strip().lower()
54:         if value in self.yes_choices:

cookiecutter\prompt.py:54
53:         value = value.strip().lower()
54:         if value in self.yes_choices:
55:             return True

cookiecutter\prompt.py:55
54:         if value in self.yes_choices:
55:             return True
56:         if value in self.no_choices:

cookiecutter\zipfile.py:38
37:     # Ensure that clone_to_dir exists
38:     clone_to_dir = Path(clone_to_dir).expanduser()
39:     make_sure_path_exists(clone_to_dir)

cookiecutter\zipfile.py:39
38:     clone_to_dir = Path(clone_to_dir).expanduser()
39:     make_sure_path_exists(clone_to_dir)
40: 

cookiecutter\zipfile.py:41
40: 
41:     if is_url:
42:         # Build the name of the cached zipfile,

cookiecutter\vcs.py:41
40:     """
41:     repo_url_values = repo_url.split('+')
42:     if len(repo_url_values) == 2:

cookiecutter\vcs.py:42
41:     repo_url_values = repo_url.split('+')
42:     if len(repo_url_values) == 2:
43:         repo_type = repo_url_values[0]

cookiecutter\vcs.py:43
42:     if len(repo_url_values) == 2:
43:         repo_type = repo_url_values[0]
44:         if repo_type in ["git", "hg"]:

cookiecutter\config.py:38
37:     """Expand both environment variables and user home in the given path."""
38:     path = os.path.expandvars(path)
39:     return os.path.expanduser(path)

cookiecutter\config.py:39
38:     path = os.path.expandvars(path)
39:     return os.path.expanduser(path)
40: 

cookiecutter\config.py:48
47:     """
48:     new_config = copy.deepcopy(default)
49: 

## Previous Validation Feedback

Mutation plan updated more than 3 rules

## Iteration History

- baseline: 62.08% (12 cases)

## Response Format

Return JSON only. Use this exact shape:

{
  "analysis": "Brief summary of what you observed",
  "overrepresented_responses": ["..."],
  "underexplored_scenario_families": ["..."],
  "reachable_by_grammar": ["..."],
  "reachable_by_harness_only": ["..."],
  "unreachable_harness_limits": ["..."],
  "line_target_hints": [
    {
      "target": "cookiecutter/generate.py:123",
      "delivery": "grammar | harness",
      "code_signal": "what the uncovered line appears to check",
      "required_inputs": "exact manifest ingredients needed to reach the line",
      "grammar_implication": "what the grammar should add or broaden if delivery is grammar"
    }
  ],
  "recommended_rule_edits": [
    {"rule": "existingRuleName", "rationale": "why this edit helps"}
  ]
}

