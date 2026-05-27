# Intro to Python — 9-Week Course

Google Colab notebooks for a 9-week introductory Python course.

## For students

Open the Colab link posted on Blackboard for each week's lecture and
homework. No local installation required.

## For instructors / contributors

### Setup

```bash
pip install -r requirements.txt
```

### Editing notebooks

Notebooks are authored as plain Python files using
[jupytext](https://jupytext.readthedocs.io/) percent-format (see `CLAUDE.md`
for conventions). After editing any `.py` source file, regenerate the
corresponding `.ipynb`:

```bash
bash build.sh
```

Then commit **both** the `.py` source and the updated `.ipynb` in `dist/`.

### Repo layout

```
grader/          # Reusable Grader class + tests
week-01/         # Week 1 source notebooks
…
dist/            # Generated .ipynb files (Colab-ready; git-tracked)
build.sh         # Build script
requirements.txt
```

See `CLAUDE.md` for full conventions.
