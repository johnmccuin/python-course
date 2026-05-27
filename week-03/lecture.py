# %% [markdown]
# # Week 3 — Functions
#
# Functions let you name a block of code so you can run it whenever you need it,
# without rewriting it every time.  This week we cover:
#
# 1. Defining and calling functions
# 2. Parameters and arguments
# 3. Return values
# 4. Default parameters
# 5. Keyword arguments
# 6. Docstrings
# 7. Variable scope
# 8. Multiple return values
# 9. Lambda functions

# %% [markdown]
# ## 1. Why Functions?
#
# Suppose we want to greet three different people.  Without functions:

# %%
print("Hello, Alice! Welcome.")
print("Hello, Bob! Welcome.")
print("Hello, Carol! Welcome.")

# %% [markdown]
# That works, but we wrote nearly the same line three times.
# If the greeting changes ("Hi" instead of "Hello"), we have to edit every line.
#
# Functions solve this: write the logic once, reuse it everywhere.

# %% [markdown]
# ## 2. Defining and Calling a Function
#
# Use the `def` keyword followed by the function name, parentheses, and a colon.
# The body must be indented.

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
#  |     └── function name (follows the same naming rules as variables)
#  └── keyword that starts the definition
# ```
#
# **Calling** the function means writing its name followed by parentheses
# with the actual value (the *argument*) you want to pass in.

# %% [markdown]
# ## 3. Parameters and Arguments
#
# A function can have zero, one, or many parameters.

# %%
def say_hello():
    print("Hello, world!")

say_hello()

# %%
def add(a, b):
    print(a + b)

add(3, 4)
add(10, -2)

# %% [markdown]
# **Parameter** = the name inside `def` (the placeholder).
# **Argument** = the actual value you pass when calling.

# %% [markdown]
# ## 4. Return Values
#
# `print` shows output on screen, but the result disappears.
# `return` sends a value *back* to whatever called the function,
# so you can store or use it.

# %%
def square(n):
    return n * n

result = square(5)
print(result)          # 25
print(square(7) + 1)   # 50

# %%
def add(a, b):
    return a + b

total = add(3, 4)
print(total)   # 7

# %% [markdown]
# If a function has no `return` statement (or just `return` with nothing after it),
# it returns `None` automatically.

# %%
def greet(name):
    print(f"Hello, {name}!")

value = greet("Dana")
print(value)   # None

# %% [markdown]
# ## 5. Default Parameters
#
# You can give a parameter a default value.
# If the caller does not supply that argument, the default is used.

# %%
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Alice")              # uses default greeting
greet("Bob", "Good morning")  # overrides the default

# %% [markdown]
# **Rule:** parameters with defaults must come *after* parameters without defaults.
#
# ```python
# def foo(a, b=10):    # OK
# def foo(a=10, b):    # SyntaxError
# ```

# %% [markdown]
# ## 6. Keyword Arguments
#
# When calling a function you can name the arguments explicitly.
# This makes calls easier to read and lets you supply them in any order.

# %%
def describe_pet(animal, name):
    print(f"I have a {animal} named {name}.")

describe_pet("dog", "Rex")                        # positional
describe_pet(name="Whiskers", animal="cat")       # keyword — order doesn't matter
describe_pet("hamster", name="Nibbles")           # mix: positional first, then keyword

# %% [markdown]
# ## 7. Docstrings
#
# A **docstring** is a string literal placed as the very first statement in a
# function body.  It documents what the function does.
# Use triple quotes so it can span multiple lines.

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

# Access the docstring with help():
help(celsius_to_fahrenheit)

# %% [markdown]
# ## 8. Variable Scope
#
# Variables created *inside* a function are **local** — they only exist
# while that function is running and cannot be seen outside.

# %%
def compute():
    x = 42        # local variable
    print(x)

compute()

# Uncomment the line below to see the error:
# print(x)   # NameError: name 'x' is not defined

# %% [markdown]
# Variables created *outside* any function are **global** and can be
# *read* inside a function.

# %%
pi = 3.14159   # global

def circle_area(radius):
    return pi * radius ** 2   # reads the global pi

print(circle_area(5))

# %% [markdown]
# **Best practice:** avoid relying on global variables inside functions.
# Pass values in as arguments instead — it makes functions easier to test
# and reuse.

# %% [markdown]
# ### Scope demo

# %%
message = "global"

def show():
    message = "local"   # new local variable; does NOT change the global
    print(message)

show()
print(message)   # still "global"

# %% [markdown]
# ## 9. Multiple Return Values
#
# Python lets a function return more than one value by separating them with commas.
# The result is a **tuple** (covered in depth in Week 4).

# %%
def min_max(numbers):
    """Return the minimum and maximum of a list."""
    return min(numbers), max(numbers)

low, high = min_max([3, 1, 4, 1, 5, 9, 2, 6])
print(f"Min: {low}, Max: {high}")

# %% [markdown]
# ## 10. Lambda Functions
#
# A **lambda** is a small, anonymous function written in a single expression.
# Use it when you need a short function just once — passing it to another
# function, for example.

# %%
# Regular function
def double(x):
    return x * 2

# Equivalent lambda
double_lambda = lambda x: x * 2

print(double(5))         # 10
print(double_lambda(5))  # 10

# %% [markdown]
# A common use: sorting by a custom key.

# %%
words = ["banana", "fig", "apple", "date", "kiwi"]

# Sort by word length
sorted_words = sorted(words, key=lambda w: len(w))
print(sorted_words)

# %% [markdown]
# **When to use lambda vs `def`:**
# - Use `lambda` for short, throwaway functions (one expression, no statements).
# - Use `def` when the function has a name you'll reuse, needs a docstring,
#   or contains more than one expression.

# %% [markdown]
# ## Summary
#
# | Concept | Syntax |
# |---|---|
# | Define a function | `def name(params):` |
# | Call a function | `name(args)` |
# | Return a value | `return value` |
# | Default parameter | `def f(x, y=0):` |
# | Keyword argument | `f(y=1, x=2)` |
# | Docstring | `"""Description."""` as first line of body |
# | Lambda | `lambda x: x * 2` |
#
# **Key takeaways:**
# - Functions are the primary tool for avoiding repeated code.
# - Always `return` a value when the caller needs the result; use `print` only
#   for output that a human should see.
# - Keep functions focused: one function, one job.

# %% [markdown]
# ## Practice Problems
#
# Try these before looking at any solutions.

# %% [markdown]
# **Problem 1.** Write a function `is_even(n)` that returns `True` if `n` is even
# and `False` otherwise.

# %%
# Your code here


# %% [markdown]
# **Problem 2.** Write a function `clamp(value, low, high)` that returns `value`
# clamped to the range `[low, high]`.
# - If `value < low`, return `low`.
# - If `value > high`, return `high`.
# - Otherwise return `value`.
#
# Examples: `clamp(5, 1, 10)` → `5`, `clamp(-3, 0, 100)` → `0`, `clamp(200, 0, 100)` → `100`

# %%
# Your code here


# %% [markdown]
# **Problem 3.** Write a function `fizzbuzz(n)` that returns:
# - `"FizzBuzz"` if `n` is divisible by both 3 and 5
# - `"Fizz"` if `n` is divisible by 3
# - `"Buzz"` if `n` is divisible by 5
# - The number itself (as a string) otherwise

# %%
# Your code here

