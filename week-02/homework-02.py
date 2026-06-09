# %% [markdown]
# <!-- Instructor note: estimated beginner completion time ~20 min working smoothly.
#      Multiply by ~3 per course prep practices → expect ~60 min real student time.
#      7 exercises: 2 if/elif/else, 2 while loops, 3 for-loops-over-lists. -->
#
# # Week 2 — Homework
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
# ## Part 1 — If / Elif / Else
#
# Quick reminder: `elif` lets you chain several conditions together.
# Python checks them **top to bottom** and runs only the first one that matches.
#
# ```python
# if condition_1:
#     result = "value_1"
# elif condition_2:
#     result = "value_2"
# else:
#     result = "default_value"
# ```

# %% [markdown]
# ---
# ### Exercise 1: game_rank
#
# An online game assigns each player a **rank** based on their `points`.
# The variable `points` is already set to `1200`.
# Write an `if/elif/else` block that assigns a variable `rank` to the
# correct rank name:
#
# | Points | Rank |
# |--------|------|
# | 2000 or more | `"Diamond"` |
# | 1500 – 1999  | `"Platinum"` |
# | 1000 – 1499  | `"Gold"` |
# | 500 – 999    | `"Silver"` |
# | Below 500    | `"Bronze"` |
#
# Your code should work correctly for **any** value of `points`, not just 1200.

# %%
points = 1200
# Your code here
rank = ...

# %%
grader.check("ex1_game_rank", lambda: checks.check_ex1(rank))

# %% [markdown]
# ---
# ### Exercise 2: shipping_cost
#
# An online store charges shipping based on package weight:
#
# | Weight | Price |
# |--------|-------|
# | 1 lb or under | \$3.99 |
# | Over 1 lb, up to 5 lbs | \$7.99 |
# | Over 5 lbs | \$14.99 |
#
# The variable `weight` is set to `3.5` (pounds).
# Write an `if/elif/else` block that assigns `cost` to the correct price.
# Your code should work correctly for **any** value of `weight`.

# %%
weight = 3.5
# Your code here
cost = ...

# %%
grader.check("ex2_shipping_cost", lambda: checks.check_ex2(cost))

# %% [markdown]
# ---
# ## Part 2 — While Loops
#
# Quick reminder: every while loop needs three things —
# a **starting value** before the loop, a **condition** to check each pass,
# and a **change** inside the body that will eventually make the condition False.
#
# ```python
# n = 10            # starting value
#
# while n > 0:      # condition
#     print(n)      # do some work
#     n -= 1        # change — without this the loop runs forever!
#
# print("Done!")    # code here runs after the loop finishes
# ```

# %% [markdown]
# ---
# ### Exercise 3: even_total
#
# `limit` is set to `20`. Use a while loop to add up every **even** number from
# `2` through `limit` (inclusive) and store the running total in `total`.
#
# Example: if `limit` were `8`, then `total` should be `2 + 4 + 6 + 8 = 20`.
#
# For `limit = 20`, `total` should be `110`.

# %%
limit = 20
total = 0
# Your code here — use a while loop

# %%
grader.check("ex3_even_total", lambda: checks.check_ex3(total))

# %% [markdown]
# ---
# ### Exercise 4: bounce_count
#
# A superball is dropped from `height = 64` feet. After each bounce it rises to
# **half** the previous height — use integer division (`//= 2`) to keep things
# clean. Count how many bounces until the height reaches exactly `1`.
#
# Trace of what happens:
# ```
# height: 64 → 32 → 16 → 8 → 4 → 2 → 1
# bounces:       1    2   3   4   5   6
# ```
# Assign the total number of bounces to `bounces`.

# %%
height = 64
bounces = 0
# Your code here — use a while loop

# %%
grader.check("ex4_bounce_count", lambda: checks.check_ex4(bounces))

# %% [markdown]
# ---
# ## Part 3 — For Loops over Lists
#
# Quick reminder: a `for` loop visits every item in a list one at a time.
# You can combine it with a counter or build a new list as you go:
#
# ```python
# numbers = [10, 3, 7, 5]
#
# # Count items that meet a condition
# count = 0
# for n in numbers:
#     if n > 6:
#         count += 1
# # count is now 2  (10 and 7 are above 6)
#
# # Build a new list
# doubled = []
# for n in numbers:
#     doubled.append(n * 2)
# # doubled is [20, 6, 14, 10]
# ```

# %% [markdown]
# ---
# ### Exercise 5: hot_days
#
# ```python
# temps = [55, 72, 68, 81, 90, 63, 77]
# ```
#
# Count how many temperatures in `temps` are **strictly above 75** and
# store the count in `hot_days`.
#
# Expected: `hot_days` should be `3`  (the values 81, 90, and 77).

# %%
temps = [55, 72, 68, 81, 90, 63, 77]
hot_days = 0
# Your code here — use a for loop

# %%
grader.check("ex5_hot_days", lambda: checks.check_ex5(hot_days))

# %% [markdown]
# ---
# ### Exercise 6: word_lengths
#
# ```python
# words = ["python", "is", "fun", "to", "learn"]
# ```
#
# Build a new list `lengths` that contains the **length of each word**,
# in the same order. Use `len(word)` to measure a word's length.
#
# Example: `len("python")` is `6`, so the first item in `lengths` should be `6`.
#
# Expected: `lengths == [6, 2, 3, 2, 5]`

# %%
words = ["python", "is", "fun", "to", "learn"]
lengths = []
# Your code here — use a for loop

# %%
grader.check("ex6_word_lengths", lambda: checks.check_ex6(lengths))

# %% [markdown]
# ---
# ### Exercise 7: largest
#
# ```python
# numbers = [5, 12, 3, 19, 7, 4, 11]
# ```
#
# Find the **largest** number in `numbers` using a for loop — no peeking at
# `max()` yet, that's the easy way out!
#
# Strategy: start with `largest = numbers[0]` as your first guess.
# Then loop through the list: whenever you find a number bigger than your
# current `largest`, update it.
#
# Expected: `largest == 19`

# %%
numbers = [5, 12, 3, 19, 7, 4, 11]
largest = numbers[0]
# Your code here — use a for loop

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
#
# Run the cell below to send your score to the gradebook.
# You can re-submit as many times as you like — only your highest score is kept.

# %%
grader.submit(student_name, SUBMIT_URL)
