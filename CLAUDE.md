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
    grader.py           # Grader class (jupytext source)
    test_grader.py      # End-to-end test notebook (jupytext source)
  week-XX/              # One folder per week (week-01, week-02, …)
    lecture.py          # Lecture notebook (jupytext source)
    homework.py         # Homework notebook (jupytext source)
  dist/                 # Generated .ipynb files — git-tracked (see below)
    grader/
      grader.ipynb
      test_grader.ipynb
    week-01/
      lecture.ipynb
      homework.ipynb
    …
  build.sh              # Converts .py sources → .ipynb in dist/
  requirements.txt      # Pinned Python deps (jupytext, etc.)
  README.md
  CLAUDE.md             # ← you are here
```

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

**Note on jupytext cell IDs:** jupytext assigns new random cell UUIDs on
every conversion run, so `dist/` files will always appear modified after a
rebuild even if content is unchanged. This is normal — just commit them
alongside the source changes. (Using `jupytext --update` instead of
`--to notebook` would preserve IDs; left as a future improvement.)

---

## Branch and repo conventions

- **Work directly on `main`** for all course content. There is no need for
  feature branches in a course repo — the deliverable is notebooks, not
  production code, and students + Colab links always point at `main`.
- **Never use branch names containing `/`** for anything student-facing.
  Colab parses the GitHub URL by splitting on `/`, so a branch like
  `feature/foo` is misread as branch=`feature`, path=`foo/…` — resulting
  in a 404.
- The repo **must be public** on GitHub. Colab and every Blackboard link
  students open fetch raw files without authentication; GitHub returns 404
  for unauthenticated requests to private repos.

---

## Colab URL pattern

The canonical URL for any notebook in this repo is:

```
https://colab.research.google.com/github/johnmccuin/python-course/blob/main/dist/<folder>/<notebook>.ipynb
```

Examples:
- Test grader: `.../dist/grader/test_grader.ipynb`
- Week 1 homework: `.../dist/week-01/homework.ipynb`

Use these URLs in Blackboard. They resolve to the latest commit on `main`
automatically — no URL update needed after pushing new content.

---

## How homework notebooks load the Grader

Each homework notebook downloads `grader.py` from the raw GitHub URL at
the top of the notebook — no cloning, no pip install:

```python
import urllib.request, pathlib, sys

urllib.request.urlretrieve(
    "https://raw.githubusercontent.com/johnmccuin/python-course/main/grader/grader.py",
    "grader.py"
)
sys.path.insert(0, str(pathlib.Path(".").resolve()))
from grader import Grader
```

This is the standard pattern to copy into every homework `.py` source.

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
