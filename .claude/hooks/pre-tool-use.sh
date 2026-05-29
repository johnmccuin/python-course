#!/bin/bash
# PreToolUse hook — blocks any git push/checkout that would leave main.
# Receives tool input as JSON on stdin.

INPUT="$(cat)"
TOOL_NAME="${CLAUDE_TOOL_NAME:-}"

if [ "$TOOL_NAME" != "Bash" ]; then
  exit 0
fi

CMD="$(echo "$INPUT" | python3 -c "import sys,json; d=json.load(sys.stdin); print(d.get('command',''))" 2>/dev/null || echo "")"

# Block: git push to any branch other than main
if echo "$CMD" | grep -qE 'git push.*origin' && ! echo "$CMD" | grep -qE 'git push.*origin main'; then
  echo "BLOCKED: Only 'git push origin main' is allowed in this repo. Work directly on main." >&2
  exit 2
fi

# Block: creating new branches
if echo "$CMD" | grep -qE 'git checkout -b|git switch -c'; then
  echo "BLOCKED: Branch creation is disabled. Commit directly to main." >&2
  exit 2
fi

exit 0
