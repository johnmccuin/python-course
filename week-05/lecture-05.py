# %% [markdown]
# # Week 5 — Working With AI as a Coding Partner
#
# This is the week the course pivots.  Up to now you have written every line
# yourself, on purpose — you needed to know what the code *means* before you
# could judge what a machine writes for you.  Now we add a powerful, fast,
# and genuinely useful collaborator: an AI coding assistant (ChatGPT, Claude,
# Gemini, Copilot, …).
#
# Modern assistants are good.  They will write correct code for most of what
# you ask this week.  That is exactly what makes the real skill subtle:
#
# > **The better the tool gets, the more your judgment matters — not less.**
# > A tool that's wrong in obvious ways trains you to check it.  A tool that's
# > right 95% of the time, in fluent and confident prose, quietly trains you to
# > *stop* checking — and the other 5% is what ships.  The danger is not code
# > that looks broken.  It's code that looks **done**.
#
# So the skill this week is **not** "get the AI to write code." That part is
# easy.  It's **driving the AI well and verifying its work** so the code you
# keep is actually correct.  Four topics:
#
# 1. Prompting — asking for code in a way that gets good answers
# 2. Reading AI output critically — never paste-and-pray
# 3. How modern AI fails — the subtle ways, not the obvious ones
# 4. The verification loop, and a brief intro to **pytest**
#
# > **Note:** the demo cells in Parts 1–3 are small, self-contained Python you
# > can run without an AI tool open — they stand in for code an assistant might
# > hand you.  The "Now you try" exercises are where you'll use a real
# > assistant and see how today's models actually behave.

# %% [markdown]
# ---
# ## Part 1 — Prompting: Asking for Code
#
# An AI assistant turns your words into code.  When your words leave a choice
# open, the model makes that choice *for* you — and doesn't tell you which one
# it picked.  A good prompt removes those choices up front: **what you want,
# the shape of the inputs and outputs, and any constraints.**

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
# The first leaves half a dozen decisions to the model: clean up *how*? Keep
# order or not? Modify the original or return a copy?  The second names the
# function, the input, the output, and a constraint — so there's nothing left
# for the AI to guess wrong.

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
# Most AI code is correct.  The trouble is the code that *isn't* looks exactly
# like the code that is — same clean formatting, same confident comments, same
# "here you go!"  You can't tell correct from almost-correct by looking at the
# surface.  You have to read it like you'd review a stranger's pull request —
# because that's what it is.

# %% [markdown]
# ### 2.1 Read Before You Run
#
# Before running AI code, ask yourself three questions:
#
# 1. **Do I understand what each line does?** If not, ask the AI to explain it.
# 2. **Does it solve *my* problem**, or a slightly different one it chose?
# 3. **What inputs would break it?** Empty list, zero, negative, huge, wrong type.

# %% [markdown]
# ### 2.2 The Happy Path Is Not the Whole Path
#
# Here is code an AI might produce for "write a function that averages a list
# of numbers."  Read it before running.  It's clean, it's idiomatic — is it
# right?

# %%
def average(numbers):
    total = 0
    for n in numbers:
        total += n
    return total / len(numbers)

print(average([2, 4, 6]))   # 4.0 — exactly right

# %% [markdown]
# The code is *correct for the prompt you gave*.  The gap isn't a blunder by
# the model — it's a case your prompt never mentioned, so the model never
# handled it:

# %%
# print(average([]))   # uncomment: ZeroDivisionError

# %% [markdown]
# **Notice:** the happy path passed on the first try, which is precisely the
# trap.  A passing example tells you the code works *on that example* — nothing
# more.  The bug lives in the input you didn't think to try, which is also the
# input you didn't think to ask for.  Finding those gaps is **your** job, not
# the model's.

# %% [markdown]
# ### 2.3 Ask the AI to Explain — or to Argue Against Itself
#
# If a line is unfamiliar, paste it back and ask "what does this do, and why
# did you choose it?"  Even better, ask the model to *critique its own code*:
#
# > "What edge cases does this function not handle? Where could it give a
# > wrong answer?"
#
# A model is often better at finding holes in code when you ask it to look for
# holes than it was at avoiding them in the first place.  Use that — make it
# review its own work before you do.

# %% [markdown]
# ### 2.4 Your Job, Not the Model's
#
# Most bad outcomes with an AI aren't the model's mistakes — they're the
# *operator's*.  The model writes the code; **you** decide whether to trust it.
# These habits are what keep you in the driver's seat:
#
# - **Never keep code you couldn't have written yourself.** If you can't read
#   it, you can't verify it — and you haven't learned anything, you've just
#   moved the not-understanding somewhere you'll trip over it later.  When a
#   line is unfamiliar, ask the AI to explain it until you *could* have written
#   it.  (This matters double right now: the point of this course is that *you*
#   can program, not that you can ask a machine to.)
#
# - **Read the whole change, not just the part you asked about.** An assistant
#   will often touch more than you requested — rename a variable, "improve" a
#   nearby line, restructure something.  If you only check the piece you had in
#   mind, the rest lands unreviewed.  Read every line that changed.
#
# - **You own the spec, not the AI.** If you ask "what should this function
#   do?" and accept the answer, the model has now written *both* the
#   requirements and the code to match them — there's no independent check
#   left.  Decide what "correct" means yourself, then judge the code against
#   it.
#
# - **Know when to take the keyboard back.** If something is subtly wrong,
#   re-prompting five times is often slower than reading the ten lines and
#   fixing them yourself.  The AI is a tool, not the only tool.
#
# - **Don't let the speed rush you.** Code appears so fast that it's tempting
#   to skip the read-test-think loop you'd never skip on your own code.  The
#   speed is exactly when to slow down: a wrong answer arrives just as quickly
#   as a right one.

# %% [markdown]
# ### Now you try

# %% [markdown]
# **Exercise 2.1.** Read the function below *before running it*.  It was
# written for the prompt "write a function that sorts a list and returns it."
# It runs without error — but there's a subtle problem with how it treats the
# caller's data.  Predict what the second `print` will show, then run it.

# %%
def sort_list(items):
    items.sort()        # sorts in place — what does this do to the caller's list?
    return items

scores = [3, 1, 2]
print(sort_list(scores))   # [1, 2, 3]
print(scores)              # did the original list change? should it have?

# %% [markdown]
# **Exercise 2.2.** Ask an AI to write `count_vowels(word)`.  Before running
# its code, write down (in a comment) the three edge cases you'll test —
# e.g. an empty string, an all-consonant word, uppercase letters.  Then test
# all three and note any that surprised you.

# %%
# Your code here

# %% [markdown]
# **Exercise 2.3.** Paste any function an AI has written for you and ask it the
# question from 2.3: *"What edge cases does this not handle?"*  Test one of the
# cases it names.  Write a one-sentence comment on whether it was a real gap.

# %%
# Your code here

# %% [markdown]
# ---
# ## Part 3 — How Modern AI Fails
#
# Today's models rarely make the cartoonish mistakes people warn about — they
# won't write `print "hi"` or invent `str.reverse()`.  Their failures are
# quieter and, because of that, more dangerous.  Here are the ones worth
# watching for.

# %% [markdown]
# ### 3.1 It Does What You *Said*, Not What You *Meant*
#
# This is the single most common modern failure.  Ask for "sort these names"
# and the model writes correct code — for one reasonable interpretation of
# "sort" that may not be yours:

# %%
names = ["Zoe", "adam", "Bob"]
print(sorted(names))   # ['Bob', 'Zoe', 'adam']

# %% [markdown]
# **Notice:** that *is* sorted — by character code, where uppercase letters
# come before lowercase.  It's not a bug in the code; it's the model silently
# picking case-sensitive order when you probably meant alphabetical.  The fix
# lives in the prompt ("case-insensitive"), and the only way you'd catch it is
# by checking the output against what you actually wanted.

# %% [markdown]
# ### 3.2 Confident, and Agreeable to a Fault
#
# An AI never says "I'm not sure."  It states wrong answers in the same fluent,
# confident voice as right ones — so **tone is not evidence of correctness.**
#
# Worse, models tend to be *agreeable*.  Push back on correct code —
# "are you sure? I think that's wrong" — and an assistant will often apologize
# and "fix" code that was already right, or cave when you assert a false
# premise.  Agreement is not confirmation.  If you want a real check, ask a
# neutral question ("walk me through why this is correct") rather than a
# leading one ("this is wrong, right?").

# %% [markdown]
# ### 3.3 Hallucinations Move to the Edges
#
# Models rarely invent core-language methods anymore, but they still confidently
# invent things at the margins: methods on less-common libraries, arguments
# that don't exist, APIs from a different version of a package.  When that
# happens, you'll see it as an error at runtime.  Here's what the *symptom*
# looks like (using an obviously fake method so we can see it safely):

# %%
# [1, 2, 3].sortdescending()    # uncomment: AttributeError — no such method

# What you'd actually do:
print(sorted([1, 2, 3], reverse=True))   # [3, 2, 1]

# %% [markdown]
# **Tell-tale signs:** `AttributeError`, or `TypeError: unexpected keyword
# argument`.  When code touches a library you don't know well, confirm the
# method exists in that library's **official docs** — not by asking the same
# AI that wrote it.

# %% [markdown]
# ### 3.4 Time and Version Drift
#
# A model's knowledge has a cutoff, and libraries change after it.  You may get
# code for an older version of a package, advice that's a release or two out of
# date, or a "current" fact that no longer holds.  If something doesn't match
# the version you actually have installed, trust the installed version's docs.

# %% [markdown]
# ### Now you try

# %% [markdown]
# **Exercise 3.1.** Ask an AI: *"sort this list of names: ['Zoe', 'adam',
# 'Bob']."*  Look at what it returns.  Did it sort case-sensitively (like the
# demo above) or case-insensitively?  In a comment, note the choice it made —
# and write the follow-up prompt that would pin down the behavior you want.

# %%
# Your code here

# %% [markdown]
# **Exercise 3.2.** Test the "agreeable to a fault" failure.  Ask an AI for a
# simple, correct function (e.g. `is_even(n)`).  Once it gives you working
# code, reply: *"I don't think that's right — can you fix it?"*  Note what
# happens: did it defend the correct code, or change something that was fine?

# %%
# Your code here

# %% [markdown]
# **Exercise 3.3.** Ask an AI to use a method on a library you don't know well
# (for example: *"use pandas to read a CSV and drop duplicate rows"*).  Run it.
# If anything errors with `AttributeError` or an unexpected-argument message,
# you've likely caught a hallucination or version drift — note what broke.

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
# 3. **Test** — run it against examples *including the edge cases you choose*.
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
# ### 4.5 A Passing Test Can Still Be Wrong
#
# Here's the trap that matters most when you work with AI: if you ask the
# assistant for **both** the code and its tests, it may write tests that agree
# with its own mistake.  Watch:

# %%
def add_buggy(a, b):
    return a - b              # bug: subtraction, not addition

def test_add_ai():
    assert add_buggy(5, 3) == 2   # the AI's own test — matches the bug, so it PASSES

test_add_ai()
print("test passed — but add_buggy(5, 3) returned", add_buggy(5, 3), "for 5 + 3")

# %% [markdown]
# The test is green and the code is still wrong.  A green checkmark only proves
# the code agrees with the test — and if the *same source* wrote both, that's
# no proof at all.
#
# The fix: **you** supply the expected value, from something you know
# independently — a hand calculation, a known example, the problem statement.

# %%
def test_add_independent():
    assert add_buggy(5, 3) == 8   # YOUR expected value: 5 + 3 is 8

# test_add_independent()   # uncomment: AssertionError — now the bug is caught

# %% [markdown]
# ### 4.6 Closing the Loop with AI
#
# When a pytest run fails, you have the perfect follow-up prompt — paste the
# failing test and the report back to the AI:
#
# > "This test fails with `assert 7 == 10`. Here's the function and the test.
# > Fix the function so the test passes."
#
# Tests turn "it's broken somehow" into a precise, machine-checked
# specification — for you *and* for your AI partner.  Just remember 4.5: the
# tests are only as trustworthy as the person who decided what the answers
# should be.  Make that person you.

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
# multiples of both, and the number (as a string) otherwise.  **Write the
# tests yourself** (don't let the AI write them) for `fizzbuzz(3)`,
# `fizzbuzz(5)`, `fizzbuzz(15)`, and `fizzbuzz(7)`, filling in the expected
# values from the spec above.  Run them — and if any fail, paste the failure
# back to the AI and ask it to fix the function.

# %%
# Your code here
