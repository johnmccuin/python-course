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


def check_ex1(Robot):
    if not isinstance(Robot, type):
        return "Robot doesn't seem to be a class — define it with `class Robot:`."

    r2d2, err = _make(Robot, "R2D2")
    if err:
        return err
    if not hasattr(r2d2, "name"):
        return "A Robot has no `name` attribute — set `self.name = name` in __init__."
    if r2d2.name != "R2D2":
        return f'Robot("R2D2").name is {r2d2.name!r}, expected "R2D2".'
    if not hasattr(r2d2, "speak") or not callable(r2d2.speak):
        return "Robot needs a `speak` method."
    try:
        got = r2d2.speak()
    except Exception as exc:
        return f"Robot(\"R2D2\").speak() raised {type(exc).__name__}: {exc} (did you include `self`?)"
    if got != "R2D2 says beep boop!":
        return f'Robot("R2D2").speak() returned {got!r}, expected "R2D2 says beep boop!".'

    wall_e, err = _make(Robot, "WallE")
    if err:
        return err
    if wall_e.speak() != "WallE says beep boop!":
        return f'Robot("WallE").speak() returned {wall_e.speak()!r} — use self.name in the message.'
    return True


def check_ex2(Pedometer):
    if not isinstance(Pedometer, type):
        return "Pedometer doesn't seem to be a class — define it with `class Pedometer:`."

    p, err = _make(Pedometer)
    if err:
        return err
    if not hasattr(p, "steps"):
        return "Pedometer has no `steps` attribute — set `self.steps = 0` in __init__."
    if p.steps != 0:
        return f"A fresh Pedometer has steps {p.steps!r}, expected 0."
    if not hasattr(p, "step") or not callable(p.step):
        return "Pedometer needs a `step` method."
    try:
        p.step()
        p.step()
        p.step()
    except Exception as exc:
        return f"step() raised {type(exc).__name__}: {exc} (remember `self.steps = self.steps + 1`)."
    if p.steps != 3:
        return f"After three step() calls, steps is {p.steps!r}, expected 3."
    if not hasattr(p, "reset") or not callable(p.reset):
        return "Pedometer needs a `reset` method."
    p.reset()
    if p.steps != 0:
        return f"After reset(), steps is {p.steps!r}, expected 0."
    return True


def check_ex3(GardenPlot):
    if not isinstance(GardenPlot, type):
        return "GardenPlot doesn't seem to be a class — define it with `class GardenPlot:`."

    g, err = _make(GardenPlot, 3, 4)
    if err:
        return err
    for meth in ("area", "perimeter"):
        if not hasattr(g, meth) or not callable(getattr(g, meth)):
            return f"GardenPlot needs a `{meth}` method."
    try:
        area = g.area()
        perim = g.perimeter()
    except Exception as exc:
        return f"calling GardenPlot(3, 4) methods raised {type(exc).__name__}: {exc} (use self.length / self.width)."
    if area != 12:
        return f"GardenPlot(3, 4).area() returned {area!r}, expected 12 (length * width)."
    if perim != 14:
        return f"GardenPlot(3, 4).perimeter() returned {perim!r}, expected 14 (2 * (length + width))."

    sq, err = _make(GardenPlot, 5, 5)
    if err:
        return err
    if sq.area() != 25:
        return f"GardenPlot(5, 5).area() returned {sq.area()!r}, expected 25."
    return True


def check_ex4(Warehouse):
    if not isinstance(Warehouse, type):
        return "Warehouse doesn't seem to be a class — define it with `class Warehouse:`."

    # Default stock.
    w, err = _make(Warehouse)
    if err:
        return err + "  (give stock a default: `def __init__(self, stock=0):`)"
    if not hasattr(w, "stock"):
        return "Warehouse has no `stock` attribute — set `self.stock = stock` in __init__."
    if w.stock != 0:
        return f"A new Warehouse() has stock {w.stock!r}, expected 0 (the default)."

    # Receive.
    if not hasattr(w, "receive") or not callable(w.receive):
        return "Warehouse needs a `receive` method."
    try:
        w.receive(50)
    except Exception as exc:
        return f"receive(50) raised {type(exc).__name__}: {exc}"
    if w.stock != 50:
        return f"After receive(50) on a new warehouse, stock is {w.stock!r}, expected 50."

    # Ship — normal case.
    if not hasattr(w, "ship") or not callable(w.ship):
        return "Warehouse needs a `ship` method."
    try:
        result = w.ship(30)
    except Exception as exc:
        return f"ship(30) raised {type(exc).__name__}: {exc}"
    if w.stock != 20:
        return f"After ship(30) from 50, stock is {w.stock!r}, expected 20."
    if result != 20:
        return f"ship(30) returned {result!r}, expected the new stock 20."

    # Ship — over-ship guard.
    try:
        result = w.ship(100)   # stock is 20
    except Exception as exc:
        return f"ship(100) raised {type(exc).__name__}: {exc} — it should return a message, not crash."
    if result != "Insufficient stock":
        return (
            f"ship(100) on a stock of 20 returned {result!r}, "
            'expected the string "Insufficient stock".'
        )
    if w.stock != 20:
        return (
            f"After a failed ship(100), stock is {w.stock!r}, expected it to stay 20 — "
            "don't subtract when there is insufficient stock."
        )
    return True


def check_ex5(Book):
    if not isinstance(Book, type):
        return "Book doesn't seem to be a class — define it with `class Book:`."

    b, err = _make(Book, "Dune", "Herbert")
    if err:
        return err
    try:
        text = str(b)
    except Exception as exc:
        return f"str(Book('Dune', 'Herbert')) raised {type(exc).__name__}: {exc}"
    if "object at 0x" in text:
        return (
            "Book is using the default text representation — define a "
            "`__str__(self)` method that returns the formatted string."
        )
    if text != "Dune by Herbert":
        return f'str(Book("Dune", "Herbert")) returned {text!r}, expected "Dune by Herbert".'

    b2, err = _make(Book, "1984", "Orwell")
    if err:
        return err
    if str(b2) != "1984 by Orwell":
        return f'str(Book("1984", "Orwell")) returned {str(b2)!r} — use self.title and self.author.'
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


def check_ex7(Elevator):
    if not isinstance(Elevator, type):
        return "Elevator doesn't seem to be a class — define it with `class Elevator:`."

    e, err = _make(Elevator, 3)
    if err:
        return err
    if not hasattr(e, "floor"):
        return "Elevator has no `floor` attribute — set `self.floor = floor` in __init__."
    if e.floor != 3:
        return f"Elevator(3).floor is {e.floor!r}, expected 3."
    for meth in ("up", "down", "is_ground_floor"):
        if not hasattr(e, meth) or not callable(getattr(e, meth)):
            return f"Elevator needs a `{meth}` method."
    try:
        e.up()
        e.up()
    except Exception as exc:
        return f"up() raised {type(exc).__name__}: {exc} (use self.floor)."
    if e.floor != 5:
        return f"After up() twice on 3, floor is {e.floor!r}, expected 5."

    # is_ground_floor logic.
    low, _ = _make(Elevator, 1)
    low.down()   # -> 0
    if low.is_ground_floor() is not True:
        return (
            f"Elevator(1) then down() gives floor {low.floor}; is_ground_floor() returned "
            f"{low.is_ground_floor()!r}, expected True (floor 0 is the ground floor)."
        )
    high, _ = _make(Elevator, 3)
    if high.is_ground_floor() is not False:
        return f"Elevator(3).is_ground_floor() returned {high.is_ground_floor()!r}, expected False."
    return True
