"""Autograder check functions for Week 3 Homework.

This module is fetched by the homework notebook at runtime and is
intentionally kept separate so students cannot see the check logic
while working on their answers.
"""


def check_ex1(shout):
    if not callable(shout):
        return "shout doesn't seem to be a function — make sure you used `def` and didn't overwrite the name."

    tests = [
        ("hello", "HELLO!"),
        ("Python is fun", "PYTHON IS FUN!"),
        ("world", "WORLD!"),
        ("", "!"),
    ]
    for text, expected in tests:
        try:
            got = shout(text)
        except Exception as exc:
            return f"shout({text!r}) raised {type(exc).__name__}: {exc}"
        if got is None:
            return "shout returned None — check that you have a return statement, not just print()."
        if not isinstance(got, str):
            return f"shout({text!r}) returned {got!r} — the result should be a string."
        if got == expected:
            continue
        # got != expected — give a specific hint
        if got == text.upper():
            return f"shout({text!r}) returned {got!r} — close! Don't forget to add '!' at the end."
        if text and got == text + "!":
            return f"shout({text!r}) returned {got!r} — the text isn't uppercased yet."
        return f"shout({text!r}) returned {got!r}, expected {expected!r}."
    return True


def check_ex2(normalize):
    if not callable(normalize):
        return "normalize doesn't seem to be a function — make sure you used `def`."

    tests = [
        ("  Hello World  ", "hello world"),
        ("  PYTHON  IS  FUN  ", "python is fun"),
        ("single", "single"),
        ("   ", ""),
        ("already fine", "already fine"),
        ("UPPER", "upper"),
    ]
    for text, expected in tests:
        try:
            got = normalize(text)
        except Exception as exc:
            return f"normalize({text!r}) raised {type(exc).__name__}: {exc}"
        if got is None:
            return "normalize returned None — check that you have a return statement."
        if not isinstance(got, str):
            return f"normalize({text!r}) returned {got!r} — the result should be a string."
        if got == expected:
            continue
        # got != expected — give a specific hint
        if got == text.strip():
            return f"normalize({text!r}) returned {got!r} — the text isn't lowercased yet."
        if got == text.strip().lower():
            return (
                f"normalize({text!r}) returned {got!r} — almost! "
                "Multiple internal spaces aren't collapsed into one. "
                "Try: split the stripped+lowercased string, then join with a single space."
            )
        return f"normalize({text!r}) returned {got!r}, expected {expected!r}."
    return True


def check_ex3(count_word):
    if not callable(count_word):
        return "count_word doesn't seem to be a function — make sure you used `def`."

    tests = [
        ("the cat sat on the mat", "the", 2),
        ("cat cats catfish", "cat", 1),
        ("Hello hello HELLO", "hello", 3),
        ("no match here", "xyz", 0),
        ("one", "one", 1),
        ("the the the", "the", 3),
    ]
    for sentence, word, expected in tests:
        try:
            got = count_word(sentence, word)
        except Exception as exc:
            return f"count_word({sentence!r}, {word!r}) raised {type(exc).__name__}: {exc}"
        if got is None:
            return "count_word returned None — check that you have a return statement."
        if not isinstance(got, int):
            return f"count_word({sentence!r}, {word!r}) returned {got!r} — the result should be an integer count."
        if sentence == "cat cats catfish" and word == "cat" and got == 3:
            return (
                "count_word('cat cats catfish', 'cat') returned 3 — "
                "that's counting 'cat' inside 'cats' and 'catfish'. "
                "Split the sentence into words first, then compare each whole word."
            )
        if got != expected:
            return (
                f"count_word({sentence!r}, {word!r}) returned {got}, expected {expected}. "
                "Make sure you lowercase both the sentence words and the target word before comparing."
            )
    return True


def check_ex4(filter_scores):
    if not callable(filter_scores):
        return "filter_scores doesn't seem to be a function — make sure you used `def`."

    tests = [
        ({"Alice": 92, "Bob": 65, "Carol": 80}, 80, {"Alice": 92, "Carol": 80}),
        ({"Alice": 92, "Bob": 65}, 100, {}),
        ({"Alice": 92, "Bob": 65}, 0, {"Alice": 92, "Bob": 65}),
        ({"solo": 50}, 50, {"solo": 50}),
        ({"solo": 50}, 51, {}),
    ]
    for scores, min_score, expected in tests:
        try:
            got = filter_scores(scores, min_score)
        except Exception as exc:
            return f"filter_scores({scores!r}, {min_score!r}) raised {type(exc).__name__}: {exc}"
        if got is None:
            return (
                "filter_scores returned None — make sure you build a result dict "
                "and return it at the end of the function."
            )
        if not isinstance(got, dict):
            return f"filter_scores returned {got!r} — the result should be a dictionary."
        if got != expected:
            # Common mistake: using > instead of >=
            strict = {k: v for k, v in scores.items() if v > min_score}
            if got == strict:
                return (
                    f"filter_scores({scores!r}, {min_score!r}) returned {got!r}: "
                    "scores exactly equal to min_score are missing. "
                    "Use >= not >."
                )
            return (
                f"filter_scores({scores!r}, {min_score!r}) returned {got!r}, "
                f"expected {expected!r}."
            )
    return True


def check_ex5(best_score):
    if not callable(best_score):
        return "best_score doesn't seem to be a function — make sure you used `def`."

    tests = [
        ({"Alice": 92, "Bob": 85, "Carol": 97}, "Carol"),
        ({"only": 75}, "only"),
        ({"Zara": 70, "Eli": 99, "Mia": 88}, "Eli"),
        ({"a": 1, "b": 100, "c": 50}, "b"),
    ]
    for scores, expected in tests:
        try:
            got = best_score(scores)
        except Exception as exc:
            return f"best_score({scores!r}) raised {type(exc).__name__}: {exc}"
        if got is None:
            return "best_score returned None — check that you have a return statement."
        # Check if they returned the score instead of the name
        if isinstance(got, (int, float)) and got == max(scores.values()):
            return (
                f"best_score({scores!r}) returned {got!r} — "
                "that's the highest score, but the function should return the student's name."
            )
        if got not in scores:
            return (
                f"best_score({scores!r}) returned {got!r}, "
                "which isn't a name in the dictionary."
            )
        if scores.get(got, -1) != max(scores.values()):
            return (
                f"best_score({scores!r}) returned {got!r} (score: {scores.get(got)}), "
                f"but {expected!r} has the highest score ({scores[expected]})."
            )
    return True


def check_ex6(min_max):
    if not callable(min_max):
        return "min_max doesn't seem to be a function — make sure you used `def`."

    tests = [
        ([3, 1, 4, 1, 5], (1, 5)),
        ([7], (7, 7)),
        ([-2, 0, 2], (-2, 2)),
        ([10, 9, 8, 7], (7, 10)),
    ]
    for numbers, expected in tests:
        try:
            got = min_max(numbers)
        except Exception as exc:
            return f"min_max({numbers!r}) raised {type(exc).__name__}: {exc}"
        if got is None:
            return "min_max returned None — check that you have a return statement."
        if isinstance(got, list):
            return (
                f"min_max({numbers!r}) returned the list {got!r} — return a tuple instead. "
                "Use parentheses or just `return min(...), max(...)`."
            )
        if not isinstance(got, tuple):
            return f"min_max({numbers!r}) returned {got!r} — the result should be a tuple (minimum, maximum)."
        if len(got) != 2:
            return f"min_max({numbers!r}) returned {got!r} — the tuple should have exactly two items."
        if got == (expected[1], expected[0]) and expected[0] != expected[1]:
            return (
                f"min_max({numbers!r}) returned {got!r} — the order is reversed. "
                "Return (minimum, maximum), smallest first."
            )
        if got != expected:
            return f"min_max({numbers!r}) returned {got!r}, expected {expected!r}."
    return True


def check_ex7(parse_point):
    if not callable(parse_point):
        return "parse_point doesn't seem to be a function — make sure you used `def`."

    tests = [
        ("3,4", (3, 4)),
        ("10,20", (10, 20)),
        ("-1,5", (-1, 5)),
        ("0,0", (0, 0)),
    ]
    for text, expected in tests:
        try:
            got = parse_point(text)
        except Exception as exc:
            return f"parse_point({text!r}) raised {type(exc).__name__}: {exc}"
        if got is None:
            return "parse_point returned None — check that you have a return statement."
        if isinstance(got, list):
            return (
                f"parse_point({text!r}) returned the list {got!r} — return a tuple instead."
            )
        if not isinstance(got, tuple):
            return f"parse_point({text!r}) returned {got!r} — the result should be a tuple of two ints."
        if len(got) != 2:
            return f"parse_point({text!r}) returned {got!r} — the tuple should have exactly two items."
        if got == tuple(str(n) for n in expected) or any(isinstance(x, str) for x in got):
            return (
                f"parse_point({text!r}) returned {got!r} — the pieces are still strings. "
                "Convert each with int() before returning."
            )
        if got != expected:
            return f"parse_point({text!r}) returned {got!r}, expected {expected!r}."
    return True
