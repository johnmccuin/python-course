# %% [markdown]
# # Week 6 — Specs, Decomposition, Architecture, and Classes
#
# Last week you learned to drive an AI and verify its work.  This week is about
# the work that surrounds the code an AI writes: deciding what to build,
# breaking it into pieces you can reason about, arranging those pieces so the
# whole stays understandable, and reading the structures — especially
# **classes** — that show up in almost everything a model produces.
#
# Start with the honest big picture, because it explains *why* these four topics
# are the right ones to spend a week on:
#
# > **Capable models have made *writing* code nearly free.  They have not made
# > *deciding what to build*, *keeping it understandable*, or *verifying it's
# > correct* free.**  Those three jobs are now the bulk of the work — and they
# > are exactly what this week is about.
#
# A second shift matters just as much.  The way professionals use AI today is
# not "ask for a function, paste it into a cell."  It's **agentic**: you state a
# goal, the assistant reads your whole project, edits several files, runs the
# tests itself, and hands you a **diff to review and steer**.  Your leverage is
# no longer how fast you type — it's the quality of the spec you give, the
# sharpness of your review, and the architectural calls only you can make.
#
# Four topics, each a skill that gets *more* valuable as the models improve:
#
# 1. **Specs** — saying precisely what "done" means; the main thing *you* author
# 2. **Decomposition** — structuring work so the AI's output stays reviewable
# 3. **Architecture** — keeping the whole comprehensible; the highest-leverage
#    human judgment
# 4. **Classes** — the data-plus-behaviour structure you'll read and judge
#    constantly
#
# > **AI note:** AI is allowed from here on, and this week you should lean on it.
# > The goal is not to do *less* with the model — it's to do *more*, by
# > supplying the judgment it doesn't reliably have.

# %% [markdown]
# ---
# ## Part 1 — Writing a Spec
#
# A **spec** (specification) is a short, plain-language description of what a
# piece of code should do — written *before* the code exists.  It's the answer
# to "how will I know this is finished and correct?"
#
# In agentic work the spec is the **main artifact you produce**.  The model
# writes the code; you write the spec the code is judged against.  A weak spec
# is the number-one reason a capable model produces confidently-wrong output —
# it filled your gaps with its own guesses.  A useful spec for a function
# answers four questions:
#
# 1. **What** does it do, in one sentence?
# 2. **Inputs** — what goes in, and of what type?
# 3. **Output** — what comes back, and of what type?
# 4. **Edge cases** — what are the tricky inputs, and what should happen?
#
# Those are the same four things a good *prompt* includes (Week 5) — because a
# spec and a prompt are the same document with different audiences.

# %% [markdown]
# ### 1.1 A Spec Is Just Words — Write It as a Comment First
#
# Before any code, the spec for a tip calculator might look like this.  Notice
# there's no Python here yet — just decisions made on purpose.

# %%
# SPEC: tip(amount, percent)
#   What:    compute the tip for a restaurant bill
#   Inputs:  amount  (float, dollars, >= 0)
#            percent (int, e.g. 20 for 20%)
#   Output:  float — the tip in dollars, rounded to 2 decimals
#   Edge:    a bill of 0 returns 0.0; percent of 0 returns 0.0

# %% [markdown]
# ### 1.2 The Spec Writes Itself Into a Docstring
#
# Once the code exists, the spec becomes the function's **docstring** — the
# triple-quoted string right under `def`.  Now the description lives with the
# code it describes (and an AI reading your file later uses it as context, too).

# %%
def tip(amount, percent):
    """Return the tip in dollars for a bill, rounded to 2 decimals."""
    return round(amount * percent / 100, 2)

print(tip(50, 20))   # 10.0

# %% [markdown]
# ### 1.3 Turn the Spec's Examples Into Checks
#
# The examples in a spec aren't decoration — they're tests waiting to be
# written.  Each "input → output" line becomes an `assert` (Week 4) or a pytest
# test (Week 5).  Writing them *from the spec* gives you a check the AI's code
# must satisfy — one you didn't let the AI define for you.

# %%
assert tip(50, 20) == 10.0    # ordinary case
assert tip(0, 20) == 0.0      # edge: zero bill
assert tip(100, 0) == 0.0     # edge: zero percent
print("matches spec")

# %% [markdown]
# **Notice:** the spec came first, and the checks came *straight from it* — not
# from the finished code.  That order is your independence.  If you let the AI
# write both the code *and* the tests, a green checkmark only proves the code
# agrees with itself (Week 5, 4.5).  The spec is the one place you, the human,
# decide what correct means.

# %% [markdown]
# ### 1.4 Specs Scale Up — and That's Where You Add the Most Value
#
# A four-line function spec is the starter rung.  In real work you'll write
# specs for whole *features* — and that's exactly the altitude where a model
# can't read your mind:
#
# > "Add a command that exports the user's saved notes to a single Markdown
# > file.  One note per section, newest first.  Skip empty notes.  If there are
# > no notes, write a file that says *No notes yet* rather than crashing."
#
# Notice what that spec does and doesn't do: it names the *behaviour and the
# edge cases* (newest first, skip empty, the empty-overall case) and leaves the
# *how* — file handling, sorting, formatting — to the model.  Specifying
# behaviour while delegating mechanism is the core skill of directing an AI well.

# %% [markdown]
# ### Now you try

# %% [markdown]
# **Exercise 1.1.** Write a spec — as a comment block, no code yet — for a
# function `initials(full_name)` that returns a person's uppercase initials
# (e.g. `"ada lovelace"` → `"AL"`).  Cover all four parts: what, inputs,
# output, and at least one edge case.

# %%
# Your code here

# %% [markdown]
# **Exercise 1.2.** Take this vague request: *"something to grade a quiz."*
# Pin it down into a four-part spec for a function — name it, decide the inputs
# and output, and name one edge case.  Then paste your spec to an AI as the
# prompt and read what it produces.  Did a clear spec get you closer on the
# first try than a vague one would have?

# %%
# Your code here

# %% [markdown]
# **Exercise 1.3.** Here is a spec.  Write the three `assert` statements that
# check it — *without writing the function, and without asking the AI for the
# expected answers*.  Reading the spec, you decide what's correct.
#
# > `clamp(n, low, high)` returns `n` if it's between `low` and `high`;
# > otherwise the nearest of the two bounds.  Example: `clamp(5, 0, 10)` is 5,
# > `clamp(-3, 0, 10)` is 0, `clamp(99, 0, 10)` is 10.

# %%
# Your code here

# %% [markdown]
# ---
# ## Part 2 — Decomposition
#
# A spec tells you *what* to build.  **Decomposition** is breaking that *what*
# into small pieces, each doing one clear job.  The unit you already have for
# this is the **function** (Week 3).  The rule of thumb: **one function, one
# job** — if you can't describe what it does without saying "and," it's probably
# two functions.
#
# Here's the part to be clear-eyed about: **a capable model does not need you to
# hand it bite-sized pieces.**  Give it the whole task and it will decompose
# perfectly well on its own.  So why learn this at all?  Because decomposition
# stopped being about helping the *model* and became about three things that are
# entirely *your* job:
#
# - **Reviewability** — a 200-line blob the AI wrote is hard to verify; the same
#   logic in small, named functions is easy to check one piece at a time.
# - **Steering** — knowing the pieces lets you direct structure precisely:
#   "pull the validation out into its own function," "this should return the
#   list, not print it."
# - **Understanding** — you can only maintain and change what you understand,
#   and named pieces are how a system stays understandable.

# %% [markdown]
# ### 2.1 The Monolith — Everything in One Place
#
# Here's a task done as a single block: take a sentence, report the average word
# length.  It works — but it does three jobs at once (split, measure, average),
# and you must read all of it to trust any of it.

# %%
sentence = "the quick brown fox"
words = sentence.split()
lengths = [len(w) for w in words]
print(sum(lengths) / len(lengths))   # 4.0

# %% [markdown]
# ### 2.2 Decomposed — One Job Per Function
#
# Same task, broken into named steps.  Each function is tiny and does exactly
# one thing — and its *name* tells you what, so you can verify the whole by
# reading the parts independently.

# %%
def split_words(text):
    return text.split()

def word_lengths(words):
    return [len(w) for w in words]

def average(numbers):
    return sum(numbers) / len(numbers)

# %% [markdown]
# Now the top-level code reads like the spec itself — a sentence of steps:

# %%
words = split_words("the quick brown fox")
print(average(word_lengths(words)))   # 4.0

# %% [markdown]
# **Notice:** the decomposed version has *more* lines, not fewer.  That's the
# trade.  What you buy is **names you can reason about**, pieces you can **test
# one at a time**, and parts you can **reuse** — `average` now works on any list
# of numbers.  When you review AI-written code, this is the shape you're steering
# it toward: not because the model can't write the blob, but because the named
# version is the one *you* can verify and change later.

# %% [markdown]
# ### 2.3 Decomposition Is How You Read a Diff
#
# In agentic work, the AI hands you a change spanning several functions or
# files.  You can't review what you can't navigate — so the structure *is* the
# reviewability.  When a diff is a single sprawling function, the right move
# isn't to squint harder; it's to ask the AI to **decompose it**:
#
# > "Split this into smaller functions, one job each, with names that say what
# > they do."
#
# That request only makes sense if *you* know what good decomposition looks
# like.  The skill didn't go away — it moved from your fingers to your judgment.

# %%
def read_scores():  pass     # naming the pieces is how you'll review the diff
def best_score():   pass
def report():       pass
print("you can judge this structure before a single body is written")

# %% [markdown]
# ### Now you try

# %% [markdown]
# **Exercise 2.1.** A task: *given a list of prices, print the total with 8%
# sales tax added.*  **Before writing or prompting**, in a comment, list the
# small one-job steps you'd break it into (e.g. "sum the prices," …).  Name
# three.  This is the structure you'd review an AI's version against.

# %%
# Your code here

# %% [markdown]
# **Exercise 2.2.** Now implement two of those steps as separate one-job
# functions (for example `subtotal(prices)` and `add_tax(amount, rate)`).  Keep
# each to a single job — if you're tempted to write "and," split it.

# %%
# Your code here

# %% [markdown]
# **Exercise 2.3.** Here's a monolith that does three jobs at once.  Ask an AI
# to split it into named one-job functions — then **read its answer critically**:
# are the names accurate? is each function really one job? Fix anything you'd
# have done differently.
#
# ```python
# nums = [4, 8, 15, 16, 23, 42]
# evens = [n for n in nums if n % 2 == 0]
# print(sum(evens) / len(evens))
# ```

# %%
# Your code here

# %% [markdown]
# ---
# ## Part 3 — Architecture and the Cost of Abstraction
#
# **Architecture** is how the pieces fit together: which part knows about which,
# what names they share, where a change ripples to.  This is the **highest-
# leverage human skill in AI-assisted coding**, and it's worth saying plainly
# why:
#
# > Because the model makes writing code nearly free, the friction that used to
# > discourage over-engineering is *gone*.  A model will happily add the
# > fifteenth slightly-different helper, couple everything together, and
# > duplicate logic — because it's optimizing for "works now," not "stays
# > understandable in six months."  Judgment about structure is precisely what
# > the model doesn't reliably supply.  **That judgment is your job, and it's the
# > part of this work that's hardest to automate.**

# %% [markdown]
# ### 3.1 Abstraction Has a Cost
#
# An **abstraction** is anything that hides detail behind a name — a function, a
# class, a module.  Decomposition (Part 2) was abstraction, and it was worth it.
# But it is **not free**: every abstraction is one more name to learn and one
# more layer to jump through when you're tracing a bug.
#
# Here's an abstraction that *isn't* worth it — a function wrapping a single
# operation that was already perfectly clear:

# %%
def add_one(x):
    return x + 1

print(add_one(4))   # 5 — but `4 + 1` was already obvious

# %% [markdown]
# `add_one(x)` is *more* to read than `x + 1`, and it hides nothing useful.
# The cost (a new name, a function call) buys you nothing.  Compare `average(numbers)`
# from Part 2, which hides a real multi-step computation behind a name worth
# having.  The question is always: **does the name hide enough to earn its
# keep?**  When you review AI output, this is a frequent edit — the model adds
# layers freely, and trimming the ones that don't pay off is your call.

# %% [markdown]
# ### 3.2 The Rule of Three — Don't Abstract Too Early
#
# A common mistake — and one AI makes constantly, because abstraction is cheap
# for it — is building a flexible, general tool the first time you need
# something.  Usually you don't yet know what "general" should mean, so the
# abstraction fits nothing well.
#
# A practical guideline: **write it inline the first time, copy it the second
# time, and only turn it into a function on the third.**  By then you've seen
# three real cases and know what they actually share.

# %%
# First time you need a greeting, just write it:
print("Hello, Ada!")
# Don't accept a configurable GreetingFactory from the AI for one hello.

# %% [markdown]
# ### 3.3 Keep the Pieces Loosely Coupled
#
# Two pieces are **tightly coupled** when changing one forces you to change the
# other.  The looser the coupling, the safer each change — and the easier each
# piece is to verify in isolation.  The simplest way to loosen coupling: have
# functions **take inputs and return outputs**, instead of reaching out to
# shared global variables.

# %%
total = 0
def add_bad(n):
    global total          # reaches outside itself — tightly coupled, hard to test
    total += n

def add_good(running, n):
    return running + n     # everything it needs comes in; result comes out

print(add_good(10, 5))     # 15 — easy to test, no hidden state

# %% [markdown]
# **Notice:** `add_good` can be checked with a single `assert add_good(10, 5) ==
# 15` — everything it touches is in front of you.  `add_bad` depends on a `total`
# defined somewhere else, so you can't understand, test, *or* safely let an AI
# modify it without tracing the whole program.  Loose coupling is what keeps an
# AI's change to one function from quietly breaking another.

# %% [markdown]
# ### Now you try

# %% [markdown]
# **Exercise 3.1.** Here is an over-abstraction: a function that wraps something
# already clear.  Rewrite the `print` to skip the function entirely, and write a
# one-line comment on why the abstraction wasn't worth its cost.  (This is the
# judgment you'll apply to AI output constantly.)
#
# ```python
# def multiply_by_two(x):
#     return x * 2
# print(multiply_by_two(9))
# ```

# %%
# Your code here

# %% [markdown]
# **Exercise 3.2.** The function below reaches out to a global variable, making
# it tightly coupled.  Rewrite it so everything it needs comes in as a parameter
# and the result comes back as a return value.
#
# ```python
# cart = [10, 20, 30]
# def cart_total():
#     return sum(cart)
# ```

# %%
# Your code here

# %% [markdown]
# **Exercise 3.3.** Ask an AI to write a small utility (anything — a function
# that formats a phone number, say).  Look at its answer through Part 3's lens:
# is anything over-abstracted? too generic for the one case you asked about?
# tightly coupled to something global?  In a comment, name one structural change
# you'd make and why.  If there's nothing to change, say why it's already sound.

# %%
# Your code here

# %% [markdown]
# ---
# ## Part 4 — Classes: Bundling Data and Behaviour
#
# In Week 3 you used objects from the standard library — `date`, `Path`,
# `Counter` — and noticed the pattern: an object bundles **data** (attributes,
# like `today.year`) and **behaviour** (methods, like `today.strftime()`) under
# one name.  Now you'll learn to build and read your own.
#
# Why classes get a whole part in an AI-assisted course: you will hand-write
# fewer classes from scratch than programmers once did — the model writes the
# boilerplate.  But AI-generated code is **full** of classes, so you must be able
# to **read them fluently, debug them, and judge whether one belongs at all.**
# That's the durable skill, and everything below builds toward it.
#
# A **class** is a blueprint.  An **instance** is one thing built from that
# blueprint.  `date` is a class; `today` is an instance of it.

# %% [markdown]
# ### 4.1 Defining a Class
#
# A class gathers related data and the functions that work on it.  Here's a
# minimal one — a bank account.  Read the three new pieces, then we'll name
# them.

# %%
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner        # an attribute: data stored on the instance
        self.balance = balance

    def deposit(self, amount):    # a method: a function that belongs to the class
        self.balance += amount

# %% [markdown]
# Three new things to name — and you'll meet all three in nearly every class an
# AI writes:
#
# - **`__init__`** — the *constructor*.  It runs automatically when you create
#   an instance and sets up its starting data.  (The double underscores mark it
#   as special to Python.)
# - **`self`** — the instance the method is working on.  Every method takes
#   `self` as its first parameter; through it, a method reads and writes that
#   instance's own attributes.
# - **attributes** (`self.owner`, `self.balance`) — the data each instance
#   carries.

# %% [markdown]
# ### 4.2 Creating and Using an Instance
#
# Calling the class like a function runs `__init__` and hands back a new
# instance.  Note you **don't** pass `self` — Python supplies it for you.

# %%
account = BankAccount("Ada", 100)   # runs __init__; self.owner="Ada", self.balance=100
print(account.owner)                # Ada      — read an attribute
print(account.balance)              # 100
account.deposit(50)                 # call a method; Python passes `account` as self
print(account.balance)              # 150

# %% [markdown]
# ### 4.3 Each Instance Has Its Own Data
#
# This is the whole point of a class: every instance carries its **own** copy of
# the attributes.  Two accounts don't share a balance.

# %%
a = BankAccount("Ada", 100)
b = BankAccount("Bob", 0)
a.deposit(25)
print(a.balance, b.balance)   # 125 0 — b is untouched

# %% [markdown]
# ### 4.4 Methods Can Use Other Attributes and Enforce Rules
#
# Because a method has access to `self`, it can use any of the instance's data —
# and it's the natural place to put rules that protect that data.  Here a
# `withdraw` method refuses to overdraw:

# %%
class SafeAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:           # a rule, living with the data it guards
            return "Insufficient funds"
        self.balance -= amount
        return f"New balance: {self.balance}"

acct = SafeAccount(50)
print(acct.withdraw(30))   # New balance: 20
print(acct.withdraw(100))  # Insufficient funds

# %% [markdown]
# **Notice:** the rule "you can't withdraw more than you have" lives *inside*
# the class, right next to the `balance` it protects.  That's the architectural
# payoff from Part 3 — data and the rules that govern it, bundled together.  When
# you read an AI's class, this is what you're checking: *are the right rules
# living with the right data, or did the model scatter them?*

# %% [markdown]
# ### 4.5 Reading for a Common Bug: a Missing `self`
#
# The single most common mistake in class code — and one you'll spot in AI
# output, not just your own — is referring to an attribute by its bare name
# instead of `self.name`.  Inside a method, the bare name doesn't exist; the
# attribute lives on `self`.  Train your eye to catch it in a diff:

# %%
class Counter:
    def __init__(self):
        self.count = 0
    def bump(self):
        count = count + 1      # BUG: should be self.count = self.count + 1

c = Counter()
# c.bump()   # uncomment: UnboundLocalError — `count` is not defined here

# %% [markdown]
# `count` on its own is a brand-new local variable with no value yet, so
# `count + 1` fails.  The attribute is `self.count`.  Whenever a method needs the
# instance's own data, it goes through `self` — every time.  Spotting this in
# someone else's code (human or model) is exactly the kind of review your
# fluency buys you.

# %% [markdown]
# ### 4.6 The Judgment Call: Does This *Need* to Be a Class?
#
# A class earns its keep when **data and behaviour travel together** and you have
# **more than one** of the thing (many accounts, many timers).  When you just
# need to transform some input into some output once, a plain **function** is
# simpler — and simpler is the Part 3 win.  An AI will sometimes reach for a
# class where a function would do; recognizing that is your call to make.
#
# - *Use a class:* several bank accounts, each tracking its own balance over time.
# - *Use a function:* "convert these Celsius readings to Fahrenheit" — no state
#   to carry, so `def to_f(c): ...` is plenty.

# %% [markdown]
# ### Now you try
#
# These exercises are short on purpose — use an AI freely, but **read every line
# it gives you** and make sure you could have written it.  That's the whole game.

# %% [markdown]
# **Exercise 4.1.** Define a class `Dog` with an `__init__` that stores a
# `name` attribute, and a method `bark(self)` that returns `f"{self.name} says
# woof!"`.  Create a `Dog` named `"Rex"` and call its `bark` method.  (Write it
# yourself first; then, if you like, ask an AI for its version and compare.)

# %%
# Your code here

# %% [markdown]
# **Exercise 4.2.** Create two different `Dog` instances with different names.
# Call `bark` on each to confirm they carry their own `name` — each should
# print its own.

# %%
# Your code here

# %% [markdown]
# **Exercise 4.3.** Read before you run.  An AI produced the class below for
# "a class that stores a width and height and returns its area."  It has the
# missing-`self` bug from 4.5.  Find it, fix it, then confirm `Rectangle(3, 4).area()`
# returns `12`.
#
# ```python
# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#     def area(self):
#         return width * height
# ```

# %%
# Your code here

# %% [markdown]
# **Exercise 4.4.** Tie the week together.  Write a one-line spec for a `Timer`
# that starts at `0`, has a `tick(self)` method that adds 1, and a `read(self)`
# method that returns the count.  Decide (Part 4.6) whether this *should* be a
# class — and in a comment, say why it earns one.  Then implement it, create one,
# tick it three times, and confirm `read()` returns `3`.

# %%
# Your code here
