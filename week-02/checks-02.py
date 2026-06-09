"""Autograder check functions for Week 2 Homework.

This module is fetched by the homework notebook at runtime and is
intentionally kept separate so students cannot see the check logic
while working on their answers.
"""


def check_ex1(rank):
    if rank is ...:
        return "You haven't written your if/elif/else yet — replace the `...` with your code."
    if rank is None:
        return "rank is None — make sure every branch of your if/elif/else assigns a value to rank."
    if not isinstance(rank, str):
        return "rank should be a string like 'Gold' or 'Silver', not a number."
    if rank not in {"Diamond", "Platinum", "Gold", "Silver", "Bronze"}:
        return f"'{rank}' isn't a valid rank. Expected one of: Diamond, Platinum, Gold, Silver, Bronze — check your spelling and capitalization."
    if rank == "Platinum":
        return "Got 'Platinum' — points=1200 is not in the 1500–1999 range. Check your boundary values."
    if rank == "Silver":
        return "Got 'Silver' — points=1200 is not in the 500–999 range. Check your boundary values."
    if rank != "Gold":
        return f"Got '{rank}' — for points=1200 the correct rank is 'Gold' (1000 ≤ points ≤ 1499). Double-check your ranges."
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
        return "total is still 0 — check that you're updating total inside the loop body (e.g. total += n)."
    if total == 90:
        return "Got 90 — that's 2+4+…+18. Your loop stopped one step early. Should it include limit=20?"
    if total == 132:
        return "Got 132 — that's 2+4+…+22. Your loop ran one step too far past limit=20. Check your condition."
    if total == 210:
        return "Got 210 — that's 1+2+…+20, every number. You're meant to add only the even numbers."
    if total != 110:
        return f"Got {total} but expected 110 (2+4+…+20). Trace through your loop on paper — which numbers are you adding?"
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
