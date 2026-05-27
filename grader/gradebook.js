/**
 * gradebook.js — Google Apps Script for the python-course gradebook
 *
 * Paste this entire file into your Google Sheet's Apps Script editor
 * (Extensions → Apps Script), then deploy it as a web app.
 * See grader/GRADEBOOK_SETUP.md for step-by-step instructions.
 *
 * Expected JSON payload (POST body):
 *   {
 *     "student_name": "Ada Lovelace",
 *     "assignment":   "Week 1 Homework",
 *     "score":        6,
 *     "total":        7,
 *     "pct":          86,
 *     "timestamp":    "2026-05-27T02:14:00Z"
 *   }
 *
 * The script appends one row per submission.  Use the MAXIFS formula
 * in a summary sheet to compute each student's highest score per
 * assignment (see GRADEBOOK_SETUP.md).
 */

// Name of the sheet tab that receives raw submissions.
var SUBMISSIONS_SHEET = "Submissions";

// Column headers written automatically on first run.
var HEADERS = [
  "Timestamp (UTC)",
  "Received (local)",
  "Student Name",
  "Assignment",
  "Score",
  "Total",
  "Percent",
];

// ---------------------------------------------------------------------------

function doPost(e) {
  try {
    var sheet = _getOrCreateSheet(SUBMISSIONS_SHEET);
    var data  = JSON.parse(e.postData.contents);

    sheet.appendRow([
      data.timestamp || "",                         // A: timestamp from client
      new Date(),                                   // B: server receipt time
      (data.student_name || "").trim(),             // C: student name
      data.assignment    || "",                     // D: assignment title
      data.score         ?? "",                     // E: exercises passed
      data.total         ?? "",                     // F: total exercises
      data.pct != null ? data.pct + "%" : "",       // G: percentage string
    ]);

    return _json({ status: "ok" });

  } catch (err) {
    return _json({ status: "error", message: err.toString() });
  }
}

// Friendly message if someone opens the URL in a browser.
function doGet(e) {
  return ContentService
    .createTextOutput("This endpoint accepts POST requests from course homework notebooks.")
    .setMimeType(ContentService.MimeType.TEXT);
}

// ---------------------------------------------------------------------------
// Helpers

function _getOrCreateSheet(name) {
  var ss    = SpreadsheetApp.getActiveSpreadsheet();
  var sheet = ss.getSheetByName(name);

  if (!sheet) {
    sheet = ss.insertSheet(name);
  }

  // Write headers if the sheet is empty.
  if (sheet.getLastRow() === 0) {
    sheet.appendRow(HEADERS);
    sheet.setFrozenRows(1);

    // Bold the header row.
    sheet.getRange(1, 1, 1, HEADERS.length).setFontWeight("bold");
  }

  return sheet;
}

function _json(obj) {
  return ContentService
    .createTextOutput(JSON.stringify(obj))
    .setMimeType(ContentService.MimeType.JSON);
}
