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
# 6. Tuples
# 7. A first look at objects (foreshadowing Week 5)

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
# Functions solve this: **write the logic once, reuse it everywhere.**

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
# def function_name (parameter list)
#     block of code that is executed to perform the function's task
#     return variable_or_expression
# ```
# * **`def`** is a keyword that starts the function definition
# * The function name should be descriptive of what the function does
# * The parameter list is the set of variables which receive the values that will be used by the function
# * A function can return a value or several values. **`return`** is the keyword that allows a function to return the value of one or more a variables or expressions.
#

# %% [markdown]
# ### 1.3 Parameters and Arguments
#
# A function can have zero, one, or many parameters.

# %%
def say_hello():
    print("Hello, world!")

say_hello()

# %%
def add(a, b):  # a and b are parameters
    return a + b

print(add(3, 4))  # 3 and 4 are the arguments
print(add(10, -2))  # 10 and -2 are the arguments
x = 5
y = 7
print(add(x, y))  # x and y are the arguments
print(add("bob", "cindy"))
print (add(5.7,3.4))
print (add(5.7,3))
# print (add("cindy",5.67))

# %% [markdown]
# **TERMINOLOGY**
#
# **Parameter** = the name inside `def` (the placeholder).
# **Argument** = the actual value passed when calling.

# %% [markdown]
# ### 1.4 Return Values
#
# `print` shows output on screen but the result is gone.
# `return` sends a value *back* to the caller so it can be stored or used.

# %%
def square(n):
    print(n * n)

square(5)  # value computed by function is lost

def square(n):
    return n * n  # value computed by function is returned

result = square(5)   # value computed by function is stored
print(result)          # 25
print(square(7) + 1)   # 50  # value computed by function is used

# %% [markdown]
# If a function has no `return` statement it automatically returns `None`.

# %%
def greet_no_return(name):
    print(f"Hello, {name}!")

value = greet_no_return("Dana")
print(value)   # None was returned since function had no return statement

# %% [markdown]
# ### 1.5 Default Parameters

# %% [markdown]
# Default values can be used for parameters to establish standard behavior.

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
def describe_pet(animal, name="Unnamed"):
    print(f"I have a {animal} named {name}.")

describe_pet("dog", "Rex")                    # positional
describe_pet(name="Whiskers", animal="cat")   # keyword — any order
describe_pet("hamster", name="Nibbles")       # mix

# %% [markdown]
# ### 1.7 Docstrings

# %% [markdown]
# A docstring is a comment block that describes the functions purpose, arguments (inputs), and returns (outputs).

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
# Variables created *inside* a function are **local** to the function — invisible outside.

# %%
def compute():
    x22 = 42
    print(x22)

compute()
print(x22)   # NameError — x22 does not exist here

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
# Inside a function, the value of local variables of the same name as global variables are used rather than the values of the global variables of the same name.

# %%
x42 = 5
def compute():
    x42 = 42
    print("inside", x42) # the local x (inside the function) is used instead of the global x (outside the function)

compute()
print("outside", x42)   # will print the value of x outside the function


# %% [markdown]
# ### 1.9 Multiple Return Values

# %%
def min_max(numbers):
    """Return (minimum, maximum) of a sequence."""
    return min(numbers), max(numbers)

low, high = min_max([3, 1, 4, 1, 5, 9, 2, 6])
print(f"Min: {low}, Max: {high}")
low = min_max([3, 1, 4, 1, 5, 9, 2, 6])[0] # specified that we wanted the first value passed
print(f"Min: {low}")
low = min_max([3, 1, 4, 1, 5, 9, 2, 6])  # if two variables are not listed, the entire tuple is saved in the variable
print(f"Max: {low}")

# %% [markdown]
# The comma creates a **tuple** — we'll cover tuples in depth in Part 4.

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

# %%
s[0]='h'

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
print(filename.find("2025"))           # index where substring starts (or -1)
print("2026" in filename)              # True — membership test
print("2025" in filename)              # False — membership test

# %% [markdown]
# ### 2.3 f-strings (review + more)

# %%
name = "Alice"
score = 92.536

# Basic interpolation
print(f"Name: {name}, Score: {score}")

# Format specifiers
print(f"Score: {score:.1f}%")       # one decimal place
print(f"Score: {score:06.2f}")      # zero-padded, 6 wide, 2 decimal places
print(f"{'centered':^20}")          # center in 20 chars
print("01234567890123456789")
print(f"{'left':<20}")             # left-align
print(f"{'right':>20}")            # right-align

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
# A **dictionary** is used to lump related data together in one data object.  It maps *keys* to *values*.
# Think of it like a real dictionary: look up a word (key) to get its
# definition (value).

# %% [markdown]
# ### 3.1 Creating a Dictionary

# %%
# Literal syntax: {key: value, ...}
student1 = {
    "name": "Alice",
    "age": 20,
    "major": "Computer Science",
}

student2 = {
    "name": "Bob",
    "age": 21,
    "major": "Mathematics",
}

print(student1)
print(student2)
print(type(student1))

# %% [markdown]
# Keys can be any **immutable** type (strings, numbers, tuples).
# Values can be anything — even other dicts or lists.

# %% [markdown]
# ### 3.2 Accessing and Modifying Values

# %%
print(student1["name"])    # Alice
print(student2["age"])     # 20

# Add a new key
student1["gpa"] = 3.8

# Update an existing key
student1["age"] = 23

print(student1)
print(student2)

# %% [markdown]
# Accessing a key that doesn't exist raises `KeyError`.
# Use `.get()` for a safe lookup with an optional default.

# %%
print(student1.get("email"))           # None
print(student1.get("email", "n/a"))    # n/a
#print(student1["email"])             # gives error because email doesn't exist as a key

# %% [markdown]
# ### 3.3 Checking Membership

# %%
print("name" in student1)      # True
print("email" in student1)     # False

# %% [markdown]
# ### 3.4 Removing Keys

# %%
print(student1)
del student1["gpa"]
print(student1)
removed = student1.pop("major")   # removes and returns the value
print(removed)
print(student1)

# %% [markdown]
# ### 3.5 Iterating Over a Dictionary

# %%
scores = {"Alice": 92, "Bob": 85, "Carol": 78}

# Keys only (default)
for x in scores:
    print(x)

# %%
# Values only
for x in scores.values():
    print(x)

# %%
# Key-value pairs
for x, y in scores.items():
    print(f"{x}: {y}")

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
# **Exercise 3.1.** Create a dictionary `book` holding a key "title", an "author", and a "year".
# Print a sentence using all three.

# %% [markdown]
# ---
# ## Part 4 — Tuples
#
# A **tuple** is an ordered collection like a list — but **immutable**: once
# created, you can't change, add, or remove items.  Use a tuple when a group of
# values belongs together and *shouldn't* change: a coordinate `(x, y)`, an
# RGB color `(255, 128, 0)`, a row from a spreadsheet.

# %% [markdown]
# ### 4.1 Creating Tuples

# %%
point = (3, 4)            # parentheses
rgb = 255, 128, 0          # parentheses are optional — the commas make the tuple
single = (42,)             # a one-item tuple needs a trailing comma
empty = ()

print(point, type(point))
print(rgb, type(rgb))
print(single, type(single))
print(empty, type(empty))

# %% [markdown]
# ### 4.2 Indexing Works Like Lists; Changing Does Not
#
# You read from a tuple exactly like a list — but assignment fails.

# %%
point = (3, 4)
print(point[0])    # 3
print(point[-1])   # 4
print(len(point))  # 2

point[0] = 99    # uncomment: TypeError — tuples are immutable

# %% [markdown]
# ### 4.3 Packing and Unpacking
#
# Listing values with commas **packs** them into a tuple.  Putting names on the
# left **unpacks** them back out — one name per item.  You met this already with
# `min_max` in Part 1.

# %%
person = ("Ada", 36, "London")   # pack
name, age, city = person          # unpack
print(name)
print(age)
print(city)

# %%
# A classic use: swap two variables in one line, no temp variable needed
a = 1
b = 2
a, b = b, a
print(a, b)   # 2 1   pattern works without temp

temp = a
a = b
b = temp
print (a,b)

a = b
b = a
print(a,b)  # pattern doesn't work without temp

# %% [markdown]
# ### 4.4 Returning Multiple Values Is Just a Tuple
#
# When a function returns several values separated by commas, it's returning one
# tuple — which the caller usually unpacks.

# %%
def divide(a, b):
    quotient = a // b
    remainder = a % b
    return quotient, remainder   # packs into a tuple

q, r = divide(17, 5)             # unpacks it
print(f"17 = {q} * 5 + {r}")     # 17 = 3 * 5 + 2

# %% [markdown]
# ### 4.5 Tuple or List — Which?
#
# | Use a **list** when… | Use a **tuple** when… |
# |---|---|
# | the collection will change (append, remove, sort) | the values are fixed and belong together |
# | items are "many of the same thing" | items are "one record with parts" |
# | e.g. a shopping list, scores to update | e.g. a coordinate, a returned pair |
#
# Because tuples can't change, Python also lets them be used as **dictionary
# keys** (lists can't be).  That's a detail for later — for now, remember:
# tuple = a fixed, ordered group of values.

# %% [markdown]
# ### Now you try

# %% [markdown]
# **Exercise 4.1.** Create a tuple `book` holding a title, an author, and a year.
# Unpack it into three variables and print a sentence using all three.

# %%
book = ("Harry Potter and the Sorcerer's Stone", "J.K. Rowling", 1997)
title, author, year = book
print(f"The book '{title}' by {author} was published in {year}.")


# %%
book = {"title": "Harry Potter and the Sorcerer's Stone", "author": "J.K. Rowling", "year": 1997}
print(f"The book '{book['title']}' by {book['author']} was published in {book['year']}.")


# %% [markdown]
# **Exercise 4.2.** Write a function `min_and_max(numbers)` that returns both the
# smallest and largest values as a tuple.  Call it and unpack the result into two
# variables `lo` and `hi`.

# %%
def min_and_max(numbers):
    return min(numbers), max(numbers)

def min_and_max(numbers):
    min = numbers[0]
    max = numbers[0]
    for num in numbers:
        if num < min:
            min = num
        if num > max:
            max = num
    return min, max

lo, hi = min_and_max([3, 1, 4, 1, 5, 9, 2, 6])
print(f"Min: {lo}, Max: {hi}")


# %% [markdown]
# **Exercise 4.3.** You have `start = "Monday"` and `end = "Friday"`.  Swap their
# values in a single line using tuple unpacking, then print both.

# %%
start = "Monday"
end = "Friday"
start, end = end, start
print(start, end)


# %% [markdown]
# ---
# ## Part 5 — A First Look at Objects
#
# You've been using objects all along without realising it.
# In Python, *everything* is an object — strings, lists, dicts, files.
# An **object** bundles data (*attributes*) and behavior (*methods*)
# together under one name.
#
# We'll build our own objects in **Week 5**.  For now, let's notice the pattern
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
print(today.strftime("%B %d, %Y"))  # method that returns a formatted string
print(today.day)
print(today.weekday())         # method, use parentheses

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
# *methods* (`.strftime()`, `.today()`, and `now()`).

# %% [markdown]
# ### 5.3 `pathlib.Path` — file paths as objects

# %%
from pathlib import Path

p = Path("report_2026.txt")
print(p.name)           # report_2026.txt
print(p.suffix)         # .txt   — attribute, no parentheses
print(p.stem)           # report_2026
print(p.exists())       # False  — we never created this file; it's just a path

# %% [markdown]
# A `Path` describes a location whether or not a file is actually there.
# `pathlib.Path` objects let you work with file paths in a clean,
# cross-platform way.  The `/` operator even builds paths:

# %%
folder = Path("data")
report = folder / "report_2026.txt"
print(report)           # data/report_2026.txt

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
# Week 5 will show you how to build your own classes like these.

# %% [markdown]
# ---
# ## Summary
#
# | Topic | Key ideas |
# |---|---|
# | Functions | `def`, parameters, `return`, defaults, kwargs, scope |
# | Strings | Indexing/slicing, `.split()`, `.join()`, `.strip()`, f-strings |
# | Dictionaries | `{k: v}`, access by key, `.get()`, `.items()`, comprehensions |
# | Tuples | Immutable ordered groups; packing/unpacking; multiple return values |
# | Objects | `object.method()` pattern; `datetime`, `Path`, `Counter` as examples |
#
# **Key takeaways:**
# - Functions are the primary tool for avoiding repeated code.
# - Strings are immutable; use methods to build new strings.
# - Dictionaries give you fast key-based lookup — the right tool when
#   you need to associate names with values.
# - Tuples are fixed, ordered groups; returning several values makes a tuple.
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
def word_lengths(sentence):
    words = sentence.split()  # string is split into a list of each word
    length_dict = {}  # create an empty dictionary that will hold our dictionary mapping word lengths
    for word in words:
        length_dict[word] = len(word)   # each key is a word in the list, with the value = the length of the word
    return length_dict

word_lengths("hi there bob")


# %% [markdown]
# **Problem 2.** Write a function `most_frequent_char(s)` that returns the
# character that appears most often in the string `s` (ignoring spaces).
# If there is a tie, returning any of the tied characters is fine.

# %%
# Your code here
def most_frequent_char(s):
    # start to process characters
    char_count = {}  #make empty dictionary to hold my character count
    for char in s:
        if char == " ":  # skip whitespace
            # print("skipping whitespace")  # a print statement for demonstration and testing
            continue
        elif char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
        #print(char_count)  # a print statement for demonstration and testing
    return max(char_count, key=char_count.get)

print(most_frequent_char(" Mi ssiss  ip  pi "))
print(most_frequent_char(" Mi ssiss  ip  pi s"))


# %% [markdown]
# **Problem 3.** Write a function `high_low(numbers)` that returns a **tuple**
# `(minimum, maximum)` of a list of numbers.  Call it and unpack the result into
# two variables.  Example: `high_low([3, 9, 1, 7])` → `(1, 9)`.

# %%
# Your code here
def high_low(numbers):
    return min(numbers), max(numbers)

lo, hi = high_low([3, 9, 1, -5, 0, 7])
print(f"Min: {lo}, Max: {hi}")


# %% [markdown]
# **Problem 4.** Using `datetime.date`, write a function `days_until(month, day)`
# that returns how many days until the next occurrence of that month/day.
# For example, if today is May 27 2026, `days_until(6, 15)` should return 19.

# %%
# Your code here
from datetime import date

def days_until(month, day):
    today = date.today()   # get today's date
    next_day = date(today.year, month, day)  # make a date object of the next date with a year of this year

    # adjust next year if needed (i.e. is the next occurrence in this year or next year?)
    if next_day < today:
        next_day = date(today.year + 1, month, day)

    return (next_day - today).days

print(days_until(date.today().month, date.today().day))  # testing with today's date
print(days_until(date.today().month, date.today().day-1))  # testing with one day before today's date
print(days_until(date.today().month, date.today().day+1))  # testing with one day after today's date
print(days_until(4, 15))
print(days_until(12, 25))


# %% [markdown]
# **Problem 5.** A food truck keeps its menu as a `{item: price}` dictionary.
# Write a function `affordable_items(menu, budget)` that **takes the menu
# dictionary** and a `budget`, and returns a **new** dictionary containing only
# the items whose price is **at most** `budget`.
#
# Example: `affordable_items({"taco": 3, "burrito": 8, "soda": 2}, 3)` →
# `{"taco": 3, "soda": 2}`.

# %%
# Your code here
def affordable_items(menu, budget):
    affordable_menu = {}   # create empty dictionary to hold the affordable items
    for item, price in menu.items():  # read the items (keys) and prices (values) from the menu dictionary
        if price <= budget:   # if the price is less than our budget, add the item to the affordable dictionary
            affordable_menu[item] = price
    return affordable_menu

print(affordable_items({"taco": 3, "burrito": 8, "soda": 2}, 3))
