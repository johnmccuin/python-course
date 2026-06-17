# %% [markdown]
# # Week 4 — Files, Modules, and Handling Problems
#
# This week we cover the tools that let programs work with the outside world
# and keep running when something goes wrong:
#
# 1. Files — reading and writing data that outlives your program
# 2. Modules and imports — reusing code across files
# 3. Error handling — catching exceptions gracefully
# 4. Tracebacks and debugging — reading errors and finding bugs
# 5. Assertions — verifying that your code does what you think

# %% [markdown]
# ---
# ## Part 1 — Files
#
# Everything you've stored so far disappears when the program ends.
# **Files** let a program save results and read data back later.
# Python makes this straightforward with the built-in `open()` function.

# %% [markdown]
# ### 1.1 Writing to a File

# %%
# open(path, mode) — "w" creates/overwrites, "a" appends, "r" reads
with open("sample.txt", "w") as f:
    f.write("Line 1\n")     # \n is the newline character — without it, no line break
    f.write("Line 2\n")
    f.write("Line 3\n")

# The `with` block automatically closes the file when it exits —
# even if an error occurs. Always prefer `with` over a manual f.close().

# %% [markdown]
# ### 1.2 Reading an Entire File
#
# `.read()` returns the whole file as one string.

# %%
with open("sample.txt", "r") as f:
    contents = f.read()

print(contents)
print(repr(contents))   # repr shows the \n characters explicitly

# %% [markdown]
# ### 1.3 Reading Line by Line
#
# Looping over a file gives you one line at a time — the memory-friendly way
# to handle large files.  Each line keeps its trailing `\n`, so `.strip()` it.

# %%
with open("sample.txt", "r") as f:
    for line in f:
        print(line.strip())   # strip() removes the trailing newline

# %% [markdown]
# ### 1.4 Reading All Lines into a List

# %%
with open("sample.txt", "r") as f:
    lines = f.readlines()

print(lines)           # list of strings, each ending with \n
print(len(lines))      # 3

# %% [markdown]
# ### 1.5 Appending to a File
#
# `"w"` stands for write and erases the file first and writes it anew.
#
# `"a"` stands for append and keeps what's there and adds to the end.
#
# `"r"` stands for read and allows you to read but not modify the file.

# %%
with open("sample.txt", "a") as f:
    f.write("Line 4\n")

with open("sample.txt") as f:   # "r" is the default mode
    print(f.read())

# %% [markdown]
# ### 1.6 A Practical Pattern: read → process → write
#
# Most file programs follow this shape: read input, compute something, write
# output.  Here we count the words in one file and save the count to another.

# %%
with open("sample.txt") as f:
    text = f.read()

words = text.split()
print(words)
word_count = len(words)

with open("summary.txt", "w") as f:
    f.write(f"Word count: {word_count}\n")

with open("summary.txt") as f:
    print(f.read())

# %% [markdown]
# ### Now you try

# %% [markdown]
# **Exercise 1.1.** Write three of your favourite foods to a file called
# `foods.txt`, one per line.  Then open the file and print its contents.

# %%
# Your code here

# %% [markdown]
# **Exercise 1.2.** Read `foods.txt` back line by line and print each food with
# a number in front, like `1. pizza`.  (Hint: keep a counter, or use
# `enumerate`.)

# %%
# Your code here

# %% [markdown]
# **Exercise 1.3.** Append one more food to `foods.txt` using `"a"` mode, then
# read the whole file again to confirm it now has four lines.

# %%
# Your code here

# %% [markdown]
# ---
# ## Part 2 — Modules and Imports
#
# A **module** is just a Python file that you can load into another file.
# Python ships with a huge **standard library** of modules — no installation
# needed.  Third-party modules (like `requests`) are installed with `pip`.

# %% [markdown]
# ### 2.1 Importing a Module
#
# `import math` loads the entire `math` module.  Access its contents with
# the dot: `math.sqrt(9)`.

# %%
import math

print(math.sqrt(16))    # 4.0
print(math.pi)          # 3.14159…
print(math.floor(3.7))  # 3
print(math.ceil(3.2))   # 4
print(math.e)

# %% [markdown]
# ### 2.2 Importing Specific Names
#
# `from module import name` brings just one name into scope — no dot needed.

# %%
from math import sqrt, pi

print(sqrt(25))   # 5.0
print(pi)         # 3.14159…
math.e                  # not in scope if entire package or math.e has not been previously loaded

# %% [markdown]
# ### 2.3 Aliases
#
# Long module names can be aliased with `as`.  In this way, you don't have to type the full name of the package.

# %%
import random as rnd
import math as m
import tensorflow as tf  # could type tf instead of full package name tensorflow

print(rnd.randint(1, 6))    # instead of random.randint, simulated die roll
print(random.randint(1,6))
print(m.e)
print(math.e)
print(rnd.choice(["heads", "tails"]))  # instead of random.choice

# %% [markdown]
# ### 2.4 Useful Standard-Library Modules
#
# A quick tour of modules you'll reach for often.

# %%
import os

print(os.getcwd())           # current working directory
print(os.path.exists("sample.txt"))  # True — we wrote it in Part 1

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
# ### 2.5 Writing Your Own Module
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
# This is exactly how the homework loads its `checks` module.

# %% [markdown]
# ### Now you try

# %% [markdown]
# **Exercise 2.1.** Import the `math` module and print the value of `math.e`
# (Euler's number).  Then use `math.log` to compute the natural log of `math.e`
# — it should be 1.0.

# %%
# Your code here

# %% [markdown]
# **Exercise 2.2.** Use `random.randint` to simulate rolling two six-sided
# dice.  Print both values and their sum.

# %%
# Your code here


# %% [markdown]
# **Exercise 2.3.** Use `os.path.exists` to check whether the file `"foods.txt"`
# you made in Part 1 exists in the current directory.  Print a message saying
# whether it was found or not.

# %%
# Your code here


# %% [markdown]
# ---
# ## Part 3 — Error Handling
#
# When something goes wrong at runtime Python raises an **exception**.
# Without handling it, the program crashes.  `try / except` lets you catch
# exceptions and decide what to do instead.

# %% [markdown]
# ### 3.1 What an Unhandled Exception Looks Like

# %%
# Uncomment to see the crash — then re-comment before moving on
# int("abc")

# %% [markdown]
# ### 3.2 Basic try / except

# %%
try:
    #value = "abc"
    value = int(input("Enter an integer: "))
except ValueError:
    print("That's not a valid integer.")
    value = 0
print(value)

# %% [markdown]
# The `except` block only runs if the specified exception type is raised.
# The program continues normally after the `try / except` block.

# %% [markdown]
# ### 3.3 Catching the Exception Object
#
# Add `as e` to inspect the error message.

# %%
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Caught an error: {e}")

# %% [markdown]
# ### 3.4 A Natural Pair: Files That Might Not Exist
#
# Opening a missing file raises `FileNotFoundError`.  This is the most common
# place a beginner's file program crashes — and `try / except` is the fix.

# %%
try:
    with open("does_not_exist.txt") as f:
        print(f.read())
except FileNotFoundError as e:
    #print(f"ERROR {e}")
    print("That file isn't here — check the name and try again.")

# %% [markdown]
# ### 3.5 Multiple except Clauses
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
# ### 3.6 The else and finally Clauses
#
# - `else` runs only if **no** exception was raised.
# - `finally` **always** runs — use it for cleanup (closing files, etc.).

# %%
try:
    number = int("abc")
except ValueError:
    print("Input must be convertible to an integer.")
else:
    print(f"Parsed successfully: {number}")   # else gets skipped since exception was raised
finally:
    print("Done — this always runs.")

# %%
try:
    number = int("4")
except ValueError:
    print("Input must be convertible to an integer.")
else:
    print(f"Parsed successfully: {number}")   # no exception, else block is run
finally:
    print("Done — this always runs.")


# %% [markdown]
# ### 3.7 Raising Exceptions
#
# Use `raise` to signal that something went wrong in your own code.

# %%
def celsius_to_fahrenheit(c):
    if c < -273.15:
        raise ValueError(f"{c} is below absolute zero.")
    return c * 9 / 5 + 32

print(celsius_to_fahrenheit(100))   # 212.0

#print(celsius_to_fahrenheit(-300))   # this will cause error because not in try block
try:
    print(celsius_to_fahrenheit(-300))
except ValueError as e:
    print(e)

# %% [markdown]
# ### 3.8 Common Exception Types
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
# **Exercise 3.1.** Write a function `safe_index(lst, i)` that returns
# `lst[i]` if `i` is a valid index, or the string `"index out of range"`
# if it is not.  Test it with a valid and an invalid index.

# %%
# Your code here


# %% [markdown]
# **Exercise 3.2.** Write a function `read_int(prompt)` that uses `input()`
# to ask the user for an integer.  If the user types something that isn't
# a valid integer, print `"That was not an integer. Please enter an integer."` and return `None`.
# Otherwise return the integer.

# %%
# Your code here

# %% [markdown]
# **Exercise 3.3.** Write a function `safe_open(filename)` that tries to open
# and return the contents of `filename`.  If the file doesn't exist, return
# the string `"File not found."` instead of crashing.  Test it on `sample.txt`
# (exists) and on a name that doesn't.

# %%
# Your code here


# %% [markdown]
# ---
# ## Part 4 — Tracebacks and Debugging Strategies
#
# A **traceback** is Python's crash report.  Learning to read it quickly is
# one of the most valuable debugging skills you can develop.

# %% [markdown]
# ### 4.1 Anatomy of a Traceback
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
print(process([1,2,3]))
print(process([1, 2, "three"]))   # uncomment to see the traceback

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
# ### 4.2 Common Bugs and How They Look

# %%
# Bug 1: Off-by-one in a loop
items = [10, 20, 30]
for i in range(len(items) + 1):   # IndexError on the last iteration
    print(items[i])

# %% [markdown]
# **Notice:** the error is `IndexError: list index out of range`.
# The range is one too long.

# %%
# Bug 2: Using = instead of == in a condition
x = 5
if x = 5:           # SyntaxError — caught before the program runs
    print("five")

if x == 5:
    print("five")

# %% [markdown]
# **Notice:** `SyntaxError` means Python couldn't even parse the code.
# Check for missing colons, mismatched parentheses, `=` vs `==`.

# %%
# Bug 3: Calling a function before defining it
print(greet("Alice"))   # NameError — greet isn't defined yet

def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))

# %% [markdown]
# ### 4.3 Debugging with print()
#
# The simplest debugger: insert `print()` calls to inspect state.

# %%
def find_first_negative(numbers):
    for i, n in enumerate(numbers):
        #print(f"  checking index {i}: {n}")   # debug print
        if n < 0:  # starting with error, <= instead of <
            return i, n
    return -1

index, number = find_first_negative([3, 7, 0, -2, 5])
print(f"First negative at index: {index} for number {number}")

# %% [markdown]
# Remove debug prints before committing code — or replace them with
# `logging` statements (a topic for a more advanced course).

# %% [markdown]
# ### 4.4 Narrowing Down a Bug
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
# **Exercise 4.1.** The function below has a bug.  Run it, read the traceback,
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

print(average([3, 4]))   # uncomment to see the error, then fix the function above

# %% [markdown]
# **Exercise 4.2.** The loop below is supposed to print the squares of 1–5,
# but it has an error.  Find and fix it.

# %%
print("The squares of 1-5 are as follows:")
for i in range(1, 5):
    print(i ** 2)

# %% [markdown]
# **Exercise 4.3.** Add two `print()` debug statements to the function below
# to trace the value of `count` on each iteration, then run it to confirm
# it counts correctly.

# %%
def count_evens(numbers):
    count = 0
    for n in numbers:
        if n % 2 == 0:
            count += 1
    return count

print(count_evens([11, 22, 33, 44, 55, 66]))

# %% [markdown]
# ---
# ## Part 5 — Assertions
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
# ### 5.1 Basic Assertions

# %%
x = 4.2
assert x > 0, "x must be positive"
assert isinstance(x, int), "x must be an integer"
print("Both assertions passed.")

# %% [markdown]
# ### 5.2 Assertions as Executable Documentation
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
# ### 5.3 Checking Function Inputs

# %%
def bmi(weight_kg, height_m):
    assert weight_kg > 0, f"weight must be positive, got {weight_kg}"
    assert height_m > 0, f"height must be positive, got {height_m}"
    return weight_kg / height_m ** 2

# Can try not inside try block
# print(bmi(70, 1.75))   # 22.86
# print(bmi(-5, 1.75))

# Can try with validated input
try:
    weight_kg = float(input("Enter your weight in kg: "))
    height_m = float(input("Enter your height in m: "))
except ValueError as e:
    print(f"Invalid input: {e}")

# can try bmi inside try block
try:
    print(bmi(weight_kg, height_m))
except AssertionError as e:
    print(f"AssertionError: {e}")

# try:
#     print(bmi(-5, 1.75))
# except AssertionError as e:
#     print(f"AssertionError: {e}")

# %% [markdown]
# ### 5.4 Checking Function Outputs
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

print(clamp(15, 10, 0))  # assert raises error and crashes since not in try
try:
    print(clamp(15, 10, 0))
except AssertionError as e:
    print(f"AssertionError: {e}")

# %% [markdown]
# ### 5.5 Assertions vs. Exceptions — When to Use Which
#
# | Situation | Use |
# |---|---|
# | Programmer logic error (should never happen) | `assert` |
# | User/external input that might be wrong | `raise ValueError` / `try-except` |
# | Cleanup regardless of success or failure | `finally` |
#
# Assertions are not a substitute for input validation — they can be
# disabled globally with `python -O` (optimize flag).  Use `raise` for
# anything a user could trigger.  (Assertions will come back in Week 7 as the
# foundation of *testing* — checking that code does what you claim.)

# %% [markdown]
# ### Now you try

# %% [markdown]
# **Exercise 5.1.** Write a function `rectangle_area(width, height)` that
# returns `width * height`.  Add assertions to verify that both arguments
# are positive numbers before computing the area.

# %%
# Your code here

# %% [markdown]
# **Exercise 5.2.** Write a function `first_and_last(lst)` that returns a
# tuple `(lst[0], lst[-1])`.  Add an assertion that `lst` is not empty
# before accessing those indices.

# %%
# Your code here


# %% [markdown]
# **Exercise 5.3.** The function below computes a letter grade from a
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

try:
    print(letter_grade(85))
except AssertionError as e:
    print(f"AssertionError: {e}")

try:
    print(letter_grade(110))
except AssertionError as e:
    print(f"AssertionError: {e}")
