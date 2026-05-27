# %% [markdown]
# # Week 1 — Homework (Reference Solution)
#
# **Instructor reference — do not distribute to students.**
#
# Running all cells top-to-bottom should score **7 / 7**.

# %%
# Setup — don't edit this cell
import urllib.request, pathlib, sys

GRADER_URL = (
    "https://raw.githubusercontent.com/johnmccuin/python-course/"
    "main/grader/grader.py"
)
dest = pathlib.Path("grader.py")

if not dest.exists():
    urllib.request.urlretrieve(GRADER_URL, dest)
    print(f"Downloaded grader.py ({dest.stat().st_size} bytes)")
else:
    print("grader.py already present — skipping download.")

if str(pathlib.Path(".").resolve()) not in sys.path:
    sys.path.insert(0, str(pathlib.Path(".").resolve()))

from grader import Grader
grader = Grader("Week 1 Homework")
print("Ready!")

# %% [markdown]
# ---
# ### Exercise 1: minutes_in_year
#
# Assign a variable named `minutes_in_year` to the total number of minutes
# in a non-leap year (365 days). Your answer should be an integer.

# %%
minutes_in_year = 365 * 24 * 60

# %%
def _check_ex1():
    if not isinstance(minutes_in_year, int):
        return "Your answer should be an integer, not a float or string."
    if minutes_in_year != 525600:
        return "Check your math — 365 days × 24 hours × 60 minutes."
    return True

grader.check("ex1_minutes_in_year", _check_ex1)

# %% [markdown]
# ---
# ### Exercise 2: greeting
#
# The variables `name` and `age` are already defined for you below. Create
# a variable `greeting` containing an f-string that reads exactly:
#
#     Hello Sam, you are 30 years old.
#
# (Include the comma, the space after it, and the period at the end.)

# %%
name = "Sam"
age = 30
greeting = f"Hello {name}, you are {age} years old."

# %%
def _check_ex2():
    if not isinstance(greeting, str):
        return "Your answer should be a string."
    if greeting != "Hello Sam, you are 30 years old.":
        if "," not in greeting:
            return "Check your punctuation — is the comma there?"
        if not greeting.endswith("."):
            return "Check your punctuation — is there a period at the end?"
        return "Your string doesn't match exactly. Compare character by character with the expected output."
    return True

grader.check("ex2_greeting", _check_ex2)

# %% [markdown]
# ---
# ### Exercise 3: is_even
#
# The variable `n` is defined below. Assign a variable `is_even` to `True`
# if `n` is an even number, `False` otherwise. Your code should work for
# any integer value of `n`, not just the one shown.

# %%
n = 14
is_even = (n % 2 == 0)

# %%
def _check_ex3():
    if is_even is not True:
        return "Use the modulo operator `%` to check divisibility by 2."
    return True

grader.check("ex3_is_even", _check_ex3)

# %% [markdown]
# ---
# ### Exercise 4: celsius_to_fahrenheit
#
# The variable `celsius` is defined below. Assign a variable `fahrenheit`
# to the temperature converted to Fahrenheit. The formula is:
#
#     F = C × 9/5 + 32

# %%
celsius = 25
fahrenheit = celsius * 9/5 + 32

# %%
def _check_ex4():
    if not isinstance(fahrenheit, (int, float)):
        return "Your answer should be a number."
    if abs(fahrenheit - 77.0) > 0.01:
        return "Check the formula: F = C × 9/5 + 32. With celsius = 25, fahrenheit should be 77."
    return True

grader.check("ex4_celsius_to_fahrenheit", _check_ex4)

# %% [markdown]
# ---
# ### Exercise 5: type_practice
#
# The variable `s` is defined below as the string `"42"`. Create a
# variable `as_number` that holds the integer value 42 (not the string).

# %%
s = "42"
as_number = int(s)

# %%
def _check_ex5():
    if isinstance(as_number, str):
        return "Your answer is still a string. Use int() to convert."
    if type(as_number) is float:
        return "Close — that's a float. We need an integer."
    if as_number != 42:
        return "Your value isn't 42. Make sure you're converting `s`, not using a different number."
    return True

grader.check("ex5_type_practice", _check_ex5)

# %% [markdown]
# ---
# ### Exercise 6: classify_number
#
# The variable `n` is defined below. Assign a variable `category` to one
# of these three strings: `"positive"`, `"negative"`, or `"zero"`,
# depending on the value of `n`. Your code should work for any value of n.

# %%
n = 7
if n > 0:
    category = "positive"
elif n < 0:
    category = "negative"
else:
    category = "zero"

# %%
def _check_ex6():
    if category not in ("positive", "negative", "zero"):
        return "Your answer should be one of: 'positive', 'negative', 'zero'. Check your spelling and capitalization."
    if category != "positive":
        return "For n=7, category should be 'positive'."
    return True

grader.check("ex6_classify_number", _check_ex6)

# %% [markdown]
# ---
# ### Exercise 7: fizz_or_buzz_lite
#
# The variable `n` is defined below. Assign a variable `result` based on
# these rules:
# - If `n` is divisible by both 3 and 5: `result = "both"`
# - If `n` is divisible by 3 (but not 5): `result = "fizz"`
# - If `n` is divisible by 5 (but not 3): `result = "buzz"`
# - Otherwise: `result = "neither"`

# %%
n = 15
if n % 15 == 0:
    result = "both"
elif n % 3 == 0:
    result = "fizz"
elif n % 5 == 0:
    result = "buzz"
else:
    result = "neither"

# %%
def _check_ex7():
    if result not in ("fizz", "buzz", "both", "neither"):
        return "Your answer should be one of: 'fizz', 'buzz', 'both', 'neither'."
    if result == "fizz":
        return "Check the order of your conditions. 15 is divisible by both 3 and 5 — make sure you handle that case first."
    if result != "both":
        return "For n=15, result should be 'both'."
    return True

grader.check("ex7_fizz_or_buzz_lite", _check_ex7)

# %% [markdown]
# ---
# ## Final Score

# %%
grader.report()
