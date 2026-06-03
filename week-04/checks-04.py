"""Autograder check functions for Week 4 Homework.

This module is fetched by the homework notebook at runtime and is
intentionally kept separate so students cannot see the check logic
while working on their answers.

Every exercise tests a concept demonstrated in lecture-04 (files, modules
and imports, error handling, tracebacks/debugging, assertions), building on
the functions, loops, lists, dicts, strings, and tuples from Weeks 1-3.
"""

import math
import pathlib


def check_ex1(save_lines):
    if not callable(save_lines):
        return "save_lines doesn't seem to be a function — make sure you used `def`."

    test_file = "hw4_ex1_test.txt"
    lines = ["apple", "banana", "cherry"]

    try:
        save_lines(test_file, lines)
    except Exception as exc:
        return f"save_lines raised {type(exc).__name__}: {exc}"

    if not pathlib.Path(test_file).exists():
        return (
            "save_lines did not create the file. "
            "Open it for writing with `with open(filename, 'w') as f:`."
        )

    content = pathlib.Path(test_file).read_text()
    got = content.splitlines()

    if got == ["".join(lines)] or (len(got) == 1 and got[0] == "applebananacherry"):
        return (
            "save_lines wrote everything on one line — add a newline after each "
            "item: `f.write(line + '\\n')`."
        )
    if [ln for ln in got if ln.strip()] != lines:
        return (
            f"The file's lines were {got!r}, expected {lines!r} "
            "(one item per line, in order)."
        )
    return True


def check_ex2(sum_numbers):
    if not callable(sum_numbers):
        return "sum_numbers doesn't seem to be a function — make sure you used `def`."

    cases = [
        ("10\n20\n30\n", 60),
        ("5\n", 5),
        ("1\n2\n3\n4\n5\n", 15),
        ("100\n-40\n", 60),
    ]
    test_file = "hw4_ex2_test.txt"
    for content, expected in cases:
        pathlib.Path(test_file).write_text(content)
        try:
            got = sum_numbers(test_file)
        except Exception as exc:
            return f"sum_numbers raised {type(exc).__name__}: {exc} (file was {content!r})"
        if got is None:
            return "sum_numbers returned None — check that you have a return statement."
        if isinstance(got, str):
            return (
                f"sum_numbers returned the string {got!r} — convert each line with "
                "int() and add the numbers."
            )
        if got != expected:
            return (
                f"sum_numbers returned {got!r} for a file of {content.split()!r}, "
                f"expected {expected}. Convert each line to int() before adding."
            )
    return True


def check_ex3(circle_area):
    if not callable(circle_area):
        return "circle_area doesn't seem to be a function — make sure you used `def`."

    tests = [
        (1, math.pi),
        (0, 0.0),
        (2, math.pi * 4),
        (3.5, math.pi * 3.5 ** 2),
    ]
    for radius, expected in tests:
        try:
            got = circle_area(radius)
        except Exception as exc:
            return f"circle_area({radius!r}) raised {type(exc).__name__}: {exc}"
        if got is None:
            return "circle_area returned None — check that you have a return statement, not just print()."
        if not isinstance(got, (int, float)):
            return f"circle_area({radius!r}) returned {got!r} — the result should be a number."
        # Common mistake: using 3.14 instead of math.pi
        if abs(got - 3.14 * radius ** 2) < 1e-9 and abs(got - expected) > 1e-6:
            return (
                f"circle_area({radius!r}) returned {got!r} — looks like you typed 3.14 by hand. "
                "Import the math module and use math.pi for full precision."
            )
        # Common mistake: forgetting to square the radius
        if abs(got - math.pi * radius) < 1e-9 and abs(got - expected) > 1e-6:
            return (
                f"circle_area({radius!r}) returned {got!r} — that's math.pi * radius. "
                "The formula is pi times the radius squared (radius ** 2)."
            )
        if abs(got - expected) > 1e-6:
            return f"circle_area({radius!r}) returned {got!r}, expected about {expected!r}."
    return True


def check_ex4(safe_divide):
    if not callable(safe_divide):
        return "safe_divide doesn't seem to be a function — make sure you used `def`."

    msg = "Cannot divide by zero."
    number_tests = [
        (10, 2, 5.0),
        (7, 7, 1.0),
        (0, 5, 0.0),
        (9, 2, 4.5),
    ]
    for a, b, expected in number_tests:
        try:
            got = safe_divide(a, b)
        except Exception as exc:
            return f"safe_divide({a!r}, {b!r}) raised {type(exc).__name__}: {exc}"
        if got is None:
            return "safe_divide returned None — check that you return the division result."
        if isinstance(got, str):
            return (
                f"safe_divide({a!r}, {b!r}) returned the error string, "
                f"but {a} / {b} is a valid division — return the number {expected}."
            )
        if abs(got - expected) > 1e-9:
            return f"safe_divide({a!r}, {b!r}) returned {got!r}, expected {expected!r}."

    # Division by zero must be handled, not crash.
    try:
        got = safe_divide(10, 0)
    except ZeroDivisionError:
        return (
            "safe_divide(10, 0) crashed with ZeroDivisionError — "
            "wrap the division in try / except ZeroDivisionError and return the message instead."
        )
    except Exception as exc:
        return f"safe_divide(10, 0) raised {type(exc).__name__}: {exc}"
    if got != msg:
        return (
            f"safe_divide(10, 0) returned {got!r}, expected the string {msg!r} "
            "(exact text, including the period)."
        )
    return True


def check_ex5(parse_scores):
    if not callable(parse_scores):
        return "parse_scores doesn't seem to be a function — make sure you used `def`."

    tests = [
        (["10", "x", "20", "3.5"], [10, 20]),
        (["1", "2", "3"], [1, 2, 3]),
        (["a", "b"], []),
        ([], []),
        (["5", "-3", "ok"], [5, -3]),
    ]
    for items, expected in tests:
        try:
            got = parse_scores(items)
        except Exception as exc:
            return f"parse_scores({items!r}) raised {type(exc).__name__}: {exc}"
        if got is None:
            return (
                "parse_scores returned None — build a list of the valid numbers "
                "and return it at the end."
            )
        if not isinstance(got, list):
            return f"parse_scores({items!r}) returned {got!r} — the result should be a list."
        if got != expected:
            # Common mistake: keeping the items as strings instead of converting to int.
            if got == list(items):
                return (
                    f"parse_scores({items!r}) returned {got!r} — the items are still strings. "
                    "Convert each one with int() inside the try block."
                )
            return (
                f"parse_scores({items!r}) returned {got!r}, expected {expected!r}. "
                "Use try / except ValueError so that items that aren't whole numbers are skipped."
            )
    return True


def check_ex6(average):
    if not callable(average):
        return "average doesn't seem to be a function — make sure you used `def`."

    tests = [
        ([2, 4, 6], 4.0),
        ([10], 10.0),
        ([1, 2], 1.5),
        ([100, 0, 50, 50], 50.0),
    ]
    for numbers, expected in tests:
        try:
            got = average(numbers)
        except Exception as exc:
            return f"average({numbers!r}) raised {type(exc).__name__}: {exc}"
        if got is None:
            return "average returned None — check that you have a return statement."
        if abs(got - expected) > 1e-9:
            return f"average({numbers!r}) returned {got!r}, expected {expected!r}."

    # The bug: the original crashes on an empty list. Fixed version returns 0.
    try:
        got = average([])
    except ZeroDivisionError:
        return (
            "average([]) still crashes with ZeroDivisionError — that's the bug. "
            "When the list is empty there's nothing to divide by; return 0 in that case."
        )
    except Exception as exc:
        return f"average([]) raised {type(exc).__name__}: {exc}"
    if got != 0:
        return f"average([]) returned {got!r}, expected 0 for an empty list."
    return True


def check_ex7(withdraw):
    if not callable(withdraw):
        return "withdraw doesn't seem to be a function — make sure you used `def`."

    valid_tests = [
        (100, 30, 70),
        (50, 50, 0),
        (200, 1, 199),
    ]
    for balance, amount, expected in valid_tests:
        try:
            got = withdraw(balance, amount)
        except AssertionError:
            return (
                f"withdraw({balance!r}, {amount!r}) raised AssertionError, "
                "but this is a valid withdrawal — your assertion is too strict."
            )
        except Exception as exc:
            return f"withdraw({balance!r}, {amount!r}) raised {type(exc).__name__}: {exc}"
        if got is None:
            return "withdraw returned None — check that you return the new balance."
        if got != expected:
            return (
                f"withdraw({balance!r}, {amount!r}) returned {got!r}, expected {expected!r} "
                "(the balance left after taking out the amount)."
            )

    # Withdrawing more than the balance, or a non-positive amount, must assert.
    bad_tests = [(100, 150), (100, -5), (100, 0)]
    for balance, amount in bad_tests:
        try:
            got = withdraw(balance, amount)
        except AssertionError:
            continue  # correct
        except Exception as exc:
            return (
                f"withdraw({balance!r}, {amount!r}) raised {type(exc).__name__} instead of "
                "AssertionError — use `assert` to guard the withdrawal."
            )
        return (
            f"withdraw({balance!r}, {amount!r}) returned {got!r} without complaining. "
            "Add assert statements: the amount must be greater than 0 and no more than the balance."
        )
    return True
