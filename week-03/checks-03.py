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


def check_ex6(save_scores):
    import pathlib

    if not callable(save_scores):
        return "save_scores doesn't seem to be a function — make sure you used `def`."

    test_file = "hw3_ex6_test.csv"
    test_scores = {"Alice": 92, "Bob": 85, "Carol": 97}

    try:
        save_scores(test_file, test_scores)
    except Exception as exc:
        return f"save_scores raised {type(exc).__name__}: {exc}"

    if not pathlib.Path(test_file).exists():
        return (
            "save_scores did not create the file. "
            "Make sure you open it for writing: `with open(filename, 'w') as f:`"
        )

    content = pathlib.Path(test_file).read_text()
    lines = [ln for ln in content.splitlines() if ln.strip()]

    if len(lines) == 0:
        return "The file is empty — make sure you're calling f.write() inside the loop."
    if len(lines) != 3:
        return (
            f"Expected 3 lines in the file, found {len(lines)}. "
            "Write one 'name,score' line per student."
        )

    expected_lines = ["Alice,92", "Bob,85", "Carol,97"]
    for i, (got_line, exp_line) in enumerate(zip(lines, expected_lines)):
        if got_line.strip() != exp_line:
            # Check if they used a different delimiter
            if got_line.strip() == exp_line.replace(",", ": "):
                return (
                    f"Line {i + 1} uses ': ' as the separator — use a comma instead. "
                    f"Expected: {exp_line!r}"
                )
            return (
                f"Line {i + 1} contains {got_line!r}, expected {exp_line!r}. "
                "Format each line as 'name,score' with no extra spaces."
            )
    return True


def check_ex7(total_from_file):
    import pathlib

    if not callable(total_from_file):
        return "total_from_file doesn't seem to be a function — make sure you used `def`."

    # Write a known test file so this check is self-contained.
    test_file = "hw3_ex7_test.csv"
    pathlib.Path(test_file).write_text("Alice,92\nBob,85\nCarol,97\n")
    expected = 274  # 92 + 85 + 97

    try:
        got = total_from_file(test_file)
    except Exception as exc:
        return f"total_from_file raised {type(exc).__name__}: {exc}"

    if got is None:
        return "total_from_file returned None — check that you have a return statement."

    # Check if they returned a string instead of an int
    if isinstance(got, str):
        return (
            f"total_from_file returned {got!r} — "
            "the result should be a number, not a string. "
            "Use int() to convert the score before adding it."
        )

    if got == 3:
        return "total_from_file returned 3 — that's the number of lines, not the sum of scores."

    if got != expected:
        # Check for string concatenation instead of addition
        try:
            str_concat = int("9285" + "97")
        except Exception:
            str_concat = None
        if got == str_concat or str(got) == "928597":
            return (
                f"total_from_file returned {got!r}: the scores are being joined as "
                "strings rather than added as numbers. Convert to int() before adding."
            )
        return (
            f"total_from_file returned {got!r}, expected {expected} (92 + 85 + 97). "
            "Make sure you convert each score to int() before adding."
        )

    # Second test with different data.
    pathlib.Path(test_file).write_text("Zara,70\nEli,99\nMia,88\n")
    expected2 = 257  # 70 + 99 + 88

    try:
        got2 = total_from_file(test_file)
    except Exception as exc:
        return f"total_from_file raised {type(exc).__name__} on second test: {exc}"

    if got2 != expected2:
        return (
            f"total_from_file returned {got2!r} for a second file (Zara 70, Eli 99, Mia 88), "
            f"expected {expected2}."
        )

    return True
