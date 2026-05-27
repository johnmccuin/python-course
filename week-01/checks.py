"""Autograder check functions for Week 1 Homework.

This module is fetched by the homework notebook at runtime and is
intentionally kept separate so students cannot see the check logic
while working on their answers.
"""


def check_ex1(minutes_in_year):
    if not isinstance(minutes_in_year, int):
        return "Your answer should be an integer, not a float or string."
    if minutes_in_year != 525600:
        return "Check your math — 365 days × 24 hours × 60 minutes."
    return True


def check_ex2(greeting):
    if not isinstance(greeting, str):
        return "Your answer should be a string."
    if greeting != "Hello Sam, you are 30 years old.":
        if "," not in greeting:
            return "Check your punctuation — is the comma there?"
        if not greeting.endswith("."):
            return "Check your punctuation — is there a period at the end?"
        return "Your string doesn't match exactly. Compare character by character with the expected output."
    return True


def check_ex3(is_even):
    if is_even is not True:
        return "Use the modulo operator `%` to check divisibility by 2."
    return True


def check_ex4(fahrenheit):
    if not isinstance(fahrenheit, (int, float)):
        return "Your answer should be a number."
    if abs(fahrenheit - 77.0) > 0.01:
        return "Check the formula: F = C × 9/5 + 32. With celsius = 25, fahrenheit should be 77."
    return True


def check_ex5(as_number):
    if isinstance(as_number, str):
        return "Your answer is still a string. Use int() to convert."
    if type(as_number) is float:
        return "Close — that's a float. We need an integer."
    if as_number != 42:
        return "Your value isn't 42. Make sure you're converting `s`, not using a different number."
    return True


def check_ex6(category):
    if category not in ("positive", "negative", "zero"):
        return "Your answer should be one of: 'positive', 'negative', 'zero'. Check your spelling and capitalization."
    if category != "positive":
        return "For n=7, category should be 'positive'."
    return True


def check_ex7(result):
    if result not in ("fizz", "buzz", "both", "neither"):
        return "Your answer should be one of: 'fizz', 'buzz', 'both', 'neither'."
    if result == "fizz":
        return "Check the order of your conditions. 15 is divisible by both 3 and 5 — make sure you handle that case first."
    if result != "both":
        return "For n=15, result should be 'both'."
    return True
