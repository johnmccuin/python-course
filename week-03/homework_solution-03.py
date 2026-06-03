# %% [markdown]
# # Week 3 — Homework (Reference Solution)
#
# **Instructor reference — do not distribute to students.**
#
# Running all cells top-to-bottom should score **7 / 7**.

# %% [markdown]
# **Enter your name below exactly as it appears on the course roster —
# spelling and capitalization matter. This is used to record your score.**

# %%
student_name = "Instructor"

# %% [markdown]
# ---
# ## Setup — RUN THIS FIRST, DO NOT MODIFY

# %%
import urllib.request, pathlib, sys

_BASE = "https://raw.githubusercontent.com/johnmccuin/python-course/main"
_FILES = {
    "grader.py": f"{_BASE}/grader/grader.py",
    "checks.py": f"{_BASE}/week-03/checks-03.py",
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
grader = Grader("Week 3 Homework")

SUBMIT_URL = "https://script.google.com/macros/s/AKfycbxmZUvgnvH3-rWYfr3ZV9vMcK8mpKvoStmjsoF0iRNLPCb_wuPNzj-MENyzRs44CwdXkQ/exec"

print("Ready!")

# %% [markdown]
# ---
# ## Part 1 — Writing Functions

# %% [markdown]
# ---
# ### Exercise 1: shout

# %%
def shout(text):
    return text.upper() + "!"

# %%
grader.check("ex1_shout", lambda: checks.check_ex1(shout))

# %% [markdown]
# ---
# ### Exercise 2: normalize

# %%
def normalize(text):
    return " ".join(text.strip().lower().split())

# %%
grader.check("ex2_normalize", lambda: checks.check_ex2(normalize))

# %% [markdown]
# ---
# ## Part 2 — Strings in Depth

# %% [markdown]
# ---
# ### Exercise 3: count_word

# %%
def count_word(sentence, word):
    count = 0
    for w in sentence.lower().split():
        if w == word.lower():
            count += 1
    return count

# %%
grader.check("ex3_count_word", lambda: checks.check_ex3(count_word))

# %% [markdown]
# ---
# ## Part 3 — Dictionaries

# %% [markdown]
# ---
# ### Exercise 4: filter_scores

# %%
def filter_scores(scores, min_score):
    result = {}
    for name, score in scores.items():
        if score >= min_score:
            result[name] = score
    return result

# %%
grader.check("ex4_filter_scores", lambda: checks.check_ex4(filter_scores))

# %% [markdown]
# ---
# ### Exercise 5: best_score

# %%
def best_score(scores):
    best_name = None
    best_val = -1
    for name, score in scores.items():
        if score > best_val:
            best_val = score
            best_name = name
    return best_name

# %%
grader.check("ex5_best_score", lambda: checks.check_ex5(best_score))

# %% [markdown]
# ---
# ## Part 4 — Tuples

# %% [markdown]
# ---
# ### Exercise 6: min_max

# %%
def min_max(numbers):
    return min(numbers), max(numbers)

# %%
grader.check("ex6_min_max", lambda: checks.check_ex6(min_max))

# %% [markdown]
# ---
# ### Exercise 7: parse_point

# %%
def parse_point(text):
    parts = text.split(",")
    return int(parts[0]), int(parts[1])

# %%
grader.check("ex7_parse_point", lambda: checks.check_ex7(parse_point))

# %% [markdown]
# ---
# ## Final Score

# %%
grader.report()

# %% [markdown]
# ---
# ## Submit

# %%
grader.submit(student_name, SUBMIT_URL)
