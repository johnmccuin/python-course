# %% [markdown]
# <!-- Instructor note: estimated beginner completion time ~25 min working smoothly.
#      Multiply by ~3 per course prep practices → expect ~75 min real student time.
#      7 exercises: 2 functions+strings warm-ups, 1 strings-in-depth, 2 dicts, 2 file-I/O. -->
#
# # Week 3 — Homework: Functions, Strings, Dicts, and Files
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
#
# Quick reminder: every function needs three things —
# a **name**, **parameters** (the inputs), and a **return value** (the output).
#
# ```python
# def add(a, b):       # def, name, parameters
#     return a + b     # return sends the result back to the caller
# ```
#
# A function that uses `print` instead of `return` looks like it works,
# but the result disappears — callers get `None` back.

# %% [markdown]
# ---
# ### Exercise 1: shout
#
# Write a function `shout(text)` that returns the text converted to
# ALL CAPS with an exclamation mark added at the end.
#
# | Call | Expected result |
# |------|----------------|
# | `shout("hello")` | `"HELLO!"` |
# | `shout("Python is fun")` | `"PYTHON IS FUN!"` |
# | `shout("")` | `"!"` |
#
# *Tip: strings have an `.upper()` method.*

# %%
def shout(text):
    pass  # ← delete this line and write your code here

# %%
grader.check("ex1_shout", lambda: checks.check_ex1(shout))

# %% [markdown]
# ---
# ### Exercise 2: normalize
#
# Write a function `normalize(text)` that:
# 1. Strips leading and trailing whitespace
# 2. Converts the text to lowercase
# 3. Collapses any internal runs of spaces into a single space
#
# | Call | Expected result |
# |------|----------------|
# | `normalize("  Hello World  ")` | `"hello world"` |
# | `normalize("  PYTHON  IS  FUN  ")` | `"python is fun"` |
# | `normalize("single")` | `"single"` |
# | `normalize("   ")` | `""` |
#
# *Tip: calling `.split()` on a string (with no argument) splits on any*
# *whitespace and throws away empty pieces. Then `" ".join(...)` puts*
# *the words back together with exactly one space between them.*

# %%
def normalize(text):
    pass  # ← delete this line and write your code here

# %%
grader.check("ex2_normalize", lambda: checks.check_ex2(normalize))

# %% [markdown]
# ---
# ## Part 2 — Strings in Depth

# %% [markdown]
# ---
# ### Exercise 3: count_word
#
# Write a function `count_word(sentence, word)` that returns how many
# times `word` appears as a complete word in `sentence`, ignoring case.
# You may assume the sentence contains only letters and spaces.
#
# | Call | Expected result |
# |------|----------------|
# | `count_word("the cat sat on the mat", "the")` | `2` |
# | `count_word("cat cats catfish", "cat")` | `1` |
# | `count_word("Hello hello HELLO", "hello")` | `3` |
# | `count_word("no match here", "xyz")` | `0` |
#
# *Note: "cat" does **not** count inside "cats" — you want complete words only.*

# %%
def count_word(sentence, word):
    pass  # ← delete this line and write your code here

# %%
grader.check("ex3_count_word", lambda: checks.check_ex3(count_word))

# %% [markdown]
# ---
# ## Part 3 — Dictionaries
#
# Quick reminder: a dictionary maps **keys** to **values**.
# You can loop over both at once using `.items()`:
#
# ```python
# scores = {"Alice": 92, "Bob": 85}
# for name, score in scores.items():
#     print(f"{name}: {score}")
# ```

# %% [markdown]
# ---
# ### Exercise 4: filter_scores
#
# Write a function `filter_scores(scores, min_score)` that takes a
# dictionary of `{name: score}` pairs and returns a **new** dictionary
# containing only the entries whose score is **greater than or equal to**
# `min_score`.
#
# | Call | Expected result |
# |------|----------------|
# | `filter_scores({"Alice": 92, "Bob": 65, "Carol": 80}, 80)` | `{"Alice": 92, "Carol": 80}` |
# | `filter_scores({"Alice": 92, "Bob": 65}, 100)` | `{}` |
# | `filter_scores({"Alice": 92, "Bob": 65}, 0)` | `{"Alice": 92, "Bob": 65}` |

# %%
def filter_scores(scores, min_score):
    pass  # ← delete this line and write your code here

# %%
grader.check("ex4_filter_scores", lambda: checks.check_ex4(filter_scores))

# %% [markdown]
# ---
# ### Exercise 5: best_score
#
# Write a function `best_score(scores)` that takes a `{name: score}`
# dictionary and returns the **name** of the student with the highest score.
# You may assume the dictionary has at least one entry.
# If two students are tied, returning either name is fine.
#
# | Call | Expected result |
# |------|----------------|
# | `best_score({"Alice": 92, "Bob": 85, "Carol": 97})` | `"Carol"` |
# | `best_score({"only": 75})` | `"only"` |
#
# *Hint: use the same "track the best so far" strategy from Week 2's*
# *`largest` exercise — but now track a name and a score together.*

# %%
def best_score(scores):
    pass  # ← delete this line and write your code here

# %%
grader.check("ex5_best_score", lambda: checks.check_ex5(best_score))

# %% [markdown]
# ---
# ## Part 4 — Reading and Writing Files
#
# ### Objects: a quick look ahead
#
# When you write `open("data.csv", "w")`, Python returns a **file object** —
# an instance of a class that knows how to talk to the filesystem.
# You call methods on it (`.write()`, `.read()`) just like you call
# `.upper()` on a string.
#
# `pathlib.Path` works the same way.  Try running the cell below:

# %%
from pathlib import Path

p = Path("hw3_scores.csv")
print(f"hw3_scores.csv exists: {p.exists()}")   # False — not created yet
print(f"Type of p: {type(p)}")

# %% [markdown]
# `Path("hw3_scores.csv")` is an **instance of a class** called `Path`.
# You haven't written a class yourself yet — that's Week 7.  For now,
# just use the objects Python provides.
#
# The next two exercises write a CSV file and then read it back.
# Run them in order — Exercise 7 reads the file that Exercise 6 creates.

# %% [markdown]
# ---
# ### Exercise 6: save_scores
#
# Write a function `save_scores(filename, scores)` that saves a
# `{name: score}` dictionary to a text file.  Write **one line per student**
# in the format `name,score`.
#
# After `save_scores("hw3_scores.csv", {"Alice": 92, "Bob": 85, "Carol": 97})`
# the file should contain:
# ```
# Alice,92
# Bob,85
# Carol,97
# ```
#
# The function does not need to return anything.
#
# *Tip: loop over the dictionary with `for name, score in scores.items():`,*
# *then write each line with `f.write(f"{name},{score}\n")`.*

# %%
def save_scores(filename, scores):
    pass  # ← delete this line and write your code here

# %%
grader.check("ex6_save_scores", lambda: checks.check_ex6(save_scores))

# %% [markdown]
# ---
# ### Exercise 7: total_from_file
#
# Write a function `total_from_file(filename)` that reads the CSV file
# created by `save_scores` and returns the **sum** of all scores as an integer.
# Each line in the file has the format `name,score`.
#
# | Call | Expected result |
# |------|----------------|
# | `total_from_file("hw3_scores.csv")` (after Exercise 6) | `274` |
#
# You may assume the file always has at least one line and all scores are integers.

# %%
def total_from_file(filename):
    pass  # ← delete this line and write your code here

# %%
grader.check("ex7_total_from_file", lambda: checks.check_ex7(total_from_file))

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
