# %% [markdown]
# # Week 5 — Working With AI as a Coding Partner
#
# This is the week the course pivots.  Up to now you have written every line
# yourself, on purpose — you needed to know what the code *means* before you
# could judge what a machine writes for you.  Now we add a powerful, fallible
# collaborator: an AI coding assistant (ChatGPT, Claude, Gemini, Copilot, …).
#
# The skill this week is **not** "get the AI to write code."  That part is
# easy.  The skill is **driving the AI well and checking its work** so the
# code you ship is actually correct.  Four topics:
#
# 1. Prompting — asking for code in a way that gets good answers
# 2. Reading AI output critically — never paste-and-pray
# 3. AI failure modes — the specific ways AI gets things wrong
# 4. The verification loop, and a brief intro to **pytest**
#
# > **Note:** the demo cells in Parts 1–3 show *example* prompts and *example*
# > AI responses pasted in as text — you don't need an AI tool open to run this
# > notebook.  The "Now you try" exercises are where you'll use a real
# > assistant.

# %% [markdown]
# ---
# ## Part 1 — Prompting: Asking for Code
#
# An AI assistant predicts a helpful response from your words.  Vague words
# get vague code.  A good prompt gives the model the same things you'd give a
# human helper: **what you want, the shape of the inputs and outputs, and any
# constraints.**

# %% [markdown]
# ### 1.1 Vague vs. Specific
#
# Compare these two requests for the same task.  Read them as a human — which
# one could you answer without guessing?
#
# > ❌ "write something to clean up a list"
#
# > ✅ "Write a Python function `dedupe(items)` that takes a list and returns
# > a new list with duplicates removed, **preserving the original order**.
# > Don't modify the input list."
#
# The second names the function, the input, the output, and a constraint
# (order-preserving) that rules out the easy-but-wrong `list(set(items))`.

# %% [markdown]
# ### 1.2 The Four Things a Good Prompt Includes
#
# 1. **Task** — what should the code do, in one sentence.
# 2. **Inputs** — types and examples (`a list of strings`, `an int 0–100`).
# 3. **Output** — what it returns or prints, with an example.
# 4. **Constraints** — edge cases, libraries to use or avoid, style.
#
# A handy template:
#
# > "Write a Python function `name(args)` that **<task>**.
# > Input: **<types/examples>**. Output: **<what it returns>**.
# > It should handle **<edge case>**. Use only the standard library."

# %% [markdown]
# ### 1.3 Give an Example of Expected Behavior
#
# One concrete example removes more ambiguity than a paragraph of description.
# This is also exactly what you'll turn into a test later.
#
# > "Write `initials(full_name)` that returns the uppercase initials.
# > Example: `initials('ada lovelace')` should return `'AL'`."

# %% [markdown]
# ### 1.4 Iterate — the First Answer Is a Draft
#
# You rarely get the final code from one prompt.  Follow-ups are normal:
#
# > "Good, but it crashes on an empty string. Handle that by returning `''`."
#
# > "Now add a docstring and rename `x` to something descriptive."
#
# Treat the conversation like pair programming, not a vending machine.

# %% [markdown]
# ### Now you try
#
# For these, open whatever AI assistant you have (ChatGPT, Claude, Gemini, or
# Colab's built-in Gemini).  Write the prompt, paste the code you get back
# into the cell, run it, and see whether it does what you asked.

# %% [markdown]
# **Exercise 1.1.** Using the four-part template from 1.2, write a prompt that
# asks for a function `word_count(text)` returning the number of words in a
# string.  Specify what should happen for an empty string.  Paste the AI's
# code below and run it.

# %%
# Your code here

# %% [markdown]
# **Exercise 1.2.** Take this deliberately vague prompt: *"make a temperature
# converter."*  Rewrite it to be specific — name the function, the direction
# of conversion, the input type, and the return value — then get the code and
# run it.

# %%
# Your code here

# %% [markdown]
# **Exercise 1.3.** Ask the AI for a function `is_palindrome(s)`.  In a
# follow-up message, ask it to also ignore spaces and capitalization so that
# `"Race car"` counts as a palindrome.  Paste the final version below.

# %%
# Your code here

# %% [markdown]
# ---
# ## Part 2 — Reading AI Output Critically
#
# AI-generated code is often correct.  It is also often *almost* correct, and
# almost-correct code is dangerous because it looks finished.  Your job is to
# read every line as if a stranger wrote it — because one did.

# %% [markdown]
# ### 2.1 Read Before You Run
#
# Before running AI code, ask yourself three questions:
#
# 1. **Do I understand what each line does?** If not, ask the AI to explain it.
# 2. **Does it actually solve *my* problem**, or a slightly different one?
# 3. **What inputs would break it?** Empty list, zero, negative, huge, wrong type.

# %% [markdown]
# ### 2.2 A Plausible-Looking Bug
#
# Here is code an AI might produce for "average of a list."  Read it before
# running.  Can you spot the problem?

# %%
def average(numbers):
    total = 0
    for n in numbers:
        total += n
    return total / len(numbers)

print(average([2, 4, 6]))   # 4.0 — looks great

# %% [markdown]
# It works for normal input.  But watch what happens on the edge case the
# prompt never mentioned:

# %%
# print(average([]))   # uncomment: ZeroDivisionError

# %% [markdown]
# **Notice:** the happy path passed, which is exactly why you can't stop at
# the happy path.  The bug only shows up on the empty list.

# %% [markdown]
# ### 2.3 "It Runs" Is Not "It's Correct"
#
# Code that runs without error can still produce the wrong answer.  Read this
# "convert Celsius to Fahrenheit" function critically:

# %%
def c_to_f(c):
    return c * 9 / 5 - 32    # bug: should be + 32

print(c_to_f(100))   # prints 148.0 — no error, but 100°C is 212°F

# %% [markdown]
# **Notice:** no traceback, no warning.  The only way to catch this is to
# check the result against a value you already know (`100°C == 212°F`).

# %% [markdown]
# ### 2.4 Ask the AI to Explain Itself
#
# If a line is unfamiliar, paste it back and ask "what does this do, and why
# did you choose it?"  A good follow-up prompt:
#
# > "Walk me through the `c * 9 / 5` line. What's the order of operations,
# > and what would this return for `c = 100`?"
#
# Making the AI explain often surfaces the bug — and teaches you something.

# %% [markdown]
# ### Now you try

# %% [markdown]
# **Exercise 2.1.** The function below was "written by an AI" for the task
# *"return the largest number in a list."*  Read it, find the bug by reasoning
# about it, then run it on `[-5, -2, -9]` to confirm.  Fix it.

# %%
def largest(numbers):
    biggest = 0                 # bug: assumes all numbers are positive
    for n in numbers:
        if n > biggest:
            biggest = n
    return biggest

print(largest([-5, -2, -9]))   # should be -2

# %% [markdown]
# **Exercise 2.2.** Ask an AI to write `count_vowels(word)`.  Before running
# its code, write down (in a comment) the three edge cases you'll test:
# e.g. an empty string, an all-consonant word, uppercase letters.  Then test
# all three.

# %%
# Your code here

# %% [markdown]
# **Exercise 2.3.** Paste any function an AI has written for you, pick the one
# line you least understand, and ask the AI to explain just that line.  Write
# a one-sentence comment summarizing what you learned.

# %%
# Your code here

# %% [markdown]
# ---
# ## Part 3 — AI Failure Modes
#
# AI assistants fail in *characteristic* ways.  Knowing the categories helps
# you anticipate where to look.

# %% [markdown]
# ### 3.1 Hallucinated APIs
#
# Models sometimes invent functions, methods, or arguments that sound real but
# don't exist.  For example, there is **no** `str.reverse()` method in Python:

# %%
# "hello".reverse()    # uncomment: AttributeError — strings have no .reverse()

# The real ways:
print("hello"[::-1])              # slicing
print("".join(reversed("hello"))) # reversed() + join

# %% [markdown]
# **Tell-tale sign:** an `AttributeError` or `TypeError: unexpected keyword
# argument`.  When in doubt, check the official docs — not the AI.

# %% [markdown]
# ### 3.2 Confidently Wrong
#
# AI never says "I'm not sure."  It states wrong answers with the same fluent
# confidence as right ones.  Tone is **not** evidence of correctness.  The
# `c_to_f` bug in 2.3 came with a cheerful "Here's your converter!"

# %% [markdown]
# ### 3.3 Subtle Off-by-One and Boundary Errors
#
# A classic: "give me the numbers from 1 to n." `range` is exclusive on the
# top end, so the obvious code is wrong:

# %%
n = 5
print(list(range(1, n)))      # [1, 2, 3, 4] — missing 5!
print(list(range(1, n + 1)))  # [1, 2, 3, 4, 5] — correct

# %% [markdown]
# ### 3.4 Solving a Slightly Different Problem
#
# Ask for "remove duplicates but keep order" and a model may hand you the
# faster, simpler — and *wrong* — version:

# %%
def dedupe_wrong(items):
    return list(set(items))    # removes dupes BUT scrambles order

print(dedupe_wrong([3, 1, 3, 2, 1]))   # order is not preserved

# %% [markdown]
# **Notice:** it technically "removes duplicates," so it looks like a win.
# It quietly ignored the constraint you cared about.  This is why naming
# constraints in the prompt (Part 1) matters so much.

# %% [markdown]
# ### 3.5 Outdated or Version-Mismatched Code
#
# Training data spans many years.  An AI may give you `print "hi"` (Python 2)
# or a library API that changed three versions ago.  If code uses syntax your
# Python rejects, suspect a version mismatch.

# %% [markdown]
# ### Now you try

# %% [markdown]
# **Exercise 3.1.** Ask an AI to "round a number to 2 decimal places" and look
# closely at what it returns for `2.005`.  Floating-point rounding is full of
# surprises — test `round(2.005, 2)` below and note whether the result is what
# you'd expect.

# %%
# Your code here

# %% [markdown]
# **Exercise 3.2.** The function below was meant to return the **last** three
# items of a list, but it has a boundary error.  Find it and fix it.

# %%
def last_three(items):
    return items[3:]          # bug: this skips the first three instead

print(last_three([1, 2, 3, 4, 5, 6]))   # should be [4, 5, 6]

# %% [markdown]
# **Exercise 3.3.** Ask an AI for a function that uses a method you're unsure
# exists (try: "a string method that centers text in a field of width 20").
# Run it.  If it works, great; if you get an `AttributeError`, you've caught a
# hallucination — note which method it invented.

# %%
# Your code here

# %% [markdown]
# ---
# ## Part 4 — The Verification Loop, and a Brief Intro to pytest
#
# Everything so far points to one habit: **verify, don't trust.**  The
# verification loop is the rhythm of working with AI:
#
# 1. **Prompt** — ask for the code.
# 2. **Read** — understand every line.
# 3. **Test** — run it against examples *including edge cases*.
# 4. **Refine** — feed failures back to the AI and repeat.
#
# Step 3 is where we get systematic.  So far you've verified with `print()`
# and `assert`.  Now meet the standard tool for it: **pytest**.

# %% [markdown]
# ### 4.1 From assert to a Test Function
#
# You already know `assert` (Week 4).  A pytest **test** is just a function
# whose name starts with `test_`, containing `assert` statements:

# %%
def add(a, b):
    return a + b

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

test_add()              # if nothing prints and no error: it passed
print("test_add passed")

# %% [markdown]
# ### 4.2 Why a Framework Instead of Calling It Yourself
#
# Calling `test_add()` by hand works for one test.  With twenty tests you want
# a tool that **finds every `test_` function, runs them all, and reports which
# passed and which failed** — without stopping at the first failure.  That tool
# is pytest.

# %% [markdown]
# ### 4.3 Running pytest in Colab
#
# pytest normally runs from the command line on a `.py` file.  In a notebook
# we write the tests to a file with `%%writefile`, then run pytest on it with
# a `!` shell command.  First, the file under test plus its tests:

# %%
# %%writefile test_math_demo.py
def fahrenheit(c):
    return c * 9 / 5 + 32

def test_freezing():
    assert fahrenheit(0) == 32

def test_boiling():
    assert fahrenheit(100) == 212

def test_body_temp():
    assert fahrenheit(37) == 98.6

# %% [markdown]
# Now run pytest on that file.  `-q` means "quiet" (compact output).

# %%
# !python -m pytest test_math_demo.py -q

# %% [markdown]
# You should see something like `3 passed`.  Each dot is a passing test.
# (The line is commented so the notebook doesn't shell out unless you run it —
# uncomment it to try.)

# %% [markdown]
# ### 4.4 Reading a Failure
#
# Failures are the whole point — they tell you exactly what's wrong.  Here is
# a test file with a bug planted in the function:

# %%
# %%writefile test_buggy_demo.py
def double(x):
    return x + 2        # bug: should be x * 2

def test_double():
    assert double(5) == 10

# %% [markdown]
# Run it and read the report:

# %%
# !python -m pytest test_buggy_demo.py -q

# %% [markdown]
# pytest shows the failing assertion **with the actual values**:
# `assert 7 == 10`.  It computed `double(5)` as `7`, not `10` — pointing you
# straight at the bug.  This is the payoff: you don't guess, you *see* the gap
# between expected and actual.

# %% [markdown]
# ### 4.5 Closing the Loop with AI
#
# When a pytest run fails, you have the perfect follow-up prompt — paste the
# failing test and the report back to the AI:
#
# > "This test fails with `assert 7 == 10`. Here's the function and the test.
# > Fix the function so the test passes."
#
# Tests turn "it's broken somehow" into a precise, machine-checked
# specification — for you *and* for your AI partner.

# %% [markdown]
# ### Now you try

# %% [markdown]
# **Exercise 4.1.** Write a function `square(n)` that returns `n * n`.  Then
# write a `test_square()` function with at least three `assert` statements
# (try a positive number, zero, and a negative number).  Call it and confirm
# it passes.

# %%
# Your code here

# %% [markdown]
# **Exercise 4.2.** Use `%%writefile` to save a function `is_even(n)` and two
# tests (`test_even` and `test_odd`) to a file called `test_even_demo.py`.
# Then run `!python -m pytest test_even_demo.py -q` and confirm 2 passed.

# %%
# Your code here

# %% [markdown]
# **Exercise 4.3.** Ask an AI for a function `fizzbuzz(n)` that returns
# `"Fizz"` for multiples of 3, `"Buzz"` for multiples of 5, `"FizzBuzz"` for
# multiples of both, and the number (as a string) otherwise.  Then write
# pytest tests for `fizzbuzz(3)`, `fizzbuzz(5)`, `fizzbuzz(15)`, and
# `fizzbuzz(7)`.  Run them — and if any fail, paste the failure back to the AI
# and ask it to fix the function.

# %%
# Your code here
