#!/usr/bin/env bash
# Starts daily-pipeline.yml with a workflow_dispatch (`source: timer`).
# Runs from a systemd timer on the self-hosted runner box, weekdays at
# 06:30 Paris time; GitHub's own cron is only the backup (see "WHEN IT
# RUNS" atop the workflow for why). The workflow's guard job skips this
# run if today's brief is already on main.
#
# Needs DISPATCH_TOKEN_FILE: a file holding a fine-grained token with
# "Actions: read and write" on this one repo and nothing else. The token
# is never printed.

set -euo pipefail

REPO="toomanybrians/brianmadden-ai"
URL="https://api.github.com/repos/$REPO/actions/workflows/daily-pipeline.yml/dispatches"

: "${DISPATCH_TOKEN_FILE:?DISPATCH_TOKEN_FILE is not set}"
token="$(<"$DISPATCH_TOKEN_FILE")"

for attempt in 1 2 3 4 5; do
  code="$(curl -sS -o /dev/null -w '%{http_code}' -X POST "$URL" \
    -H "Authorization: Bearer $token" \
    -H "Accept: application/vnd.github+json" \
    -H "X-GitHub-Api-Version: 2022-11-28" \
    -d '{"ref":"main","inputs":{"source":"timer"}}')" || code="000"

  if [ "$code" = "204" ] || [ "$code" = "200" ]; then
    echo "dispatched daily-pipeline.yml (attempt $attempt)"
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
