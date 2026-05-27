# %% [markdown]
# # Week 2 — Making Decisions and Repeating
#
# **Topics today:**
# 1. If / else / elif — making decisions
# 2. While loops — repeating until something changes
# 3. Lists — storing ordered collections
# 4. For loops over lists — where loops start to feel useful

# %% [markdown]
# ---
# ## Part 1 — If / Else / Elif

# %% [markdown]
# ### Quick recap: comparisons and booleans
#
# Python has two boolean values: `True` and `False`.
# Comparison operators produce them:
#
# | Operator | Meaning |
# |----------|---------|
# | `==` | equal to |
# | `!=` | not equal to |
# | `<`  | less than |
# | `>`  | greater than |
# | `<=` | less than or equal |
# | `>=` | greater than or equal |
#
# Use `and`, `or`, and `not` to combine conditions.

# %%
print(5 > 3)
print(10 == 9)
print("apple" != "orange")
print(4 >= 4)

# %% [markdown]
# ### if / else
#
# An `if` block runs **only when** the condition is `True`.
# The `else` block runs when it is `False`.
#
# ```python
# if condition:
#     # runs when True
# else:
#     # runs when False
# ```
#
# The colon `:` after the condition is **required**.
# The body must be indented (4 spaces or one Tab).

# %%
temperature = 72

if temperature > 80:
    print("It's hot outside.")
else:
    print("It's comfortable outside.")

# %% [markdown]
# ### elif — checking multiple conditions
#
# `elif` ("else if") lets you chain conditions.
# Python checks each one **top to bottom** and runs the first matching block.
# At most one block ever executes.

# %%
score = 85

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")

# %%
# Change score and re-run to see a different result
score = 55

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")

# %% [markdown]
# ### Nested if statements (keep it shallow)
#
# You can put an `if` inside another `if`.
# Avoid going deeper than two levels — it gets hard to read fast.

# %%
age = 20
has_id = True

if age >= 18:
    if has_id:
        print("You may enter.")
    else:
        print("You need a valid ID.")
else:
    print("You must be 18 or older.")

# %% [markdown]
# ### Now you try

# %% [markdown]
# **Exercise 1.1 — Even or odd**
#
# Assign any integer to a variable called `number`.
# Print `"even"` if it is divisible by 2, `"odd"` otherwise.
#
# Hint: `%` gives the remainder — `7 % 2` is `1`, `8 % 2` is `0`.

# %%


# %% [markdown]
# **Exercise 1.2 — Temperature category**
#
# Given a variable `temp` (°F), print:
# - `"freezing"` if below 32
# - `"cold"` if 32 – 59
# - `"comfortable"` if 60 – 79
# - `"hot"` if 80 or above
#
# Test with at least two different values.

# %%


# %% [markdown]
# **Exercise 1.3 — Ticket price**
#
# A theater charges:
# - \$5 for children under 12
# - \$9 for seniors 65 and over
# - \$12 for everyone else
#
# Given an `age` variable, print the correct ticket price.

# %%


# %% [markdown]
# **Exercise 1.4 — Login check**
#
# Set `username = "alice"` and `password = "secret123"`.
# Write an if/elif/else that prints:
# - `"Access granted"` — both correct
# - `"Wrong password"` — username right, password wrong
# - `"Unknown user"` — username wrong

# %%


# %% [markdown]
# ---
# ## Part 2 — While Loops

# %% [markdown]
# ### The idea: repeat until something changes
#
# A `while` loop runs its body **as long as** the condition is `True`.
#
# ```python
# while condition:
#     # body
# ```
#
# Every while loop needs three things:
# 1. A **starting state** — initialize a variable before the loop
# 2. A **condition** — checked at the top of every pass
# 3. A **change** inside the body that will eventually make the condition `False`
#
# Miss step 3 and you have an **infinite loop**. In Colab, click the stop
# button (■) next to the cell to interrupt it.

# %%
# Count from 1 to 5
count = 1                  # 1. starting state

while count <= 5:          # 2. condition
    print(count)
    count = count + 1      # 3. change  (also written: count += 1)

print("Done!")

# %%
# Countdown by twos
n = 10

while n > 0:
    print(n)
    n -= 2

print("Liftoff!")

# %% [markdown]
# ### Accumulating with a while loop
#
# A **running total** (accumulator) is a variable you initialize before the
# loop and update each pass. Read the result after the loop finishes.

# %%
# Sum the numbers 1 through 10
total = 0
i = 1

while i <= 10:
    total += i
    i += 1

print("Sum:", total)

# %% [markdown]
# ### Bug demos — while loops
#
# Study these before writing your own loops.

# %%
# BUG 1: Infinite loop
# The counter never changes — condition stays True forever.
# (Left as a comment so you don't accidentally run it.)
#
# count = 1
# while count <= 5:
#     print(count)
#     # forgot: count += 1     <-- this line is missing

# %%
# BUG 2: Off-by-one error
# Goal: print 1 through 5. What does this actually print? Why?

count = 1
while count < 5:      # should be <= 5
    print(count)
    count += 1

# Fix: change < to <=

# %% [markdown]
# ### Now you try

# %% [markdown]
# **Exercise 2.1 — Count by twos**
#
# Use a while loop to print every even number from 2 to 20 inclusive.

# %%


# %% [markdown]
# **Exercise 2.2 — Factorial**
#
# The factorial of n (written n!) is n × (n−1) × … × 2 × 1. For example, 5! = 120.
#
# Use a while loop to compute the factorial of 6. Print the result.

# %%


# %% [markdown]
# **Exercise 2.3 — Secret number hunt**
#
# Set `secret = 37`. Start with `guess = 1`.
# Use a while loop to increment `guess` by 1 each pass until it equals `secret`.
# Count every attempt. Print: `"Found it in X attempts."`

# %%


# %% [markdown]
# **Exercise 2.4 — Digit sum**
#
# Given `number = 12345`, repeatedly pull off the last digit
# (`number % 10`) and chop it off (`number //= 10`) until `number` is 0.
# Add up all the digits. Print the total.

# %%


# %% [markdown]
# ---
# ## Part 3 — Lists

# %% [markdown]
# ### What is a list?
#
# A **list** is an ordered, changeable collection of values.
# Items can be any type — numbers, strings, booleans, even other lists.
#
# ```python
# my_list = [item0, item1, item2]
# ```

# %%
fruits = ["apple", "banana", "cherry"]
numbers = [10, 20, 30, 40, 50]
mixed = [1, "hello", 3.14, True]
empty = []

print(fruits)
print(len(fruits))    # number of items

# %% [markdown]
# ### Indexing
#
# Access an item by its **index** (position), starting at **0**.
#
# ```
# fruits = ["apple", "banana", "cherry"]
# index:       0         1         2
# ```
#
# Negative indexes count from the end: `-1` is the last item.

# %%
fruits = ["apple", "banana", "cherry"]

print(fruits[0])     # first
print(fruits[2])     # last (by positive index)
print(fruits[-1])    # last (by negative index)
print(fruits[-2])    # second to last

# %% [markdown]
# ### Slicing
#
# A slice pulls out a sub-list: `my_list[start:stop]`
# - `start` is **included**, `stop` is **excluded**
# - Omit `start` to begin at 0; omit `stop` to go to the end

# %%
numbers = [10, 20, 30, 40, 50]

print(numbers[1:3])   # [20, 30]
print(numbers[:3])    # [10, 20, 30]
print(numbers[2:])    # [30, 40, 50]
print(numbers[-2:])   # [40, 50]

# %% [markdown]
# ### Modifying lists
#
# Lists are **mutable** — you can change them after creation.

# %%
fruits = ["apple", "banana"]
print("Start:", fruits)

fruits.append("cherry")         # add to the end
print("append:", fruits)

fruits[0] = "avocado"           # replace by index
print("replace index 0:", fruits)

fruits.insert(1, "blueberry")   # insert at a position
print("insert at 1:", fruits)

fruits.remove("banana")         # remove first occurrence of value
print("remove banana:", fruits)

# %%
# Useful built-in functions on lists
numbers = [3, 1, 4, 1, 5, 9, 2, 6]

print("len:", len(numbers))
print("sum:", sum(numbers))
print("min:", min(numbers))
print("max:", max(numbers))
print("sorted:", sorted(numbers))   # returns a new list
print("original:", numbers)         # unchanged

numbers.sort()                       # modifies the list in place
print("after .sort():", numbers)

# %% [markdown]
# ### Now you try

# %% [markdown]
# **Exercise 3.1 — Build a list**
#
# Create a list called `cities` with at least 4 city names.
# Print the first city, the last city, and the total count.

# %%


# %% [markdown]
# **Exercise 3.2 — Slice it up**
#
# Given `data = [5, 10, 15, 20, 25, 30, 35, 40]`:
# - Print the first three items.
# - Print the last two items.
# - Print items at indices 2 through 5 (inclusive — watch the stop index).

# %%


# %% [markdown]
# **Exercise 3.3 — List mutation**
#
# Start with `shopping = ["milk", "eggs", "bread"]`.
# 1. Append `"butter"`.
# 2. Replace `"eggs"` with `"cheese"`.
# 3. Remove `"bread"`.
# 4. Print the final list.

# %%


# %% [markdown]
# **Exercise 3.4 — Temperature range**
#
# Given `temps = [72, 68, 75, 80, 65, 90, 77]`, use `min()` and `max()`
# to compute and print the range (max − min).

# %%


# %% [markdown]
# ---
# ## Part 4 — For Loops Over Lists

# %% [markdown]
# ### The payoff: loops + lists together
#
# A **for loop** visits every item in a list, one at a time.
#
# ```python
# for item in my_list:
#     # do something with item
# ```
#
# Python picks each element, assigns it to the loop variable, runs the body,
# then automatically moves to the next element.
# No index arithmetic. No counter to maintain.

# %%
fruits = ["apple", "banana", "cherry", "date"]

for fruit in fruits:
    print(fruit)

# %%
# f-strings work great inside loops
prices = [1.99, 3.49, 0.89, 4.25]

for price in prices:
    print(f"${price:.2f}")

# %% [markdown]
# ### The accumulator pattern with for loops
#
# Same idea as with while loops: initialize before, update inside, read after.

# %%
scores = [88, 92, 75, 100, 63]

total = 0
for score in scores:
    total += score

print("Total:", total)
print("Average:", total / len(scores))

# %%
# Build a new list of converted values
temps_f = [32, 68, 98.6, 212]

temps_c = []
for f in temps_f:
    c = (f - 32) * 5 / 9
    temps_c.append(round(c, 1))

print(temps_c)

# %% [markdown]
# ### Filtering with if inside a loop
#
# Combine a for loop with an if statement to keep only the items you want.

# %%
numbers = [4, 7, 2, 9, 1, 6, 3, 8, 5]

evens = []
for n in numbers:
    if n % 2 == 0:
        evens.append(n)

print("Evens:", evens)

# %%
grades = [45, 82, 60, 71, 38, 95, 55, 68]

passing = []
for grade in grades:
    if grade >= 60:
        passing.append(grade)

print("Passing grades:", passing)
print("Number passing:", len(passing))

# %% [markdown]
# ### Bug demos — for loops
#
# Two mistakes that produce confusing output (and won't raise an error):

# %%
# BUG 1: Loop variable name wrong inside the body
# What prints? Why is it not what we expected?

words = ["hello", "world", "python"]

for word in words:
    print(words)    # BUG: `words` is the whole list; should be `word`

# Fix: change `words` to `word` on the print line

# %%
# BUG 2: Modifying a list while iterating over it
# Python skips items silently — the result is wrong and no error is raised.

numbers = [1, 2, 3, 4, 5, 6]

for n in numbers:
    if n % 2 == 0:
        numbers.remove(n)    # BUG: mutating the list mid-loop

print("Result:", numbers)    # Not what you'd expect — try it and see

# %%
# Correct fix: collect into a NEW list instead of modifying the original
numbers = [1, 2, 3, 4, 5, 6]
odds = []

for n in numbers:
    if n % 2 != 0:
        odds.append(n)

print("Odds:", odds)

# %% [markdown]
# ### Now you try

# %% [markdown]
# **Exercise 4.1 — Greet everyone**
#
# Given `names = ["Alice", "Bob", "Charlie", "Diana"]`,
# print `"Hello, <name>!"` for each name.

# %%


# %% [markdown]
# **Exercise 4.2 — Sum of squares**
#
# Given `nums = [1, 2, 3, 4, 5]`, use a for loop to compute
# 1² + 2² + 3² + 4² + 5². Print the result.
#
# Hint: `n ** 2` raises n to the power of 2.

# %%


# %% [markdown]
# **Exercise 4.3 — Count the long words**
#
# Given `words = ["cat", "elephant", "dog", "hippopotamus", "ant", "butterfly"]`,
# count how many words have more than 5 characters. Print the count.

# %%


# %% [markdown]
# **Exercise 4.4 — Uppercase list**
#
# Given `colors = ["red", "green", "blue", "yellow"]`,
# build a new list `upper_colors` where every color is uppercase.
# Use `"red".upper()` as a pattern. Print the new list.

# %%


# %% [markdown]
# **Exercise 4.5 — First negative**
#
# Given `values = [10, 25, 3, -7, 14, -2, 8]`,
# find and print the **first** negative number, then stop looking.
#
# Hint: `break` exits a loop immediately.

# %%


# %% [markdown]
# **Exercise 4.6 — Putting it all together**
#
# Given:
# ```python
# scores = [72, 45, 88, 91, 55, 63, 78, 82, 39, 95]
# ```
# Write code that prints:
# 1. The number of students who passed (score ≥ 60)
# 2. The number who failed
# 3. The average score of **only the passing** students

# %%
