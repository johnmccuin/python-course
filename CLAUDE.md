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

## Folder layout

```
python-course/
  grader/
    grader.py             # Grader class (jupytext source) — fetched by notebooks at runtime
    test_grader.py        # End-to-end test notebook (jupytext source)
    gradebook.js          # Google Apps Script template (paste into Sheet's script editor)
    GRADEBOOK_SETUP.md    # Step-by-step instructions for deploying the gradebook
  week-XX/                # One folder per week (week-01, week-02, …)
    lecture.py            # Lecture notebook (jupytext source)
    homework.py           # Homework notebook (jupytext source)
    homework_solution.py  # Instructor reference solution (jupytext source, NOT in dist/)
    checks.py             # Autograder check functions (plain Python module, NOT in dist/)
  dist/                   # Generated .ipynb files — git-tracked (see below)
    grader/
      grader.ipynb
      test_grader.ipynb
    week-01/
      lecture.ipynb
      homework.ipynb
      # homework_solution.ipynb is intentionally absent — see below
    …
  build.sh                # Converts .py sources → .ipynb in dist/
  requirements.txt        # Pinned Python deps (jupytext, etc.)
  README.md
  CLAUDE.md               # ← you are here
```

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
| `week-XX/lecture.py` | `dist/week-XX/` | Converted to dist/ |
| `week-XX/homework.py` | `dist/week-XX/` | Converted to dist/ |
| `week-XX/homework_solution.py` | `week-XX/` (in-place) | **Not** in dist/ — instructor only |
| `week-XX/checks.py` | — | **Skipped** — plain Python module, not a notebook |

**`homework_solution.ipynb` is git-ignored.** It is built locally by
`build.sh` for instructor use but never committed to the public repo so
students cannot find it by browsing GitHub.

Run `build.sh` after any edit to a `.py` source before committing.

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

- **Work directly on `main`** for all course content. There is no need for
  feature branches — the deliverable is notebooks, and students + Colab
  links always point at `main`.
- **Never use branch names containing `/`** for anything student-facing.
  Colab parses the GitHub URL by splitting on `/`, so a branch like
  `feature/foo` is misread as branch=`feature`, path=`foo/…` — 404.
- The repo **must be public** on GitHub. Colab and every Blackboard link
  fetch raw files without authentication.

---

## Colab URL pattern

The canonical URL for any student notebook is:

```
https://colab.research.google.com/github/johnmccuin/python-course/blob/main/dist/<folder>/<notebook>.ipynb
```

Examples:
- Week 1 homework: `.../dist/week-01/homework.ipynb`
- Week 1 lecture: `.../dist/week-01/lecture.ipynb`

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

### 2. Setup cell (instructor fills in SUBMIT_URL before publishing)
```python
# %%
# Setup — DO NOT EDIT THIS CELL
import urllib.request, pathlib, sys

_BASE = "https://raw.githubusercontent.com/johnmccuin/python-course/main"
_FILES = {
    "grader.py": f"{_BASE}/grader/grader.py",
    "checks.py": f"{_BASE}/week-0N/checks.py",   # ← update N for each week
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
grader = Grader("Week N Homework")   # ← update N for each week

SUBMIT_URL = "https://script.google.com/macros/s/AKfycbxmZUvgnvH3-rWYfr3ZV9vMcK8mpKvoStmjsoF0iRNLPCb_wuPNzj-MENyzRs44CwdXkQ/exec"

print("Ready!")
```

### 3. Student name cell
```python
# %% [markdown]
# ## Before you begin
#
# Enter your name in the cell below **exactly as it appears on the course
# roster** — spelling and capitalization matter. This is used to record
# your score in the gradebook.

# %%
student_name = "Your Name Here"
```

### 4. Exercises (repeat for each)

Each exercise is exactly three cells:

```python
# %% [markdown]
# ---
# ### Exercise N: <title>
#
# <prompt text>

# %%
# Your code here (plus any prefilled variables above this comment)
variable_name = ...

# %%
grader.check("exN_<short_name>", lambda: checks.check_exN(variable_name))
```

- The check cell is always a **single line** — a lambda that passes the
  student's variable into the corresponding function in `checks.py`.
- Never put check logic in the notebook itself. Students can read it.

### 5. Final Score cell
```python
# %% [markdown]
# ---
# ## Final Score

# %%
grader.report()
```

### 6. Submit cell
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

## checks.py — autograder check functions

Each `week-XX/checks.py` is a **plain Python module** (no jupytext cell
markers). It contains one function per exercise. Each function:

- Is named `check_exN` (e.g. `check_ex1`, `check_ex2`, …)
- Accepts the student's answer variable(s) as argument(s)
- Returns `True` if correct, or a hint string if wrong

```python
# week-XX/checks.py

def check_ex1(variable_name):
    if <wrong>:
        return "Hint message shown to student."
    return True

def check_ex2(var1, var2):
    ...
```

`checks.py` is:
- Fetched by the homework notebook at runtime (from the raw GitHub URL)
- **Excluded from `build.sh`** — not converted to a notebook
- **Committed to the repo** (it's intentionally opaque — students see only
  one-liner lambda calls, not the logic inside)

---

## homework_solution.py — instructor reference

- Contains correct answers filled in (no `...` placeholders)
- Uses `student_name = "Instructor"`
- Same `SUBMIT_URL` as the student notebook
- **Excluded from `build.sh`'s dist/ output** — built in-place to
  `week-XX/homework_solution.ipynb` instead
- `week-XX/homework_solution.ipynb` is **git-ignored** — never committed
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

**SUBMIT_URL** (same for all weeks):
```
https://script.google.com/macros/s/AKfycbxmZUvgnvH3-rWYfr3ZV9vMcK8mpKvoStmjsoF0iRNLPCb_wuPNzj-MENyzRs44CwdXkQ/exec
```

---

## Checklist for building a new week's homework

- [ ] Create `week-0N/checks.py` — one `check_exK` function per exercise
- [ ] Create `week-0N/homework.py` — follow the structure above exactly;
      update the `checks.py` URL and `grader = Grader("Week N Homework")`
- [ ] Create `week-0N/homework_solution.py` — correct answers filled in,
      `student_name = "Instructor"`
- [ ] Run `bash build.sh`
- [ ] Verify `dist/week-0N/homework.ipynb` was created
- [ ] Verify `week-0N/homework_solution.ipynb` was created (in-place, not dist/)
- [ ] Verify `week-0N/homework_solution.ipynb` does **not** appear in `git status`
- [ ] `git add` sources + dist/ files; commit and push to `main`
- [ ] Test the student notebook in Colab (setup cell, exercises, submit)
- [ ] Test the solution notebook locally (should score N/N)

---

## Requirements

- `jupytext` (pinned in `requirements.txt`) — the only hard dependency for
  the build step. Install with `pip install -r requirements.txt`.
- Students need no local setup; they use Google Colab.

---

## Course structure (planned)

| Week | Topic |
|------|-------|
| 01   | Variables, types, basic I/O |
| 02   | Conditionals & loops |
| 03   | Functions |
| 04   | Lists & tuples |
| 05   | Dictionaries & sets |
| 06   | File I/O & exceptions |
| 07   | Classes & objects |
| 08   | Libraries (numpy, pandas intro) |
| 09   | Mini-project |
