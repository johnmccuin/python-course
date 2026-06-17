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
# ### Exercise 4: popular_pages

# %%
def popular_pages(views, min_views):
    result = {}
    for page, count in views.items():
        if count >= min_views:
            result[page] = count
    return result

# %%
grader.check("ex4_popular_pages", lambda: checks.check_ex4(popular_pages))

# %% [markdown]
# ---
# ### Exercise 5: top_page

# %%
def top_page(views):
    best_name = None
    best_val = -1
    for page, count in views.items():
        if count > best_val:
            best_val = count
            best_name = page
    return best_name

# %%
grader.check("ex5_top_page", lambda: checks.check_ex5(top_page))

# %% [markdown]
# ---
# ## Part 4 — Tuples

# %% [markdown]
# ---
# ### Exercise 6: count_and_total

# %%
def count_and_total(numbers):
    return len(numbers), sum(numbers)

# %%
grader.check("ex6_count_and_total", lambda: checks.check_ex6(count_and_total))

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
