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
