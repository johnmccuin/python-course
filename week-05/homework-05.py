# %% [markdown]
# <!-- Instructor note: estimated beginner completion time ~30 min working smoothly.
#      Multiply by ~3 per course prep practices → expect ~90 min real student time.
#      7 exercises mapped to lecture-05 (Classes and Objects):
#      1 basic class+method, 1 mutating state, 1 computed methods, 1 rule-guarding
#      method, 1 __str__, 1 collection attribute, 1 multi-method tie-together.
#      Only concepts from lectures 1-5 are tested. -->
#
# # Week 5 — Homework: Classes and Objects
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
    "checks.py": f"{_BASE}/week-05/checks-05.py",
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
grader = Grader("Week 5 Homework")

SUBMIT_URL = "https://script.google.com/macros/s/AKfycbxmZUvgnvH3-rWYfr3ZV9vMcK8mpKvoStmjsoF0iRNLPCb_wuPNzj-MENyzRs44CwdXkQ/exec"

print("Ready!")

# %% [markdown]
# ---
# ## Part 1 — Defining a Class
#
# Quick reminder: `__init__` sets up an instance's data; `self` is the instance;
# attributes live on `self`.
#
# ```python
# class Cat:
#     def __init__(self, name):
#         self.name = name          # an attribute
#     def meow(self):               # a method — first parameter is always self
#         return f"{self.name} says meow!"
# ```

# %% [markdown]
# ---
# ### Exercise 1: Dog
#
# Define a class `Dog` with:
# - an `__init__(self, name)` that stores `name` as an attribute, and
# - a method `bark(self)` that returns the string `f"{name} says woof!"`.
#
# | Code | Expected result |
# |------|----------------|
# | `Dog("Rex").name` | `"Rex"` |
# | `Dog("Rex").bark()` | `"Rex says woof!"` |
# | `Dog("Fifi").bark()` | `"Fifi says woof!"` |

# %%
class Dog:
    pass  # ← replace this with your __init__ and bark methods

# %%
grader.check("ex1_dog", lambda: checks.check_ex1(Dog))

# %% [markdown]
# ---
# ### Exercise 2: Counter
#
# Define a class `Counter` with:
# - an `__init__(self)` that sets `self.count = 0`,
# - a method `increment(self)` that adds 1 to `self.count`, and
# - a method `reset(self)` that sets `self.count` back to 0.
#
# | Code | Expected result |
# |------|----------------|
# | a fresh `Counter().count` | `0` |
# | after `increment()` three times | `count == 3` |
# | after `reset()` | `count == 0` |
#
# *Remember: inside a method, the attribute is `self.count`, never bare `count`.*

# %%
class Counter:
    pass  # ← replace this with your __init__, increment, and reset methods

# %%
grader.check("ex2_counter", lambda: checks.check_ex2(Counter))

# %% [markdown]
# ---
# ## Part 2 — Methods That Compute and Enforce Rules

# %% [markdown]
# ---
# ### Exercise 3: Rectangle
#
# Define a class `Rectangle` with:
# - an `__init__(self, width, height)` storing both, and
# - methods `area(self)` (returns `width * height`) and `perimeter(self)`
#   (returns `2 * (width + height)`).
#
# | Code | Expected result |
# |------|----------------|
# | `Rectangle(3, 4).area()` | `12` |
# | `Rectangle(3, 4).perimeter()` | `14` |
# | `Rectangle(5, 5).area()` | `25` |

# %%
class Rectangle:
    pass  # ← replace this with your __init__, area, and perimeter methods

# %%
grader.check("ex3_rectangle", lambda: checks.check_ex3(Rectangle))

# %% [markdown]
# ---
# ### Exercise 4: BankAccount
#
# Define a class `BankAccount` with:
# - an `__init__(self, balance=0)` storing the starting balance (default 0),
# - a method `deposit(self, amount)` that adds `amount` to the balance, and
# - a method `withdraw(self, amount)` that:
#     - if `amount` is **more than** the balance, returns the string
#       `"Insufficient funds"` **and leaves the balance unchanged**, otherwise
#     - subtracts `amount` from the balance and returns the new balance.
#
# | Code | Expected result |
# |------|----------------|
# | `BankAccount().balance` | `0` |
# | after `deposit(50)` on a new account | `balance == 50` |
# | `withdraw(30)` on a balance of 50 | returns `20`, balance is `20` |
# | `withdraw(100)` on a balance of 20 | returns `"Insufficient funds"`, balance still `20` |

# %%
class BankAccount:
    pass  # ← replace this with your __init__, deposit, and withdraw methods

# %%
grader.check("ex4_bank_account", lambda: checks.check_ex4(BankAccount))

# %% [markdown]
# ---
# ## Part 3 — Strings, Collections, and Tying It Together

# %% [markdown]
# ---
# ### Exercise 5: Student
#
# Define a class `Student` with:
# - an `__init__(self, name, grade)` storing both, and
# - a `__str__(self)` method that returns `f"{name} (grade {grade})"`.
#
# | Code | Expected result |
# |------|----------------|
# | `str(Student("Ada", 95))` | `"Ada (grade 95)"` |
# | `str(Student("Bob", 72))` | `"Bob (grade 72)"` |
#
# *Remember: `__str__` is what `print()` and `str()` use to turn an instance*
# *into text.*

# %%
class Student:
    pass  # ← replace this with your __init__ and __str__ methods

# %%
grader.check("ex5_student", lambda: checks.check_ex5(Student))

# %% [markdown]
# ---
# ### Exercise 6: Playlist
#
# A class can hold a whole collection as an attribute. Define `Playlist` with:
# - an `__init__(self)` that sets `self.songs = []` (an empty list),
# - a method `add(self, song)` that appends `song` to `self.songs`, and
# - a method `count(self)` that returns how many songs are in the playlist.
#
# | Code | Expected result |
# |------|----------------|
# | a fresh `Playlist().count()` | `0` |
# | after adding two songs | `count() == 2` |
# | two separate playlists | each keeps its **own** songs |

# %%
class Playlist:
    pass  # ← replace this with your __init__, add, and count methods

# %%
grader.check("ex6_playlist", lambda: checks.check_ex6(Playlist))

# %% [markdown]
# ---
# ### Exercise 7: Thermostat
#
# Tie it together. Define a class `Thermostat` with:
# - an `__init__(self, temp)` storing the temperature,
# - a method `warmer(self)` that raises `self.temp` by 1,
# - a method `cooler(self)` that lowers `self.temp` by 1, and
# - a method `is_freezing(self)` that returns `True` when `self.temp` is 32 or
#   below, and `False` otherwise.
#
# | Code | Expected result |
# |------|----------------|
# | `Thermostat(70).temp` | `70` |
# | after `warmer()` twice on 70 | `temp == 72` |
# | `Thermostat(33)` then `cooler()` then `is_freezing()` | `True` |
# | `Thermostat(70).is_freezing()` | `False` |

# %%
class Thermostat:
    pass  # ← replace this with your __init__, warmer, cooler, and is_freezing methods

# %%
grader.check("ex7_thermostat", lambda: checks.check_ex7(Thermostat))

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
