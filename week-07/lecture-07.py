# %% [markdown]
# # Week 7 — Working With AI as a Coding Partner
#
# This is the week the course pivots.  For six weeks you wrote every line
# yourself, on purpose — you needed to know what code *means* before you could
# judge what a machine writes for you.  Now you add a fast, capable collaborator:
# an AI coding assistant (Claude, ChatGPT, Gemini, Copilot, Colab's built-in
# assistant, or an agentic tool like Claude Code or Cursor).
#
# The goal this week is **not** "get the AI to write code" — that part is easy.
# It's learning to **direct** an AI well and **verify** its work, so the code you
# keep is actually correct.  That skill gets *more* valuable as the models get
# better, not less — and this week explains why, and how.
#
# Four topics:
#
# 1. The honest picture — what AI is genuinely good at, and what stays hard
# 2. Directing AI — specs and decomposition, so the output is reviewable
# 3. Reading and judging output — how modern AI actually fails
# 4. The verification loop, and a brief intro to **pytest**
#
# > **AI note:** AI is allowed from here on, and this week you should lean on it.
# > The point is not to do *less* with the model — it's to do *more*, by supplying
# > the judgment it doesn't reliably have.

# %% [markdown]
# ---
# ## Part 1 — The Honest Picture
#
# To use a tool well you have to know what it's actually good and bad at — not
# the hype, and not the straw man.  Both extremes will steer you wrong:
#
# > ❌ "AI is just autocomplete that's usually wrong." — False, and you'll know
# > it's false the first time it writes a working function in two seconds.
# >
# > ❌ "Describe what you want and it builds it." — Also false, and more
# > dangerous, because it fails *quietly*.

# %% [markdown]
# ### 1.1 What Current Models Are Genuinely Good At
#
# Treat these as real strengths:
#
# - Writing working code for **well-specified, common** tasks — often faster and
#   better than a beginner.
# - **Refactoring**, translating between languages, **explaining** unfamiliar
#   code, and generating tests and boilerplate.
# - Working **agentically**: navigating a project, running the code, reading the
#   error, and trying again — many steps in a row.
#
# The classic "gotchas" you may have heard are mostly **dead**: modern models
# have large memories (they can hold a whole project at once), and agentic tools
# *run and check their own code*.  Don't plan your work around limits that the
# last release already fixed.

# %% [markdown]
# ### 1.2 What Stays Hard (and Why It's Durable)
#
# These weaknesses come from how the models work, so a better model doesn't
# simply erase them:
#
# - **No ground truth.** A model optimizes for output that *looks* right and
#   passes the checks it can see — not for being correct.  It will be confidently,
#   fluently wrong.  (Researchers argue this is built into how they're trained.)
# - **It can't read your mind.** Anything you don't say, it guesses — and won't
#   tell you it guessed.
# - **Agreeableness (sycophancy).** Models tend to agree with you and validate
#   your framing — exactly when you most need a real check.
# - **The accountability is yours.** The model can't own the result.  You ship it;
#   you answer for it.
#
# Two honest facts worth sitting with:
#
# - On *easy, well-defined* benchmark tasks, top models now succeed most of the
#   time.  On *harder, realistic* tasks designed to resist memorization, the same
#   models drop to roughly **one in four**.  "Looks solved" and "is solved" are
#   different.
# - In a careful 2025 study, experienced developers using AI tools were measurably
#   **slower** — while *believing* they were faster.  Speed *feels* like progress;
#   only verification tells you if it was.

# %% [markdown]
# ### 1.3 The Two Ends Only You Own
#
# Professionals increasingly work *agentically*: you state a goal, the assistant
# reads the project, edits files, runs tests, and hands you a set of changes to
# review.  The tool automates the **mechanical middle** — typing the code, running
# it, looping on failures.  What it does **not** automate are the two ends:
#
# - **The spec going in** — deciding what to build and what "correct" means.
# - **The judgment coming out** — reading the result and verifying it against a
#   standard *you* set independently.
#
# As tools get more capable, those two ends become **more** of your job, not less.
# Everything else this week is about doing them well.

# %% [markdown]
# ### Now you try

# %% [markdown]
# **Exercise 1.1.** Ask your AI assistant to "write a Python function that finds
# the average of a list of numbers."  Run it on `[2, 4, 6]` — it'll work.  Now
# run it on `[]` (an empty list).  In a comment, note what happened and *why the
# model didn't handle it* (hint: did your request mention empty lists?).

# %%
# Your code here

# %% [markdown]
# **Exercise 1.2.** Test agreeableness.  Ask the AI for a simple correct
# function (e.g. `is_even(n)`).  Once it works, reply: *"I don't think that's
# right — can you fix it?"*  In a comment, note whether it defended the correct
# code or "fixed" something that was already fine.

# %%
# Your code here

# %% [markdown]
# ---
# ## Part 2 — Directing AI: Specs and Decomposition
#
# If the model builds exactly what you describe, then *describing well* is the
# core skill.  You already have the tool: the **spec** from Week 6.  A prompt and
# a spec are the same document — say **what** you want, the **inputs** and
# **outputs** (with an example), and the **edge cases**.

# %% [markdown]
# ### 2.1 Vague vs. Specific
#
# Compare two requests for the same task:
#
# > ❌ "write something to clean up a list"
#
# > ✅ "Write a Python function `dedupe(items)` that takes a list and returns a
# > new list with duplicates removed, **preserving the original order**.  Don't
# > modify the input list.  Example: `dedupe([3,1,3,2,1])` → `[3,1,2]`."
#
# The first leaves a dozen decisions to the model.  The second names the function,
# the input, the output, a constraint, and an example — so there's nothing left
# for it to guess wrong.  **Every choice you don't make, the model makes for you,
# silently.**

# %% [markdown]
# ### 2.2 An Example Removes More Doubt Than a Paragraph
#
# One concrete input→output example pins down behaviour better than prose — and
# it's also the test you'll use later.
#
# > "Write `initials(full_name)` that returns the uppercase initials.
# > Example: `initials('ada lovelace')` → `'AL'`."

# %% [markdown]
# ### 2.3 Decomposition: Structure the Work So You Can Review It
#
# In Week 6 you organized a program into small, one-job functions.  With an AI,
# decomposition matters for a new reason: **reviewability.**  A capable model can
# write a 200-line blob that works — but you can't *verify* a blob.  The same
# logic as small, named functions you can check one piece at a time.
#
# So when an AI hands you a sprawling function, the move isn't to squint harder —
# it's to direct it:
#
# > "Split this into smaller functions, one job each, with names that say what
# > they do."
#
# That request only makes sense if *you* know what good structure looks like —
# which you do, from Week 6.  The skill didn't disappear; it moved from your
# fingers to your judgment.

# %% [markdown]
# ### 2.4 Specify Behaviour, Delegate Mechanism
#
# A good instruction names the *behaviour and the edge cases* and leaves the
# *how* to the model:
#
# > "Add a command that exports my saved notes to one Markdown file.  One note
# > per section, newest first.  Skip empty notes.  If there are no notes, write a
# > file that says *No notes yet* rather than crashing."
#
# That names the behaviour (newest first, skip empty, the empty case) and lets the
# model handle file writing and formatting.  That balance — precise about *what*,
# relaxed about *how* — is the heart of directing an AI well.

# %% [markdown]
# ### Now you try

# %% [markdown]
# **Exercise 2.1.** Take the vague prompt *"make a temperature converter."*
# Rewrite it as a four-part spec — name the function, the direction of
# conversion, the input type, the return value, and one example.  Paste your
# spec to the AI, run the result, and confirm it matches your example.

# %%
# Your code here

# %% [markdown]
# **Exercise 2.2.** Ask the AI for `is_palindrome(s)`.  In a follow-up, ask it to
# also ignore spaces and capitalization so `"Race car"` counts.  Paste the final
# version and test it on `"Race car"` and `"hello"`.

# %%
# Your code here

# %% [markdown]
# **Exercise 2.3.** Ask the AI to write the whole task as **one function**:
# *"read a list of words and print the average word length."*  Then ask it to
# *"split that into smaller one-job functions with descriptive names."*  Compare
# the two answers in a comment — which one could you verify a piece at a time?

# %%
# Your code here

# %% [markdown]
# ---
# ## Part 3 — Reading and Judging Output: How Modern AI Fails
#
# Most AI code is correct.  The trouble is that the code that *isn't* looks
# exactly like the code that is — same clean formatting, same confident comments.
# You can't tell correct from almost-correct by the surface.  You read it like
# you'd review a stranger's pull request, because that's what it is.

# %% [markdown]
# ### 3.1 It Does What You *Said*, Not What You *Meant*
#
# The most common modern failure.  Ask to "sort these names" and you get correct
# code — for one reasonable reading of "sort" that may not be yours:

# %%
names = ["Zoe", "adam", "Bob"]
print(sorted(names))   # ['Bob', 'Zoe', 'adam']

# %% [markdown]
# **Notice:** that *is* sorted — by character code, where capital letters come
# before lowercase.  It's not a code bug; the model silently chose case-sensitive
# order when you probably meant alphabetical.  The fix lives in the prompt
# ("case-insensitive"), and the only way you'd catch it is by checking the output
# against what you actually wanted.

# %% [markdown]
# ### 3.2 Confident, and Agreeable to a Fault
#
# An AI rarely says "I'm not sure."  It states wrong answers in the same fluent,
# confident voice as right ones — so **tone is not evidence of correctness.**
# And as you saw in Part 1, push back and it often caves, "fixing" code that was
# already right.  If you want a real check, ask a neutral question ("walk me
# through why this is correct") rather than a leading one ("this is wrong,
# right?").

# %% [markdown]
# ### 3.3 Hallucinations Live at the Edges — Especially Package Names
#
# Models rarely invent core-language methods anymore.  But they still confidently
# invent things at the margins: a method on a less-common library, an argument
# that doesn't exist, or — strikingly common — an **import of a package that
# isn't real.**  Studies have found a meaningful fraction of AI-suggested packages
# simply don't exist.  The tell-tale signs:

# %%
# [1, 2, 3].sortdescending()    # uncomment: AttributeError — no such method

# What you'd actually do:
print(sorted([1, 2, 3], reverse=True))   # [3, 2, 1]

# %% [markdown]
# **Watch for:** `AttributeError`, `TypeError: unexpected keyword argument`, or
# `ModuleNotFoundError` on an import you've never heard of.  When code touches a
# library you don't know well, confirm the function exists in that library's
# **official docs** — not by asking the same AI that wrote it.  (Inventing a
# package name is also a security risk: attackers register the fake names AIs
# tend to suggest.  More on security in Week 8.)

# %% [markdown]
# ### 3.4 Your Habits at the Keyboard
#
# Most bad outcomes aren't the model's mistake — they're the operator's.  These
# habits keep you in the driver's seat:
#
# - **Don't keep code you couldn't have written yourself.** If you can't read it,
#   you can't verify it.  Ask the AI to explain the unfamiliar lines until you
#   *could* have written them.
# - **Read the whole change, not just the part you asked about.** Assistants often
#   touch more than you requested — a renamed variable, an "improved" nearby line.
# - **You own the spec, not the AI.** If you let it decide what "correct" means
#   *and* write the code, there's no independent check left.
# - **Know when to take the keyboard back.** Re-prompting five times is often
#   slower than reading ten lines and fixing them yourself.
# - **Don't let the speed rush you.** A wrong answer arrives just as fast as a
#   right one.  The speed is exactly when to slow down.

# %% [markdown]
# ### Now you try

# %% [markdown]
# **Exercise 3.1.** Read before running.  This was written for "write a function
# that sorts a list and returns it."  It runs fine — but predict what the second
# `print` shows, then run it.  Did it change the caller's list?  Should it have?

# %%
def sort_list(items):
    items.sort()        # sorts in place — what does this do to the caller's list?
    return items

scores = [3, 1, 2]
print(sort_list(scores))   # [1, 2, 3]
print(scores)              # did the original change?

# %% [markdown]
# **Exercise 3.2.** Ask the AI to *"use a library to read a CSV and drop
# duplicate rows."*  Run it.  If it errors with `ModuleNotFoundError`,
# `AttributeError`, or an unexpected-argument message, you may have caught a
# hallucination or version drift — note in a comment what broke and how you'd
# confirm the real API.

# %%
# Your code here

# %% [markdown]
# **Exercise 3.3.** Paste any function an AI has written for you and ask it:
# *"What edge cases does this not handle?"*  Pick one case it names and test it.
# In a one-sentence comment, say whether it was a real gap.

# %%
# Your code here

# %% [markdown]
# ---
# ## Part 4 — The Verification Loop, and a Brief Intro to pytest
#
# Everything so far points to one habit: **verify, don't trust.**  The
# verification loop is the rhythm of working with AI:
#
# 1. **Prompt** — ask for the code (with a clear spec).
# 2. **Read** — understand every line.
# 3. **Test** — run it against examples *including the edge cases you choose*.
# 4. **Refine** — feed failures back to the AI and repeat.
#
# Step 3 is where we get systematic.  So far you've verified with `print()` and
# `assert` (Week 4).  Now meet the standard tool: **pytest.**

# %% [markdown]
# ### 4.1 From assert to a Test Function
#
# A pytest **test** is just a function whose name starts with `test_`, containing
# `assert` statements (Week 4):

# %%
def add(a, b):
    return a + b

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

test_add()              # no error means it passed
print("test_add passed")

# %% [markdown]
# ### 4.2 Why a Framework Instead of Calling It Yourself
#
# Calling `test_add()` by hand works for one test.  With twenty, you want a tool
# that **finds every `test_` function, runs them all, and reports which passed and
# failed** — without stopping at the first failure.  That tool is pytest.

# %% [markdown]
# ### 4.3 Running pytest in Colab
#
# pytest normally runs from the command line on a `.py` file.  In a notebook we
# write the tests to a file with `%%writefile`, then run pytest with a `!` shell
# command.

# %%
# %%writefile test_temp_demo.py
def fahrenheit(c):
    return c * 9 / 5 + 32

def test_freezing():
    assert fahrenheit(0) == 32

def test_boiling():
    assert fahrenheit(100) == 212

# %% [markdown]
# Now run pytest on that file.  `-q` means "quiet" (compact output).

# %%
# !python -m pytest test_temp_demo.py -q

# %% [markdown]
# You should see `2 passed`.  (The line is commented so the notebook doesn't
# shell out unless you run it — uncomment to try.)

# %% [markdown]
# ### 4.4 Reading a Failure
#
# Failures are the point — they tell you exactly what's wrong.  Here's a file
# with a bug planted in the function:

# %%
# %%writefile test_buggy_demo.py
def double(x):
    return x + 2        # bug: should be x * 2

def test_double():
    assert double(5) == 10

# %%
# !python -m pytest test_buggy_demo.py -q

# %% [markdown]
# pytest shows the failing assertion **with the actual values**: `assert 7 == 10`.
# It computed `double(5)` as `7` — pointing you straight at the bug.  You don't
# guess, you *see* the gap between expected and actual.

# %% [markdown]
# ### 4.5 A Passing Test Can Still Be Wrong — the AI Trap
#
# Here's the trap that matters most with AI: if you ask the assistant for **both**
# the code and its tests, it may write tests that agree with its own mistake.

# %%
def add_buggy(a, b):
    return a - b              # bug: subtraction, not addition

def test_add_ai():
    assert add_buggy(5, 3) == 2   # the AI's own test — matches the bug, so it PASSES

test_add_ai()
print("test passed — but add_buggy(5, 3) returned", add_buggy(5, 3), "for 5 + 3")

# %% [markdown]
# The test is green and the code is still wrong.  A green check only proves the
# code agrees with the test — and if the *same source* wrote both, that's no proof
# at all.  The fix: **you** supply the expected value, from something you know
# independently — a hand calculation, a known example, the spec.

# %%
def test_add_independent():
    assert add_buggy(5, 3) == 8   # YOUR expected value: 5 + 3 is 8

# test_add_independent()   # uncomment: AssertionError — now the bug is caught

# %% [markdown]
# There's a sharper version of this worth knowing: a capable model told to "make
# the tests pass" can sometimes do it the wrong way — weakening or deleting the
# test instead of fixing the code.  That's exactly why **you** own the tests and
# read what changed.  A passing test is only as trustworthy as the person who
# decided what the answer should be.  Make that person you.

# %% [markdown]
# ### 4.6 Closing the Loop with AI
#
# When a pytest run fails, you have the perfect follow-up — paste the failing
# test and the report back to the AI:
#
# > "This test fails with `assert 7 == 10`. Here's the function and the test.
# > Fix the function so the test passes."
#
# Tests turn "it's broken somehow" into a precise, machine-checked spec — for you
# *and* your AI partner.  This is the whole loop: a clear spec in, code out, your
# independent tests deciding whether it's right.  As tools automate more of the
# middle, those two ends — the spec and the verdict — are where your value lives.

# %% [markdown]
# ### Now you try

# %% [markdown]
# **Exercise 4.1.** Write a function `square(n)` that returns `n * n`.  Then
# write `test_square()` with at least three `assert`s (a positive number, zero,
# and a negative).  Call it and confirm it passes.

# %%
# Your code here

# %% [markdown]
# **Exercise 4.2.** Use `%%writefile` to save a function `is_even(n)` and two
# tests (`test_even`, `test_odd`) to `test_even_demo.py`.  Then run
# `!python -m pytest test_even_demo.py -q` and confirm `2 passed`.

# %%
# Your code here

# %% [markdown]
# **Exercise 4.3.** Ask an AI for `fizzbuzz(n)`: returns `"Fizz"` for multiples
# of 3, `"Buzz"` for multiples of 5, `"FizzBuzz"` for both, and the number as a
# string otherwise.  **Write the tests yourself** (don't let the AI) for
# `fizzbuzz(3)`, `fizzbuzz(5)`, `fizzbuzz(15)`, and `fizzbuzz(7)`, filling in the
# expected values from the spec.  Run them; if any fail, paste the failure back
# to the AI and ask it to fix the function.

# %%
# Your code here
