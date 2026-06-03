# %% [markdown]
# # Week 6 — Pulling It Together, and Writing a Project Spec
#
# You now know the whole core of Python: values and variables, decisions and
# loops, functions, the main data structures, files, error handling, and
# classes.  This week has two halves.
#
# **First half — pulling it together.**  A few finishing tools that make real
# programs shorter and cleaner (comprehensions and a tour of the standard
# library), then a worked example of organizing a complete small program out of
# the pieces you already have.
#
# **Second half — your project.**  The rest of the course is a capstone project.
# Today you'll brainstorm an idea, scope it to something achievable, and write a
# **spec**: a clear, plain-language description of what you're going to build.
# That spec is the bridge to Weeks 7–8, where you'll learn to build with an AI
# partner — and a clear spec is the single most important thing you bring to that
# partnership.
#
# Four topics:
#
# 1. Comprehensions — building lists and dicts in one readable line
# 2. A tour of the standard library — batteries included
# 3. Organizing a small program end-to-end
# 4. Project ideation and writing a spec

# %% [markdown]
# ---
# ## Part 1 — Comprehensions
#
# A **list comprehension** builds a list in one line.  You've written this shape
# many times already — make an empty list, loop, `append` — and a comprehension
# is the compact way to say the same thing.

# %% [markdown]
# ### 1.1 From a Loop to a Comprehension
#
# Here is the long way and the short way, side by side.

# %%
# The long way (Week 2):
squares = []
for n in range(1, 6):
    squares.append(n ** 2)
print(squares)   # [1, 4, 9, 16, 25]

# %%
# The same thing as a comprehension:
squares = [n ** 2 for n in range(1, 6)]
print(squares)   # [1, 4, 9, 16, 25]

# %% [markdown]
# Read it left to right: **"`n ** 2` for each `n` in `range(1, 6)`."**
# The expression on the left is what goes into the new list.

# %% [markdown]
# ### 1.2 Filtering with `if`
#
# Add an `if` at the end to keep only some items.

# %%
numbers = [4, 7, 2, 9, 1, 6, 3, 8]
evens = [n for n in numbers if n % 2 == 0]
print(evens)   # [4, 2, 6, 8]

# %%
words = ["cat", "elephant", "dog", "hippopotamus"]
long_words = [w.upper() for w in words if len(w) > 3]
print(long_words)   # ['ELEPHANT', 'HIPPOPOTAMUS']

# %% [markdown]
# ### 1.3 Dict Comprehensions
#
# The same idea builds a dictionary (you saw a glimpse in Week 3).

# %%
names = ["Ada", "Bob", "Cy"]
name_lengths = {name: len(name) for name in names}
print(name_lengths)   # {'Ada': 3, 'Bob': 3, 'Cy': 2}

# %% [markdown]
# ### 1.4 When *Not* to Use One
#
# A comprehension is for building a collection.  If you just want to *do*
# something for each item (like print), a plain `for` loop is clearer.  And if
# the logic needs more than a simple condition, reach for a regular loop — a
# comprehension you can't read at a glance has lost its only advantage.

# %% [markdown]
# ### Now you try

# %% [markdown]
# **Exercise 1.1.** Use a list comprehension to build a list of the cubes
# (`n ** 3`) of the numbers 1 through 6.

# %%
# Your code here

# %% [markdown]
# **Exercise 1.2.** Given `temps_c = [0, 20, 37, 100]`, use a comprehension to
# build a list of the same temperatures in Fahrenheit (`c * 9 / 5 + 32`).

# %%
# Your code here

# %% [markdown]
# **Exercise 1.3.** Given `scores = [45, 82, 91, 58, 77, 60]`, use a
# comprehension with an `if` to build a list of only the **passing** scores
# (60 or above).

# %%
# Your code here

# %% [markdown]
# ---
# ## Part 2 — A Tour of the Standard Library
#
# Python "comes with batteries included": a large standard library of modules
# you can `import` (Week 4) without installing anything.  Knowing what's in the
# box saves you from reinventing it.  Here are a few you'll reach for constantly.

# %% [markdown]
# ### 2.1 `statistics` — averages and spread

# %%
import statistics

grades = [88, 92, 75, 100, 63, 88]
print(statistics.mean(grades))    # the average
print(statistics.median(grades))  # the middle value
print(statistics.mode(grades))    # the most common value

# %% [markdown]
# ### 2.2 `collections.Counter` — tallying things
#
# You met `Counter` in Week 3.  It counts occurrences in one step.

# %%
from collections import Counter

votes = ["yes", "no", "yes", "yes", "no", "abstain"]
tally = Counter(votes)
print(tally)                  # Counter({'yes': 3, 'no': 2, 'abstain': 1})
print(tally.most_common(1))   # [('yes', 3)] — the winner

# %% [markdown]
# ### 2.3 `datetime` — dates and times
#
# Also from Week 3 — dates are objects with attributes and methods.

# %%
from datetime import date

today = date.today()
print(today.year)
print(today.strftime("%B %d, %Y"))   # e.g. June 03, 2026

# %% [markdown]
# ### 2.4 `random` — choices and shuffling

# %%
import random

deck = ["A", "K", "Q", "J"]
print(random.choice(deck))    # one random card
random.shuffle(deck)          # shuffle in place
print(deck)

# %% [markdown]
# ### Now you try

# %% [markdown]
# **Exercise 2.1.** Use `statistics.mean` to compute and print the average of
# `[10, 20, 30, 40]`.

# %%
# Your code here

# %% [markdown]
# **Exercise 2.2.** Given the sentence below, split it into words and use
# `Counter` to find the most common word.
#
# `text = "the cat sat on the mat and the cat ran"`

# %%
# Your code here

# %% [markdown]
# **Exercise 2.3.** Use `random.randint(1, 6)` to simulate rolling a die 5
# times, collecting the results into a list, then print the list and its sum.

# %%
# Your code here

# %% [markdown]
# ---
# ## Part 3 — Organizing a Small Program End-to-End
#
# A real program is more than a single cell.  The skill is **organizing** it:
# breaking the work into small functions that each do one job, then composing
# them.  The rule of thumb is **one function, one job** — if you can't describe
# what a function does without saying "and," it's probably two functions.
#
# Let's build a small **grade reporter** out of the pieces you already have.

# %% [markdown]
# ### 3.1 Start by Naming the Jobs
#
# Before writing code, list the steps in plain words:
#
# 1. Turn a numeric score into a letter grade.
# 2. Compute the class average.
# 3. Print a tidy report.
#
# Each of those becomes one small function.  Naming the jobs first *is* the
# design — you can see the whole shape before writing a single line of logic.

# %% [markdown]
# ### 3.2 One Function Per Job

# %%
def letter_grade(score):
    """Return the letter grade for a 0–100 score."""
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    return "F"

def class_average(scores):
    """Return the average of a list of scores."""
    return sum(scores) / len(scores)

# %% [markdown]
# ### 3.3 Compose Them Into the Program
#
# With the small pieces in place, the top-level code reads like the plan from 3.1.

# %%
def print_report(students):
    """Print each student's letter grade, then the class average.

    students: a dict mapping name -> numeric score.
    """
    for name, score in students.items():
        print(f"{name:10} {score:3}  {letter_grade(score)}")
    print("-" * 20)
    print(f"Average: {class_average(list(students.values())):.1f}")

gradebook = {"Ada": 95, "Bob": 72, "Cy": 88, "Dee": 54}
print_report(gradebook)

# %% [markdown]
# **Notice:** each function is small enough to read and trust on its own, and
# `print_report` reads like a sentence.  If a letter grade looks wrong, you know
# exactly which function to check.  *That* is what organizing code buys you —
# and it's the same structure that will let you review an AI's work in Week 7.

# %% [markdown]
# ### Now you try

# %% [markdown]
# **Exercise 3.1.** Write a one-job function `is_passing(score)` that returns
# `True` when a score is 60 or above.  Test it on a passing and a failing score.

# %%
# Your code here

# %% [markdown]
# **Exercise 3.2.** Write a function `count_passing(scores)` that uses a loop
# (or a comprehension) to return how many scores in a list are passing.  Reuse
# `is_passing` inside it.

# %%
# Your code here

# %% [markdown]
# **Exercise 3.3.** Compose them: given `scores = [55, 81, 72, 49, 90]`, print
# a one-line summary like `"3 of 5 students passed."` using `count_passing`
# and `len`.

# %%
# Your code here

# %% [markdown]
# ---
# ## Part 4 — Your Project: Ideation and a Spec
#
# The rest of the course is a project of your own.  Weeks 7–8 are work time:
# you'll build it with an AI coding partner, and present it in Week 9.  The
# single most valuable thing you can do *today* is decide what you're building
# and write it down clearly.

# %% [markdown]
# ### 4.1 Finding an Idea
#
# A good first project is **small, real, and yours.**  The best ideas scratch
# your own itch.  Some directions:
#
# - A tool: a tip splitter, a study-flashcard quizzer, a unit converter.
# - A small game: number-guessing, hangman, rock-paper-scissors.
# - A data cruncher: read a file of your data (workouts, expenses, grades) and
#   report on it.
#
# Pick something you could describe to a friend in two sentences.

# %% [markdown]
# ### 4.2 Scope It Down
#
# The number-one beginner mistake is building too big.  Aim for a program you
# could finish the *core* of in an afternoon.  Write down a **minimum version**
# (the smallest thing that's still useful) and a few **"if there's time"**
# extras.  You ship the minimum first.
#
# > Too big: "an app that tracks all my finances with charts and login."
# > Right-sized: "read `expenses.txt`, total the spending per category, print
# > the three biggest."

# %% [markdown]
# ### 4.3 What a Spec Is
#
# A **spec** (specification) is a short, plain-language description of what your
# program should do — written *before* the code exists.  It answers "how will I
# know this is finished and correct?"  A useful spec covers four things:
#
# 1. **What** it does, in one or two sentences.
# 2. **Inputs** — what goes in (a file? user typing? a list?), and of what kind.
# 3. **Output** — what comes out, with a concrete example.
# 4. **Edge cases** — the tricky inputs, and what should happen for each.

# %% [markdown]
# ### 4.4 An Example Spec
#
# Here's a spec for the expense tool above.  Notice there's no Python — just
# decisions made on purpose, in words anyone could read.

# %%
# SPEC: Expense Summarizer
#   What:    read a file of expenses and print the total per category,
#            plus the three largest single expenses.
#   Inputs:  a text file "expenses.txt"; each line is "category,amount"
#            e.g.  food,12.50
#   Output:  one line per category with its total, then a "Top 3" list.
#   Edge:    - a missing file prints a friendly message, doesn't crash
#            - a blank line is skipped
#            - amounts always have 2 decimals in the output

print("A spec is just words — but words you've committed to.")

# %% [markdown]
# ### 4.5 Why the Spec Is the Bridge to Weeks 7–8
#
# Next week you start working with an AI coding partner.  An AI will write code
# fast — but it builds *exactly what you describe*, and silently guesses at
# anything you leave out.  The clearer your spec, the better the result and the
# easier it is to check.  **The spec is the part only you can write**, because
# only you know what you actually want.  Today's spec is the thing you'll hand
# over first.

# %% [markdown]
# ### Now you try

# %% [markdown]
# **Exercise 4.1.** Brainstorm.  In a comment, write down **three** project
# ideas you'd find genuinely useful or fun.  One sentence each.

# %%
# Your ideas here

# %% [markdown]
# **Exercise 4.2.** Pick your favourite and **scope it.**  In a comment, write
# the *minimum useful version* in one sentence, then list two "if there's time"
# extras you'd add later.

# %%
# Your scope here

# %% [markdown]
# **Exercise 4.3.** Write the full **four-part spec** for your minimum version
# (What / Inputs / Output / Edge cases), in the comment-block style of 4.4.
# This is your starting point for next week — keep it.

# %%
# Your spec here
