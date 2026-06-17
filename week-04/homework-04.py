# %% [markdown]
# <!-- Instructor note: estimated beginner completion time ~30 min working smoothly.
#      Multiply by ~3 per course prep practices → expect ~90 min real student time.
#      7 exercises mapped to the five lecture-04 parts:
#      2 files, 1 modules/imports, 2 error handling, 1 debugging fix, 1 assertions.
#      Only concepts from lectures 1-4 are tested. -->
#
# # Week 4 — Homework: Files, Modules, Errors, and Assertions
#
# Work through each exercise in order.
# After finishing an exercise, run its **check cell** to see if your answer is correct.
# When you're done, run the **Final Score** cell, then the **Submit** cell.

# %% [markdown]
# **Enter your name below exactly as it appears on the course roster —
# spelling and capitalization matter. This is used to record your score.**

# %%
student_name = "Your Name Here"

# %% [markdown]
# ---
# ## Setup — RUN AT BEGINNING, DO NOT MODIFY

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
#
# Quick reminder: open a file with `with open(path, mode) as f:` — `"w"` writes
# (overwriting), `"r"` reads. The `with` block closes the file for you.
#
# ```python
# with open("notes.txt", "w") as f:
#     f.write("first line\n")    # \n starts a new line
#
# with open("notes.txt") as f:   # "r" is the default
#     text = f.read()
# ```

# %% [markdown]
# ---
# ### Exercise 1: save_lines
#
# Write a function `save_lines(filename, lines)` that writes each string in the
# list `lines` to `filename`, **one per line**. The function does not need to
# return anything.
#
# After `save_lines("hw4.txt", ["apple", "banana", "cherry"])` the file should
# contain:
# ```
# apple
# banana
# cherry
# ```
#
# *Tip: open the file with `"w"` mode, loop over `lines`, and write each one*
# *followed by a newline: `f.write(line + "\n")`.*

# %%
def save_lines(filename, lines):
    pass  # ← delete this line and write your code here

# %%
grader.check("ex1_save_lines", lambda: checks.check_ex1(save_lines))

# %% [markdown]
# ---
# ### Exercise 2: sum_numbers
#
# Write a function `sum_numbers(filename)` that reads a file with **one whole
# number per line** and returns the **sum** of those numbers as an integer.
#
# For a file containing:
# ```
# 10
# 20
# 30
# ```
# `sum_numbers(...)` should return `60`.
#
# *Tip: loop over the file line by line, `int()` each line, and add it to a*
# *running total. Watch out — `int(" 10\n")` works, but build the habit of*
# *`.strip()`-ing each line first.*

# %%
def sum_numbers(filename):
    pass  # ← delete this line and write your code here

# %%
grader.check("ex2_sum_numbers", lambda: checks.check_ex2(sum_numbers))

# %% [markdown]
# ---
# ## Part 2 — Modules and Imports
#
# Quick reminder: `import` loads a module so you can use the code inside it.
# Reach for the standard library before writing things by hand.
#
# ```python
# import math
# print(math.sqrt(16))   # 4.0 — access contents with a dot
# ```

# %% [markdown]
# ---
# ### Exercise 3: circle_area
#
# Write a function `circle_area(radius)` that returns the area of a circle
# with the given radius. Use `math.pi` for full precision — don't type
# `3.14` by hand.
#
# $$A = \pi r^2$$
#
# | Call | Expected result |
# |------|----------------|
# | `circle_area(1)` | `3.14159…` (the value of `math.pi`) |
# | `circle_area(0)` | `0.0` |
# | `circle_area(2)` | `12.566…` |
#
# *Tip: `import math` at the top of the cell, then use `math.pi`.*

# %%
def circle_area(radius):
    pass  # ← delete this line and write your code here

# %%
grader.check("ex3_circle_area", lambda: checks.check_ex3(circle_area))

# %% [markdown]
# ---
# ## Part 3 — Error Handling
#
# Quick reminder: `try / except` lets you catch an exception and decide what
# to do instead of crashing.
#
# ```python
# try:
#     value = int("abc")          # this raises ValueError
# except ValueError:
#     print("not a number")       # runs instead of crashing
# ```

# %% [markdown]
# ---
# ### Exercise 4: safe_lookup
#
# A price catalog is a dictionary mapping each item name to its price, e.g.
# `{"apple": 50, "pear": 75}`. Write a function `safe_lookup(prices, item)`
# that returns `prices[item]`. If `item` isn't in the catalog, catch the
# `KeyError` and return the string `"Item not found."` instead of crashing.
#
# | Call | Expected result |
# |------|----------------|
# | `safe_lookup({"apple": 50, "pear": 75}, "apple")` | `50` |
# | `safe_lookup({"apple": 50, "pear": 75}, "pear")` | `75` |
# | `safe_lookup({"apple": 50}, "banana")` | `"Item not found."` |
#
# *Tip: put the lookup `prices[item]` inside a `try` block and handle*
# *`except KeyError:`.*

# %%
def safe_lookup(prices, item):
    pass  # ← delete this line and write your code here

# %%
grader.check("ex4_safe_lookup", lambda: checks.check_ex4(safe_lookup))

# %% [markdown]
# ---
# ### Exercise 5: parse_scores
#
# Write a function `parse_scores(items)` that takes a list of strings and
# returns a **new list** of integers — one for each item that can be
# converted to a whole number. Items that aren't valid whole numbers should
# be **skipped** (not cause a crash).
#
# | Call | Expected result |
# |------|----------------|
# | `parse_scores(["10", "x", "20", "3.5"])` | `[10, 20]` |
# | `parse_scores(["1", "2", "3"])` | `[1, 2, 3]` |
# | `parse_scores(["a", "b"])` | `[]` |
#
# *Note: `int("3.5")` raises `ValueError`, so `"3.5"` is skipped too.*
#
# *Tip: loop over `items`; inside the loop, `try` to `int()` each one and*
# *append it, and `except ValueError:` to skip the bad ones.*

# %%
def parse_scores(items):
    pass  # ← delete this line and write your code here

# %%
grader.check("ex5_parse_scores", lambda: checks.check_ex5(parse_scores))

# %% [markdown]
# ---
# ## Part 4 — Debugging and Tracebacks
#
# Quick reminder: a traceback is Python's crash report — read it bottom-up to
# find the line and error type. The function below has a bug that only shows
# up in one situation.

# %% [markdown]
# ---
# ### Exercise 6: fix success_rate
#
# The function `success_rate(passed, total)` is supposed to return the
# percentage of attempts that passed: `passed / total * 100`. It works when
# `total` is positive but **crashes when `total` is 0** with a
# `ZeroDivisionError` (dividing by 0).
#
# Fix it so that `total == 0` returns `0.0` instead of crashing. Leave the
# behavior for a positive `total` unchanged.
#
# | Call | Expected result |
# |------|----------------|
# | `success_rate(3, 4)` | `75.0` |
# | `success_rate(9, 10)` | `90.0` |
# | `success_rate(0, 0)` | `0.0` |
#
# *Tip: check whether `total` is 0 before dividing — `if total == 0:`*
# *return 0.0; otherwise do the normal calculation.*

# %%
def success_rate(passed, total):
    # BUG: this line crashes when total is 0. Fix the function.
    return passed / total * 100

# %%
grader.check("ex6_success_rate", lambda: checks.check_ex6(success_rate))

# %% [markdown]
# ---
# ## Part 5 — Assertions
#
# Quick reminder: an assertion is a sanity check that stops the program with
# an `AssertionError` if a condition you expect to be true turns out false.
#
# ```python
# assert amount > 0, "amount must be positive"
# ```

# %% [markdown]
# ---
# ### Exercise 7: withdraw
#
# Write a function `withdraw(balance, amount)` that takes money out of an
# account and returns the new balance (`balance - amount`). Guard it with
# `assert` statements:
#
# - the `amount` must be greater than 0, and
# - the `amount` must be no more than the current `balance`.
#
# | Call | Expected result |
# |------|----------------|
# | `withdraw(100, 30)` | `70` |
# | `withdraw(50, 50)` | `0` |
# | `withdraw(100, 150)` | raises `AssertionError` |
# | `withdraw(100, -5)` | raises `AssertionError` |
#
# *Tip: write the two `assert` lines first, then return the new balance.*

# %%
def withdraw(balance, amount):
    pass  # ← delete this line and write your code here

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
#
# Run the cell below to send your score to the gradebook.
# You can re-submit as many times as you like — only your highest score is kept.

# %%
grader.submit(student_name, SUBMIT_URL)
