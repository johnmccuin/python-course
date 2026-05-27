# %% [markdown]
# # Week 1 — Homework
#
# Work through each exercise in order.
# After finishing an exercise, run its **check cell** to see if your answer is correct.
# When you're done, run the **Final Score** cell, then the **Submit** cell.

# %%
# Setup — don't edit this cell
import urllib.request, pathlib, sys

_BASE = "https://raw.githubusercontent.com/johnmccuin/python-course/main"
_FILES = {
    "grader.py": f"{_BASE}/grader/grader.py",
    "checks.py": f"{_BASE}/week-01/checks.py",
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
grader = Grader("Week 1 Homework")

SUBMIT_URL = "https://script.google.com/macros/s/YOUR_SCRIPT_ID/exec"

print("Ready!")

# %% [markdown]
# ## Before you begin
#
# Enter your name in the cell below **exactly as it appears on the course
# roster** — spelling and capitalization matter. This is used to record
# your score in the gradebook.

# %%
student_name = "Your Name Here"

# %% [markdown]
# ---
# ### Exercise 1: minutes_in_year
#
# Assign a variable named `minutes_in_year` to the total number of minutes
# in a non-leap year (365 days). Your answer should be an integer.

# %%
# Your code here
minutes_in_year = ...

# %%
grader.check("ex1_minutes_in_year", lambda: checks.check_ex1(minutes_in_year))

# %% [markdown]
# ---
# ### Exercise 2: greeting
#
# The variables `name` and `age` are already defined for you below. Create
# a variable `greeting` containing an f-string that reads exactly:
#
#     Hello Sam, you are 30 years old.
#
# (Include the comma, the space after it, and the period at the end.)

# %%
name = "Sam"
age = 30
# Your code here
greeting = ...

# %%
grader.check("ex2_greeting", lambda: checks.check_ex2(greeting))

# %% [markdown]
# ---
# ### Exercise 3: is_even
#
# The variable `n` is defined below. Assign a variable `is_even` to `True`
# if `n` is an even number, `False` otherwise. Your code should work for
# any integer value of `n`, not just the one shown.

# %%
n = 14
# Your code here
is_even = ...

# %%
grader.check("ex3_is_even", lambda: checks.check_ex3(is_even))

# %% [markdown]
# ---
# ### Exercise 4: celsius_to_fahrenheit
#
# The variable `celsius` is defined below. Assign a variable `fahrenheit`
# to the temperature converted to Fahrenheit. The formula is:
#
#     F = C × 9/5 + 32

# %%
celsius = 25
# Your code here
fahrenheit = ...

# %%
grader.check("ex4_celsius_to_fahrenheit", lambda: checks.check_ex4(fahrenheit))

# %% [markdown]
# ---
# ### Exercise 5: type_practice
#
# The variable `s` is defined below as the string `"42"`. Create a
# variable `as_number` that holds the integer value 42 (not the string).

# %%
s = "42"
# Your code here
as_number = ...

# %%
grader.check("ex5_type_practice", lambda: checks.check_ex5(as_number))

# %% [markdown]
# ---
# ### Exercise 6: classify_number
#
# The variable `n` is defined below. Assign a variable `category` to one
# of these three strings: `"positive"`, `"negative"`, or `"zero"`,
# depending on the value of `n`. Your code should work for any value of n.

# %%
n = 7
# Your code here
category = ...

# %%
grader.check("ex6_classify_number", lambda: checks.check_ex6(category))

# %% [markdown]
# ---
# ### Exercise 7: fizz_or_buzz_lite
#
# The variable `n` is defined below. Assign a variable `result` based on
# these rules:
# - If `n` is divisible by both 3 and 5: `result = "both"`
# - If `n` is divisible by 3 (but not 5): `result = "fizz"`
# - If `n` is divisible by 5 (but not 3): `result = "buzz"`
# - Otherwise: `result = "neither"`

# %%
n = 15
# Your code here
result = ...

# %%
grader.check("ex7_fizz_or_buzz_lite", lambda: checks.check_ex7(result))

# %% [markdown]
# ---
# ## Final Score

# %%
grader.report()

# %% [markdown]
# ---
# ## Submit
#
# Run the cell below to send your score to the gradebook.
# You can re-submit as many times as you like — only your highest score
# is kept.

# %%
grader.submit(student_name, SUBMIT_URL)
