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
# ### Exercise 1: Robot
#
# Define a class `Robot` with:
# - an `__init__(self, name)` that stores `name` as an attribute, and
# - a method `speak(self)` that returns the string `f"{name} says beep boop!"`.
#
# | Code | Expected result |
# |------|----------------|
# | `Robot("R2D2").name` | `"R2D2"` |
# | `Robot("R2D2").speak()` | `"R2D2 says beep boop!"` |
# | `Robot("WallE").speak()` | `"WallE says beep boop!"` |

# %%
class Robot:
    pass  # ← replace this with your __init__ and speak methods

# %%
grader.check("ex1_robot", lambda: checks.check_ex1(Robot))

# %% [markdown]
# ---
# ### Exercise 2: Pedometer
#
# Define a class `Pedometer` with:
# - an `__init__(self)` that sets `self.steps = 0`,
# - a method `step(self)` that adds 1 to `self.steps`, and
# - a method `reset(self)` that sets `self.steps` back to 0.
#
# | Code | Expected result |
# |------|----------------|
# | a fresh `Pedometer().steps` | `0` |
# | after `step()` three times | `steps == 3` |
# | after `reset()` | `steps == 0` |
#
# *Remember: inside a method, the attribute is `self.steps`, never bare `steps`.*

# %%
class Pedometer:
    pass  # ← replace this with your __init__, step, and reset methods

# %%
grader.check("ex2_pedometer", lambda: checks.check_ex2(Pedometer))

# %% [markdown]
# ---
# ## Part 2 — Methods That Compute and Enforce Rules

# %% [markdown]
# ---
# ### Exercise 3: GardenPlot
#
# Define a class `GardenPlot` with:
# - an `__init__(self, length, width)` storing both, and
# - methods `area(self)` (returns `length * width`, the planting area) and
#   `perimeter(self)` (returns `2 * (length + width)`, the fencing needed).
#
# | Code | Expected result |
# |------|----------------|
# | `GardenPlot(3, 4).area()` | `12` |
# | `GardenPlot(3, 4).perimeter()` | `14` |
# | `GardenPlot(5, 5).area()` | `25` |

# %%
class GardenPlot:
    pass  # ← replace this with your __init__, area, and perimeter methods

# %%
grader.check("ex3_garden_plot", lambda: checks.check_ex3(GardenPlot))

# %% [markdown]
# ---
# ### Exercise 4: Warehouse
#
# Define a class `Warehouse` with:
# - an `__init__(self, stock=0)` storing the starting stock (default 0),
# - a method `receive(self, amount)` that adds `amount` to the stock, and
# - a method `ship(self, amount)` that:
#     - if `amount` is **more than** the stock, returns the string
#       `"Insufficient stock"` **and leaves the stock unchanged**, otherwise
#     - subtracts `amount` from the stock and returns the new stock.
#
# | Code | Expected result |
# |------|----------------|
# | `Warehouse().stock` | `0` |
# | after `receive(50)` on a new warehouse | `stock == 50` |
# | `ship(30)` on a stock of 50 | returns `20`, stock is `20` |
# | `ship(100)` on a stock of 20 | returns `"Insufficient stock"`, stock still `20` |

# %%
class Warehouse:
    pass  # ← replace this with your __init__, receive, and ship methods

# %%
grader.check("ex4_warehouse", lambda: checks.check_ex4(Warehouse))

# %% [markdown]
# ---
# ## Part 3 — Strings, Collections, and Tying It Together

# %% [markdown]
# ---
# ### Exercise 5: Book
#
# Define a class `Book` with:
# - an `__init__(self, title, author)` storing both, and
# - a `__str__(self)` method that returns `f"{title} by {author}"`.
#
# | Code | Expected result |
# |------|----------------|
# | `str(Book("Dune", "Herbert"))` | `"Dune by Herbert"` |
# | `str(Book("1984", "Orwell"))` | `"1984 by Orwell"` |
#
# *Remember: `__str__` is what `print()` and `str()` use to turn an instance*
# *into text.*

# %%
class Book:
    pass  # ← replace this with your __init__ and __str__ methods

# %%
grader.check("ex5_book", lambda: checks.check_ex5(Book))

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
# ### Exercise 7: Elevator
#
# Tie it together. Define a class `Elevator` with:
# - an `__init__(self, floor)` storing the current floor,
# - a method `up(self)` that raises `self.floor` by 1,
# - a method `down(self)` that lowers `self.floor` by 1, and
# - a method `is_ground_floor(self)` that returns `True` when `self.floor` is 0,
#   and `False` otherwise.
#
# | Code | Expected result |
# |------|----------------|
# | `Elevator(3).floor` | `3` |
# | after `up()` twice on 3 | `floor == 5` |
# | `Elevator(1)` then `down()` then `is_ground_floor()` | `True` |
# | `Elevator(3).is_ground_floor()` | `False` |

# %%
class Elevator:
    pass  # ← replace this with your __init__, up, down, and is_ground_floor methods

# %%
grader.check("ex7_elevator", lambda: checks.check_ex7(Elevator))

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
