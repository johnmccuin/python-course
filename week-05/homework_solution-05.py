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
# ### Exercise 1: Dog

# %%
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        return f"{self.name} says woof!"

# %%
grader.check("ex1_dog", lambda: checks.check_ex1(Dog))

# %% [markdown]
# ---
# ### Exercise 2: Counter

# %%
class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

    def reset(self):
        self.count = 0

# %%
grader.check("ex2_counter", lambda: checks.check_ex2(Counter))

# %% [markdown]
# ---
# ## Part 2 — Methods That Compute and Enforce Rules

# %% [markdown]
# ---
# ### Exercise 3: Rectangle

# %%
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

# %%
grader.check("ex3_rectangle", lambda: checks.check_ex3(Rectangle))

# %% [markdown]
# ---
# ### Exercise 4: BankAccount

# %%
class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds"
        self.balance -= amount
        return self.balance

# %%
grader.check("ex4_bank_account", lambda: checks.check_ex4(BankAccount))

# %% [markdown]
# ---
# ## Part 3 — Strings, Collections, and Tying It Together

# %% [markdown]
# ---
# ### Exercise 5: Student

# %%
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def __str__(self):
        return f"{self.name} (grade {self.grade})"

# %%
grader.check("ex5_student", lambda: checks.check_ex5(Student))

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
# ### Exercise 7: Thermostat

# %%
class Thermostat:
    def __init__(self, temp):
        self.temp = temp

    def warmer(self):
        self.temp += 1

    def cooler(self):
        self.temp -= 1

    def is_freezing(self):
        return self.temp <= 32

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

# %%
grader.submit(student_name, SUBMIT_URL)
