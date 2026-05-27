/**
 * gradebook.js — Google Apps Script for the python-course gradebook
 *
 * Paste this entire file into your Google Sheet's Apps Script editor
 * (Extensions → Apps Script), then deploy it as a web app.
 * See grader/GRADEBOOK_SETUP.md for step-by-step instructions.
 *
 * Submissions arrive as GET requests with query parameters:
 *   student_name, assignment, score, total, pct, timestamp
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

// Primary handler — called by grader.submit() via GET + query parameters.
function doGet(e) {
  // If there are no parameters this is just a browser visit — return info.
  if (!e.parameter || !e.parameter.student_name) {
    return ContentService
      .createTextOutput("This endpoint accepts submissions from course homework notebooks.")
      .setMimeType(ContentService.MimeType.TEXT);
  }

  try {
    var sheet = _getOrCreateSheet(SUBMISSIONS_SHEET);
    var p = e.parameter;

    sheet.appendRow([
      p.timestamp  || "",                              // A: timestamp from client
      new Date(),                                      // B: server receipt time
      (p.student_name || "").trim(),                   // C: student name
      p.assignment || "",                              // D: assignment title
      p.score  !== undefined ? Number(p.score)  : "", // E: exercises passed
      p.total  !== undefined ? Number(p.total)  : "", // F: total exercises
      p.pct    !== undefined ? p.pct + "%"      : "", // G: percentage string
    ]);

    return _json({ status: "ok" });

  } catch (err) {
    return _json({ status: "error", message: err.toString() });
  }
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
    sheet.getRange(1, 1, 1, HEADERS.length).setFontWeight("bold");
  }

  return sheet;
}

function _json(obj) {
  return ContentService
    .createTextOutput(JSON.stringify(obj))
    .setMimeType(ContentService.MimeType.JSON);
}
