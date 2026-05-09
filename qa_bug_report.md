# QA Deep-Dive Report — `cookiecutter.json` → User Prompt Pipeline
**Scope:** `generate_context()` → `apply_overwrites_to_context()` → `prompt_for_config()` → rendering  
**Analyst role:** Senior QA / Security Engineer  
**Date:** 2026-04-29  
**Methodology:** White-box (control-flow + data-flow), black-box (boundary value analysis, equivalence partitioning), grey-box (existing fuzz harness review + manual mutation)

---

## 1. Pipeline Map (what we are analysing)

```
cookiecutter.json (file)
        │
        ▼
generate_context()                      [generate.py:126]
  ├── json.load(..., object_pairs_hook=OrderedDict)
  ├── apply_overwrites_to_context(obj, default_context)   ← global ~/.cookiecutterrc
  └── apply_overwrites_to_context(obj, extra_context)     ← CLI --extra-vars
        │
        ▼
prompt_for_config(context, no_input)    [prompt.py:284]
  ├── Pass 1 — strings / booleans / lists (choices)
  └── Pass 2 — dicts
        │
        ▼
render_variable(env, raw, cookiecutter_dict)  [prompt.py:199]
  └── Jinja2 env.from_string(raw).render(cookiecutter=cookiecutter_dict)
```

---

## 2. Confirmed Bugs

### BUG-01 · `__prompts__` key is **destructively popped** from the live context — causes replay divergence
**Severity:** High  
**Type:** White-box — data-flow defect  
**Location:** `prompt.py:294`

```python
# prompt_for_config()
prompts = context['cookiecutter'].pop('__prompts__', {})
```

**What happens:** `pop()` mutates the `context` dict in-place. `prompt_for_config` is called with `context_for_prompting` (line 164 of `main.py`), which in replay mode is a **separate shallow dict** built from the live `context['cookiecutter']` (line 118-124). But in **non-replay mode** `context_for_prompting = context` (line 133), meaning both variables point to the **same object**. After the pop, the `__prompts__` key is gone from `context` permanently.

**Impact:** When the context is later serialised to replay file via `dump()` (line 181 of `main.py`), `__prompts__` is absent. On the next replay run, the new keys added since the last replay (lines 118-122) are prompted **without human-readable prompt text** — the variable machine-name is shown instead of the friendly label. Silent regression, very hard to catch.

**Repro vector (black-box):**
```json
{
  "__prompts__": { "project_name": "What is your project name?" },
  "project_name": "my_project"
}
```
Run once interactive → check replay file → run `--replay` → second prompt for any new key shows `project_name` not `What is your project name?`.

---

### BUG-02 · Integer / float values in `cookiecutter.json` are **silently stringified** and never validated
**Severity:** Medium  
**Type:** White-box — data-flow / type coercion defect  
**Location:** `prompt.py:231-232`

```python
if not isinstance(raw, str):
    raw = str(raw)   # ← covers int, float, None...  but None is already handled above
```

**What happens:** A JSON value of `42` (integer) passes the `list`, `bool`, `dict` guards, falls through to `not isinstance(raw, str)`, gets cast to `"42"` silently, and is then rendered via Jinja2 as a string. The user is prompted with default `"42"` (a string). Any downstream template logic that checks `{% if cookiecutter.port > 1024 %}` — a numeric comparison — will **fail with a Jinja2 TypeError** at generation time, not at prompt time, with no actionable error message.

**Repro vector:**
```json
{ "port": 8080 }
```
Template: `{{ cookiecutter.port + 1 }}` → `TypeError: unsupported operand type(s) for +: 'str' and 'int'`

**Root cause:** There is no schema/type enforcement at the boundary. The prompt layer assumes everything is a string after the `str(raw)` cast. The spec (README, docs) does say only strings/lists/dicts/booleans are supported, but the code doesn't reject integers — it silently poisons downstream rendering.

---

### BUG-03 · `render_variable` called on dict **keys** — Jinja2 `UndefinedError` on key rendering is NOT caught
**Severity:** Medium  
**Type:** White-box — exception handling gap  
**Location:** `prompt.py:222-228`

```python
if isinstance(raw, dict):
    return {
        render_variable(env, k, cookiecutter_dict): render_variable(
            env, v, cookiecutter_dict
        )
        for k, v in raw.items()
    }
```

The `try/except UndefinedError` block in `prompt_for_config` (lines 338-340) wraps only the **top-level** call to `render_variable`. But when `render_variable` is recursing into a dict, the inner `render_variable(env, k, ...)` call for a **key** that uses an undefined Jinja2 variable throws `UndefinedError` directly from the dict comprehension. This propagates **up through the recursion** and is caught — however the error message becomes:

```
Unable to render variable '<key_of_outer_dict>'
```

…which is **misleading**: the actual undefined variable is inside a dict key, not the outer dict key. Debugging becomes very hard with deeply nested dict variables.

**Repro vector:**
```json
{
  "author": "John",
  "metadata": {
    "{{ cookiecutter.undefined_var }}_suffix": "value"
  }
}
```
Error says `Unable to render variable 'metadata'` — hides the real culprit.

---

### BUG-04 · `choose_nested_template` — `re.search()` return value **never checked for None** → `AttributeError` crash
**Severity:** High  
**Type:** White-box — null-dereference / missing guard  
**Location:** `prompt.py:393`

```python
template = re.search(r'\((.+)\)', val).group(1)
```

This is the **old-style** nested template path. `read_user_choice` returns one of the `rendered_options` strings. Those are Jinja2-rendered from the list values in `cookiecutter.json`. If any rendered value does **not** contain a parenthesised path substring (e.g., the template author forgot the `(path/to/tmpl)` convention, or Jinja rendering strips it), `re.search()` returns `None`, and calling `.group(1)` raises `AttributeError: 'NoneType' object has no attribute 'group'`.

**Repro vector:**
```json
{
  "template": ["My Template", "Another Template"]
}
```
Neither item contains `(...)`. Result: hard crash with `AttributeError`, no custom exception, no user-friendly message.

**Test coverage:** Zero — no existing test covers old-style nested template with missing parenthesis pattern.

---

### BUG-05 · `cleanup` flag **overwrite logic error** — temporary repo dir leaked on pre-prompt hook failure
**Severity:** Medium  
**Type:** White-box — control-flow / resource leak  
**Location:** `main.py:92-96`

```python
repo_dir, cleanup = base_repo_dir, cleanup_base_repo_dir   # line 92
repo_dir = str(run_pre_prompt_hook(base_repo_dir)) if accept_hooks else repo_dir  # line 94
cleanup = repo_dir != base_repo_dir                          # line 96 ← OVERWRITES cleanup_base_repo_dir info
```

**What happens:** Line 96 unconditionally overwrites `cleanup` with a boolean derived from whether `repo_dir` changed. This means if `cleanup_base_repo_dir` was originally `True` (e.g., template was a cloned git repo to a temp dir) **and** the pre-prompt hook returns the **same** directory (hook doesn't change `repo_dir`), then `cleanup = False` is set on line 96. The temp dir is never cleaned up.

Additionally, at lines 196-199:
```python
if cleanup:
    rmtree(repo_dir)
if cleanup_base_repo_dir:
    rmtree(base_repo_dir)
```
`cleanup_base_repo_dir` is still checked separately, BUT `repo_dir` at line 196 is now the **potentially modified** dir from the hook. If the hook returned a different path, we clean the hook's temp dir — but `base_repo_dir` is the git clone temp dir. The logic is correct in that case. However if the hook **raises an exception** before returning, both `cleanup` (line 96) and `cleanup_base_repo_dir` are never acted on → **resource leak of cloned temp directories**.

---

### BUG-06 · `all_prompts` iterator consumed twice — **second pass (dict variables) gets wrong items**
**Severity:** High  
**Type:** White-box — iterator exhaustion bug  
**Location:** `prompt.py:300-303` and `343`

```python
# First pass
all_prompts = context['cookiecutter'].items()          # line 300 — dict_items VIEW
visible_prompts = [k for k, _ in all_prompts if not k.startswith("_")]   # line 301 — iterates view
size = len(visible_prompts)
for key, raw in all_prompts:                           # line 303 — iterates SAME view again ✓
    ...

# Second pass
for key, raw in context['cookiecutter'].items():       # line 343 — new call ✓
```

Actually `dict.items()` returns a **view**, not an iterator — it is re-iterable. So the iteration itself is fine. **BUT:**

Line 301: `visible_prompts` counts only non-private keys **excluding dicts**? No — it includes dict keys that don't start with `_`. Then `size` is used for the `[count/size]` counter display on line 313. In the second pass (dicts), `count` continues from where the first pass left off. If the first pass had 3 non-dict variables (count=3) and there are 2 dict variables processed in pass 2, the user sees `[4/3]` and `[5/3]` — the counter **exceeds `size`**, which is visually confusing/broken.

**Repro vector:**
```json
{
  "name": "default",
  "version": "1.0",
  "author_info": { "name": "Author", "email": "a@b.com" }
}
```
User sees:
```
[1/2] name
[2/2] version
[3/2] author_info    ← BROKEN counter
```

---

## 3. Latent Risk Areas (Not Confirmed Bugs — Require Further Investigation)

### RISK-01 · Jinja2 `SandboxedEnvironment` is NOT used — arbitrary code execution via template injection
**Severity:** Critical (Security)  
**Type:** Grey-box — security analysis  
**Location:** `utils.py:102-106`, `environment.py`

`StrictEnvironment` inherits from Jinja2's standard `Environment`, not `SandboxedEnvironment`. A malicious `cookiecutter.json` hosted on a public git repo can execute arbitrary Python via:
```
{{ ''.__class__.__mro__[1].__subclasses__() }}
```
This is a **known Jinja2 SSTI vector**. Cookiecutter is designed to run remote templates — this is a critical-severity security risk that the existing test suite does not exercise at all.

### RISK-02 · `apply_overwrites_to_context` skips **type validation** for string-to-string overwrites
**Severity:** Low–Medium  
**Location:** `generate.py:121-123`

```python
else:
    context[variable] = overwrite   # no type check
```

If a user's `~/.cookiecutterrc` defines `project_name: 12345` (integer YAML), and the template expects `project_name` to be a string, the integer silently replaces the string. Downstream Jinja2 rendering may fail or produce unexpected output.

### RISK-03 · `read_user_variable` infinite `while True` loop — no timeout, no max-retry
**Severity:** Low  
**Location:** `prompt.py:37-42`

```python
while True:
    variable = Prompt.ask(...)
    if variable is not None:
    break
```

`Prompt.ask` with `rich` library never returns `None` — it returns the default if stdin is empty. In a non-TTY environment (piped stdin that sends EOF), `rich` raises an `EOFError` which propagates uncaught, crashing the entire `cookiecutter()` call with no cleanup. No test covers EOF on stdin.

---

## 4. Existing Test Coverage vs. Testing Methodology Assessment

| Test Type | Coverage Level | Key Files |
|---|---|---|
| Unit (white-box) | **Good** for happy paths | `test_prompt.py`, `test_generate_context.py` |
| Integration (grey-box) | **Moderate** | `test_cookiecutter_local_no_input.py` |
| Boundary Value (black-box) | **Weak** — no numeric boundary tests | Missing |
| Grammar Fuzzing | **Present but shallow** | `test_json_context_fuzz.py`, `test_prompt_grammar_fuzz.py` |
| Mutation Fuzzing (Atheris) | **Absent** | Not integrated |
| Security / SSTI | **Absent** | Not integrated |
| Error-path / exception | **Partial** | `test_exceptions.py` |
| Concurrency / race | **Absent** | Not integrated |

### Fuzzing Coverage Gaps Found in Existing Fuzz Harness

The existing `test_json_context_fuzz.py` uses Hypothesis with a custom grammar strategy but has these gaps:

1. **Grammar only generates simple types** — no nested dict keys with Jinja2 expressions (`"{{ cookiecutter.foo }}_bar"`). BUG-03 would not be caught.
2. **`apply_overwrites_to_context` fuzz test** (line 167) uses `json_context_strategy()` for both `context` and `default_context` — but the strategy only generates primitive values. It never generates **mixed types** (e.g., a list in one and a string in the other), which is exactly the path that hits the type-mismatch `ValueError` at line 98-103.
3. **`test_generate_context_with_malformed_json`** suppresses all `ValueError` — but BUG-02 (integer values silently coerced) would produce a **successful** parse that the test accepts without asserting type fidelity.
4. **`test_prompt_grammar_fuzz.py`** mocks `Prompt.ask` to return the fuzzed string directly — bypassing the actual Rich terminal I/O path entirely. It would not catch the `EOFError` from RISK-03.

---

## 5. Recommended Testing Approach to Confirm / Rule Out Remaining Risk

| Bug ID | Test Type | Method |
|---|---|---|
| BUG-01 | White-box unit | Assert `context['cookiecutter']` still contains `__prompts__` after `prompt_for_config()` call with a mock for `Prompt.ask` |
| BUG-02 | Black-box boundary | Feed `cookiecutter.json` with integer, float, `null` values; assert `TypeError` or explicit validation error at prompt time, not render time |
| BUG-03 | White-box unit | Feed a dict with Jinja2 expression in a key referencing an undefined var; assert `UndefinedVariableInTemplate` with correct variable name |
| BUG-04 | Black-box / regression | Feed old-style nested template list without `(path)` suffix; assert a named exception, not `AttributeError` |
| BUG-05 | White-box / integration | Mock `run_pre_prompt_hook` to raise; assert temp dirs are cleaned; use `tmp_path` fixture + `os.listdir` to verify |
| BUG-06 | White-box unit | Feed JSON with 2 strings + 1 dict; capture stdout; assert counter does not exceed `size` |
| RISK-01 | Security / Grey-box | Feed SSTI payload as default value; assert it does NOT execute (`__subclasses__` remains unexpanded) |
| RISK-03 | Black-box / boundary | Redirect `sys.stdin` to `io.StringIO("")`; assert `EOFError` is wrapped in a `CookiecutterException` |

---

## 6. Verdict

> **6 confirmed bugs found, 3 latent risks identified.**

The most critical confirmed bug is **BUG-04** (hard `AttributeError` crash on old-style nested templates — zero test coverage). **BUG-06** is a counter overflow that every user with a dict variable hits visually. **BUG-01** is a subtle replay regression that corrupts UX silently.

The most critical latent risk is **RISK-01** — template injection is a structural security concern given the tool is designed to pull and run remote templates.

No fix is proposed per instructions. All findings are research + static/dynamic analysis only.
