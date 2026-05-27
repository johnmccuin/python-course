# %% [markdown]
# # Week 1 — First Steps with Python
#
# Welcome! Tonight we'll get Python running and learn the building
# blocks of every program: values, variables, types, input/output,
# and making decisions.

# %% [markdown]
# ## ⚠️ Before you do anything else
#
# Click **File → Save a copy in Drive** at the top. Otherwise your
# work tonight won't be saved!

# %% [markdown]
# Click the cell below, then press **Shift+Enter** to run it.

# %%
print("hello, python")

# %% [markdown]
# ## Block 1: Expressions and Values
#
# Python can be used as a calculator. Let's see what it can do.

# %%
2 + 3

# %%
10 * 4

# %% [markdown]
# Notice: division always gives a decimal.

# %%
7 / 2

# %% [markdown]
# Integer division (`//` drops the decimal).

# %%
7 // 2

# %% [markdown]
# Modulo: the remainder after division.

# %%
7 % 2

# %%
"hello"

# %% [markdown]
# Strings can be added together.

# %%
"hello" + " " + "world"

# %% [markdown]
# Strings can be multiplied by numbers.

# %%
"ha" * 3

# %%
5 > 3

# %% [markdown]
# Double-equals (`==`) tests if two values are equal.
# Single-equals (`=`) is for assignment — we'll see that next.

# %%
5 == 5

# %%
5 == 6

# %% [markdown]
# ### Now you try

# %% [markdown]
# **Exercise 1.** Calculate how many minutes are in one week.

# %%
# Your code here

# %% [markdown]
# **Exercise 2.** Print your name three times in a row using `*`.

# %%
# Your code here

# %% [markdown]
# **Exercise 3.** Write a comparison with two different numbers
# that evaluates to `True`.

# %%
# Your code here

# %% [markdown]
# ## Block 2: Variables
#
# A variable is a name that holds a value. You can use the value
# later by referring to the name.

# %%
x = 5

# %% [markdown]
# Now we can use `x` in an expression.

# %%
x + 3

# %% [markdown]
# ### Reassignment
#
# We can change the value a variable holds. The right side runs
# first, then the result is stored in the variable.

# %% [markdown]
# Predict what `x` will be **before** you run the next cell.

# %%
x = x + 1

# %%
x

# %%
student_name = "Alex"
total_score = 92

print(student_name, "scored", total_score)

# %% [markdown]
# ### A note on names
#
# Variable names can have letters, digits, and underscores, but they
# can't start with a digit. Convention: lowercase with underscores
# between words.
#
# Good: `student_name`, `total_score`, `count`
# Not allowed: `1score`, `total-points`

# %% [markdown]
# ### Now you try

# %% [markdown]
# **Exercise 1.** Create a variable `age` set to your age, and a
# variable `name` set to your name. Then print a sentence using
# both — for now, use commas inside `print()`.

# %%
# Your code here

# %% [markdown]
# **Exercise 2a.** Start with `count = 0`. In the cell below,
# reassign `count` to itself plus 10. Predict the value before
# you run it.

# %%
count = 0
# Your code here

# %% [markdown]
# **Exercise 2b.** Now reassign `count` to itself times 2.
# Predict the value before you run it.

# %%
# Your code here

# %% [markdown]
# ## Block 3: Types, Input, and f-strings
#
# Every value in Python has a "type." So far we've seen numbers and
# strings — they behave differently, and mixing them up causes most
# beginner bugs.

# %%
type(5)

# %% [markdown]
# Numbers with a decimal are `float`; without are `int`.

# %%
type(5.0)

# %% [markdown]
# Watch carefully: this looks like a number but it's a string.

# %%
type("5")

# %%
type(True)

# %% [markdown]
# What do you think this will produce?

# %%
"5" + "3"

# %%
5 + 3

# %%
int("5")

# %%
str(5)

# %%
float("3.14")

# %% [markdown]
# Sometimes conversion fails — let's see what that looks like.

# %%
int("hello")

# %% [markdown]
# `input()` lets us ask the user for something. Run this cell
# and type a response when prompted.

# %%
name = input("What's your name? ")
print(name)

# %% [markdown]
# Here's a trap. We ask for an age expecting a number, but watch what we get.

# %%
age = input("Your age? ")
type(age)

# %% [markdown]
# Let's fix that — wrap `input()` in `int()` to convert right away.

# %%
age = int(input("Your age? "))
type(age)

# %% [markdown]
# The cleanest way to build a string with variables in it.

# %%
name = "Alex"
age = 25
f"Hello, {name}! You are {age} years old."

# %% [markdown]
# ### Now you try

# %% [markdown]
# **Exercise 1.** Ask the user for their favorite number, store
# it as an integer, and print an f-string that says
# `"Your favorite number times 2 is ___"`.

# %%
# Your code here

# %% [markdown]
# **Exercise 2.** Ask the user for two numbers and print their
# sum. Watch the types!

# %%
# Your code here

# %% [markdown]
# ---
# ## ☕ 15-minute break
#
# See you back here at the time the instructor announces!
# ---

# %% [markdown]
# ## Block 4: Making Decisions with if / elif / else
#
# So far our programs do the same thing every time. Now we'll make
# them respond to different inputs differently.

# %% [markdown]
# Notice two new things: the colon at the end of the `if` line,
# and the indentation. Both matter.

# %%
age = int(input("Your age? "))
if age >= 18:
    print("You can vote.")

# %%
age = int(input("Your age? "))
if age >= 18:
    print("You can vote.")
else:
    print("Not yet.")

# %% [markdown]
# For multiple cases, use `elif` (short for "else if").

# %%
age = int(input("Your age? "))
if age < 13:
    print("child")
elif age < 20:
    print("teen")
else:
    print("adult")

# %% [markdown]
# **What's wrong here?** Predict the error, then run.

# %%
if 5 > 3
    print("yes")

# %% [markdown]
# **What about this one?**

# %%
age = 18
if age = 18:
    print("happy birthday")

# %% [markdown]
# **And this one?**

# %%
x = 10
if x > 5:
    print("big")
 print("done")

# %% [markdown]
# ### Now you try

# %% [markdown]
# **Exercise 1.** Ask the user for a number. Print whether it's
# positive, negative, or zero.

# %%
# Your code here

# %% [markdown]
# **Exercise 2.** Ask the user for a temperature in Fahrenheit.
# Print "cold" if below 50, "warm" if 50–80, "hot" if above 80.

# %%
# Your code here

# %% [markdown]
# ## That's it for tonight!
#
# Open the homework notebook (linked in Blackboard) to start
# practicing. You can work on it now, finish it during class, or
# take it home — it's autograded, so you'll know how you did.
#
# See you next week!
