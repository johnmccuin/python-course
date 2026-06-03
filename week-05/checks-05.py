"""Autograder check functions for Week 5 Homework.

This module is fetched by the homework notebook at runtime and is
intentionally kept separate so students cannot see the check logic
while working on their answers.

Every exercise tests a concept demonstrated in lecture-05 (classes and
objects: __init__, self, attributes, methods, instances, __str__), building
on everything from Weeks 1-4.
"""


def _make(cls, *args):
    """Instantiate a student's class, turning failures into readable hints."""
    try:
        return cls(*args), None
    except Exception as exc:
        return None, f"creating {cls.__name__}({', '.join(repr(a) for a in args)}) raised {type(exc).__name__}: {exc}"


def check_ex1(Dog):
    if not isinstance(Dog, type):
        return "Dog doesn't seem to be a class — define it with `class Dog:`."

    rex, err = _make(Dog, "Rex")
    if err:
        return err
    if not hasattr(rex, "name"):
        return "A Dog has no `name` attribute — set `self.name = name` in __init__."
    if rex.name != "Rex":
        return f'Dog("Rex").name is {rex.name!r}, expected "Rex".'
    if not hasattr(rex, "bark") or not callable(rex.bark):
        return "Dog needs a `bark` method."
    try:
        got = rex.bark()
    except Exception as exc:
        return f"Dog(\"Rex\").bark() raised {type(exc).__name__}: {exc} (did you include `self`?)"
    if got != "Rex says woof!":
        return f'Dog("Rex").bark() returned {got!r}, expected "Rex says woof!".'

    fifi, err = _make(Dog, "Fifi")
    if err:
        return err
    if fifi.bark() != "Fifi says woof!":
        return f'Dog("Fifi").bark() returned {fifi.bark()!r} — use self.name in the message.'
    return True


def check_ex2(Counter):
    if not isinstance(Counter, type):
        return "Counter doesn't seem to be a class — define it with `class Counter:`."

    c, err = _make(Counter)
    if err:
        return err
    if not hasattr(c, "count"):
        return "Counter has no `count` attribute — set `self.count = 0` in __init__."
    if c.count != 0:
        return f"A fresh Counter has count {c.count!r}, expected 0."
    if not hasattr(c, "increment") or not callable(c.increment):
        return "Counter needs an `increment` method."
    try:
        c.increment()
        c.increment()
        c.increment()
    except Exception as exc:
        return f"increment() raised {type(exc).__name__}: {exc} (remember `self.count = self.count + 1`)."
    if c.count != 3:
        return f"After three increments, count is {c.count!r}, expected 3."
    if not hasattr(c, "reset") or not callable(c.reset):
        return "Counter needs a `reset` method."
    c.reset()
    if c.count != 0:
        return f"After reset(), count is {c.count!r}, expected 0."
    return True


def check_ex3(Rectangle):
    if not isinstance(Rectangle, type):
        return "Rectangle doesn't seem to be a class — define it with `class Rectangle:`."

    r, err = _make(Rectangle, 3, 4)
    if err:
        return err
    for meth in ("area", "perimeter"):
        if not hasattr(r, meth) or not callable(getattr(r, meth)):
            return f"Rectangle needs a `{meth}` method."
    try:
        area = r.area()
        perim = r.perimeter()
    except Exception as exc:
        return f"calling Rectangle(3, 4) methods raised {type(exc).__name__}: {exc} (use self.width / self.height)."
    if area != 12:
        return f"Rectangle(3, 4).area() returned {area!r}, expected 12 (width * height)."
    if perim != 14:
        return f"Rectangle(3, 4).perimeter() returned {perim!r}, expected 14 (2 * (width + height))."

    sq, err = _make(Rectangle, 5, 5)
    if err:
        return err
    if sq.area() != 25:
        return f"Rectangle(5, 5).area() returned {sq.area()!r}, expected 25."
    return True


def check_ex4(BankAccount):
    if not isinstance(BankAccount, type):
        return "BankAccount doesn't seem to be a class — define it with `class BankAccount:`."

    # Default balance.
    a, err = _make(BankAccount)
    if err:
        return err + "  (give balance a default: `def __init__(self, balance=0):`)"
    if not hasattr(a, "balance"):
        return "BankAccount has no `balance` attribute — set `self.balance = balance` in __init__."
    if a.balance != 0:
        return f"A new BankAccount() has balance {a.balance!r}, expected 0 (the default)."

    # Deposit.
    if not hasattr(a, "deposit") or not callable(a.deposit):
        return "BankAccount needs a `deposit` method."
    try:
        a.deposit(50)
    except Exception as exc:
        return f"deposit(50) raised {type(exc).__name__}: {exc}"
    if a.balance != 50:
        return f"After deposit(50) on a new account, balance is {a.balance!r}, expected 50."

    # Withdraw — normal case.
    if not hasattr(a, "withdraw") or not callable(a.withdraw):
        return "BankAccount needs a `withdraw` method."
    try:
        result = a.withdraw(30)
    except Exception as exc:
        return f"withdraw(30) raised {type(exc).__name__}: {exc}"
    if a.balance != 20:
        return f"After withdraw(30) from 50, balance is {a.balance!r}, expected 20."
    if result != 20:
        return f"withdraw(30) returned {result!r}, expected the new balance 20."

    # Withdraw — overdraw guard.
    try:
        result = a.withdraw(100)   # balance is 20
    except Exception as exc:
        return f"withdraw(100) raised {type(exc).__name__}: {exc} — it should return a message, not crash."
    if result != "Insufficient funds":
        return (
            f"withdraw(100) on a balance of 20 returned {result!r}, "
            'expected the string "Insufficient funds".'
        )
    if a.balance != 20:
        return (
            f"After a failed withdraw(100), balance is {a.balance!r}, expected it to stay 20 — "
            "don't subtract when there are insufficient funds."
        )
    return True


def check_ex5(Student):
    if not isinstance(Student, type):
        return "Student doesn't seem to be a class — define it with `class Student:`."

    s, err = _make(Student, "Ada", 95)
    if err:
        return err
    try:
        text = str(s)
    except Exception as exc:
        return f"str(Student('Ada', 95)) raised {type(exc).__name__}: {exc}"
    if "object at 0x" in text:
        return (
            "Student is using the default text representation — define a "
            "`__str__(self)` method that returns the formatted string."
        )
    if text != "Ada (grade 95)":
        return f'str(Student("Ada", 95)) returned {text!r}, expected "Ada (grade 95)".'

    s2, err = _make(Student, "Bob", 72)
    if err:
        return err
    if str(s2) != "Bob (grade 72)":
        return f'str(Student("Bob", 72)) returned {str(s2)!r} — use self.name and self.grade.'
    return True


def check_ex6(Playlist):
    if not isinstance(Playlist, type):
        return "Playlist doesn't seem to be a class — define it with `class Playlist:`."

    p, err = _make(Playlist)
    if err:
        return err
    if not hasattr(p, "songs"):
        return "Playlist has no `songs` attribute — set `self.songs = []` in __init__."
    if p.songs != []:
        return f"A fresh Playlist().songs is {p.songs!r}, expected an empty list []."
    for meth in ("add", "count"):
        if not hasattr(p, meth) or not callable(getattr(p, meth)):
            return f"Playlist needs an `{meth}` method."
    try:
        if p.count() != 0:
            return f"A fresh Playlist().count() returned {p.count()!r}, expected 0."
        p.add("Yesterday")
        p.add("Let It Be")
    except Exception as exc:
        return f"calling add()/count() raised {type(exc).__name__}: {exc}"
    if p.count() != 2:
        return f"After adding two songs, count() returned {p.count()!r}, expected 2."

    # Independence of instances.
    other, err = _make(Playlist)
    if err:
        return err
    if other.count() != 0:
        return (
            f"A second, separate Playlist already has {other.count()} songs — "
            "each instance must get its own list. Set self.songs = [] inside __init__, "
            "not at the class level."
        )
    return True


def check_ex7(Thermostat):
    if not isinstance(Thermostat, type):
        return "Thermostat doesn't seem to be a class — define it with `class Thermostat:`."

    t, err = _make(Thermostat, 70)
    if err:
        return err
    if not hasattr(t, "temp"):
        return "Thermostat has no `temp` attribute — set `self.temp = temp` in __init__."
    if t.temp != 70:
        return f"Thermostat(70).temp is {t.temp!r}, expected 70."
    for meth in ("warmer", "cooler", "is_freezing"):
        if not hasattr(t, meth) or not callable(getattr(t, meth)):
            return f"Thermostat needs a `{meth}` method."
    try:
        t.warmer()
        t.warmer()
    except Exception as exc:
        return f"warmer() raised {type(exc).__name__}: {exc} (use self.temp)."
    if t.temp != 72:
        return f"After warmer() twice on 70, temp is {t.temp!r}, expected 72."

    # is_freezing logic.
    cold, _ = _make(Thermostat, 33)
    cold.cooler()   # -> 32
    if cold.is_freezing() is not True:
        return (
            f"Thermostat(33) then cooler() gives temp {cold.temp}; is_freezing() returned "
            f"{cold.is_freezing()!r}, expected True (32 or below counts as freezing)."
        )
    warm, _ = _make(Thermostat, 70)
    if warm.is_freezing() is not False:
        return f"Thermostat(70).is_freezing() returned {warm.is_freezing()!r}, expected False."
    return True
