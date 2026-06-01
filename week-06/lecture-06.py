# %% [markdown]
# # Week 6 — Specs, Decomposition, Architecture, and Classes
#
# Last week you learned to drive an AI and verify its work.  But "verify"
# assumes you already know what *correct* looks like.  This week is about the
# work that comes **before** the code — deciding what to build, breaking it
# into pieces, and arranging those pieces so they're easy to understand and
# change.  Then we introduce the most important tool for organizing related
# data and behaviour: the **class**.
#
# The thread running through all four parts is the same: *good software is
# mostly good decisions made before you type, not clever tricks typed in the
# moment.*  Four topics:
#
# 1. **Specs** — deciding what "done" means before you write code
# 2. **Decomposition** — breaking a big problem into small, named pieces
# 3. **Architecture** — how the pieces fit, and the cost of abstraction
# 4. **Classes** — bundling data and behaviour together (`__init__`, methods,
#    instances)
#
# > **AI note:** From here on, AI is allowed.  Everything this week makes you a
# > *better* AI driver — a spec is what you hand the model, decomposition is how
# > you keep its output reviewable, and classes are a structure you'll need to
# > read in almost any code it writes for you.

# %% [markdown]
# ---
# ## Part 1 — Writing a Spec
#
# A **spec** (specification) is a short, plain-language description of what a
# piece of code should do — written *before* the code exists.  It's the answer
# to "how will I know this is finished and correct?"
#
# Last week's mantra was *you own the spec, not the AI.*  This is where you
# write it down.  A useful spec for a function answers four questions:
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
# Once you write the code, the spec becomes the function's **docstring** — the
# triple-quoted string right under `def`.  Now the description lives with the
# code it describes.

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
# test (Week 5).  If these pass, the code matches the spec you wrote.

# %%
assert tip(50, 20) == 10.0    # ordinary case
assert tip(0, 20) == 0.0      # edge: zero bill
assert tip(100, 0) == 0.0     # edge: zero percent
print("matches spec")

# %% [markdown]
# **Notice:** the spec came first, and the checks came *straight from it* — not
# from the finished code.  That order matters.  If you write tests by reading
# your own code (or the AI's), you only prove the code agrees with itself.  The
# spec is your independent source of truth.

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
# and output, and name one edge case.  Write only the spec (a comment block),
# not the implementation.

# %%
# Your code here

# %% [markdown]
# **Exercise 1.3.** Here is a spec.  Write the three `assert` statements that
# check it — *without writing the function*.  (Reading the spec, you can decide
# the expected answers yourself.)
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
# this is the **function** (Week 3).
#
# The rule of thumb: **one function, one job.**  If you can't describe what a
# function does without saying "and", it's probably two functions.

# %% [markdown]
# ### 2.1 The Monolith — Everything in One Place
#
# Here's a task done as a single block: take a sentence, and report the average
# word length.  It works — but it does three jobs at once (split, measure,
# average), and you have to read all of it to understand any of it.

# %%
sentence = "the quick brown fox"
words = sentence.split()
lengths = [len(w) for w in words]
print(sum(lengths) / len(lengths))   # 4.0

# %% [markdown]
# ### 2.2 Decomposed — One Job Per Function
#
# Same task, broken into named steps.  Each function is tiny and does exactly
# one thing — and its *name* tells you what, so you can understand the whole
# without reading the parts.

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
# of numbers, not just word lengths.

# %% [markdown]
# ### 2.3 Decompose Before You Code
#
# The real win is doing this *before* writing the bodies.  Sketch the steps as
# function names with `pass`, confirm the shape makes sense, then fill them in.
# This is also the perfect unit to hand an AI: small, specified, one at a time.

# %%
def read_scores():  pass     # later: load numbers from a file
def best_score():   pass     # later: return the max
def report():       pass     # later: print a summary
print("the plan exists before the code does")

# %% [markdown]
# ### Now you try

# %% [markdown]
# **Exercise 2.1.** A task: *given a list of prices, print the total with 8%
# sales tax added.*  **Don't write it yet** — first, in a comment, list the
# small one-job steps you'd break it into (e.g. "sum the prices", …).  Name
# three.

# %%
# Your code here

# %% [markdown]
# **Exercise 2.2.** Now implement two of those steps as separate one-job
# functions (for example `subtotal(prices)` and `add_tax(amount, rate)`).  Keep
# each function to a single job — if you're tempted to write "and", split it.

# %%
# Your code here

# %% [markdown]
# **Exercise 2.3.** Here's a monolith that does three jobs at once.  Rewrite it
# as two or three named functions, then call them to get the same result.
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
# what names they share, where a change ripples to.  You don't need diagrams for
# a 50-line program — but two ideas pay off at every size.

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
# The cost (a new name, a function call) buys you nothing.  Compare that to
# `average(numbers)` from Part 2, which hides a real multi-step computation
# behind a name worth having.  The question is always: **does the name hide
# enough to earn its keep?**

# %% [markdown]
# ### 3.2 The Rule of Three — Don't Abstract Too Early
#
# A common mistake is building a flexible, general tool the first time you need
# something.  Usually you don't yet know what "general" should mean — so you
# guess wrong and the abstraction fits nothing well.
#
# A practical guideline: **write it inline the first time, copy it the second
# time, and only turn it into a function on the third.**  By then you've seen
# three real cases and know what they actually share.

# %%
# First time you need a greeting, just write it:
print("Hello, Ada!")
# Don't build a configurable GreetingFactory for one hello.

# %% [markdown]
# ### 3.3 Keep the Pieces Loosely Coupled
#
# Two pieces are **tightly coupled** when changing one forces you to change the
# other.  The looser the coupling, the safer each change.  The simplest way to
# loosen coupling: have functions **take inputs and return outputs**, instead of
# reaching out to shared global variables.

# %%
total = 0
def add_bad(n):
    global total          # reaches outside itself — tightly coupled, hard to test
    total += n

def add_good(running, n):
    return running + n     # everything it needs comes in; result comes out

print(add_good(10, 5))     # 15 — easy to test, no hidden state

# %% [markdown]
# **Notice:** `add_good` can be tested with a single `assert add_good(10, 5) ==
# 15` — everything it touches is in front of you.  `add_bad` depends on a
# `total` defined somewhere else, so you can't understand or test it in
# isolation.  Prefer the version whose every dependency is visible in its
# signature.

# %% [markdown]
# ### Now you try

# %% [markdown]
# **Exercise 3.1.** Here is an over-abstraction: a function that wraps something
# already clear.  Rewrite the `print` to skip the function entirely, and write a
# one-line comment on why the abstraction wasn't worth its cost.
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
# **Exercise 3.3.** Think of a small task you've written more than once (or
# imagine one).  In a comment, decide using the Rule of Three: have you hit it
# enough times to justify turning it into a function yet?  Write one sentence
# explaining your call.

# %%
# Your code here

# %% [markdown]
# ---
# ## Part 4 — Classes: Bundling Data and Behaviour
#
# In Week 3 you used objects from the standard library — `date`, `Path`,
# `Counter` — and noticed the pattern: an object bundles **data** (attributes,
# like `today.year`) and **behaviour** (methods, like `today.strftime()`) under
# one name.  Now you'll build your own.
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
# Three new things to name:
#
# - **`__init__`** — the *constructor*.  It runs automatically when you create
#   an instance, and sets up its starting data.  (The double underscores mark it
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
# payoff from Part 3 — the data and the rules that govern it are bundled
# together, so anyone using a `SafeAccount` gets the rule for free.

# %% [markdown]
# ### 4.5 A Common Bug: Forgetting `self`
#
# The single most common beginner mistake with classes is referring to an
# attribute by its bare name instead of `self.name`.  Inside a method, the bare
# name doesn't exist — the attribute lives on `self`.

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
# instance's own data, it goes through `self` — every time.

# %% [markdown]
# ### Now you try

# %% [markdown]
# **Exercise 4.1.** Define a class `Dog` with an `__init__` that stores a
# `name` attribute, and a method `bark(self)` that returns `f"{self.name} says
# woof!"`.  Create a `Dog` named `"Rex"` and call its `bark` method.

# %%
# Your code here

# %% [markdown]
# **Exercise 4.2.** Create two different `Dog` instances with different names.
# Call `bark` on each to confirm they carry their own `name` — each should
# print its own.

# %%
# Your code here

# %% [markdown]
# **Exercise 4.3.** Define a class `Rectangle` whose `__init__` takes `width`
# and `height` and stores them as attributes.  Add a method `area(self)` that
# returns `width * height` (remember: use `self.width`, not `width`).  Make a
# `Rectangle(3, 4)` and print its `area()` — expect `12`.

# %%
# Your code here

# %% [markdown]
# **Exercise 4.4.** Build a small class `Timer` that starts at `0` seconds.
# Give it a `tick(self)` method that adds 1 to its count, and a `read(self)`
# method that returns the current count.  Create one, tick it three times, and
# confirm `read()` returns `3`.  (This ties the week together: write a one-line
# spec first, decompose into the two methods, then implement.)

# %%
# Your code here
