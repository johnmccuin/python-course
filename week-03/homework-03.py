# %% [markdown]
# <!-- Instructor note: estimated beginner completion time ~25 min working smoothly.
#      Multiply by ~3 per course prep practices → expect ~75 min real student time.
#      7 exercises: 2 functions+strings warm-ups, 1 strings-in-depth, 2 dicts, 2 tuples. -->
#
# # Week 3 — Homework: Functions, Strings, Dicts, and Tuples
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
# ### Exercise 4: popular_pages
#
# Write a function `popular_pages(views, min_views)` that takes a
# dictionary of `{page_name: view_count}` pairs and returns a **new**
# dictionary containing only the pages whose view_count is **greater than
# or equal to** `min_views`.
#
# | Call | Expected result |
# |------|----------------|
# | `popular_pages({"home": 1200, "about": 300, "blog": 800}, 800)` | `{"home": 1200, "blog": 800}` |
# | `popular_pages({"home": 1200, "about": 300}, 5000)` | `{}` |
# | `popular_pages({"home": 1200, "about": 300}, 0)` | `{"home": 1200, "about": 300}` |

# %%
def popular_pages(views, min_views):
    pass  # ← delete this line and write your code here

# %%
grader.check("ex4_popular_pages", lambda: checks.check_ex4(popular_pages))

# %% [markdown]
# ---
# ### Exercise 5: top_page
#
# Write a function `top_page(views)` that takes a `{page_name: view_count}`
# dictionary and returns the **name** of the page with the most views.
# You may assume the dictionary has at least one entry.
# If two pages are tied, returning either name is fine.
#
# | Call | Expected result |
# |------|----------------|
# | `top_page({"home": 1200, "about": 300, "blog": 800})` | `"home"` |
# | `top_page({"only": 75})` | `"only"` |
#
# *Hint: use the same "track the best so far" strategy from Week 2's*
# *`largest` exercise — but now track a page name and its view count together.*

# %%
def top_page(views):
    pass  # ← delete this line and write your code here

# %%
grader.check("ex5_top_page", lambda: checks.check_ex5(top_page))

# %% [markdown]
# ---
# ## Part 4 — Tuples
#
# Quick reminder: a **tuple** is a fixed, ordered group of values.  Listing
# values with commas **packs** them into a tuple; names on the left **unpack**
# them back out.  Returning several values from a function makes a tuple.
#
# ```python
# def divide(a, b):
#     return a // b, a % b      # packs a tuple
# q, r = divide(17, 5)          # unpacks it: q=3, r=2
# ```

# %% [markdown]
# ---
# ### Exercise 6: count_and_total
#
# Write a function `count_and_total(numbers)` that returns a **tuple**
# `(count, total)` for a list of numbers, where `count` is how many items
# are in the list and `total` is their sum.  You may use the built-in
# `len()` and `sum()`.
#
# | Call | Expected result |
# |------|----------------|
# | `count_and_total([3, 1, 4, 1, 5])` | `(5, 14)` |
# | `count_and_total([7])` | `(1, 7)` |
# | `count_and_total([])` | `(0, 0)` |
#
# *Tip: a tuple is just values separated by commas — `return len(...), sum(...)`*
# *returns the two of them as one tuple.*

# %%
def count_and_total(numbers):
    pass  # ← delete this line and write your code here

# %%
grader.check("ex6_count_and_total", lambda: checks.check_ex6(count_and_total))

# %% [markdown]
# ---
# ### Exercise 7: parse_point
#
# Write a function `parse_point(text)` that takes a string like `"3,4"` and
# returns a **tuple of two integers** `(3, 4)`.  Split on the comma and convert
# each piece to an `int`.
#
# | Call | Expected result |
# |------|----------------|
# | `parse_point("3,4")` | `(3, 4)` |
# | `parse_point("10,20")` | `(10, 20)` |
# | `parse_point("-1,5")` | `(-1, 5)` |
#
# *Tip: `text.split(",")` gives you a list of two strings; convert each with*
# *`int(...)` and return them as a tuple.*

# %%
def parse_point(text):
    pass  # ← delete this line and write your code here

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
#
# Run the cell below to send your score to the gradebook.
# You can re-submit as many times as you like — only your highest score is kept.

# %%
grader.submit(student_name, SUBMIT_URL)
