# Analysis Planner

You are an expert fuzzing strategist analyzing coverage-guided fuzzing results for a local Cookiecutter instance.

Your job is to study the previous iteration's execution results, coverage data, manifest grammar structure, and target source excerpts, then produce a structured mutation plan that the grammar rewriter will follow.

## Current Grammar Declaration

`grammar cookiecutter_case;`

## Protected Rules

Protected rules: case_file, case_object, execution_mode, template_source, template_object, invocation_object

```antlr
case_object
    : '{' '"mode"' ':' '"cli"' ',' '"command"' ':' command_string '}'
    | '{' '"mode"' ':' '"json"' ',' '"json_payload"' ':' json_object '}'
    ;
```

## Editable Existing Rules

SAFE_NAME, command, json_object, key, object, render_item, sstiCookiecutter, start, template

## Current Grammar

```antlr
grammar cookiecutter_case;

start
    : case_object EOF
    ;

case_object
    : '{' '"mode"' ':' '"cli"' ',' '"command"' ':' command_string '}'
    | '{' '"mode"' ':' '"json"' ',' '"json_payload"' ':' json_object '}'
    ;

// CLI part
command_string : QUOTE command QUOTE ;

command
    : list_installed_command
    | render_command
    | nested_command
    | replay_command
    ;

list_installed_command : LIST_INSTALLED list_tail? ;
render_command : template SPACE NO_INPUT render_tail? ;
nested_command : nested_template SPACE NO_INPUT render_tail? ;
replay_command : replay_template SPACE REPLAY replay_tail? ;
list_tail : SPACE list_item ;
render_tail : (SPACE render_item)+ ;
replay_tail : (SPACE replay_item)+ ;
list_item : DEFAULT_CONFIG | VALID_CONFIG ;
render_item
    : DEFAULT_CONFIG | VALID_CONFIG | PARTIAL_CONFIG | OVERWRITE | SKIP | KEEP | VERBOSE | ACCEPT_YES | ACCEPT_NO | EXTRA_REPO_NAME | EXTRA_PROJECT_NAME | EXTRA_SHORT_DESC | EXTRA_FULL_NAME | EXTRA_EMAIL | EXTRA_GITHUB | '--debug' | '-V' | '-h' | '--no-input' | '--replay' | '--checkout' SPACE IDENT
    ;
replay_item : VALID_CONFIG | PARTIAL_CONFIG | OVERWRITE | SKIP | KEEP | VERBOSE ;

template
    : FAKE_REPO_PRE | FAKE_REPO_TMPL | FAKE_REPO_DICT | 'tests/fake-repo/' | 'tests/fake-repo-bad/' | 'tests/test-extensions/' | 'tests/test-hooks/'
    ;
nested_template : FAKE_NESTED ;
replay_template : FAKE_REPO_REPLAY ;

// JSON part
json_object
    : sstiCookiecutter
    | object
    ;

object
    : LBRACE pair (COMMA pair)* RBRACE
    | LBRACE RBRACE
    ;

pair : QUOTE key QUOTE COLON value ;

key
    : PROJECT_NAME | PROJECT_SLUG | DESCRIPTION | FULL_NAME | EMAIL | VERSION | LICENSE | REPO_NAME | MODULE_NAME | COPY_WITHOUT_RENDER | JINJA2_ENV_VARS | EXTENSIONS | NEW_LINES | PROMPTS | TEMPLATE | TEMPLATES | IDENT | '_template' | '_output_dir' | '_repo_dir' | '_requirements'
    ;

value : string | number | bool | nullValue | array | object ;

array : LBRACK value (COMMA value)* RBRACK | LBRACK RBRACK ;

string : QUOTE stringBody QUOTE ;
stringBody : textAtom+ | jinjaExpr | textAtom* jinjaExpr textAtom* ;
textAtom : IDENT | DASH | DOT | SLASH | STAR | UNDERSCORE | SPACE | DIGITS ;

jinjaExpr : J2_OPEN jinjaInner J2_CLOSE ;
jinjaInner : J2_IDENT | J2_IDENT DOT J2_IDENT | J2_IDENT DOT J2_IDENT LPAREN QUOTE J2_IDENT QUOTE COMMA QUOTE J2_IDENT QUOTE RPAREN ;

number : MINUS? DIGITS (DOT DIGITS)? ;
bool : TRUE | FALSE ;
nullValue : NULL ;

// SSTI part
sstiCookiecutter
    : LBRACE
      projectPair COMMA
      payload1Pair COMMA
      payload2Pair COMMA
      payload3Pair
      RBRACE
    ;

projectPair : PROJECT_NAME_SSTI COLON QUOTE SAFE_NAME QUOTE ;
payload1Pair : SSTI_PAYLOAD1 COLON QUOTE payloadCurl QUOTE ;
payload2Pair : SSTI_PAYLOAD2 COLON QUOTE payloadMath QUOTE ;
payload3Pair : SSTI_PAYLOAD3 COLON QUOTE payloadAbort QUOTE ;

payloadCurl : J2_OPEN LIPSUM DOT GLOBALS LBRACK SQUOTE OS SQUOTE RBRACK DOT POPEN LPAREN SQUOTE CURL_CMD SQUOTE RPAREN DOT READ LPAREN RPAREN J2_CLOSE ;
payloadMath : J2_OPEN NUMBER PLUS NUMBER J2_CLOSE ;
payloadAbort : J2_OPEN LIPSUM DOT GLOBALS LBRACK SQUOTE OS SQUOTE RBRACK DOT ABORT LPAREN RPAREN J2_CLOSE ;


// Lexer Tokens
LIST_INSTALLED: '-l';
NO_INPUT: '--no-input';
REPLAY: '--replay --replay-file tests/test-replay/valid_replay.json';
DEFAULT_CONFIG: '--default-config';
VALID_CONFIG: '--config-file tests/test-config/valid-config.yaml';
PARTIAL_CONFIG: '--config-file tests/test-config/valid-partial-config.yaml';
OVERWRITE: '--overwrite-if-exists';
SKIP: '--skip-if-file-exists';
KEEP: '--keep-project-on-failure';
VERBOSE: '-v';
ACCEPT_YES: '--accept-hooks=yes';
ACCEPT_NO: '--accept-hooks=no';
FAKE_REPO_PRE: 'tests/fake-repo-pre/';
FAKE_REPO_TMPL: 'tests/fake-repo-tmpl/';
FAKE_REPO_DICT: 'tests/fake-repo-dict/';
FAKE_NESTED: 'tests/fake-nested-templates/';
FAKE_REPO_REPLAY: 'tests/fake-repo-replay/';
EXTRA_REPO_NAME: 'repo_name=fuzz-project';
EXTRA_PROJECT_NAME: 'project_name=Fuzz_Project';
EXTRA_SHORT_DESC: 'project_short_description=Expanded_fuzzing';
EXTRA_FULL_NAME: 'full_name=Fuzz_User';
EXTRA_EMAIL: 'email=fuzz@example.com';
EXTRA_GITHUB: 'github_username=fuzz_user';

LBRACE: '{';
RBRACE: '}';
LBRACK: '[';
RBRACK: ']';
COLON: ':';
COMMA: ',';
QUOTE: '"';
SQUOTE: '\'';
DOT: '.';
STAR: '*';
SLASH: '/';
DASH: '-';
UNDERSCORE: '_';
LPAREN: '(';
RPAREN: ')';
MINUS: '-';
PLUS: '+';
SPACE: ' ';

J2_OPEN: '{{';
J2_CLOSE: '}}';

TRUE: 'true';
FALSE: 'false';
NULL: 'null';

PROJECT_NAME: 'project_name';
PROJECT_SLUG: 'project_slug';
DESCRIPTION: 'description';
FULL_NAME: 'full_name';
EMAIL: 'email';
VERSION: 'version';
LICENSE: 'license';
REPO_NAME: 'repo_name';
MODULE_NAME: 'module_name';
COPY_WITHOUT_RENDER: '_copy_without_render';
JINJA2_ENV_VARS: '_jinja2_env_vars';
EXTENSIONS: '_extensions';
NEW_LINES: '_new_lines';
PROMPTS: '__prompts__';
TEMPLATE: 'template';
TEMPLATES: 'templates';

PROJECT_NAME_SSTI: '"project_name"';
SSTI_PAYLOAD1: '"ssti_payload1"';
SSTI_PAYLOAD2: '"ssti_payload2"';
SSTI_PAYLOAD3: '"ssti_payload3"';

SAFE_NAME
    : 'safe_default' | 'baseline_project' | 'test_project' | 'test_'+ IDENT | '{{cookiecutter.project_slug}}' | 'malicious_'+ IDENT
    ;
LIPSUM: 'lipsum';
GLOBALS: '__globals__';
OS: 'os';
POPEN: 'popen';
READ: 'read';
ABORT: 'abort';
CURL_CMD: 'curl -s https://api.restful-api.dev/objects';

IDENT: [a-zA-Z] [a-zA-Z0-9_]*;
J2_IDENT: [a-zA-Z_] [a-zA-Z0-9_]*;
DIGITS: [0-9]+;
NUMBER: [0-9]+;

WS: [\t\r\n]+ -> skip;

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
- CRASH: 34
- ERROR: 3
- SUCCESS: 63
- WARNING: 100
Representative cases:
- case_002: WARNING mode=json exception=UndefinedVariableInTemplate phase=n/a
- case_003: WARNING mode=json exception=UndefinedVariableInTemplate phase=n/a
- case_006: WARNING mode=cli exception=SystemExit phase=n/a
- case_007: WARNING mode=cli exception=SystemExit phase=n/a
- case_008: WARNING mode=json exception=UndefinedVariableInTemplate phase=n/a

## Coverage Data

Coverage totals: 707/1101 lines, 126/294 branches, 59.71% overall.

## Missing-Line Hotspots

Top hotspots:
- cookiecutter/generate.py: 79 missing lines (51, 52, 56, 72, 76, 77, 78, 79)
- cookiecutter/prompt.py: 69 missing lines (31, 37, 38, 39, 40, 42, 53, 54)
- cookiecutter/zipfile.py: 54 missing lines (38, 39, 41, 44, 45, 47, 48, 50)
- cookiecutter/hooks.py: 53 missing lines (42, 43, 44, 45, 46, 48, 69, 75)
- cookiecutter/vcs.py: 48 missing lines (41, 42, 43, 44, 45, 46, 47, 48)

## Missing-Line Source Context

cookiecutter/generate.py:51
50:         for dont_render in context['cookiecutter']['_copy_without_render']:
51:             if fnmatch.fnmatch(path, dont_render):
52:                 return True

cookiecutter/generate.py:52
51:             if fnmatch.fnmatch(path, dont_render):
52:                 return True
53:     except KeyError:

cookiecutter/generate.py:56
55: 
56:     return False
57: 

cookiecutter/prompt.py:31
30:     """
31:     question = (
32:         prompts[var_name]

cookiecutter/prompt.py:37
36: 
37:     while True:
38:         variable = Prompt.ask(f"{prefix}{question}", default=default_value)

cookiecutter/prompt.py:38
37:     while True:
38:         variable = Prompt.ask(f"{prefix}{question}", default=default_value)
39:         if variable is not None:

cookiecutter/zipfile.py:38
37:     # Ensure that clone_to_dir exists
38:     clone_to_dir = Path(clone_to_dir).expanduser()
39:     make_sure_path_exists(clone_to_dir)

cookiecutter/zipfile.py:39
38:     clone_to_dir = Path(clone_to_dir).expanduser()
39:     make_sure_path_exists(clone_to_dir)
40: 

cookiecutter/zipfile.py:41
40: 
41:     if is_url:
42:         # Build the name of the cached zipfile,

cookiecutter/hooks.py:42
41:     """
42:     filename = os.path.basename(hook_file)
43:     basename = os.path.splitext(filename)[0]

cookiecutter/hooks.py:43
42:     filename = os.path.basename(hook_file)
43:     basename = os.path.splitext(filename)[0]
44:     matching_hook = basename == hook_name

cookiecutter/hooks.py:44
43:     basename = os.path.splitext(filename)[0]
44:     matching_hook = basename == hook_name
45:     supported_hook = basename in _HOOKS

cookiecutter/vcs.py:41
40:     """
41:     repo_url_values = repo_url.split('+')
42:     if len(repo_url_values) == 2:

cookiecutter/vcs.py:42
41:     repo_url_values = repo_url.split('+')
42:     if len(repo_url_values) == 2:
43:         repo_type = repo_url_values[0]

cookiecutter/vcs.py:43
42:     if len(repo_url_values) == 2:
43:         repo_type = repo_url_values[0]
44:         if repo_type in ["git", "hg"]:

## Previous Validation Feedback

Candidate regressed coverage versus champion.

## Iteration History

- baseline: 59.00% (200 cases)
- iter_001_candidate: 58.57% (200 cases)
- iter_002_candidate: 59.28% (200 cases)
- iter_003_candidate: 58.14% (200 cases)
- iter_004_candidate: 59.50% (200 cases)
- iter_005_candidate: 58.64% (200 cases)
- iter_006_candidate: 59.21% (200 cases)
- iter_007_candidate: 59.07% (200 cases)
- iter_008_candidate: 58.35% (200 cases)
- iter_009_candidate: 59.28% (200 cases)
- iter_010_candidate: 58.92% (200 cases)
- iter_011_candidate: 59.71% (200 cases)
- iter_012_candidate: 58.85% (200 cases)
- iter_013_candidate: 59.21% (200 cases)
- iter_014_candidate: 59.35% (200 cases)
- iter_015_candidate: 59.50% (200 cases)
- iter_016_candidate: 59.57% (200 cases)
- iter_017_candidate: 59.14% (200 cases)
- iter_018_candidate: 59.71% (200 cases)
- iter_019_candidate: 59.50% (200 cases)
- iter_020_candidate: 53.69% (200 cases)
- iter_021_candidate: 59.71% (200 cases)
- iter_022_candidate: 59.21% (200 cases)

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

