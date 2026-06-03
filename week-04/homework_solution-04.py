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
# ## Part 1 — Files

# %% [markdown]
# ---
# ### Exercise 1: save_lines

# %%
def save_lines(filename, lines):
    with open(filename, "w") as f:
        for line in lines:
            f.write(line + "\n")

# %%
grader.check("ex1_save_lines", lambda: checks.check_ex1(save_lines))

# %% [markdown]
# ---
# ### Exercise 2: sum_numbers

# %%
def sum_numbers(filename):
    total = 0
    with open(filename) as f:
        for line in f:
            line = line.strip()
            if line:
                total += int(line)
    return total

# %%
grader.check("ex2_sum_numbers", lambda: checks.check_ex2(sum_numbers))

# %% [markdown]
# ---
# ## Part 2 — Modules and Imports

# %% [markdown]
# ---
# ### Exercise 3: circle_area

# %%
import math

def circle_area(radius):
    return math.pi * radius ** 2

# %%
grader.check("ex3_circle_area", lambda: checks.check_ex3(circle_area))

# %% [markdown]
# ---
# ## Part 3 — Error Handling

# %% [markdown]
# ---
# ### Exercise 4: safe_divide

# %%
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero."

# %%
grader.check("ex4_safe_divide", lambda: checks.check_ex4(safe_divide))

# %% [markdown]
# ---
# ### Exercise 5: parse_scores

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
grader.check("ex5_parse_scores", lambda: checks.check_ex5(parse_scores))

# %% [markdown]
# ---
# ## Part 4 — Debugging and Tracebacks

# %% [markdown]
# ---
# ### Exercise 6: fix average

# %%
def average(numbers):
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)

# %%
grader.check("ex6_average", lambda: checks.check_ex6(average))

# %% [markdown]
# ---
# ## Part 5 — Assertions

# %% [markdown]
# ---
# ### Exercise 7: withdraw

# %%
def withdraw(balance, amount):
    assert amount > 0, "amount must be positive"
    assert amount <= balance, "amount must not exceed the balance"
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
