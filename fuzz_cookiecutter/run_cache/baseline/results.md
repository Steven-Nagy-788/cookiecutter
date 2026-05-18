# Batch Results

- Cases: 12
- Coverage: 63.80%
- Covered lines: 750/1101
- Covered branches: 140/294

| Case | Status | Mode | Exit | Exception | Phase | Files |
| --- | --- | --- | --- | --- | --- | --- |
| case_000 | WARNING | cli | 1 | SystemExit | render_path | 1 |
| case_001 | SUCCESS | api | 0 |  | render_file | 1 |
| case_002 | WARNING | cli | 1 | SystemExit | hook_script_render | 0 |
| case_003 | WARNING | api | 1 | NonTemplatedInputDirException | generate_files | 0 |
| case_004 | WARNING | cli | 1 | SystemExit | render_file | 0 |
| case_005 | WARNING | cli | 1 | NonTemplatedInputDirException | generate_files | 0 |
| case_006 | WARNING | api | 1 | OutputDirExistsException | render_path | 1 |
| case_007 | WARNING | cli | 1 | SystemExit | pre_prompt | 1 |
| case_008 | SUCCESS | api | 0 |  | render_file | 0 |
| case_009 | SUCCESS | cli | 0 |  | hook_run | 0 |
| case_010 | SUCCESS | api | 0 |  | render_file | 2 |
| case_011 | WARNING | cli | 1 | SystemExit | pre_prompt | 1 |
