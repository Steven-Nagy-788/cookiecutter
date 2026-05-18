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
