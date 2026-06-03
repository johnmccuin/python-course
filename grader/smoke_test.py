#!/usr/bin/env python3
"""Offline smoke-test for the autograded homework (Weeks 1-5).

For each week it:
  1. builds an isolated temp dir,
  2. drops the real grader.py and that week's checks-0N.py into it (so the
     notebook's download step is skipped — no network),
  3. executes the *reference solution* exactly as the notebook would,
  4. reads grader._results and asserts the solution scores N / N.

The grader's network `submit()` is monkeypatched to a no-op, so nothing is
posted to the live gradebook.  Each week runs in its own subprocess so the
per-week `checks` / `grader` module imports can't contaminate each other.

Usage:
    python grader/smoke_test.py
Exit code 0 if every week scores full marks, 1 otherwise.
"""

import pathlib
import shutil
import subprocess
import sys
import tempfile

REPO = pathlib.Path(__file__).resolve().parent.parent
WEEKS = [1, 2, 3, 4, 5]

# Driver executed inside each isolated temp dir (its own Python process).
DRIVER = r'''
import pathlib, sys
sys.path.insert(0, ".")
import grader as _g
_g.Grader.submit = lambda *a, **k: None        # never touch the network
ns = {}
src = pathlib.Path("solution.py").read_text()
exec(compile(src, "solution.py", "exec"), ns)
g = ns.get("grader")
if g is None:
    print("RESULT error no-grader-object")
    sys.exit(0)
results = g._results
passed = sum(1 for p, _ in results.values() if p)
total = len(results)
print(f"RESULT {passed} {total}")
for name, (ok, hint) in results.items():
    if not ok:
        print(f"FAIL {name} :: {hint}")
'''


def run_week(week: int) -> tuple[bool, str]:
    wk = f"{week:02d}"
    solution = REPO / f"week-{wk}" / f"homework_solution-{wk}.py"
    checks = REPO / f"week-{wk}" / f"checks-{wk}.py"
    grader = REPO / "grader" / "grader.py"

    for required in (solution, checks, grader):
        if not required.exists():
            return False, f"missing file: {required.relative_to(REPO)}"

    with tempfile.TemporaryDirectory() as tmp:
        tmp = pathlib.Path(tmp)
        shutil.copy(grader, tmp / "grader.py")
        shutil.copy(checks, tmp / "checks.py")
        shutil.copy(solution, tmp / "solution.py")

        proc = subprocess.run(
            [sys.executable, "-c", DRIVER],
            cwd=tmp,
            capture_output=True,
            text=True,
            timeout=120,
        )

    out = proc.stdout
    result_line = next((ln for ln in out.splitlines() if ln.startswith("RESULT")), "")
    fails = [ln for ln in out.splitlines() if ln.startswith("FAIL")]

    if proc.returncode != 0 and not result_line:
        return False, f"solution crashed:\n{proc.stderr.strip()[-800:]}"
    if not result_line or "error" in result_line:
        return False, f"could not read score (stderr: {proc.stderr.strip()[-400:]})"

    _, passed, total = result_line.split()
    detail = f"{passed}/{total}"
    if fails:
        detail += "\n    " + "\n    ".join(fails)
    return passed == total and int(total) > 0, detail


def main() -> int:
    print("Homework solution smoke-test (offline)\n" + "=" * 38)
    all_ok = True
    for week in WEEKS:
        ok, detail = run_week(week)
        mark = "PASS" if ok else "FAIL"
        first = detail.splitlines()[0] if detail else ""
        print(f"  Week {week:02d}: {mark}  {first}")
        for extra in detail.splitlines()[1:]:
            print(f"           {extra}")
        all_ok = all_ok and ok
    print("=" * 38)
    print("ALL WEEKS PASS" if all_ok else "SOME WEEKS FAILED")
    return 0 if all_ok else 1


if __name__ == "__main__":
    sys.exit(main())
