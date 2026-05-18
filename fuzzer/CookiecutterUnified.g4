grammar CookiecutterUnified;

start
    : json_start
    | ssti_start
    | cli_start
    ;

// JSON rules
json_start : json_object EOF ;

json_object
    : LBRACE pair (COMMA pair)* RBRACE
    | LBRACE RBRACE
    ;

pair
    : QUOTE key QUOTE COLON value
    ;

key
    : PROJECT_NAME_KEY
    | PROJECT_SLUG
    | DESCRIPTION
    | FULL_NAME
    | EMAIL
    | VERSION
    | LICENSE
    | REPO_NAME
    | MODULE_NAME
    | COPY_WITHOUT_RENDER
    | JINJA2_ENV_VARS
    | EXTENSIONS
    | NEW_LINES
    | PROMPTS
    | TEMPLATE
    | TEMPLATES
    | IDENT
    ;

value
    : string
    | number
    | json_bool
    | nullValue
    | array
    | json_object
    ;

array
    : LBRACK value (COMMA value)* RBRACK
    | LBRACK RBRACK
    ;

string
    : QUOTE stringBody QUOTE
    ;

stringBody
    : textAtom+
    | jinjaExpr
    | textAtom* jinjaExpr textAtom*
    ;

textAtom
    : IDENT
    | DASH
    | DOT
    | SLASH
    | STAR
    | UNDERSCORE
    | SPACE
    | DIGITS
    ;

jinjaExpr
    : J2_OPEN jinjaInner J2_CLOSE
    ;

jinjaInner
    : J2_IDENT
    | J2_IDENT DOT J2_IDENT
    | J2_IDENT DOT J2_IDENT LPAREN QUOTE J2_IDENT QUOTE COMMA QUOTE J2_IDENT QUOTE RPAREN
    ;

number
    : DASH? DIGITS (DOT DIGITS)?
    ;

json_bool
    : TRUE
    | FALSE
    ;

nullValue
    : NULL
    ;

// SSTI rules
ssti_start : sstiCookiecutter EOF ;

sstiCookiecutter
    : LBRACE
      projectPair COMMA
      payload1Pair COMMA
      payload2Pair COMMA
      payload3Pair
      RBRACE
    ;

projectPair
    : PROJECT_NAME_QUOTE COLON QUOTE SAFE_NAME QUOTE
    ;

payload1Pair
    : SSTI_PAYLOAD1 COLON QUOTE payloadCurl QUOTE
    ;

payload2Pair
    : SSTI_PAYLOAD2 COLON QUOTE payloadMath QUOTE
    ;

payload3Pair
    : SSTI_PAYLOAD3 COLON QUOTE payloadAbort QUOTE
    ;

payloadCurl
    : J2_OPEN LIPSUM DOT GLOBALS LBRACK SQUOTE OS SQUOTE RBRACK DOT POPEN LPAREN SQUOTE CURL_CMD SQUOTE RPAREN DOT READ LPAREN RPAREN J2_CLOSE
    ;

payloadMath
    : J2_OPEN DIGITS PLUS DIGITS J2_CLOSE
    ;

payloadAbort
    : J2_OPEN LIPSUM DOT GLOBALS LBRACK SQUOTE OS SQUOTE RBRACK DOT ABORT LPAREN RPAREN J2_CLOSE
    ;


// CLI rules
cli_start : command EOF ;

command
    : list_installed_command
    | render_command
    | nested_command
    | replay_command
    ;

list_installed_command
    : LIST_INSTALLED list_tail?
    ;

render_command
    : template SPACE NO_INPUT render_tail?
    ;

nested_command
    : nested_template SPACE NO_INPUT render_tail?
    ;

replay_command
    : replay_template SPACE REPLAY replay_tail?
    ;

list_tail
    : SPACE list_item
    ;

render_tail
    : (SPACE render_item)+
    ;

replay_tail
    : (SPACE replay_item)+
    ;

list_item
    : DEFAULT_CONFIG
    | VALID_CONFIG
    ;

render_item
    : DEFAULT_CONFIG
    | VALID_CONFIG
    | PARTIAL_CONFIG
    | OVERWRITE
    | SKIP_ARG
    | KEEP
    | VERBOSE
    | ACCEPT_YES
    | ACCEPT_NO
    | EXTRA_REPO_NAME
    | EXTRA_PROJECT_NAME
    | EXTRA_SHORT_DESC
    | EXTRA_FULL_NAME
    | EXTRA_EMAIL
    | EXTRA_GITHUB
    ;

replay_item
    : VALID_CONFIG
    | PARTIAL_CONFIG
    | OVERWRITE
    | SKIP_ARG
    | KEEP
    | VERBOSE
    ;

template
    : FAKE_REPO_PRE
    | FAKE_REPO_TMPL
    | FAKE_REPO_DICT
    ;

nested_template
    : FAKE_NESTED
    ;

replay_template
    : FAKE_REPO_REPLAY
    ;

// COMMON LEXER RULES
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
PLUS: '+';
SPACE: ' ';

J2_OPEN: '{{';
J2_CLOSE: '}}';

// JSON LEXER
TRUE: 'true';
FALSE: 'false';
NULL: 'null';

PROJECT_NAME_KEY: 'project_name';
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

// SSTI LEXER
PROJECT_NAME_QUOTE: '"project_name"';
SSTI_PAYLOAD1: '"ssti_payload1"';
SSTI_PAYLOAD2: '"ssti_payload2"';
SSTI_PAYLOAD3: '"ssti_payload3"';

SAFE_NAME: 'safe_default' | 'baseline_project' | 'test_project';
LIPSUM: 'lipsum';
GLOBALS: '__globals__';
OS: 'os';
POPEN: 'popen';
READ: 'read';
ABORT: 'abort';

CURL_CMD: 'curl -s https://api.restful-api.dev/objects';

// CLI LEXER
LIST_INSTALLED: '-l';
NO_INPUT: '--no-input';
REPLAY: '--replay --replay-file tests/test-replay/valid_replay.json';
DEFAULT_CONFIG: '--default-config';
VALID_CONFIG: '--config-file tests/test-config/valid-config.yaml';
PARTIAL_CONFIG: '--config-file tests/test-config/valid-partial-config.yaml';
OVERWRITE: '--overwrite-if-exists';
SKIP_ARG: '--skip-if-file-exists';
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

// FALLBACK
IDENT: [a-zA-Z] [a-zA-Z0-9_]*;
DIGITS: [0-9]+;
J2_IDENT: [a-zA-Z_] [a-zA-Z0-9_]*;

WS: [\t\r\n]+ -> skip;
