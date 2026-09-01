#!/usr/bin/env bash
# Unconditionally blocks the Read tool from opening .env/.env.local —
# unlike Bash, Read has no partial/safe mode (any successful Read shows
# the full file), so there's no "safe pattern" carve-out here the way
# guard-env-read.sh has for Bash. .env.example is deliberately excluded
# (public, no real secrets, meant to be read).
set -uo pipefail

input="$(cat)"
file_path="$(printf '%s' "$input" | jq -r '.tool_input.file_path // empty' 2>/dev/null || true)"

if printf '%s' "$file_path" | grep -qE '(^|/)\.env(\.local)?$'; then
  echo '{
  "hookSpecificOutput": {
    "hookEventName": "PreToolUse",
    "permissionDecision": "deny",
    "permissionDecisionReason": "Blocked: reading .env directly would print every credential in it into the conversation. Use Bash with grep -q/-c/-l or test -f for an existence/match check instead."
  }
}'
fi
exit 0
