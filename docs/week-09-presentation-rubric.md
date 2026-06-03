# Week 9 — Capstone Presentation Rubric

*Instructor + student handout. Pairs with `docs/capstone-project-brief.md`.*

Each student gives a short presentation (target **5–7 minutes** + 2 minutes of
questions) of their capstone project. Presentations are scored out of **100
points** across five categories. The categories deliberately mirror the course:
the spec (Week 6), the build and its structure (Weeks 1–5, 7), connecting to the
world (Week 8), and honest reflection on AI (Week 7).

---

## What to cover in the talk

1. **The idea** — what it does and who it's for, in two sentences.
2. **The spec** — what you set out to build; how you scoped it.
3. **A live demo** — run it. Show the happy path and at least one edge case.
4. **The architecture** — walk through how the pieces fit (the main
   functions/classes and what each does). Show one piece of code you're proud of
   or found tricky.
5. **Working with AI** — where it helped, where it got something wrong, and how
   you caught it.

---

## Scoring

| Category | Points | What full marks looks like |
|----------|:------:|----------------------------|
| **1. Spec & scope** | 20 | A clear spec (what / inputs / output / edge cases) and a sensibly scoped project — a minimum useful version that was actually finished, not an over-ambitious one left half-done. |
| **2. Working demo** | 25 | The program runs live. It does what the spec promised, handles at least one edge case gracefully, and doesn't crash on obvious bad input. |
| **3. Code & architecture** | 25 | Organized into small, well-named pieces (functions and/or a class). The student can **explain any line** and how the parts fit. Failure cases are handled. Secrets (if any) are kept out of the code. |
| **4. Reflection on AI** | 15 | An honest, specific account of directing and verifying the AI: a real example where the model was wrong or made an unstated assumption, and how the student caught and fixed it. |
| **5. Presentation** | 15 | Clear, organized, within time. Explains *why*, not just *what*. Handles questions thoughtfully. |

**Total: 100**

---

## Scoring guidance (per category)

Use roughly these bands within each category:

- **Full / strong (90–100% of the points):** meets the description above with no
  significant gaps.
- **Solid (70–85%):** mostly there; one noticeable weakness (e.g., the demo
  works but no edge case shown; the reflection is honest but vague).
- **Developing (50–65%):** the piece is present but thin (e.g., a spec that's
  one line; code the student can only partly explain).
- **Missing (0–40%):** the element is largely absent (no spec; demo doesn't run;
  "the AI did it and it worked" with no verification story).

---

## The two things that move a grade most

These are the course's whole thesis, so weight them when you're on the fence:

- **Can the student explain their own code?** (Category 3.) The point of Weeks
  1–5 was that *they* can program. A student who fully understands a small
  program demonstrates more than one who demos a large program they can't walk
  through. If they can't explain a line, that's the signal.
- **Is the AI reflection honest and specific?** (Category 4.) "It all just
  worked" is a weaker answer than "it confidently used a function that didn't
  exist, my test caught it, and here's how I fixed it." Reward students who show
  they *verified* rather than trusted — that's the durable skill the back half
  of the course is about.

---

## Logistics checklist (instructor)

- [ ] Set the presentation order; keep a timer visible (5–7 min each).
- [ ] Have each student open and **run** their notebook before they start (cold
      starts eat demo time).
- [ ] Collect the three deliverables (spec, program, reflection) — see the
      capstone brief.
- [ ] Budget ~10 min total per student (talk + demo + questions + handoff).
- [ ] Close with the "what to learn next" discussion from the Week 9 lecture
      plan.
