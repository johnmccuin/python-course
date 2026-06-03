# %% [markdown]
# # Week 5 — Classes and Objects
#
# In Week 3 you used objects from the standard library — `date`, `Path`,
# `Counter` — and noticed the pattern: an object bundles **data** (attributes,
# like `today.year`) and **behaviour** (methods, like `today.strftime()`) under
# one name.  This week you learn to build your own.
#
# A **class** is a blueprint.  An **instance** is one thing built from that
# blueprint.  `date` is a class; a particular `today` is an instance of it.
# Classes are how Python programs model "a thing that has some data and some
# things it can do" — a bank account, a player in a game, a timer.
#
# Four topics:
#
# 1. Defining a class — `__init__`, `self`, attributes, instances
# 2. Methods — behaviour that works on an instance's own data
# 3. Many instances, each with its own data — and printing them readably
# 4. Reading and judging class code — common bugs, and when a class is overkill

# %% [markdown]
# ---
# ## Part 1 — Defining a Class
#
# A class gathers related data and the functions that work on it.  Here's a
# minimal one — a bank account.  Read the three new pieces, then we'll name them.

# %%
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner        # an attribute: data stored on the instance
        self.balance = balance

    def deposit(self, amount):    # a method: a function that belongs to the class
        self.balance += amount

# %% [markdown]
# Three new things to name — you'll meet all three in nearly every class:
#
# - **`__init__`** — the *constructor*.  It runs automatically when you create
#   an instance and sets up its starting data.  (The double underscores mark it
#   as special to Python; say it "dunder init".)
# - **`self`** — the instance the method is working on.  Every method takes
#   `self` as its first parameter; through it, a method reads and writes that
#   instance's own attributes.
# - **attributes** (`self.owner`, `self.balance`) — the data each instance
#   carries.

# %% [markdown]
# ### 1.1 Creating and Using an Instance
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
# ### 1.2 The Dot Connects an Instance to Its Data and Methods
#
# `account.balance` reads an **attribute** (no parentheses — it's a value).
# `account.deposit(50)` calls a **method** (parentheses — it's an action).
# It's the same dot you've used since Week 1 on strings and lists.

# %%
account = BankAccount("Bob")    # balance uses the default of 0
print(account.owner, account.balance)
account.deposit(25)
account.deposit(25)
print(account.balance)          # 50

# %% [markdown]
# ### Now you try

# %% [markdown]
# **Exercise 1.1.** Define a class `Dog` with an `__init__` that stores a `name`
# attribute.  Create a `Dog` named `"Rex"` and print its `name`.

# %%
# Your code here

# %% [markdown]
# **Exercise 1.2.** Add a method `bark(self)` to your `Dog` that returns the
# string `f"{self.name} says woof!"`.  Create a dog and call `bark()`.

# %%
# Your code here

# %% [markdown]
# **Exercise 1.3.** Define a class `Counter` with `__init__` that sets
# `self.count = 0`, and a method `increment(self)` that adds 1 to `self.count`.
# Create one, increment it twice, and print `count`.

# %%
# Your code here

# %% [markdown]
# ---
# ## Part 2 — Methods: Behaviour That Uses `self`
#
# A method is a function defined inside a class.  Because it receives `self`, it
# can read and change any of the instance's data — and it's the natural home for
# the **rules** that protect that data.

# %% [markdown]
# ### 2.1 A Method That Enforces a Rule
#
# Here a `withdraw` method refuses to overdraw the account.

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
# the class, right next to the `balance` it protects.  Bundling data with the
# rules that govern it is the whole point of a class.

# %% [markdown]
# ### 2.2 Methods Can Call Other Methods
#
# A method can use `self.` to call another method on the same instance.

# %%
class Wallet:
    def __init__(self):
        self.dollars = 0

    def add(self, amount):
        self.dollars += amount

    def add_tip(self, amount, percent):
        self.add(amount)                       # reuse our own method
        self.add(amount * percent / 100)       # add the tip too

w = Wallet()
w.add_tip(40, 20)        # a $40 item plus a 20% tip
print(w.dollars)         # 48.0

# %% [markdown]
# ### 2.3 Methods Can Return Computed Values
#
# A method doesn't have to change the instance — it can just compute something
# from the instance's data and return it.

# %%
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

r = Rectangle(3, 4)
print(r.area())        # 12
print(r.perimeter())   # 14

# %% [markdown]
# ### Now you try

# %% [markdown]
# **Exercise 2.1.** Give the `Counter` from Exercise 1.3 a `reset(self)` method
# that sets `self.count` back to 0.  Increment a few times, reset, and confirm
# `count` is 0 again.

# %%
# Your code here

# %% [markdown]
# **Exercise 2.2.** Write a class `Thermostat` with `__init__(self, temp)` that
# stores `self.temp`, plus methods `warmer(self)` and `cooler(self)` that raise
# or lower the temperature by 1.  Create one at 70, warm it twice, cool it once,
# and print the result.

# %%
# Your code here

# %% [markdown]
# **Exercise 2.3.** Add a method `is_square(self)` to the `Rectangle` class that
# returns `True` when width and height are equal.  Test it on a 3×4 and a 5×5.

# %%
# Your code here

# %% [markdown]
# ---
# ## Part 3 — Many Instances, Each With Its Own Data
#
# The reason classes matter: every instance carries its **own** copy of the
# attributes.  Build ten accounts and each tracks its own balance.

# %% [markdown]
# ### 3.1 Separate Instances Don't Share Data

# %%
a = BankAccount("Ada", 100)
b = BankAccount("Bob", 0)
a.deposit(25)
print(a.balance, b.balance)   # 125 0 — b is untouched

# %% [markdown]
# ### 3.2 A List of Instances
#
# Instances are ordinary values, so you can put them in a list and loop over
# them — combining everything from Weeks 2–3 with this week's classes.

# %%
accounts = [
    BankAccount("Ada", 100),
    BankAccount("Bob", 40),
    BankAccount("Cy", 75),
]

total = 0
for acct in accounts:
    total += acct.balance

print(f"Total held across {len(accounts)} accounts: {total}")   # 215

# %% [markdown]
# ### 3.3 Make Instances Print Readably with `__str__`
#
# By default, printing an instance shows something unhelpful like
# `<__main__.BankAccount object at 0x7f...>`.  Define a `__str__` method that
# returns a string, and `print()` will use it.

# %%
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def __str__(self):
        return f"{self.name} (grade {self.grade})"

s = Student("Ada", 95)
print(s)                 # Ada (grade 95) — much nicer than the default

# %% [markdown]
# `__str__` is another *dunder* method, like `__init__`.  Python calls it
# automatically whenever an instance needs to become a string.

# %% [markdown]
# ### Now you try

# %% [markdown]
# **Exercise 3.1.** Create two different `Dog` instances (from Part 1) with
# different names.  Call `bark()` on each to confirm they carry their own
# `name` — each should say its own.

# %%
# Your code here

# %% [markdown]
# **Exercise 3.2.** Make a list of three `Rectangle` instances of different
# sizes.  Loop over the list and print each one's area.

# %%
# Your code here

# %% [markdown]
# **Exercise 3.3.** Add a `__str__` method to `Rectangle` that returns
# something like `"3x4 rectangle"`.  Create one and `print()` it to confirm.

# %%
# Your code here

# %% [markdown]
# ---
# ## Part 4 — Reading and Judging Class Code
#
# You'll read far more class code than you write — your own from last week, a
# teammate's, an example online.  Two skills matter most: spotting the common
# bugs, and judging whether something *should* be a class at all.

# %% [markdown]
# ### 4.1 The Most Common Bug: a Missing `self`
#
# Inside a method, an attribute is always reached through `self`.  Use the bare
# name and Python thinks you mean a brand-new local variable — which doesn't
# exist yet.

# %%
class BrokenCounter:
    def __init__(self):
        self.count = 0
    def bump(self):
        count = count + 1      # BUG: should be self.count = self.count + 1

c = BrokenCounter()
# c.bump()   # uncomment: UnboundLocalError — `count` is not defined here

# %% [markdown]
# `count` on its own is a new local variable with no value, so `count + 1`
# fails.  The attribute is `self.count`.  Whenever a method needs the instance's
# own data, it goes through `self` — every time.

# %% [markdown]
# ### 4.2 Another Bug: Forgetting `self` in the Method Definition
#
# Every method's first parameter must be `self`.  Leave it out and the call
# passes the argument into the wrong slot.

# %%
class Greeter:
    def __init__(self, name):
        self.name = name
    def greet():                 # BUG: no self parameter
        return "hello"

g = Greeter("Ada")
# g.greet()   # uncomment: TypeError — greet() takes 0 args but 1 was given

# %% [markdown]
# **Notice:** Python automatically passes the instance as the first argument, so
# a method *must* have a parameter to receive it.  The fix is `def greet(self):`.

# %% [markdown]
# ### 4.3 The Judgment Call: Does This *Need* to Be a Class?
#
# A class earns its keep when **data and behaviour travel together** and you have
# **more than one** of the thing (many accounts, many students).  When you just
# need to turn some input into some output once, a plain **function** is simpler
# — and simpler is better.
#
# - *Use a class:* several bank accounts, each tracking its own balance over time.
# - *Use a function:* "convert these Celsius readings to Fahrenheit" — there's no
#   state to carry, so `def to_f(c): ...` is plenty.
#
# Reaching for a class when a function would do adds names and indentation that
# buy you nothing.  Recognizing the difference is a real skill.

# %% [markdown]
# ### Now you try

# %% [markdown]
# **Exercise 4.1.** Read before you run.  The class below was written for
# "store a width and height and return the area," but it has the missing-`self`
# bug from 4.1.  Find it, fix it, then confirm `Box(3, 4).area()` returns `12`.
#
# ```python
# class Box:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#     def area(self):
#         return width * height
# ```

# %%
# Your code here

# %% [markdown]
# **Exercise 4.2.** For each task, decide **class or function** and write one
# sentence saying why.  (Don't implement them — just judge.)
#
# 1. Round a price up to the nearest dollar.
# 2. Track a player's score, level, and lives across a whole game.
# 3. Count the vowels in a single word.

# %%
# Your answer here (as comments)

# %% [markdown]
# **Exercise 4.3.** Tie the week together.  Write a class `Timer` that starts at
# `0`, has a `tick(self)` method that adds 1, and a `read(self)` method that
# returns the count.  Create one, tick it three times, and confirm `read()`
# returns `3`.  Then add a `__str__` that returns `f"Timer at {self.count}"` and
# print the instance.

# %%
# Your code here
