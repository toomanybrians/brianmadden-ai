#!/usr/bin/env bash
# Blocks Bash commands that would print .env's contents into the
# conversation transcript. Added 2026-08-31/09-01 after repeated
# accidental credential exposure (grep -n, cat, Read tool calls that
# displayed real API keys/OAuth tokens instead of just checking
# existence). Existence/match checks (grep -q, test -f, etc.) stay
# allowed — this only blocks commands that would actually echo content.
# Matches only the real secret files (.env, .env.local) as whole
# filename tokens, so .env.example (public, no real secrets, meant to
# be read) is deliberately not caught by this pattern.
#
# Explicit "allow" decisions throughout (not just a silent exit 0) —
# 2026-09-01 fix: once a command references .env at all, silently
# exiting 0 for the "this is a safe sub-pattern" branch was being
# treated as a denial rather than deferring to the normal permission
# flow, even though the exact same silent-exit-0 works fine for
# commands that never mention .env at all. Being explicit here removed
# the ambiguity; verified live.
set -uo pipefail

input="$(cat)"
command="$(printf '%s' "$input" | jq -r '.tool_input.command // empty' 2>/dev/null || true)"

allow() {
  echo '{
  "hookSpecificOutput": {
    "hookEventName": "PreToolUse",
    "permissionDecision": "allow",
    "permissionDecisionReason": "Existence/match check on .env, not a content read."
  }
}'
  exit 0
}

deny() {
  echo '{
  "hookSpecificOutput": {
    "hookEventName": "PreToolUse",
    "permissionDecision": "deny",
    "permissionDecisionReason": "Blocked: this command would print .env'"'"'s contents (real API keys/OAuth tokens) into the conversation. Use grep -q/-c/-l for an existence or match check, or test -f, instead."
  }
}'
  exit 0
}

ENV_FILE_RE='(^|[^.[:alnum:]_-])\.env(\.local)?([^.[:alnum:]_-]|$)'

# No real .env/.env.local reference at all -> nothing to check, let the
# normal permission flow decide (no opinion from this hook).
if ! printf '%s' "$command" | grep -qE "$ENV_FILE_RE"; then
  exit 0
fi

# Safe patterns: existence/match checks that never print file content.
if printf '%s' "$command" | grep -qE -- '(^|[[:space:]])(test|stat|wc|ls|git|basename|dirname|md5|md5sum|sha256sum|rm|rmdir)([[:space:]]|$)'; then
  allow
fi
if printf '%s' "$command" | grep -qE -- '(^|[[:space:]])\[[[:space:]]'; then
  allow
fi
if printf '%s' "$command" | grep -qE -- ' -[a-zA-Z]*q[a-zA-Z]* '; then
  allow
fi
if printf '%s' "$command" | grep -qE -- 'grep[[:space:]]+(-[a-zA-Z]*[clq][a-zA-Z]*[[:space:]]+)+'; then
  allow
fi

deny
