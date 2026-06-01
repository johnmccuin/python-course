# %% [markdown]
# # Week 3 — Functions and More Data
#
# This week we cover a lot of ground:
#
# 1. Defining and calling functions
# 2. Parameters, return values, defaults, keyword args
# 3. Docstrings and scope
# 4. Strings in depth
# 5. Dictionaries
# 6. Basic file I/O
# 7. A first look at objects (foreshadowing Week 6)

# %% [markdown]
# ---
# ## Part 1 — Functions

# %% [markdown]
# ### 1.1 Why Functions?
#
# Suppose we want to greet three different people.  Without functions:

# %%
print("Hello, Alice! Welcome.")
print("Hello, Bob! Welcome.")
print("Hello, Carol! Welcome.")

# %% [markdown]
# That works, but we wrote nearly the same line three times.
# If the greeting changes, we have to edit every line.
#
# Functions solve this: write the logic once, reuse it everywhere.

# %% [markdown]
# ### 1.2 Defining and Calling a Function

# %%
def greet(name):
    print(f"Hello, {name}! Welcome.")

greet("Alice")
greet("Bob")
greet("Carol")

# %% [markdown]
# **Anatomy of a function definition:**
#
# ```
# def  greet  (name)  :
#  ^     ^      ^
#  |     |      └── parameter (placeholder for the real value)
#  |     └── function name
#  └── keyword that starts the definition
# ```

# %% [markdown]
# ### 1.3 Parameters and Arguments
#
# A function can have zero, one, or many parameters.

# %%
def say_hello():
    print("Hello, world!")

say_hello()

# %%
def add(a, b):
    return a + b

print(add(3, 4))
print(add(10, -2))

# %% [markdown]
# **Parameter** = the name inside `def` (the placeholder).
# **Argument** = the actual value passed when calling.

# %% [markdown]
# ### 1.4 Return Values
#
# `print` shows output on screen but the result is gone.
# `return` sends a value *back* to the caller so it can be stored or used.

# %%
def square(n):
    return n * n

result = square(5)
print(result)          # 25
print(square(7) + 1)   # 50

# %% [markdown]
# If a function has no `return` statement it automatically returns `None`.

# %%
def greet_no_return(name):
    print(f"Hello, {name}!")

value = greet_no_return("Dana")
print(value)   # None

# %% [markdown]
# ### 1.5 Default Parameters

# %%
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Alice")                  # uses default
greet("Bob", "Good morning")   # overrides default

# %% [markdown]
# **Rule:** parameters with defaults must come *after* parameters without defaults.
#
# ```python
# def foo(a, b=10):   # OK
# def foo(a=10, b):   # SyntaxError
# ```

# %% [markdown]
# ### 1.6 Keyword Arguments

# %%
def describe_pet(animal, name):
    print(f"I have a {animal} named {name}.")

describe_pet("dog", "Rex")                    # positional
describe_pet(name="Whiskers", animal="cat")   # keyword — any order
describe_pet("hamster", name="Nibbles")       # mix

# %% [markdown]
# ### 1.7 Docstrings

# %%
def celsius_to_fahrenheit(celsius):
    """Convert a temperature from Celsius to Fahrenheit.

    Args:
        celsius: Temperature in degrees Celsius (int or float).

    Returns:
        Temperature in degrees Fahrenheit (float).
    """
    return celsius * 9 / 5 + 32

print(celsius_to_fahrenheit(0))    # 32.0
print(celsius_to_fahrenheit(100))  # 212.0
help(celsius_to_fahrenheit)

# %% [markdown]
# ### 1.8 Variable Scope
#
# Variables created *inside* a function are **local** — invisible outside.

# %%
def compute():
    x = 42
    print(x)

compute()
# print(x)   # NameError — x does not exist here

# %% [markdown]
# Variables created *outside* any function are **global** and can be *read*
# inside a function.  Best practice: pass values as arguments instead of
# relying on globals — it makes functions easier to test and reuse.

# %%
pi = 3.14159

def circle_area(radius):
    return pi * radius ** 2

print(circle_area(5))

# %% [markdown]
# ### 1.9 Multiple Return Values

# %%
def min_max(numbers):
    """Return (minimum, maximum) of a sequence."""
    return min(numbers), max(numbers)

low, high = min_max([3, 1, 4, 1, 5, 9, 2, 6])
print(f"Min: {low}, Max: {high}")

# %% [markdown]
# The comma creates a **tuple** — we'll cover tuples in depth in Week 4.

# %% [markdown]
# ---
# ## Part 2 — Strings in Depth
#
# You already know string basics.  Now let's look at the rich set of
# operations strings support.

# %% [markdown]
# ### 2.1 Indexing and Slicing

# %%
s = "Hello, World!"

print(s[0])     # H       — first character
print(s[-1])    # !       — last character
print(s[7:12])  # World   — characters 7 through 11
print(s[:5])    # Hello   — from the start up to (not including) 5
print(s[7:])    # World!  — from 7 to the end
print(s[::2])   # every second character

# %% [markdown]
# Strings are **immutable** — you cannot change a character in place.
#
# ```python
# s[0] = "h"   # TypeError
# ```
#
# Instead, build a new string.

# %% [markdown]
# ### 2.2 Common String Methods

# %%
text = "  Hello, World!  "

print(text.strip())          # remove leading/trailing whitespace
print(text.lower())          # all lowercase
print(text.upper())          # all uppercase
print(text.replace("World", "Python"))  # substitute

# %%
sentence = "one two three four"
words = sentence.split()          # split on whitespace → list
print(words)

csv_line = "Alice,30,Engineer"
fields = csv_line.split(",")      # split on a specific delimiter
print(fields)

# %%
# join is the inverse of split
parts = ["2026", "05", "27"]
date_str = "-".join(parts)
print(date_str)   # 2026-05-27

# %%
filename = "report_2026.txt"
print(filename.startswith("report"))   # True
print(filename.endswith(".txt"))        # True
print(filename.find("2026"))           # index where substring starts (or -1)
print("2026" in filename)              # True — membership test

# %% [markdown]
# ### 2.3 f-strings (review + more)

# %%
name = "Alice"
score = 92.5

# Basic interpolation
print(f"Name: {name}, Score: {score}")

# Format specifiers
print(f"Score: {score:.1f}%")       # one decimal place
print(f"Score: {score:06.2f}")      # zero-padded, 6 wide, 2 decimal places
print(f"{'centered':^20}")          # center in 20 chars
print(f"{'left':<20}|")             # left-align
print(f"{'right':>20}|")            # right-align

# %% [markdown]
# ### 2.4 Multi-line Strings

# %%
poem = """Roses are red,
Violets are blue,
Python is great,
And so are you."""

print(poem)
print(poem.count("\n"))   # 3 newlines → 4 lines

# %% [markdown]
# ---
# ## Part 3 — Dictionaries
#
# A **dictionary** maps *keys* to *values*.
# Think of it like a real dictionary: look up a word (key) to get its
# definition (value).

# %% [markdown]
# ### 3.1 Creating a Dictionary

# %%
# Literal syntax: {key: value, ...}
student = {
    "name": "Alice",
    "age": 20,
    "major": "Computer Science",
}

print(student)
print(type(student))

# %% [markdown]
# Keys can be any **immutable** type (strings, numbers, tuples).
# Values can be anything — even other dicts or lists.

# %% [markdown]
# ### 3.2 Accessing and Modifying Values

# %%
print(student["name"])    # Alice
print(student["age"])     # 20

# Add a new key
student["gpa"] = 3.8

# Update an existing key
student["age"] = 21

print(student)

# %% [markdown]
# Accessing a key that doesn't exist raises `KeyError`.
# Use `.get()` for a safe lookup with an optional default.

# %%
print(student.get("email"))           # None
print(student.get("email", "n/a"))    # n/a

# %% [markdown]
# ### 3.3 Checking Membership

# %%
print("name" in student)      # True
print("email" in student)     # False

# %% [markdown]
# ### 3.4 Removing Keys

# %%
del student["gpa"]
removed = student.pop("major")   # removes and returns the value
print(removed)
print(student)

# %% [markdown]
# ### 3.5 Iterating Over a Dictionary

# %%
scores = {"Alice": 92, "Bob": 85, "Carol": 78}

# Keys only (default)
for name in scores:
    print(name)

# %%
# Values only
for score in scores.values():
    print(score)

# %%
# Key-value pairs
for name, score in scores.items():
    print(f"{name}: {score}")

# %% [markdown]
# ### 3.6 Useful Dictionary Patterns

# %%
# Build a frequency count
text = "hello world"
freq = {}
for ch in text:
    freq[ch] = freq.get(ch, 0) + 1

print(freq)

# %%
# Dict comprehension
squares = {n: n**2 for n in range(1, 6)}
print(squares)   # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# %% [markdown]
# ---
# ## Part 4 — Basic File I/O
#
# Programs often need to read data from files or save results.
# Python makes this straightforward with the built-in `open()` function.

# %% [markdown]
# ### 4.1 Writing to a File

# %%
# open(path, mode) — "w" creates/overwrites, "a" appends, "r" reads
with open("sample.txt", "w") as f:
    f.write("Line 1\n")
    f.write("Line 2\n")
    f.write("Line 3\n")

# The `with` block automatically closes the file when it exits —
# even if an error occurs. Always prefer `with` over manual f.close().

# %% [markdown]
# ### 4.2 Reading an Entire File

# %%
with open("sample.txt", "r") as f:
    contents = f.read()

print(contents)
print(repr(contents))   # show the \n characters explicitly

# %% [markdown]
# ### 4.3 Reading Line by Line

# %%
with open("sample.txt", "r") as f:
    for line in f:
        print(line.strip())   # strip() removes the trailing newline

# %% [markdown]
# ### 4.4 Reading All Lines into a List

# %%
with open("sample.txt", "r") as f:
    lines = f.readlines()

print(lines)           # list of strings, each ending with \n
print(len(lines))      # 3

# %% [markdown]
# ### 4.5 Appending to a File

# %%
with open("sample.txt", "a") as f:
    f.write("Line 4\n")

with open("sample.txt") as f:   # "r" is the default mode
    print(f.read())

# %% [markdown]
# ### 4.6 A Practical Pattern: read → process → write

# %%
# Count words in the file and write the result to a new file
with open("sample.txt") as f:
    text = f.read()

word_count = len(text.split())

with open("summary.txt", "w") as f:
    f.write(f"Word count: {word_count}\n")

with open("summary.txt") as f:
    print(f.read())

# %% [markdown]
# ---
# ## Part 5 — A First Look at Objects
#
# You've been using objects all along without realising it.
# In Python, *everything* is an object — strings, lists, dicts, files.
# An **object** bundles data (*attributes*) and behaviour (*methods*)
# together under one name.
#
# We'll build our own objects in Week 6.  For now, let's notice the pattern
# by exploring a few objects from the **standard library**.

# %% [markdown]
# ### 5.1 The Pattern: `object.method()`
#
# Every time you write `some_string.upper()` or `my_list.append(x)`,
# you are calling a **method** — a function that belongs to an object.
#
# ```python
# "hello".upper()    # str object, upper method
# [1,2].append(3)    # list object, append method
# my_dict.items()    # dict object, items method
# ```

# %% [markdown]
# ### 5.2 `datetime` — dates and times

# %%
from datetime import date, datetime

today = date.today()            # calling a method on the class itself
print(today)                    # 2026-05-27
print(today.year)               # attribute: no parentheses
print(today.month)
print(today.strftime("%B %d, %Y"))  # format as string

# %%
now = datetime.now()
print(now)
print(now.strftime("%H:%M:%S"))

# %%
birthday = date(2000, 6, 15)
age_days = today - birthday       # subtraction returns a timedelta object
print(age_days.days, "days old")

# %% [markdown]
# Notice: `today`, `birthday`, `now` are all **objects**.
# They have *attributes* (`.year`, `.month`, `.days`) and
# *methods* (`.strftime()`, `.today()`).

# %% [markdown]
# ### 5.3 `pathlib.Path` — file paths as objects

# %%
from pathlib import Path

p = Path("sample.txt")
print(p.exists())       # True/False
print(p.name)           # sample.txt
print(p.suffix)         # .txt
print(p.stem)           # sample
print(p.stat().st_size) # file size in bytes

# %% [markdown]
# `pathlib.Path` objects let you work with file paths in a clean,
# cross-platform way.  The `/` operator even builds paths:

# %%
folder = Path(".")
notebook = folder / "sample.txt"
print(notebook)

# %% [markdown]
# ### 5.4 `collections.Counter`

# %%
from collections import Counter

words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
counts = Counter(words)
print(counts)
print(counts["apple"])           # 3
print(counts.most_common(2))     # top 2

# %% [markdown]
# `Counter` is a dict subclass — all dict operations work on it.
# Week 6 will show you how to build your own classes like these.

# %% [markdown]
# ---
# ## Summary
#
# | Topic | Key ideas |
# |---|---|
# | Functions | `def`, parameters, `return`, defaults, kwargs, scope |
# | Strings | Indexing/slicing, `.split()`, `.join()`, `.strip()`, f-strings |
# | Dictionaries | `{k: v}`, access by key, `.get()`, `.items()`, comprehensions |
# | File I/O | `open()`, `with` block, `"r"/"w"/"a"` modes, `.read()`, iteration |
# | Objects | `object.method()` pattern; `datetime`, `Path`, `Counter` as examples |
#
# **Key takeaways:**
# - Functions are the primary tool for avoiding repeated code.
# - Strings are immutable; use methods to build new strings.
# - Dictionaries give you fast key-based lookup — the right tool when
#   you need to associate names with values.
# - Always use `with` when opening files.
# - Objects bundle data and behaviour; you've been using them all along.

# %% [markdown]
# ---
# ## Practice Problems

# %% [markdown]
# **Problem 1.** Write a function `word_lengths(sentence)` that takes a string
# and returns a dictionary mapping each word to its length.
#
# Example: `word_lengths("hi there bob")` → `{"hi": 2, "there": 5, "bob": 3}`

# %%
# Your code here


# %% [markdown]
# **Problem 2.** Write a function `most_frequent_char(s)` that returns the
# character that appears most often in the string `s` (ignoring spaces).
# If there is a tie, returning any of the tied characters is fine.

# %%
# Your code here


# %% [markdown]
# **Problem 3.** Write a function `read_and_count(filename)` that opens the
# file at `filename`, reads its contents, and returns a dictionary with two
# keys: `"lines"` (number of lines) and `"words"` (number of words).

# %%
# Your code here


# %% [markdown]
# **Problem 4.** Using `datetime.date`, write a function `days_until(month, day)`
# that returns how many days until the next occurrence of that month/day.
# For example, if today is May 27 2026, `days_until(6, 15)` should return 19.

# %%
# Your code here
