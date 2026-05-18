# Batch Results

- Cases: 12
- Coverage: 59.21%
- Covered lines: 704/1101
- Covered branches: 122/294

| Case | Status | Mode | Exit | Exception | Phase | Files |
| --- | --- | --- | --- | --- | --- | --- |
| case_000 | SUCCESS | api | 0 |  | render_file | 4 |
| case_001 | WARNING | api | 1 | NonTemplatedInputDirException | generate_files | 1 |
| case_002 | WARNING | api | 1 | UndefinedVariableInTemplate | render_file | 1 |
| case_003 | SUCCESS | api | 0 |  | render_file | 0 |
| case_004 | WARNING | cli | 1 | SystemExit | render_file | 1 |
| case_005 | WARNING | api | 1 | FailedHookException | pre_prompt | 0 |
| case_006 | WARNING | api | 1 | UndefinedVariableInTemplate | render_file | 0 |
| case_007 | SUCCESS | cli | 0 |  | render_file | 4 |
| case_008 | WARNING | cli | 1 | SystemExit | pre_prompt | 1 |
| case_009 | WARNING | api | 1 | OutputDirExistsException | render_path | 1 |
| case_010 | WARNING | cli | 1 | SystemExit | render_file | 2 |
| case_011 | WARNING | api | 1 | FailedHookException | pre_prompt | 0 |
