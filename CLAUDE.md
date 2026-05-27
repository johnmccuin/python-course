# CLAUDE.md — Repo Conventions

This file is read by Claude at the start of every session.
Follow these conventions for all work in this repository.

---

## What this repo is

A 9-week introductory Python course delivered via Google Colab.
Students open `.ipynb` links from Blackboard; each link points at a file
inside the `dist/` folder of this GitHub repo.

This is **not** a typical software project. There are no servers, no
deployments, no test runners to invoke in CI (yet). The primary
deliverable is a set of well-structured Jupyter notebooks.

---

## Course structure (planned)

This schedule is the source of truth for what each week covers. Do not infer topic order from filenames or generic intro-Python conventions.

| Week | Topic | AI Use |
|------|-------|--------|
| 01 | First Steps: Python setup (Colab), variables, numbers, strings, booleans, expressions, print/input, if/else | No AI |
| 02 | Making Decisions and Repeating: if/else, while loops, for loops, lists (motivating loops) | No AI |
| 03 | Functions and More Data: functions (parameters, return values), dicts, strings in depth, basic file I/O; foreshadow classes via stdlib objects | No AI |
| 04 | Organizing Code and Handling Problems: modules and imports, error handling, tracebacks, debugging strategies, assertions for verification | No AI |
| 05 | Working With AI as a Coding Partner: prompting, reading AI output critically, verification loop, AI failure modes, brief pytest intro | AI pivot (AI introduced) |
| 06 | Specs, Decomposition, Architecture, and Classes: writing specs, decomposition, architecture principles, cost of abstraction, intro to classes (`__init__`, methods, instances) | AI allowed |
| 07 | Connecting to the World: APIs and LLMs: HTTP basics, `requests`, REST/JSON, Anthropic/OpenAI SDK, system prompts, structured output; capstone assigned | AI allowed |
| 08 | Capstone Build Week: brief opening on scoping and planning, spec due partway through, supervised work time | AI allowed |
| 09 | Capstone Presentations and Closing: presentations (spec, demo, architecture, reflection on AI), discussion of what to learn next | AI allowed |

---

## Folder layout

```
python-course/
  grader/
    grader.py               # Grader class (jupytext source) — fetched by notebooks at runtime
    test_grader.py          # End-to-end test notebook (jupytext source)
    gradebook.js            # Google Apps Script template (paste into Sheet's script editor)
    GRADEBOOK_SETUP.md      # Step-by-step instructions for deploying the gradebook
  week-XX/                  # One folder per week (week-01, week-02, …)
    lecture-XX.py           # Lecture notebook (jupytext source)
    homework-XX.py          # Homework notebook (jupytext source)
    homework_solution-XX.py # Instructor reference solution (jupytext source, NOT in dist/)
    checks-XX.py            # Autograder check functions (plain Python module, NOT in dist/)
  dist/                     # Generated .ipynb files — git-tracked (see below)
    grader/
      grader.ipynb
      test_grader.ipynb
    week-01/
      lecture-01.ipynb
      homework-01.ipynb
      # homework_solution-01.ipynb is intentionally absent — see below
    …
  build.sh                  # Converts .py sources → .ipynb in dist/
  requirements.txt          # Pinned Python deps (jupytext, etc.)
  README.md
  CLAUDE.md                 # ← you are here
```

**File naming convention:** every week-specific file ends with the zero-padded week
number: `homework-01.py`, `checks-02.py`, `lecture-03.py`, etc. This makes the week
immediately obvious from the filename alone, whether you're looking at the source
folder or the dist folder.

---

## Notebook authoring: jupytext percent-format

Every `.py` source file that becomes a student notebook is a
**jupytext percent-format** notebook.

- Code cells are delimited by `# %%`
- Markdown cells are delimited by `# %% [markdown]`
- The first cell should be a markdown cell with the notebook title
- Regular Python comments inside a cell are just `#` — only `# %%` at the
  start of a line opens a new cell

**Never hand-edit `.ipynb` files.** Always edit the `.py` source and
regenerate via `build.sh`.

---

## Building notebooks: build.sh

```bash
bash build.sh
```

`build.sh` converts `.py` sources to `.ipynb` files with these rules:

| File | Output location | Notes |
|------|----------------|-------|
| `grader/*.py` | `dist/grader/` | All `.py` files converted |
| `week-XX/lecture-XX.py` | `dist/week-XX/` | Converted to dist/ |
| `week-XX/homework-XX.py` | `dist/week-XX/` | Converted to dist/ |
| `week-XX/homework_solution-XX.py` | `week-XX/` (in-place) | **Not** in dist/ — instructor only |
| `week-XX/checks-XX.py` | — | **Skipped** — plain Python module, not a notebook |

**`homework_solution-XX.ipynb` is git-ignored.** It is built locally by
`build.sh` for instructor use but never committed to the public repo so
students cannot find it by browsing GitHub.

Run `build.sh` after any edit to a `.py` source before committing.

**Branch-aware URL patching:** `build.sh` detects the current git branch.
On a feature branch it rewrites every `python-course/main` URL in the
generated `.ipynb` files to `python-course/<branch-name>`, so the setup
cell's `urllib` downloads resolve correctly when testing in Colab before
a merge. On `main` the patch is a no-op. Source `.py` files always
contain `main` — never change them to a branch name manually.

---

## The `.ipynb`-files-are-checked-in convention

The `dist/` folder is **fully git-tracked**.
Rationale: Colab opens notebooks by fetching a raw GitHub URL. That URL
must resolve to a real file on the default branch.

**Workflow every time you touch a source file:**

1. Edit the `.py` source.
2. Run `bash build.sh`.
3. `git add` the `.py` source and all modified files under `dist/`.
4. Commit with a clear message.
5. Push.

**Note on jupytext cell IDs:** jupytext assigns new random cell UUIDs on
every conversion run, so `dist/` files will always appear modified after a
rebuild even if content is unchanged. This is normal — commit them
alongside the source changes.

---

## Branch and repo conventions

- **Intended workflow: merge to `main` before students use the content.**
  Colab and Blackboard links always point at `main`, so notebooks must
  be on `main` to be accessible to students.
- **Claude Code on the web always creates a `claude/...` feature branch.**
  This is fine — use it for development, test in Colab (the branch URL
  patching in `build.sh` makes this work), then merge to `main` via a PR
  before sharing links with students.
- **Never use branch names containing `/`** for anything student-facing.
  Colab parses the GitHub URL by splitting on `/`, so a branch like
  `feature/foo` is misread as branch=`feature`, path=`foo/…` — 404.
  (The `claude/...` branches are never in student-facing URLs, so the
  slash in those names is harmless.)
- The repo **must be public** on GitHub. Colab and every Blackboard link
  fetch raw files without authentication.

---

## Colab URL pattern

The canonical URL for any student notebook is:

```
https://colab.research.google.com/github/johnmccuin/python-course/blob/main/dist/<folder>/<notebook>.ipynb
```

Examples:
- Week 1 homework: `.../dist/week-01/homework-01.ipynb`
- Week 1 lecture: `.../dist/week-01/lecture-01.ipynb`

Use these URLs in Blackboard. They always resolve to the latest commit
on `main` — no URL update needed after pushing new content.

---

## Homework notebook structure

Every homework notebook follows this exact structure, in order:

### 1. Title cell
```python
# %% [markdown]
# # Week N — Homework
#
# Work through each exercise in order.
# After finishing an exercise, run its **check cell** to see if your answer is correct.
# When you're done, run the **Final Score** cell, then the **Submit** cell.
```

### 2. Student name cell (comes BEFORE setup — very first interactive cell)
```python
# %% [markdown]
# **Enter your name below exactly as it appears on the course roster —
# spelling and capitalization matter. This is used to record your score.**

# %%
student_name = "Your Name Here"
```

### 3. Setup section (update the two week numbers — SUBMIT_URL is already set)
```python
# %% [markdown]
# ---
# ## Setup — RUN AT BEGINNING, DO NOT MODIFY

# %%
import urllib.request, pathlib, sys

_BASE = "https://raw.githubusercontent.com/johnmccuin/python-course/main"
_FILES = {
    "grader.py": f"{_BASE}/grader/grader.py",
    "checks.py": f"{_BASE}/week-0N/checks-0N.py",   # ← update N (both places)
}
for _name, _url in _FILES.items():
    _dest = pathlib.Path(_name)
    if not _dest.exists():
        urllib.request.urlretrieve(_url, _dest)
        print(f"Downloaded {_name} ({_dest.stat().st_size} bytes)")
    else:
        print(f"{_name} already present — skipping download.")

if str(pathlib.Path(".").resolve()) not in sys.path:
    sys.path.insert(0, str(pathlib.Path(".").resolve()))

from grader import Grader
import checks
grader = Grader("Week N Homework")   # ← update N

SUBMIT_URL = "https://script.google.com/macros/s/AKfycbxmZUvgnvH3-rWYfr3ZV9vMcK8mpKvoStmjsoF0iRNLPCb_wuPNzj-MENyzRs44CwdXkQ/exec"

print("Ready!")
```

> **Note:** `checks-0N.py` is fetched from GitHub under its week-numbered name
> but saved locally as `checks.py` so that `import checks` works without issue.
> Never change the dict key (`"checks.py"`) — only update the URL value.

### 4. Exercises section header
```python
# %% [markdown]
# ---
# ## Exercises
```

### 5. Exercises (repeat for each)

Each exercise is exactly three cells:

```python
# %% [markdown]
# ---
# ### Exercise N: <title>
#
# <prompt text>
#
# $$<formula in LaTeX if needed>$$

# %%
prefilled_var = <value>     # any prefilled variables come FIRST
# Your code here
answer_var = ...            # student fills this in

# %%
grader.check("exN_<short_name>", lambda: checks.check_exN(answer_var))
```

- The check cell is always a **single line** — a lambda that passes the
  student's variable into the corresponding function in `checks.py`.
- Never put check logic in the notebook itself. Students can read it.
- Prefilled variables (e.g. `n = 14`, `name = "Sam"`) go **above**
  `# Your code here`. The student's answer variable goes below it with
  `= ...` as the placeholder.
- Use LaTeX `$$...$$` for any mathematical formulas in the prompt.
  Example: `# $$F = C \times \frac{9}{5} + 32$$`

**Two exercise patterns depending on the task:**

*Pattern A — expression answer* (Week 1 style): the student replaces `...`
with a value or expression. Use when the answer is a single assignment.
```python
# %%
n = 14
# Your code here
is_even = ...
```

*Pattern B — loop/block answer*: pre-initialize the result variable to its
correct starting value and let the student add the loop or if-block below.
Use when the student must write several lines (while loop, for loop, etc.).
The check detects "did nothing" by testing whether the variable still holds
its initial value.
```python
# %%
limit = 15
total = 0
# Your code here — use a while loop
```

**Multi-concept weeks:** when a homework spans more than one concept
(e.g., if/elif AND while loops AND for loops), group exercises under
`## Part N — <Concept>` section headers instead of a single `## Exercises`
header. Open each Part with a brief generic reminder code block — generic
enough that it does not give away the solution.  Example:
```python
# %% [markdown]
# ---
# ## Part 2 — While Loops
#
# Quick reminder: ...
#
# ```python
# n = 10          # starting value
# while n > 0:    # condition
#     print(n)    # do some work
#     n -= 1      # change
# ```
```

### 6. Final Score cell
```python
# %% [markdown]
# ---
# ## Final Score

# %%
grader.report()
```

### 7. Submit cell
```python
# %% [markdown]
# ---
# ## Submit
#
# Run the cell below to send your score to the gradebook.
# You can re-submit as many times as you like — only your highest score
# is kept.

# %%
grader.submit(student_name, SUBMIT_URL)
```

---

## checks-XX.py — autograder check functions

Each `week-XX/checks-XX.py` is a **plain Python module** (no jupytext cell
markers). It contains one function per exercise. Each function:

- Is named `check_exN` (e.g. `check_ex1`, `check_ex2`, …)
- Accepts the student's answer variable(s) as argument(s)
- Returns `True` if correct, or a hint string if wrong

```python
# week-XX/checks-XX.py

def check_ex1(variable_name):
    if <wrong>:
        return "Hint message shown to student."
    return True

def check_ex2(var1, var2):
    ...
```

**Hint writing rules:**
- Name the **symptom**, never the fix. ✓ "Got 0 — check that you're updating `total` inside the loop." ✗ "Add `total += i` inside the loop."
- For wrong numeric answers, call out the specific value and what it suggests: "Got 105 — that's 1+2+…+14, so your loop stopped one step early."
- For the `= ...` (Ellipsis) pattern, add `if answer is ...: return "You haven't filled this in yet."` as the first check.
- For pre-initialized variables (Pattern B), check whether the variable still holds its starting value: `if total == 0: return "total is still 0 — ..."`.
- Always verify the checks file before committing: run `python3` and call each `check_exN` with the correct answer (expect `True`) and several common wrong answers (expect a hint string).

`checks-XX.py` is:
- Fetched by the homework notebook at runtime and saved locally as `checks.py`
  (so `import checks` works — dashes are not valid in Python module names)
- **Excluded from `build.sh`** — not converted to a notebook
- **Committed to the repo** (it's intentionally opaque — students see only
  one-liner lambda calls, not the logic inside)

---

## homework_solution-XX.py — instructor reference

- Contains correct answers filled in (no `...` placeholders)
- Uses `student_name = "Instructor"`
- Same `SUBMIT_URL` as the student notebook
- **Excluded from `build.sh`'s dist/ output** — built in-place to
  `week-XX/homework_solution-XX.ipynb` instead
- `week-XX/homework_solution-XX.ipynb` is **git-ignored** — never committed
- Run `bash build.sh` locally to regenerate it whenever you need to verify

---

## Score submission: how it works

`grader.submit(student_name, SUBMIT_URL)` sends the score to a Google
Sheet via a Google Apps Script web app:

- Uses a **GET request with URL query parameters** (not POST — Google's
  Apps Script infrastructure rejects POST from non-browser clients with 405)
- Parameters: `student_name`, `assignment`, `score`, `total`, `pct`, `timestamp`
- The same `SUBMIT_URL` is used for **every week** — the `assignment` field
  (`"Week 1 Homework"`, `"Week 2 Homework"`, etc.) separates them in the Sheet
- Students may submit multiple times; the Sheet stores all submissions and
  a MAXIFS formula picks the highest score per student per assignment

The Apps Script source is in `grader/gradebook.js`.
Setup instructions are in `grader/GRADEBOOK_SETUP.md`.

**Important operational notes:**
- If `gradebook.js` is ever changed, the Apps Script deployment must be
  updated: Deploy → Manage deployments → Edit → New version → Deploy.
  The URL stays the same after redeployment.
- Colab caches `grader.py` and `checks.py` for the lifetime of a session.
  If either file is updated on GitHub, students (and you) must do
  **Runtime → Restart session** in Colab before the new version takes effect.

**SUBMIT_URL** (same for all weeks):
```
https://script.google.com/macros/s/AKfycbxmZUvgnvH3-rWYfr3ZV9vMcK8mpKvoStmjsoF0iRNLPCb_wuPNzj-MENyzRs44CwdXkQ/exec
```

---

## Checklist for building a new week's homework

- [ ] Read `week-0N/lecture-0N.py` first — only test concepts actually demonstrated there
- [ ] Create `week-0N/checks-0N.py` — one `check_exK` function per exercise
- [ ] Create `week-0N/homework-0N.py` — follow the structure above exactly;
      update the `checks-0N.py` URL (both the folder and filename) and
      `grader = Grader("Week N Homework")`
- [ ] Create `week-0N/homework_solution-0N.py` — correct answers filled in,
      `student_name = "Instructor"`
- [ ] Verify checks: run each `check_exN` with the correct answer (must return `True`)
      and several wrong answers (must return hint strings, not crash)
- [ ] Run `bash build.sh`
- [ ] Verify `dist/week-0N/homework-0N.ipynb` was created
- [ ] Verify `week-0N/homework_solution-0N.ipynb` was created (in-place, not dist/)
- [ ] Verify `week-0N/homework_solution-0N.ipynb` does **not** appear in `git status`
- [ ] `git add` sources + dist/ files; commit and push to the feature branch
- [ ] Test the student notebook in Colab — the branch URL patching means it
      works before merging to `main`; the setup cell downloads from the branch
- [ ] Merge to `main` via PR when satisfied
- [ ] Confirm final notebooks on `main` use `main` URLs (run `build.sh` on main
      after merge and push, or verify the PR merge triggered a clean rebuild)

---

## Requirements

- `jupytext` (pinned in `requirements.txt`) — the only hard dependency for
  the build step. Install with `pip install -r requirements.txt`.
- Students need no local setup; they use Google Colab.

---

## Lecture notebook conventions

These rules apply to every `lecture-XX.py` file.

### File naming
Lecture sources are named `lecture-XX.py` where `XX` matches the week number
(e.g. `week-01/lecture-01.py` → `dist/week-01/lecture-01.ipynb`).

### Purpose
Lecture notebooks are the script for a live class session. Students copy them
to their Drive and follow along. They are **not** autograded.

- **No `grader.py` import.** The notebook stands alone.
- **No solution cells.** Leave exercise code cells empty; the instructor
  produces solutions live on the projected screen.

### Block structure
Each lecture has four topic blocks. Each block follows this rhythm:

1. A markdown heading + concept explanation.
2. Short prebuilt demo code cells (1–3 lines each) the instructor runs live,
   each preceded by a brief markdown note about what to notice.
3. A `### Now you try` markdown divider, followed by exercises.

The notebook ends after the last exercise's empty code cell. Do **not**
add a break marker, a "15-minute break" cell, a closing "That's it for
tonight!" cell, or any other housekeeping text — the instructor manages
pacing and wrap-up live.

### Exercise pairing rule (critical)
Every individual exercise gets **its own instruction markdown cell immediately
followed by its own empty code cell**. Never group multiple exercises under
one instruction cell.

```
# %% [markdown]
# **Exercise 1.** Description of exercise 1.

# %%
# Your code here

# %% [markdown]
# **Exercise 2.** Description of exercise 2.

# %%
# Your code here
```

### Bug-demo cells
When showing intentionally broken code, each bug gets its own markdown
prompt cell + code cell pair. Include a mix of:
- **Syntax errors** (missing colon, `=` vs `==`) — these crash with an
  error message students can read.
- **Logic errors** (PEMDAS mistakes, wrong `if/elif` order, type confusion)
  — these run without crashing but produce wrong answers, which is often
  harder to spot and more important to teach.


