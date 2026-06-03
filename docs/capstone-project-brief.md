# Capstone Project Brief

*Student handout — Weeks 6–9. Post to Blackboard or share the GitHub link.*

For the last third of the course you build a small program of your own. There
is no homework in Weeks 6–8 — **the project is the work.** You choose it, spec
it, build it with an AI coding partner, and present it in Week 9.

This is where everything comes together: the Python you can now write yourself
(Weeks 1–5), the spec you learn to write (Week 6), the skill of directing and
verifying an AI (Week 7), and connecting your program to the world (Week 8).

---

## Timeline

| When | What you do |
|------|-------------|
| **Week 6 (back half)** | Brainstorm ideas, scope one down, write your **spec**. |
| **Weeks 7–8 (class work time)** | Build it with an AI partner; verify as you go. |
| **Week 9** | **Present** it to the class. |

Your spec is due at the **end of Week 6** so you start Week 7 ready to build.

---

## What to build

A **small, real, useful-to-you** program. The best projects scratch your own
itch. Some directions:

- **A tool** — a tip splitter, a flashcard quizzer, a unit converter, a
  password generator.
- **A small game** — number-guessing, hangman, rock-paper-scissors, a text
  adventure.
- **A data cruncher** — read a file of *your* data (workouts, expenses, grades,
  a CSV you download) and report on it.
- **Something with an API or an LLM** (Week 8) — fetch live data, or use a model
  to summarize, classify, or generate text inside your program.

If you can describe it to a friend in two sentences, it's a good candidate.

### Scope it down

The number-one mistake is building too big. Define a **minimum useful version**
— the smallest thing that still does something worthwhile — and a short list of
**"if there's time"** extras. You ship the minimum first, then add.

> Too big: "an app that tracks all my finances with charts and a login."
> Right-sized: "read `expenses.txt`, total the spending per category, and print
> the three biggest."

---

## Requirements

Your project must:

1. **Be driven by you.** Use AI as much as you like — but you must **understand
   every line you keep** and be able to explain it (Week 7). If you can't read
   it, you can't verify it, and you haven't learned it.
2. **Start from a written spec** (Week 6): what it does, inputs, output, and
   edge cases.
3. **Use core Python** from the course — functions and at least one of: a data
   structure used meaningfully (list/dict/tuple), a file, or a class.
4. **Handle the obvious failure cases** — bad input, a missing file, or a failed
   network call shouldn't crash it (Week 4 / Week 8).
5. **Be verified** — show that it works with a few checks or tests *you* decided
   the answers to (Week 7), not just "it ran once."

Your project may **optionally**:

- Call a web API or an LLM (Week 8). Encouraged, not required.
- If it does, **keep secrets out of your code** — load API keys from Colab
  Secrets, never paste or commit them (Week 8).

---

## Deliverables

Bring three things to Week 9:

1. **The spec** — your Week 6 spec, updated to match what you actually built.
2. **The working program** — a Colab notebook (or `.py`) that runs.
3. **A short reflection** (½ page is plenty): where the AI helped, where it got
   something wrong and how you *caught* it, and one thing you'd do differently
   next time. This is graded — honest "here's where I had to fix the AI" beats
   "it all worked perfectly."

---

## How it's graded

Your Week 9 presentation is scored with the **Week 9 Presentation Rubric**
(`docs/week-09-presentation-rubric.md`). The five things it rewards:

- a clear **spec** and sensible **scope**,
- a working **demo**,
- understandable **structure** (you can explain how the pieces fit),
- an honest **reflection on working with AI**, and
- a clear **presentation**.

You are not graded on building something big or flashy. A small program you
fully understand, cleanly specced and honestly presented, scores higher than a
sprawling one you can't explain.

---

## A few tips

- **Commit early to a small version.** A finished small thing beats an
  unfinished big thing every time.
- **Verify as you go.** Don't build the whole thing and test at the end — check
  each piece against your spec as you add it.
- **Keep the spec open while you build.** When the AI asks (implicitly) "what
  should happen here?", the answer is in your spec.
- **Save your work** — in Colab, *File → Save a copy in Drive.*
