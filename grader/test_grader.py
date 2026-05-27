# %% [markdown]
# # Grader — End-to-End Tests
#
# This notebook exercises every feature of the `Grader` class.
# Run all cells top-to-bottom. The final `report()` cell should show
# **Score: 3 / 5  (60%)** — three passes and two intentional failures.
#
# ---
# ## Setup
#
# Download `grader.py` from the course repo into the Colab session, then
# import `Grader` from it.  Re-running this cell is safe — it skips the
# download if the file is already present.
#
# > **Note:** the course repo must be **public** on GitHub for this URL to
# > work without authentication.  Students opening homework notebooks from
# > Blackboard also require the repo to be public.

# %%
import urllib.request, pathlib, sys

GRADER_URL = (
    "https://raw.githubusercontent.com/johnmccuin/python-course/"
    "main/grader/grader.py"
)
dest = pathlib.Path("grader.py")

if not dest.exists():
    urllib.request.urlretrieve(GRADER_URL, dest)
    print(f"Downloaded grader.py ({dest.stat().st_size} bytes)")
else:
    print("grader.py already present — skipping download.")

# Add the current directory to sys.path so `import grader` finds the file.
if str(pathlib.Path(".").resolve()) not in sys.path:
    sys.path.insert(0, str(pathlib.Path(".").resolve()))

from grader import Grader
print("Grader imported successfully.")

# %% [markdown]
# ---
# ## Section 1 — Instantiate the Grader
#
# Create a `Grader` for this test session.

# %%
grader = Grader("Grader Test Suite")
print(f"Grader created with title: {grader.title!r}")

# %% [markdown]
# ---
# ## Section 2 — Passing exercise
#
# `check_fn` returns `True` → should print `✓ ex_pass`.

# %%
answer_pass = 42   # correct answer

def _check_pass():
    if answer_pass == 42:
        return True
    return "Expected 42."

grader.check("ex_pass", _check_pass)

# %% [markdown]
# **Expected output:** `✓ ex_pass`

# %% [markdown]
# ---
# ## Section 3 — Failing exercise with hint
#
# `check_fn` returns a hint string → should print `✗ ex_fail: <hint>`.

# %%
answer_fail = "hello"   # wrong — should be a list

def _check_fail():
    if isinstance(answer_fail, list):
        return True
    return f"Expected a list, but got {type(answer_fail).__name__}."

grader.check("ex_fail", _check_fail)

# %% [markdown]
# **Expected output:** `✗ ex_fail: Expected a list, but got str.`

# %% [markdown]
# ---
# ## Section 4 — Re-running an exercise
#
# First run the cell with a **wrong** answer, then fix it and re-run.
# The Grader should overwrite the old result so `ex_rerun` appears **once**
# in the report, with the final (passing) result.

# %%
# --- First attempt (wrong) ---
answer_rerun = 0   # wrong

def _check_rerun():
    if answer_rerun == 99:
        return True
    return f"Got {answer_rerun!r}, expected 99."

grader.check("ex_rerun", _check_rerun)

# %% [markdown]
# **Expected output:** `✗ ex_rerun: Got 0, expected 99.`

# %%
# --- Second attempt (correct) — simulates student fixing their answer ---
answer_rerun = 99  # now correct

grader.check("ex_rerun", _check_rerun)

# %% [markdown]
# **Expected output:** `✓ ex_rerun`
#
# After these two cells `ex_rerun` will appear **once** in the report
# (in its original position) with a ✓.

# %% [markdown]
# ---
# ## Section 5 — Exception inside check_fn
#
# If the student's code raises an exception (common: `NameError` when a
# variable hasn't been defined yet), the Grader catches it and shows a
# helpful message instead of crashing the notebook.

# %%
# Simulate a student who hasn't defined `my_list` yet.
# The check references it, triggering a NameError.

def _check_exception():
    # `my_list` is intentionally not defined — this raises NameError
    return my_list == [1, 2, 3]   # noqa: F821

grader.check("ex_exception", _check_exception)

# %% [markdown]
# **Expected output:**
# ```
# ✗ ex_exception: Your code raised an error before the check could run:
#     NameError: name 'my_list' is not defined
# ```

# %% [markdown]
# ---
# ## Section 6 — One more passing exercise
#
# Confirms we can keep adding checks after an exception.

# %%
my_greeting = "Hello, Python!"

def _check_greeting():
    if isinstance(my_greeting, str) and my_greeting.startswith("Hello"):
        return True
    return "Expected a string that starts with 'Hello'."

grader.check("ex_greeting", _check_greeting)

# %% [markdown]
# **Expected output:** `✓ ex_greeting`

# %% [markdown]
# ---
# ## Final Report
#
# Should show **3 passes** (`ex_pass`, `ex_rerun`, `ex_greeting`) and
# **2 failures** (`ex_fail`, `ex_exception`) → **Score: 3 / 5  (60%)**.

# %%
grader.report()
