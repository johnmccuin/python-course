# Gradebook Setup Guide

This guide walks you through connecting the homework autograder to a
Google Sheet so student scores are recorded automatically when they
submit their homework.

---

## Overview

```
Student runs notebook
        │
        │  POST (JSON score)
        ▼
Google Apps Script web app   ←── gradebook.js
        │
        │  appendRow()
        ▼
Google Sheet  (Submissions tab)
        │
        │  MAXIFS formula
        ▼
Summary tab  (highest score per student per assignment)
```

---

## Step 1 — Create the Google Sheet

1. Go to [sheets.google.com](https://sheets.google.com) and create a
   new blank spreadsheet.
2. Name it something like **Python Course Gradebook**.
3. Leave the first tab as-is (the script will rename/create it automatically).

---

## Step 2 — Open the Apps Script editor

Inside the spreadsheet: **Extensions → Apps Script**.

A new browser tab opens with a code editor showing a blank `function myFunction() {}`.

---

## Step 3 — Paste the script

1. Select all the existing code in the editor and delete it.
2. Open `grader/gradebook.js` from this repo and copy its entire contents.
3. Paste it into the Apps Script editor.
4. Click **Save** (the floppy-disk icon, or Ctrl/Cmd+S).
   Name the project something like **Python Course Gradebook**.

---

## Step 4 — Deploy as a web app

1. Click **Deploy → New deployment**.
2. Click the gear icon next to "Select type" and choose **Web app**.
3. Fill in the fields:
   - **Description**: `Python Course Gradebook v1` (or anything)
   - **Execute as**: **Me** (your Google account)
   - **Who has access**: **Anyone**
4. Click **Deploy**.
5. Google will ask you to authorize the script — click through the
   permission screens (the script only needs access to the spreadsheet
   it lives in).
6. Copy the **Web app URL** — it looks like:
   ```
   https://script.google.com/macros/s/AKfycb.../exec
   ```
   Keep this URL private (anyone with it can write to your sheet),
   but it does **not** need to be secret from students — fake
   submissions are low-risk for an intro course.

> **Every time you change the script** you must click
> **Deploy → Manage deployments → Edit → New version → Deploy**
> to push the update.  Re-deploying gives you a new URL.

---

## Step 5 — Wire the URL into the homework notebook

Open `week-01/homework.py` and replace the placeholder in the setup cell:

```python
SUBMIT_URL = "https://script.google.com/macros/s/YOUR_SCRIPT_ID/exec"
```

with your actual URL, then run `bash build.sh` and commit.

---

## Step 6 — Test it

Run the solution notebook locally (or in Colab) with a test name like
`"Test Student"`.  Open your Google Sheet — you should see a new row in
the **Submissions** tab within a few seconds.

---

## Step 7 — Add a Summary tab (highest score per student)

1. In your Google Sheet, click **+** to add a new tab and name it
   **Summary**.
2. In cell A1 add headers:

   | A | B | C | D | E |
   |---|---|---|---|---|
   | Student Name | Assignment | Best Score | Total | Best % |

3. As students submit, unique names will accumulate in the Submissions tab.
   You can pull the best score for each student/assignment pair with
   `MAXIFS`:

   ```
   =MAXIFS(Submissions!E:E, Submissions!C:C, A2, Submissions!D:D, B2)
   ```

   where A2 is the student name and B2 is the assignment title.

   Or use a pivot table: **Insert → Pivot table**, rows = Student Name,
   columns = Assignment, values = Score (MAX).

---

## Reusing for future weeks

For each new homework:

1. Copy `week-01/homework.py` → `week-02/homework.py` etc.
2. The same `SUBMIT_URL` works for all assignments — the `assignment`
   field in the payload (`"Week 2 Homework"`, etc.) distinguishes them
   in the sheet.
3. No changes to the Apps Script needed.
