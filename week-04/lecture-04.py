# %% [markdown]
# # Week 4 — Organizing Code and Handling Problems
#
# This week we cover four topics that make programs more reliable and
# easier to maintain:
#
# 1. Modules and imports — reusing code across files
# 2. Error handling — catching exceptions gracefully
# 3. Tracebacks and debugging — reading errors and finding bugs
# 4. Assertions — verifying that your code does what you think

# %% [markdown]
# ---
# ## Part 1 — Modules and Imports
#
# A **module** is just a Python file that you can load into another file.
# Python ships with a huge **standard library** of modules — no installation
# needed.  Third-party modules (like `requests`) are installed with `pip`.

# %% [markdown]
# ### 1.1 Importing a Module
#
# `import math` loads the entire `math` module.  Access its contents with
# the dot: `math.sqrt(9)`.

# %%
import math

print(math.sqrt(16))    # 4.0
print(math.pi)          # 3.14159…
print(math.floor(3.7))  # 3
print(math.ceil(3.2))   # 4

# %% [markdown]
# ### 1.2 Importing Specific Names
#
# `from module import name` brings just one name into scope — no dot needed.

# %%
from math import sqrt, pi

print(sqrt(25))   # 5.0
print(pi)         # 3.14159…

# %% [markdown]
# ### 1.3 Aliases
#
# Long module names can be aliased with `as`.

# %%
import random as rnd

print(rnd.randint(1, 6))    # simulated die roll
print(rnd.choice(["heads", "tails"]))

# %% [markdown]
# ### 1.4 Useful Standard-Library Modules
#
# A quick tour of modules you'll reach for often.

# %%
import os

print(os.getcwd())           # current working directory
print(os.path.exists("nonexistent.txt"))  # False

# %%
import sys

print(sys.version)   # Python version string

# %%
import random

numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)   # shuffles in-place
print(numbers)

sample = random.sample(range(100), 5)   # 5 unique random numbers 0–99
print(sample)

# %%
import string

print(string.ascii_lowercase)   # abcdefghijklmnopqrstuvwxyz
print(string.digits)            # 0123456789
print(string.punctuation)       # !"#$%&'()*+,...

# %% [markdown]
# ### 1.5 Writing Your Own Module
#
# Any `.py` file is a module.  If `helpers.py` lives in the same folder:
#
# ```python
# # helpers.py
# def greet(name):
#     return f"Hello, {name}!"
# ```
#
# ```python
# # main.py
# import helpers
# print(helpers.greet("Alice"))
# ```
#
# We'll use this pattern in the homework.

# %% [markdown]
# ### Now you try

# %% [markdown]
# **Exercise 1.1.** Import the `math` module and print the value of `math.e`
# (Euler's number).  Then use `math.log` to compute the natural log of `math.e`
# — it should be 1.0.

# %%
# Your code here

# %% [markdown]
# **Exercise 1.2.** Use `random.randint` to simulate rolling two six-sided
# dice.  Print both values and their sum.

# %%
# Your code here

# %% [markdown]
# **Exercise 1.3.** Use `os.path.exists` to check whether a file called
# `"lecture-04.py"` exists in the current directory.  Print a message saying
# whether it was found or not.

# %%
# Your code here

# %% [markdown]
# ---
# ## Part 2 — Error Handling
#
# When something goes wrong at runtime Python raises an **exception**.
# Without handling it, the program crashes.  `try / except` lets you catch
# exceptions and decide what to do instead.

# %% [markdown]
# ### 2.1 What an Unhandled Exception Looks Like

# %%
# Uncomment to see the crash — then re-comment before moving on
# int("abc")

# %% [markdown]
# ### 2.2 Basic try / except

# %%
try:
    value = int("abc")
except ValueError:
    print("That's not a valid integer.")

# %% [markdown]
# The `except` block only runs if the specified exception type is raised.
# The program continues normally after the `try / except` block.

# %% [markdown]
# ### 2.3 Catching the Exception Object
#
# Add `as e` to inspect the error message.

# %%
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Caught an error: {e}")

# %% [markdown]
# ### 2.4 Multiple except Clauses
#
# Handle different errors differently.

# %%
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero."
    except TypeError:
        return "Both arguments must be numbers."

print(safe_divide(10, 2))    # 5.0
print(safe_divide(10, 0))    # Cannot divide by zero.
print(safe_divide(10, "x"))  # Both arguments must be numbers.

# %% [markdown]
# ### 2.5 The else and finally Clauses
#
# - `else` runs only if **no** exception was raised.
# - `finally` **always** runs — use it for cleanup (closing files, etc.).

# %%
try:
    number = int("42")
except ValueError:
    print("Bad input.")
else:
    print(f"Parsed successfully: {number}")   # runs here
finally:
    print("Done — this always runs.")

# %% [markdown]
# ### 2.6 Raising Exceptions
#
# Use `raise` to signal that something went wrong in your own code.

# %%
def celsius_to_fahrenheit(c):
    if c < -273.15:
        raise ValueError(f"{c} is below absolute zero.")
    return c * 9 / 5 + 32

print(celsius_to_fahrenheit(100))   # 212.0

try:
    print(celsius_to_fahrenheit(-300))
except ValueError as e:
    print(e)

# %% [markdown]
# ### 2.7 Common Exception Types
#
# | Exception | When it occurs |
# |---|---|
# | `ValueError` | Right type, wrong value (`int("abc")`) |
# | `TypeError` | Wrong type (`"hi" + 5`) |
# | `ZeroDivisionError` | Division or modulo by zero |
# | `IndexError` | List index out of range |
# | `KeyError` | Dict key not found |
# | `FileNotFoundError` | `open()` on a missing file |
# | `AttributeError` | Object has no such attribute |

# %% [markdown]
# ### Now you try

# %% [markdown]
# **Exercise 2.1.** Write a function `safe_index(lst, i)` that returns
# `lst[i]` if `i` is a valid index, or the string `"index out of range"`
# if it is not.  Test it with a valid and an invalid index.

# %%
# Your code here

# %% [markdown]
# **Exercise 2.2.** Write a function `read_int(prompt)` that uses `input()`
# to ask the user for an integer.  If the user types something that isn't
# a valid integer, print `"Please enter a whole number."` and return `None`.
# Otherwise return the integer.

# %%
# Your code here

# %% [markdown]
# **Exercise 2.3.** Write a function `safe_open(filename)` that tries to open
# and return the contents of `filename`.  If the file doesn't exist, return
# the string `"File not found."` instead of crashing.

# %%
# Your code here

# %% [markdown]
# ---
# ## Part 3 — Tracebacks and Debugging Strategies
#
# A **traceback** is Python's crash report.  Learning to read it quickly is
# one of the most valuable debugging skills you can develop.

# %% [markdown]
# ### 3.1 Anatomy of a Traceback
#
# Run the cell below and study the output.

# %%
def double(x):
    return x * 2

def process(items):
    total = 0
    for item in items:
        total += double(item)
    return total

# process([1, 2, "three"])   # uncomment to see the traceback

# %% [markdown]
# A traceback reads **bottom-up**:
#
# ```
# Traceback (most recent call last):      ← always this header
#   File "...", line N, in <module>        ← outermost call
#     process([1, 2, "three"])
#   File "...", line N, in process         ← moves inward
#     total += double(item)
#   File "...", line N, in double          ← where it actually failed
#     return x * 2
# TypeError: can only concatenate str (not "int") to str   ← the error
# ```
#
# **Strategy:** jump to the *last* frame in your own code, not in library code.
# That's almost always where the bug lives.

# %% [markdown]
# ### 3.2 Common Bugs and How They Look

# %%
# Bug 1: Off-by-one in a loop
items = [10, 20, 30]
# for i in range(len(items) + 1):   # IndexError on the last iteration
#     print(items[i])

# %% [markdown]
# **Notice:** the error is `IndexError: list index out of range`.
# The range is one too long.

# %%
# Bug 2: Using = instead of == in a condition
x = 5
# if x = 5:           # SyntaxError — caught before the program runs
#     print("five")

if x == 5:
    print("five")

# %% [markdown]
# **Notice:** `SyntaxError` means Python couldn't even parse the code.
# Check for missing colons, mismatched parentheses, `=` vs `==`.

# %%
# Bug 3: Calling a function before defining it
# print(greet("Alice"))   # NameError — greet isn't defined yet

def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))

# %% [markdown]
# ### 3.3 Debugging with print()
#
# The simplest debugger: insert `print()` calls to inspect state.

# %%
def find_first_negative(numbers):
    for i, n in enumerate(numbers):
        print(f"  checking index {i}: {n}")   # debug print
        if n < 0:
            return i
    return -1

result = find_first_negative([3, 7, -2, 5])
print(f"First negative at index: {result}")

# %% [markdown]
# Remove debug prints before committing code — or replace them with
# `logging` statements (a topic for a more advanced course).

# %% [markdown]
# ### 3.4 Narrowing Down a Bug
#
# When a bug is hard to find, apply **binary search**:
# 1. Add a print halfway through the suspect code.
# 2. If the output is wrong, the bug is before that point.
# 3. Repeat, halving the search space each time.
#
# This sounds simple, but it reliably cuts debugging time in half.

# %% [markdown]
# ### Now you try

# %% [markdown]
# **Exercise 3.1.** The function below has a bug.  Run it, read the traceback,
# identify the problem, and fix it.
#
# ```python
# def average(numbers):
#     return sum(numbers) / len(numbers)
#
# print(average([]))
# ```

# %%
def average(numbers):
    return sum(numbers) / len(numbers)

# print(average([]))   # uncomment to see the error, then fix the function above

# %% [markdown]
# **Exercise 3.2.** The loop below is supposed to print the squares of 1–5,
# but it has an off-by-one error.  Find and fix it.

# %%
for i in range(1, 5):   # bug is here
    print(i ** 2)

# %% [markdown]
# **Exercise 3.3.** Add two `print()` debug statements to the function below
# to trace the value of `count` on each iteration, then run it to confirm
# it counts correctly.

# %%
def count_evens(numbers):
    count = 0
    for n in numbers:
        if n % 2 == 0:
            count += 1
    return count

print(count_evens([1, 2, 3, 4, 5, 6]))

# %% [markdown]
# ---
# ## Part 4 — Assertions
#
# An **assertion** is a sanity check you write directly in your code.
# It says: "At this point, this must be true — if it isn't, something is
# very wrong."
#
# ```python
# assert condition, "Optional message shown if assertion fails"
# ```
#
# If `condition` is `False`, Python raises `AssertionError` and stops.

# %% [markdown]
# ### 4.1 Basic Assertions

# %%
x = 42
assert x > 0, "x must be positive"
assert isinstance(x, int), "x must be an integer"
print("Both assertions passed.")

# %% [markdown]
# ### 4.2 Assertions as Executable Documentation
#
# An assertion tells the reader (and Python) what you *expect* to be true.
# Compare:
#
# ```python
# # Comment-only version:
# # radius is always positive here
# area = math.pi * radius ** 2
#
# # Assertion version:
# assert radius > 0, "radius must be positive"
# area = math.pi * radius ** 2
# ```
#
# The second version *verifies* the assumption instead of just stating it.

# %% [markdown]
# ### 4.3 Checking Function Inputs

# %%
def bmi(weight_kg, height_m):
    assert weight_kg > 0, f"weight must be positive, got {weight_kg}"
    assert height_m > 0, f"height must be positive, got {height_m}"
    return weight_kg / height_m ** 2

print(bmi(70, 1.75))   # 22.86

try:
    print(bmi(-5, 1.75))
except AssertionError as e:
    print(f"AssertionError: {e}")

# %% [markdown]
# ### 4.4 Checking Function Outputs
#
# You can also assert something about what a function *returns*.

# %%
def clamp(value, lo, hi):
    """Return value clamped to the range [lo, hi]."""
    result = max(lo, min(value, hi))
    assert lo <= result <= hi, "clamp produced an out-of-range result"
    return result

print(clamp(5, 0, 10))    # 5
print(clamp(-3, 0, 10))   # 0
print(clamp(15, 0, 10))   # 10

# %% [markdown]
# ### 4.5 Assertions vs. Exceptions — When to Use Which
#
# | Situation | Use |
# |---|---|
# | Programmer logic error (should never happen) | `assert` |
# | User/external input that might be wrong | `raise ValueError` / `try-except` |
# | Cleanup regardless of success or failure | `finally` |
#
# Assertions are not a substitute for input validation — they can be
# disabled globally with `python -O` (optimize flag).  Use `raise` for
# anything a user could trigger.

# %% [markdown]
# ### Now you try

# %% [markdown]
# **Exercise 4.1.** Write a function `rectangle_area(width, height)` that
# returns `width * height`.  Add assertions to verify that both arguments
# are positive numbers before computing the area.

# %%
# Your code here

# %% [markdown]
# **Exercise 4.2.** Write a function `first_and_last(lst)` that returns a
# tuple `(lst[0], lst[-1])`.  Add an assertion that `lst` is not empty
# before accessing those indices.

# %%
# Your code here

# %% [markdown]
# **Exercise 4.3.** The function below computes a letter grade from a
# percentage score.  Add an assertion that `score` is between 0 and 100
# (inclusive) before the grade is computed.

# %%
def letter_grade(score):
    # add your assertion here
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

print(letter_grade(85))

# try:
#     print(letter_grade(110))
# except AssertionError as e:
#     print(f"AssertionError: {e}")
