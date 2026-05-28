#!/bin/bash
# Session-start hook for python-course
# Runs at the start of every Claude Code web session.
# - Installs jupytext if needed
# - Ensures we're on main and up to date
# - Deletes the auto-created session branch (it's never used)

set -euo pipefail

# Only run in remote (web) sessions
if [ "${CLAUDE_CODE_REMOTE:-}" != "true" ]; then
  exit 0
fi

# ── 1. Install jupytext if missing ────────────────────────────────────────────
if ! command -v jupytext &>/dev/null; then
  pip install -r "$CLAUDE_PROJECT_DIR/requirements.txt" -q
fi

# ── 2. Record the auto-created session branch name, then switch to main ───────
SESSION_BRANCH="$(git -C "$CLAUDE_PROJECT_DIR" rev-parse --abbrev-ref HEAD)"

if [ "$SESSION_BRANCH" != "main" ]; then
  git -C "$CLAUDE_PROJECT_DIR" checkout main
fi

# ── 3. Pull latest main ───────────────────────────────────────────────────────
git -C "$CLAUDE_PROJECT_DIR" pull origin main --ff-only --quiet

# ── 4. Delete the session branch if it has no unique commits ─────────────────
if [ "$SESSION_BRANCH" != "main" ]; then
  UNIQUE=$(git -C "$CLAUDE_PROJECT_DIR" log --oneline "origin/main..origin/$SESSION_BRANCH" 2>/dev/null | wc -l || echo "0")
  if [ "$UNIQUE" -eq 0 ]; then
    # Delete locally (may not exist locally yet, so ignore errors)
    git -C "$CLAUDE_PROJECT_DIR" branch -D "$SESSION_BRANCH" 2>/dev/null || true
    # Delete on remote
    git -C "$CLAUDE_PROJECT_DIR" push origin --delete "$SESSION_BRANCH" 2>/dev/null || true
  fi
fi

echo "Session ready: on main, jupytext available."
