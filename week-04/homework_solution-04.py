# %% [markdown]
# # Week 4 — Homework (Reference Solution)
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
    "checks.py": f"{_BASE}/week-04/checks-04.py",
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
grader = Grader("Week 4 Homework")

SUBMIT_URL = "https://script.google.com/macros/s/AKfycbxmZUvgnvH3-rWYfr3ZV9vMcK8mpKvoStmjsoF0iRNLPCb_wuPNzj-MENyzRs44CwdXkQ/exec"

print("Ready!")

# %% [markdown]
# ---
# ## Part 1 — Modules and Imports

# %% [markdown]
# ---
# ### Exercise 1: circle_area

# %%
import math

def circle_area(radius):
    return math.pi * radius ** 2

# %%
grader.check("ex1_circle_area", lambda: checks.check_ex1(circle_area))

# %% [markdown]
# ---
# ### Exercise 2: count_punctuation

# %%
import string

def count_punctuation(text):
    count = 0
    for ch in text:
        if ch in string.punctuation:
            count += 1
    return count

# %%
grader.check("ex2_count_punctuation", lambda: checks.check_ex2(count_punctuation))

# %% [markdown]
# ---
# ## Part 2 — Error Handling

# %% [markdown]
# ---
# ### Exercise 3: safe_divide

# %%
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero."

# %%
grader.check("ex3_safe_divide", lambda: checks.check_ex3(safe_divide))

# %% [markdown]
# ---
# ### Exercise 4: parse_scores

# %%
def parse_scores(items):
    result = []
    for item in items:
        try:
            result.append(int(item))
        except ValueError:
            continue
    return result

# %%
grader.check("ex4_parse_scores", lambda: checks.check_ex4(parse_scores))

# %% [markdown]
# ---
# ## Part 3 — Debugging and Tracebacks

# %% [markdown]
# ---
# ### Exercise 5: fix average

# %%
def average(numbers):
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)

# %%
grader.check("ex5_average", lambda: checks.check_ex5(average))

# %% [markdown]
# ---
# ## Part 4 — Assertions

# %% [markdown]
# ---
# ### Exercise 6: rectangle_area

# %%
def rectangle_area(width, height):
    assert width > 0, "width must be positive"
    assert height > 0, "height must be positive"
    return width * height

# %%
grader.check("ex6_rectangle_area", lambda: checks.check_ex6(rectangle_area))

# %% [markdown]
# ---
# ### Exercise 7: withdraw

# %%
def withdraw(balance, amount):
    assert amount > 0, "amount must be positive"
    assert amount <= balance, "amount exceeds balance"
    return balance - amount

# %%
grader.check("ex7_withdraw", lambda: checks.check_ex7(withdraw))

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
