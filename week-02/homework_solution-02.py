# %% [markdown]
# # Week 2 — Homework (Reference Solution)
#
# **Instructor reference — do not distribute to students.**
#
# This file is excluded from `build.sh` and the `dist/` folder so it is
# never published. Running all cells top-to-bottom should score **7 / 7**.

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
    "checks.py": f"{_BASE}/week-02/checks-02.py",
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
grader = Grader("Week 2 Homework")

SUBMIT_URL = "https://script.google.com/macros/s/AKfycbxmZUvgnvH3-rWYfr3ZV9vMcK8mpKvoStmjsoF0iRNLPCb_wuPNzj-MENyzRs44CwdXkQ/exec"

print("Ready!")

# %% [markdown]
# ---
# ## Exercises

# %% [markdown]
# ---
# ### Exercise 1: game_rank

# %%
points = 1200

if points >= 2000:
    rank = "Diamond"
elif points >= 1500:
    rank = "Platinum"
elif points >= 1000:
    rank = "Gold"
elif points >= 500:
    rank = "Silver"
else:
    rank = "Bronze"

# %%
grader.check("ex1_game_rank", lambda: checks.check_ex1(rank))

# %% [markdown]
# ---
# ### Exercise 2: shipping_cost

# %%
weight = 3.5

if weight <= 1:
    cost = 3.99
elif weight <= 5:
    cost = 7.99
else:
    cost = 14.99

# %%
grader.check("ex2_shipping_cost", lambda: checks.check_ex2(cost))

# %% [markdown]
# ---
# ### Exercise 3: even_total

# %%
limit = 20
total = 0
n = 2

while n <= limit:
    total += n
    n += 2

# %%
grader.check("ex3_even_total", lambda: checks.check_ex3(total))

# %% [markdown]
# ---
# ### Exercise 4: bounce_count

# %%
height = 64
bounces = 0

while height > 1:
    height //= 2
    bounces += 1

# %%
grader.check("ex4_bounce_count", lambda: checks.check_ex4(bounces))

# %% [markdown]
# ---
# ### Exercise 5: hot_days

# %%
temps = [55, 72, 68, 81, 90, 63, 77]
hot_days = 0

for t in temps:
    if t > 75:
        hot_days += 1

# %%
grader.check("ex5_hot_days", lambda: checks.check_ex5(hot_days))

# %% [markdown]
# ---
# ### Exercise 6: word_lengths

# %%
words = ["python", "is", "fun", "to", "learn"]
lengths = []

for word in words:
    lengths.append(len(word))

# %%
grader.check("ex6_word_lengths", lambda: checks.check_ex6(lengths))

# %% [markdown]
# ---
# ### Exercise 7: largest

# %%
numbers = [5, 12, 3, 19, 7, 4, 11]
largest = numbers[0]

for n in numbers:
    if n > largest:
        largest = n

# %%
grader.check("ex7_largest", lambda: checks.check_ex7(largest))

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
