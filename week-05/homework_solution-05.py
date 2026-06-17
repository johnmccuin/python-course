# %% [markdown]
# # Week 5 — Homework (Reference Solution)
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

# %% [markdown]
# ---
# ### Exercise 1: Robot

# %%
class Robot:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} says beep boop!"

# %%
grader.check("ex1_robot", lambda: checks.check_ex1(Robot))

# %% [markdown]
# ---
# ### Exercise 2: Pedometer

# %%
class Pedometer:
    def __init__(self):
        self.steps = 0

    def step(self):
        self.steps += 1

    def reset(self):
        self.steps = 0

# %%
grader.check("ex2_pedometer", lambda: checks.check_ex2(Pedometer))

# %% [markdown]
# ---
# ## Part 2 — Methods That Compute and Enforce Rules

# %% [markdown]
# ---
# ### Exercise 3: GardenPlot

# %%
class GardenPlot:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

# %%
grader.check("ex3_garden_plot", lambda: checks.check_ex3(GardenPlot))

# %% [markdown]
# ---
# ### Exercise 4: Warehouse

# %%
class Warehouse:
    def __init__(self, stock=0):
        self.stock = stock

    def receive(self, amount):
        self.stock += amount

    def ship(self, amount):
        if amount > self.stock:
            return "Insufficient stock"
        self.stock -= amount
        return self.stock

# %%
grader.check("ex4_warehouse", lambda: checks.check_ex4(Warehouse))

# %% [markdown]
# ---
# ## Part 3 — Strings, Collections, and Tying It Together

# %% [markdown]
# ---
# ### Exercise 5: Book

# %%
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"

# %%
grader.check("ex5_book", lambda: checks.check_ex5(Book))

# %% [markdown]
# ---
# ### Exercise 6: Playlist

# %%
class Playlist:
    def __init__(self):
        self.songs = []

    def add(self, song):
        self.songs.append(song)

    def count(self):
        return len(self.songs)

# %%
grader.check("ex6_playlist", lambda: checks.check_ex6(Playlist))

# %% [markdown]
# ---
# ### Exercise 7: Elevator

# %%
class Elevator:
    def __init__(self, floor):
        self.floor = floor

    def up(self):
        self.floor += 1

    def down(self):
        self.floor -= 1

    def is_ground_floor(self):
        return self.floor == 0

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

# %%
grader.submit(student_name, SUBMIT_URL)
