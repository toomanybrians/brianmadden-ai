#!/usr/bin/env bash
# Just-in-time reminder: when a Claude session is about to WRITE to one of the
# maintainer journals (BUILD.md etc.), inject a short "this is public" note into
# its context. It never blocks anything; the commit-time lint
# (scripts/check_public_safe.py) is the actual gate. Added 2026-10-04 after a
# personal compensation aside ended up quoted in BUILD.md.
set -uo pipefail
input="$(cat)"
tool="$(printf '%s' "$input" | jq -r '.tool_name // empty' 2>/dev/null || true)"
file="$(printf '%s' "$input" | jq -r '.tool_input.file_path // empty' 2>/dev/null || true)"
cmd="$(printf '%s' "$input" | jq -r '.tool_input.command // empty' 2>/dev/null || true)"

names='(BUILD|MAINTAINER|GOVERNANCE)\.md|governance-log\.md|lessons\.md'
hit=""
case "$tool" in
  Edit|Write|MultiEdit)
    if printf '%s' "$(basename "$file")" | grep -q -E "^($names)$"; then hit=1; fi ;;
  Bash)
    # Mentions a journal AND looks like a write (redirect, sed -i, tee, python/open-for-write).
    if printf '%s' "$cmd" | grep -q -E "$names" && \
       printf '%s' "$cmd" | grep -q -E '>>|[^>=]>[^>=]|sed +-i|tee |\.write\(|python3? '; then hit=1; fi ;;
esac

[ -z "$hit" ] && exit 0
cat <<'JSON'
{"hookSpecificOutput":{"hookEventName":"PreToolUse","additionalContext":"PUBLIC REPO REMINDER: you are writing to a maintainer journal (BUILD.md / MAINTAINER.md / lessons / governance log). This repo and all of its git history are public. Do not record: personal finances or compensation, employer-internal strategy/people/customers, private network or machine details, credentials or where they live, offhand personal quotes, or other people's private details. Summarize decisions and outcomes, not asides. Deleting later does not remove it from history."}}
JSON
exit 0
