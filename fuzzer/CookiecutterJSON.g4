grammar CookiecutterJSON;

start
    : object EOF
    ;

object
    : LBRACE pair (COMMA pair)* RBRACE
    | LBRACE RBRACE
    ;

pair
    : QUOTE key QUOTE COLON value
    ;

key
    : PROJECT_NAME
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
    | bool
    | nullValue
    | array
    | object
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
    : MINUS? DIGITS (DOT DIGITS)?
    ;

bool
    : TRUE
    | FALSE
    ;

nullValue
    : NULL
    ;

LBRACE: '{';
RBRACE: '}';
LBRACK: '[';
RBRACK: ']';
COLON: ':';
COMMA: ',';
QUOTE: '"';
DOT: '.';
STAR: '*';
SLASH: '/';
DASH: '-';
UNDERSCORE: '_';
LPAREN: '(';
RPAREN: ')';
MINUS: '-';
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

IDENT: [a-zA-Z] [a-zA-Z0-9_]*;
DIGITS: [0-9]+;
J2_IDENT: [a-zA-Z_] [a-zA-Z0-9_]*;

WS: [\t\r\n]+ -> skip;
