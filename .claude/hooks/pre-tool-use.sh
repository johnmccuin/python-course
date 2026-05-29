#!/bin/bash
# PreToolUse hook — blocks git commands that create branches or push to non-main.
# Matched to Bash tool only via settings.json. Input JSON arrives on stdin.
# Claude Code input format: {"tool_name": "Bash", "tool_input": {"command": "..."}}

INPUT="$(cat)"
CMD="$(echo "$INPUT" | python3 -c "
import sys, json
d = json.load(sys.stdin)
print(d.get('tool_input', {}).get('command', ''))
" 2>/dev/null || echo "")"

# Block: creating new branches
if echo "$CMD" | grep -qE 'git (checkout -b|switch -c)'; then
  echo "BLOCKED: Branch creation is disabled. Commit directly to main." >&2
  exit 2
fi

# Block: git push to any remote branch other than main
if echo "$CMD" | grep -qE 'git push' && echo "$CMD" | grep -qE 'origin' && ! echo "$CMD" | grep -qE 'origin main|origin HEAD'; then
  echo "BLOCKED: Only 'git push origin main' is allowed. Do not push to feature branches." >&2
  exit 2
fi

exit 0
