# %% [markdown]
# <!-- Instructor note: estimated beginner completion time ~30 min working smoothly.
#      Multiply by ~3 per course prep practices → expect ~90 min real student time.
#      7 exercises mapped to the four lecture-04 parts:
#      2 modules/imports, 2 error handling, 1 debugging fix, 2 assertions.
#      Only concepts from lectures 1-4 are tested. -->
#
# # Week 4 — Homework: Modules, Errors, Debugging, and Assertions
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
# ## Part 1 — Modules and Imports
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
# ### Exercise 1: circle_area
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
grader.check("ex1_circle_area", lambda: checks.check_ex1(circle_area))

# %% [markdown]
# ---
# ### Exercise 2: count_punctuation
#
# Write a function `count_punctuation(text)` that returns how many characters
# in `text` are punctuation marks. Use the `string` module's
# `string.punctuation` (the string of all punctuation characters) instead of
# listing them yourself.
#
# | Call | Expected result |
# |------|----------------|
# | `count_punctuation("Hello, World!")` | `2` |
# | `count_punctuation("no punctuation here")` | `0` |
# | `count_punctuation("a.b.c")` | `2` |
# | `count_punctuation("")` | `0` |
#
# *Tip: `import string`, then loop over the characters and check*
# *`if ch in string.punctuation:`.*

# %%
def count_punctuation(text):
    pass  # ← delete this line and write your code here

# %%
grader.check("ex2_count_punctuation", lambda: checks.check_ex2(count_punctuation))

# %% [markdown]
# ---
# ## Part 2 — Error Handling
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
# ### Exercise 3: safe_divide
#
# Write a function `safe_divide(a, b)` that returns `a / b`. If `b` is zero,
# catch the `ZeroDivisionError` and return the string
# `"Cannot divide by zero."` instead of crashing.
#
# | Call | Expected result |
# |------|----------------|
# | `safe_divide(10, 2)` | `5.0` |
# | `safe_divide(9, 2)` | `4.5` |
# | `safe_divide(10, 0)` | `"Cannot divide by zero."` |
#
# *Tip: put the division inside a `try` block and handle*
# *`except ZeroDivisionError:`.*

# %%
def safe_divide(a, b):
    pass  # ← delete this line and write your code here

# %%
grader.check("ex3_safe_divide", lambda: checks.check_ex3(safe_divide))

# %% [markdown]
# ---
# ### Exercise 4: parse_scores
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
grader.check("ex4_parse_scores", lambda: checks.check_ex4(parse_scores))

# %% [markdown]
# ---
# ## Part 3 — Debugging and Tracebacks
#
# Quick reminder: a traceback is Python's crash report — read it bottom-up to
# find the line and error type. The function below has a bug that only shows
# up in one situation.

# %% [markdown]
# ---
# ### Exercise 5: fix average
#
# The function `average(numbers)` is supposed to return the mean of a list.
# It works for non-empty lists but **crashes on an empty list** with a
# `ZeroDivisionError` (dividing by `len([])`, which is 0).
#
# Fix it so that an empty list returns `0` instead of crashing. Leave the
# behavior for non-empty lists unchanged.
#
# | Call | Expected result |
# |------|----------------|
# | `average([2, 4, 6])` | `4.0` |
# | `average([10])` | `10.0` |
# | `average([])` | `0` |
#
# *Tip: check whether the list is empty before dividing — `if len(numbers) == 0:`*
# *return 0; otherwise do the normal calculation.*

# %%
def average(numbers):
    # BUG: this line crashes when numbers is empty. Fix the function.
    return sum(numbers) / len(numbers)

# %%
grader.check("ex5_average", lambda: checks.check_ex5(average))

# %% [markdown]
# ---
# ## Part 4 — Assertions
#
# Quick reminder: an assertion is a sanity check that stops the program with
# an `AssertionError` if a condition you expect to be true turns out false.
#
# ```python
# assert amount > 0, "amount must be positive"
# ```

# %% [markdown]
# ---
# ### Exercise 6: rectangle_area
#
# Write a function `rectangle_area(width, height)` that returns
# `width * height`. **Before** computing the area, add two `assert` statements
# verifying that `width` and `height` are each greater than 0.
#
# | Call | Expected result |
# |------|----------------|
# | `rectangle_area(3, 4)` | `12` |
# | `rectangle_area(2.5, 2)` | `5.0` |
# | `rectangle_area(-1, 4)` | raises `AssertionError` |
# | `rectangle_area(3, 0)` | raises `AssertionError` |
#
# *Tip: `assert width > 0, "width must be positive"` (and one for height),*
# *then `return width * height`.*

# %%
def rectangle_area(width, height):
    pass  # ← delete this line and write your code here

# %%
grader.check("ex6_rectangle_area", lambda: checks.check_ex6(rectangle_area))

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
