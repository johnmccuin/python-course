# CLAUDE.md — Repo Conventions

This file is read by Claude at the start of every session.
Follow these conventions for all work in this repository.

---

## What this repo is

A 9-week introductory Python course delivered via Google Colab.
Students open `.ipynb` links from Blackboard; each link points at a file
inside the `dist/` folder of this GitHub repo.

This is **not** a typical software project. There are no servers, no
deployments, and no automated test runners. The primary deliverable is a
set of well-structured Jupyter notebooks.

---

## Git workflow — main only

**Always work directly on `main`. No feature branches.**

Every session:
1. `git pull origin main` — get the latest before touching anything
2. Make changes to `.py` source files
3. `bash build.sh` — regenerate the `.ipynb` files in `dist/`
4. `git add` the changed `.py` and `dist/` files
5. `git commit -m "clear message"`
6. `git push origin main`

**Why main-only?** Feature branches caused merge conflicts because the
session container's local clone was sometimes stale. Since there is one
instructor, no automated tests, and git history on main is a complete
safety net, branches add friction without benefit.

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

---

## Folder layout

```
python-course/
  grader/
    grader.py               # Grader class (jupytext source)
    test_grader.py          # End-to-end test notebook (jupytext source)
  week-XX/                  # One folder per week (week-01, week-02, …)
    lecture-XX.py           # Lecture notebook (jupytext source)
    homework-XX.py          # Homework notebook (jupytext source)
    homework_solution-XX.py # Reference solution — instructor only, not in dist/
    checks-XX.py            # Autograder check functions — downloaded at runtime
  dist/                     # Generated .ipynb files — git-tracked (see below)
    grader/
      grader.ipynb
      test_grader.ipynb
    week-01/
      lecture-01.ipynb
      homework-01.ipynb
    …
  build.sh                  # Converts .py sources → .ipynb in dist/
  requirements.txt          # Pinned Python deps (jupytext, etc.)
  README.md
  CLAUDE.md                 # ← you are here
```

**File naming:** all week-level source files use the suffix `-NN` (e.g.
`homework-03.py`, `checks-03.py`).  The `XX` above is a two-digit
zero-padded week number.

### Three-file pattern per week

Every homework week has three source files in `week-XX/`:

| File | Purpose | In `dist/`? |
|---|---|---|
| `homework-XX.py` | Student-facing notebook | Yes |
| `checks-XX.py` | Check functions — downloaded at runtime by the notebook; students never see the source | Yes |
| `homework_solution-XX.py` | Reference solution (instructor only) | Yes (but URL not shared) |

The homework notebook downloads **both** `grader.py` and `checks.py` at
runtime so students can't read the check logic ahead of time:

```python
_FILES = {
    "grader.py": f"{_BASE}/grader/grader.py",
    "checks.py": f"{_BASE}/week-03/checks-03.py",
}
```

Each exercise in the homework calls:
```python
grader.check("ex1_function_name", lambda: checks.check_ex1(student_variable_or_fn))
```

And `checks-XX.py` defines `check_ex1(val)` → returns `True` on pass or
a hint string on failure.

---

## Notebook authoring: jupytext percent-format

Every `.py` source file is a **jupytext percent-format** notebook.

- Code cells are delimited by `# %%`
- Markdown cells are delimited by `# %% [markdown]`
- The first cell should be a markdown cell with the notebook title
- Regular Python comments inside a cell are just `#` — only `# %%` at the
  start of a line opens a new cell

Example:

```python
# %% [markdown]
# # Week 1 — Introduction to Python

# %%
# This is a code cell
print("Hello, world!")

# %% [markdown]
# ## Exercise 1
# Complete the function below.

# %%
def greet(name):
    # TODO: return a greeting string
    pass
```

**Never hand-edit `.ipynb` files.** Always edit the `.py` source and
regenerate via `build.sh`.

---

## Building notebooks: build.sh

```bash
bash build.sh
```

`build.sh` scans every `*.py` file in `grader/` and `week-XX/` folders,
converts each one to a `.ipynb` using `jupytext --to notebook`, and places
the result in the matching subdirectory under `dist/`.

It prints each file it converts so you can confirm the output.

Run `build.sh` after any edit to a `.py` source before committing.

---

## The `.ipynb`-files-are-checked-in convention

The `dist/` folder is **fully git-tracked**.  
Rationale: Colab opens notebooks by fetching a raw GitHub URL. That URL
must resolve to a real file on the default (or specified) branch — GitHub
Actions or a build step that only runs on push would work, but checking in
the generated files is simpler and keeps everything self-contained.

**Workflow every time you touch a source file:**

1. Edit the `.py` source.
2. Run `bash build.sh`.
3. `git add` both the `.py` and the generated `.ipynb` in `dist/`.
4. Commit with a clear message.
5. Push.

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
| 03   | Functions, strings in depth, dicts, file I/O (overview) |
| 04   | Lists & tuples |
| 05   | Dictionaries & sets (deep dive) |
| 06   | File I/O & exceptions (deep dive) |
| 07   | Classes & objects |
| 08   | Libraries (numpy, pandas intro) |
| 09   | Mini-project |

**Note:** Week 3 is intentionally wide — the lecture (`week-03/lecture-03.py`)
covers all four topics at survey depth. Weeks 4–6 revisit each in depth.
The class-foreshadowing moment (using `Path`, file objects, or `datetime` as
examples of "instances of a class") belongs in Week 3 with a note pointing
to Week 7.

### Testing homework solutions locally

Because the homework notebooks download `grader.py` and `checks.py` from
GitHub at runtime, testing them locally requires copying those files into
a scratch directory before running the solution as a plain Python script:

```bash
mkdir -p /tmp/hw_test
cp grader/grader.py /tmp/hw_test/
cp week-03/checks-03.py /tmp/hw_test/checks.py
cd /tmp/hw_test && python /path/to/homework_solution-03.py
```

The download cells skip if the files are already present, so the script
runs entirely offline against the local copies.
