#!/usr/bin/env bash
# Starts missed-brief-alert.yml with a workflow_dispatch. Runs from a
# systemd timer on the runner box, weekdays at 08:15 Paris time, an hour and forty-five
# minutes after the daily pipeline's timer and well inside Brian's
# 9-11am reading window. The workflow checks whether today's brief is on
# main and emails him only if it isn't. Same shape as dispatch-daily.sh, and
# it reuses the same token file (an "Actions: read and write" token on this
# repo dispatches any workflow in it), so nothing new needs creating.
#
# One-time install on the box, mirroring the existing daily timer (the unit
# files for that live on the box, not in the repo):
#   1. Copy missed-brief-alert.service/.timer from the daily pair, changing
#      ExecStart to this script and OnCalendar to "Mon..Fri 08:15".
#   2. systemctl enable --now missed-brief-alert.timer
#   3. Fire it once by hand to check: systemctl start missed-brief-alert.service
#      (a normal day sends nothing; add -f test=true when dispatching the
#      workflow by hand if you want a labelled test email).

set -euo pipefail

REPO="toomanybrians/brianmadden-ai"
URL="https://api.github.com/repos/$REPO/actions/workflows/missed-brief-alert.yml/dispatches"

: "${DISPATCH_TOKEN_FILE:?DISPATCH_TOKEN_FILE is not set}"
token="$(<"$DISPATCH_TOKEN_FILE")"

for attempt in 1 2 3 4 5; do
  code="$(curl -sS -o /dev/null -w '%{http_code}' -X POST "$URL" \
    -H "Authorization: Bearer $token" \
    -H "Accept: application/vnd.github+json" \
    -H "X-GitHub-Api-Version: 2022-11-28" \
    -d '{"ref":"main"}')" || code="000"

  if [ "$code" = "204" ] || [ "$code" = "200" ]; then
    echo "dispatched missed-brief-alert.yml (attempt $attempt)"
    exit 0
  fi
  echo "dispatch failed with HTTP $code (attempt $attempt)" >&2
  # A bad, expired, or under-scoped token won't fix itself on retry.
  if [ "$code" = "401" ] || [ "$code" = "403" ] || [ "$code" = "404" ]; then
    exit 1
  fi
  sleep $((attempt * 60))
done
exit 1
