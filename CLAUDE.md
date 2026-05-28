# CLAUDE.md — Repo Conventions

This file is read by Claude at the start of every session. Follow these conventions for all work in this repository.

---

## What This Repo Is

A 9-week introductory Python course delivered via Google Colab. Students open `.ipynb` links from Blackboard; each link points to a file inside the `dist/` folder of this GitHub repo.

This is **not** a typical software project — no servers, no deployments. The primary deliverable is a set of well-structured Jupyter notebooks.

---

## Course Structure

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

**Note:** Week 3 is intentionally wide — the lecture covers functions, dicts, strings in depth, and basic file I/O at survey depth. Later weeks revisit each topic in depth. The class-foreshadowing moment (using `Path`, file objects, or `datetime` as examples of "instances of a class") belongs in Week 3 with a note pointing to Week 7.

---

## Git Workflow — Main Only

**Always work directly on `main`. No feature branches.**

Every session:
1. `git pull origin main` — get the latest before touching anything
2. Make changes to `.py` source files
3. `bash build.sh` — regenerate the `.ipynb` files in `dist/`
4. `git add` the changed `.py` and `dist/` files
5. `git commit -m "clear message"`
6. `git push origin main`

**Why main-only?** Feature branches caused merge conflicts because the session container's local clone was sometimes stale. Since there is one instructor, no automated tests, and git history on main is a complete safety net, branches add friction without benefit.

**Rolling back a single file** is safe and does not affect anything else:
```bash
git log --oneline -- week-03/lecture-03.py   # find the version you want
git show <hash>:week-03/lecture-03.py        # preview it
git checkout <hash> -- week-03/lecture-03.py # restore just that file
bash build.sh
git add week-03/lecture-03.py dist/week-03/lecture-03.ipynb
git commit -m "Restore lecture-03 to <date> version"
git push origin main
```

**Repo must be public.** Colab and every Blackboard link fetch raw files without authentication. Never use branch names containing `/` for anything student-facing — Colab parses the GitHub URL by splitting on `/` and will 404.

---

## Folder Layout

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
  dist/                     # Generated .ipynb files — git-tracked
    grader/
      grader.ipynb
      test_grader.ipynb
    week-01/
      lecture-01.ipynb
      homework-01.ipynb
      # homework_solution-01.ipynb is intentionally absent
    …
  build.sh                  # Converts .py sources → .ipynb in dist/
  requirements.txt          # Pinned Python deps (jupytext, etc.)
  README.md
  CLAUDE.md                 # ← you are here
```

**File naming:** every week-specific file ends with the zero-padded week number: `homework-01.py`, `checks-02.py`, `lecture-03.py`, etc.

**Three files per homework week** in `week-XX/`:

| File | Purpose | In `dist/`? |
|------|---------|-------------|
| `homework-XX.py` | Student-facing notebook | Yes |
| `checks-XX.py` | Check functions — downloaded at runtime; students never see the source | Yes |
| `homework_solution-XX.py` | Reference solution (instructor only) | Yes (but URL not shared) |

---

## Notebook Authoring: jupytext Percent-Format

Every `.py` source file is a **jupytext percent-format** notebook:

- `# %%` — opens a code cell
- `# %% [markdown]` — opens a markdown cell
- Regular `#` comments inside a cell are just Python comments, not cell delimiters
- The first cell should be a markdown cell with the notebook title

**Never hand-edit `.ipynb` files.** Always edit the `.py` source and regenerate via `build.sh`.

---

## Building and Committing: build.sh

```bash
bash build.sh
```

`build.sh` converts `.py` sources to `.ipynb` with these rules:

| File | Output location | Notes |
|------|----------------|-------|
| `grader/*.py` | `dist/grader/` | All `.py` files converted |
| `week-XX/lecture-XX.py` | `dist/week-XX/` | Converted to dist/ |
| `week-XX/homework-XX.py` | `dist/week-XX/` | Converted to dist/ |
| `week-XX/homework_solution-XX.py` | `week-XX/` (in-place) | **Not** in dist/ — instructor only |
| `week-XX/checks-XX.py` | — | **Skipped** — plain Python module, not a notebook |

`homework_solution-XX.ipynb` is **git-ignored** — built locally for instructor use but never committed so students can't find it on GitHub.

**The `dist/` folder is fully git-tracked.** Colab fetches notebooks via raw GitHub URLs, so generated files must be committed. Run `build.sh` after every source edit, then commit both the `.py` and the generated `.ipynb` together.

**Note on jupytext cell IDs:** jupytext assigns new random cell UUIDs on every conversion run, so `dist/` files will always appear modified after a rebuild even if content is unchanged. This is normal — commit them alongside the source changes.

---

## Colab URL Pattern

```
https://colab.research.google.com/github/johnmccuin/python-course/blob/main/dist/<folder>/<notebook>.ipynb
```

Examples:
- Week 1 lecture: `.../dist/week-01/lecture-01.ipynb`
- Week 1 homework: `.../dist/week-01/homework-01.ipynb`

Use these URLs in Blackboard. They always resolve to the latest commit on `main` — no URL update needed after pushing.

---

## Homework Notebook Structure

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

### 2. Student name cell (BEFORE setup — very first interactive cell)
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

> **Note:** `checks-0N.py` is fetched from GitHub under its week-numbered name but saved locally as `checks.py` so that `import checks` works. Never change the dict key (`"checks.py"`) — only update the URL value.

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
prefilled_var = <value>     # prefilled variables come FIRST
# Your code here
answer_var = ...            # student fills this in

# %%
grader.check("exN_<short_name>", lambda: checks.check_exN(answer_var))
```

- The check cell is always a **single line** — a lambda passing the student's variable to `checks.py`.
- Never put check logic in the notebook itself. Students can read it.
- Prefilled variables go **above** `# Your code here`; the student's answer variable goes below with `= ...` as the placeholder.
- Use LaTeX `$$...$$` for mathematical formulas. Example: `# $$F = C \times \frac{9}{5} + 32$$`

**Two exercise patterns:**

*Pattern A — expression answer:* student replaces `...` with a value or expression. Use when the answer is a single assignment.
```python
# %%
n = 14
# Your code here
is_even = ...
```

*Pattern B — loop/block answer:* pre-initialize the result variable and let the student add the loop or block below. The check detects "did nothing" by testing whether the variable still holds its initial value.
```python
# %%
limit = 15
total = 0
# Your code here — use a while loop
```

**Multi-concept weeks:** group exercises under `## Part N — <Concept>` headers instead of a single `## Exercises` header. Open each part with a brief generic reminder code block — generic enough that it does not give away the solution:
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
# You can re-submit as many times as you like — only your highest score is kept.

# %%
grader.submit(student_name, SUBMIT_URL)
```

---

## checks-XX.py — Autograder Check Functions

Each `week-XX/checks-XX.py` is a **plain Python module** (no jupytext markers). One function per exercise:

- Named `check_exN` (e.g. `check_ex1`, `check_ex2`, …)
- Accepts the student's answer variable(s) as arguments
- Returns `True` if correct, or a hint string if wrong

```python
def check_ex1(answer):
    if <wrong>:
        return "Hint message shown to student."
    return True
```

**Hint writing rules:**
- Name the **symptom**, never the fix. ✓ "Got 0 — check that you're updating `total` inside the loop." ✗ "Add `total += i` inside the loop."
- For wrong numeric answers, call out the value and what it suggests: "Got 105 — that's 1+2+…+14, so your loop stopped one step early."
- For Pattern A (`= ...`), add `if answer is ...: return "You haven't filled this in yet."` as the first check.
- For Pattern B (pre-initialized), check whether the variable still holds its starting value: `if total == 0: return "total is still 0 — ..."`.
- Always verify before committing: call each `check_exN` with the correct answer (expect `True`) and several wrong answers (expect hint strings).

`checks-XX.py` is fetched at runtime and saved locally as `checks.py` (so `import checks` works — dashes aren't valid in module names). It is excluded from `build.sh` and committed to the repo as-is (students see only the one-liner lambda calls, not the logic inside).

---

## homework_solution-XX.py — Instructor Reference

- Contains correct answers filled in (no `...` placeholders)
- Uses `student_name = "Instructor"`
- Same `SUBMIT_URL` as the student notebook
- Built in-place to `week-XX/homework_solution-XX.ipynb` — **not** in `dist/`
- `week-XX/homework_solution-XX.ipynb` is **git-ignored** — never committed

**Testing locally:** because notebooks download `grader.py` and `checks.py` from GitHub at runtime, copy them first:

```bash
mkdir -p /tmp/hw_test
cp grader/grader.py /tmp/hw_test/
cp week-0N/checks-0N.py /tmp/hw_test/checks.py   # ← update N
cd /tmp/hw_test && python /path/to/week-0N/homework_solution-0N.py
```

The download cells skip if files are already present, so local copies are used. The submit call will still post to the live gradebook under `"Instructor"` — this is expected and harmless.

---

## Score Submission

`grader.submit(student_name, SUBMIT_URL)` sends scores to a Google Sheet via Google Apps Script:

- Uses a **GET request** (not POST — Apps Script rejects POST from non-browser clients with 405)
- Parameters: `student_name`, `assignment`, `score`, `total`, `pct`, `timestamp`
- The same `SUBMIT_URL` is used every week — the `assignment` field (`"Week 1 Homework"`, etc.) separates them in the Sheet
- Students may submit multiple times; a MAXIFS formula keeps the highest score per student per assignment

Source: `grader/gradebook.js`. Setup: `grader/GRADEBOOK_SETUP.md`.

**If `gradebook.js` is changed**, redeploy: Deploy → Manage deployments → Edit → New version → Deploy. URL stays the same.

**If `grader.py` or `checks.py` is updated on GitHub**, students must do **Runtime → Restart session** in Colab before the new version takes effect.

**SUBMIT_URL** (same for all weeks):
```
https://script.google.com/macros/s/AKfycbxmZUvgnvH3-rWYfr3ZV9vMcK8mpKvoStmjsoF0iRNLPCb_wuPNzj-MENyzRs44CwdXkQ/exec
```

---

## Checklist: Building a New Week's Homework

- [ ] Read `week-0N/lecture-0N.py` first — only test concepts actually demonstrated there
- [ ] Create `week-0N/checks-0N.py` — one `check_exK` function per exercise
- [ ] Create `week-0N/homework-0N.py` — follow the structure above; update the `checks-0N.py` URL and `grader = Grader("Week N Homework")`
- [ ] Create `week-0N/homework_solution-0N.py` — correct answers filled in, `student_name = "Instructor"`
- [ ] Verify checks: each `check_exN` returns `True` for the correct answer and hint strings for wrong answers
- [ ] Run `bash build.sh`
- [ ] Verify `dist/week-0N/homework-0N.ipynb` was created
- [ ] Verify `week-0N/homework_solution-0N.ipynb` was created (in-place, not in dist/)
- [ ] Verify `week-0N/homework_solution-0N.ipynb` does **not** appear in `git status`
- [ ] Test the solution locally — confirm it scores N/N and posts to the gradebook
- [ ] `git add` sources + dist/ files; commit and push to `main`
- [ ] Test the student notebook in Colab (setup cell, exercises, submit)

---

## Lecture Notebook Conventions

### Purpose and rules
Lecture notebooks are the script for a live class session. Students copy them to their Drive and follow along. They are **not** autograded.

- No `grader.py` import — the notebook stands alone.
- No solution cells — leave exercise code cells empty; the instructor fills them in live.
- Named `lecture-XX.py` matching the week number (`week-01/lecture-01.py` → `dist/week-01/lecture-01.ipynb`).

### Block structure
Each lecture has four topic blocks. Each block follows this rhythm:

1. A markdown heading + concept explanation.
2. Short prebuilt demo code cells (1–3 lines each) the instructor runs live, each preceded by a brief markdown note about what to notice.
3. A `### Now you try` markdown divider, followed by exercises.

The notebook ends after the last exercise's empty code cell. Do **not** add a break marker, closing cell, or any housekeeping text — the instructor manages pacing live.

### Exercise pairing rule (critical)
Every exercise gets **its own instruction markdown cell immediately followed by its own empty code cell**. Never group multiple exercises under one instruction cell.

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
Each bug gets its own markdown prompt cell + code cell pair. Include a mix of:
- **Syntax errors** (missing colon, `=` vs `==`) — crash with a readable error message.
- **Logic errors** (PEMDAS mistakes, wrong `if/elif` order, type confusion) — run without crashing but produce wrong answers, which is harder to spot and more important to teach.

---

## Requirements

`jupytext` is the only hard dependency for the build step. Install with:

```bash
pip install -r requirements.txt
```

Students need no local setup — they use Google Colab.
