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


def check_ex4(popular_pages):
    if not callable(popular_pages):
        return "popular_pages doesn't seem to be a function — make sure you used `def`."

    tests = [
        ({"home": 1200, "about": 300, "blog": 800}, 800, {"home": 1200, "blog": 800}),
        ({"home": 1200, "about": 300}, 5000, {}),
        ({"home": 1200, "about": 300}, 0, {"home": 1200, "about": 300}),
        ({"solo": 500}, 500, {"solo": 500}),
        ({"solo": 500}, 501, {}),
    ]
    for views, min_views, expected in tests:
        try:
            got = popular_pages(views, min_views)
        except Exception as exc:
            return f"popular_pages({views!r}, {min_views!r}) raised {type(exc).__name__}: {exc}"
        if got is None:
            return (
                "popular_pages returned None — make sure you build a result dict "
                "and return it at the end of the function."
            )
        if not isinstance(got, dict):
            return f"popular_pages returned {got!r} — the result should be a dictionary."
        if got != expected:
            # Common mistake: using > instead of >=
            strict = {k: v for k, v in views.items() if v > min_views}
            if got == strict:
                return (
                    f"popular_pages({views!r}, {min_views!r}) returned {got!r}: "
                    "pages whose view_count exactly equals min_views are missing. "
                    "Use >= not >."
                )
            return (
                f"popular_pages({views!r}, {min_views!r}) returned {got!r}, "
                f"expected {expected!r}."
            )
    return True


def check_ex5(top_page):
    if not callable(top_page):
        return "top_page doesn't seem to be a function — make sure you used `def`."

    tests = [
        ({"home": 1200, "about": 300, "blog": 800}, "home"),
        ({"only": 75}, "only"),
        ({"news": 70, "shop": 990, "faq": 880}, "shop"),
        ({"a": 1, "b": 1000, "c": 500}, "b"),
    ]
    for views, expected in tests:
        try:
            got = top_page(views)
        except Exception as exc:
            return f"top_page({views!r}) raised {type(exc).__name__}: {exc}"
        if got is None:
            return "top_page returned None — check that you have a return statement."
        # Check if they returned the view count instead of the page name
        if isinstance(got, (int, float)) and got == max(views.values()):
            return (
                f"top_page({views!r}) returned {got!r} — "
                "that's the highest view count, but the function should return the page name."
            )
        if got not in views:
            return (
                f"top_page({views!r}) returned {got!r}, "
                "which isn't a page name in the dictionary."
            )
        if views.get(got, -1) != max(views.values()):
            return (
                f"top_page({views!r}) returned {got!r} (views: {views.get(got)}), "
                f"but {expected!r} has the most views ({views[expected]})."
            )
    return True


def check_ex6(count_and_total):
    if not callable(count_and_total):
        return "count_and_total doesn't seem to be a function — make sure you used `def`."

    tests = [
        ([3, 1, 4, 1, 5], (5, 14)),
        ([7], (1, 7)),
        ([], (0, 0)),
        ([10, 9, 8, 7], (4, 34)),
    ]
    for numbers, expected in tests:
        try:
            got = count_and_total(numbers)
        except Exception as exc:
            return f"count_and_total({numbers!r}) raised {type(exc).__name__}: {exc}"
        if got is None:
            return "count_and_total returned None — check that you have a return statement."
        if isinstance(got, list):
            return (
                f"count_and_total({numbers!r}) returned the list {got!r} — return a tuple instead. "
                "Use parentheses or just `return len(...), sum(...)`."
            )
        if not isinstance(got, tuple):
            return f"count_and_total({numbers!r}) returned {got!r} — the result should be a tuple (count, total)."
        if len(got) != 2:
            return f"count_and_total({numbers!r}) returned {got!r} — the tuple should have exactly two items."
        if got == (expected[1], expected[0]) and expected[0] != expected[1]:
            return (
                f"count_and_total({numbers!r}) returned {got!r} — the order is reversed. "
                "Return (count, total) — how many items first, then their sum."
            )
        if got != expected:
            return f"count_and_total({numbers!r}) returned {got!r}, expected {expected!r}."
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
