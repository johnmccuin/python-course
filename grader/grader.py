# %% [markdown]
# # Grader — Autograding Utility
#
# Reusable class for checking homework exercises in Google Colab notebooks.
# Import it with:
#
# ```python
# from grader import Grader
# ```
#
# when `grader.py` is in the same folder as the running notebook.

# %%
class Grader:
    """Tracks exercise results across a homework notebook.

    Usage:
        grader = Grader("Week 1 Homework")

        def _check():
            if answer != 42:
                return "Hint about what's wrong."
            return True
        grader.check("ex1", _check)

        # ... more exercises ...

        grader.report()
    """

    def __init__(self, title: str):
        """
        Parameters
        ----------
        title : str
            Appears in the final report header, e.g. "Week 1 Homework".
        """
        self.title = title
        # Dict preserves insertion order (Python 3.7+).
        # Key: exercise name.  Value: (passed: bool, hint: str | None)
        # Updating an existing key keeps it in its original position,
        # so re-running a cell shows the exercise in the original order.
        self._results: dict[str, tuple[bool, str | None]] = {}

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def check(self, name: str, check_fn) -> None:
        """Run *check_fn* and record the result.

        Parameters
        ----------
        name : str
            Short label for the exercise, e.g. ``"ex1"``.  Used as the
            key in the results table.  If *name* has been checked before
            in this session the new result **replaces** the old one, so
            students can fix their answer and re-run.
        check_fn : callable
            A zero-argument callable that returns:

            * ``True``  — exercise passed.
            * A ``str`` — exercise failed; the string is the hint shown
              to the student.

            Any exception raised inside *check_fn* is caught and treated
            as a failure with an informative hint.  This handles the very
            common case where a student hasn't defined the expected
            variable yet and a ``NameError`` would otherwise crash the
            notebook.
        """
        try:
            result = check_fn()
        except Exception as exc:
            passed = False
            hint = (
                f"Your code raised an error before the check could run: "
                f"{type(exc).__name__}: {exc}"
            )
        else:
            if result is True:
                passed = True
                hint = None
            else:
                passed = False
                hint = str(result)

        # Store / overwrite — dict keeps original insertion position when
        # the key already exists, preserving first-seen exercise order.
        self._results[name] = (passed, hint)

        if passed:
            print(f"✓ {name}")
        else:
            print(f"✗ {name}: {hint}")

    def report(self) -> None:
        """Print the full results table and total score.

        Example output::

            Week 1 Homework — Results
            =========================
            ex1                 ✓
            ex2                 ✗
            ex3                 ✓
            -------------------------
            Score: 2 / 3  (67%)

        Safe to call before all checks have run — only recorded results
        are shown; the denominator equals the number of checks so far.
        """
        header = f"{self.title} — Results"  # em-dash

        # Width for the separator lines: wide enough for the header and
        # for the widest exercise line (name + 2 spaces + symbol).
        names = list(self._results)
        max_name_len = max((len(n) for n in names), default=0)
        name_col = max(20, max_name_len + 4)   # left-aligned name column
        sep_width = max(len(header), name_col + 1)

        print(header)
        print("=" * sep_width)

        passed_count = 0
        for name, (passed, _hint) in self._results.items():
            symbol = "✓" if passed else "✗"   # ✓ / ✗
            print(f"{name:<{name_col}}{symbol}")
            if passed:
                passed_count += 1

        total = len(self._results)
        print("-" * sep_width)

        if total == 0:
            print("Score: 0 / 0")
        else:
            pct = round(100 * passed_count / total)
            print(f"Score: {passed_count} / {total}  ({pct}%)")
