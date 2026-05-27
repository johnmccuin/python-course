"""Autograder check functions for Week 2 Homework.

This module is fetched by the homework notebook at runtime and is
intentionally kept separate so students cannot see the check logic
while working on their answers.
"""


def check_ex1(label):
    if label is ...:
        return "You haven't written your if/elif/else yet — replace the `...` with your code."
    if label is None:
        return "label is None — make sure every branch of your if/elif/else assigns a value to label."
    if not isinstance(label, str):
        return "label should be a string like 'A' or 'B', not a number."
    if label not in {"A", "B", "C", "D", "F"}:
        return f"'{label}' isn't a valid label. Expected one of: A, B, C, D, F — check your spelling."
    if label == "A":
        return "Got 'A' — score=83 is not in the 90–100 range. Check your boundary values."
    if label == "C":
        return "Got 'C' — score=83 is not in the 70–79 range. Check your boundary values."
    if label != "B":
        return f"Got '{label}' — for score=83 the correct label is 'B' (80 ≤ score ≤ 89). Double-check your ranges."
    return True


def check_ex2(cost):
    if cost is ...:
        return "You haven't written your if/elif/else yet — replace the `...` with your code."
    if cost is None:
        return "cost is None — make sure every branch of your if/elif/else assigns a value to cost."
    if not isinstance(cost, (int, float)):
        return "cost should be a number like 7.99, not a string."
    if abs(cost - 3.99) <= 0.01:
        return "Got 3.99 — that's the price for packages 1 lb or under. weight=3.5 is in a different range."
    if abs(cost - 14.99) <= 0.01:
        return "Got 14.99 — that's for packages over 5 lbs. weight=3.5 is in a different range."
    if abs(cost - 7.99) > 0.01:
        return f"Got {cost} but expected 7.99. Check your boundary conditions — which range does 3.5 lbs fall into?"
    return True


def check_ex3(total):
    if not isinstance(total, (int, float)):
        return f"total should be a number, not {type(total).__name__}."
    if total == 0:
        return "total is still 0 — check that you're updating total inside the loop body (e.g. total += i)."
    if total == 105:
        return "Got 105 — that's 1+2+…+14. Your loop stopped one step early. Is your condition < or <=?"
    if total == 136:
        return "Got 136 — that's 1+2+…+16. Your loop ran one step too many. Check your condition."
    if total == 55:
        return "Got 55 — that's 1+2+…+10 (the lecture example). Make sure you're looping up to limit=15."
    if total != 120:
        return f"Got {total} but expected 120 (1+2+…+15). Trace through your loop on paper — what value does your counter reach?"
    return True


def check_ex4(bounces):
    if not isinstance(bounces, int):
        return f"bounces should be a whole number (int), not {type(bounces).__name__}."
    if bounces == 0:
        return "bounces is still 0 — the counter isn't increasing. Are you adding 1 to bounces inside the loop?"
    if bounces == 5:
        return "Got 5 — your loop stopped one bounce too early. Should the condition be `height > 1` or `height > 2`?"
    if bounces == 7:
        return "Got 7 — your loop ran one extra time. Should it stop when height reaches 1, or goes below 1?"
    if bounces != 6:
        return f"Got {bounces} but expected 6. Trace the path: 64→32→16→8→4→2→1 — count the arrows."
    return True


def check_ex5(hot_days):
    if not isinstance(hot_days, int):
        return f"hot_days should be a whole number, not {type(hot_days).__name__}."
    if hot_days == 0:
        return "hot_days is 0 — check your if condition. To test 'strictly above 75' use >, not >=."
    if hot_days == 4:
        return "Got 4 — looks like you're counting 75 itself. The condition is strictly *above* 75 (use >)."
    if hot_days == 7:
        return "Got 7 — that's every item in the list. Your if condition might be letting everything through."
    if hot_days != 3:
        return f"Got {hot_days} but expected 3. The values above 75 in [55, 72, 68, 81, 90, 63, 77] are 81, 90, and 77."
    return True


def check_ex6(lengths):
    if not isinstance(lengths, list):
        return f"lengths should be a list, not {type(lengths).__name__}."
    if len(lengths) == 0:
        return "lengths is empty — make sure you're calling lengths.append(...) inside the loop."
    if len(lengths) != 5:
        return f"lengths has {len(lengths)} item(s) but should have 5 — one per word."
    expected = [6, 2, 3, 2, 5]
    if lengths != expected:
        for i, (got, exp) in enumerate(zip(lengths, expected)):
            if got != exp:
                return f"Item at index {i} is {got} but should be {exp}. Are you using len() on each individual word?"
    return True


def check_ex7(largest):
    if not isinstance(largest, (int, float)):
        return f"largest should be a number, not {type(largest).__name__}."
    if largest == 5:
        return "Got 5 — that's the starting value and it was never updated. Check your if condition: when should largest change?"
    if largest == 12:
        return "Got 12 — your loop found a bigger number than 5, but stopped updating before it reached 19. Check the condition again."
    if largest != 19:
        return f"Got {largest} but expected 19. Make sure your if updates largest whenever the current number is bigger than it."
    return True
