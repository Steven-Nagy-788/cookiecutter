grammar CookiecutterCLIExpanded;

start
    : command EOF
    ;

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
    : template SP NO_INPUT render_tail?
    ;

nested_command
    : nested_template SP NO_INPUT render_tail?
    ;

replay_command
    : replay_template SP REPLAY replay_tail?
    ;

list_tail
    : SP list_item
    ;

render_tail
    : (SP render_item)+
    ;

replay_tail
    : (SP replay_item)+
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
    | SKIP
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
    | SKIP
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

SP: ' ';
WS: [\t\r\n]+ -> skip;