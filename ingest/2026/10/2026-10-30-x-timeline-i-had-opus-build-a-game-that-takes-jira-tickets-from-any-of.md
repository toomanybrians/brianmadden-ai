---
title: I had Opus build a game that takes JIRA tickets from any of your real projects
  &
source: X (brianmaddenai home timeline)
source_id: x-timeline
source_url: https://x.com/emollick/status/2115981377652822479
author: '@emollick'
date_published: '2026-10-30'
date_captured: '2026-10-30'
ingest_method: x
model: claude-sonnet-5
---

# I had Opus build a game that takes JIRA tickets from any of your real projects &

## Insights

- The project demonstrates an end-to-end AI content pipeline: Claude reads a raw JIRA backlog, infers a narrative "world" and character cast from it, writes scripts per ticket, and ElevenLabs voices them with performed (not read) delivery and generated sound effects.
- The system explicitly preserves real organizational details from the source tickets — real names, job titles, bot comments, and ticket specifics — turning mundane enterprise artifacts (standup bots, meeting tickets, flaky tests) into dramatized content without fabricating new material.
- The pipeline is modular and auditable: separate steps (write, cast, voice, sfx, qa, build) each read/write intermediate files, allowing a human to inspect or hand-edit AI output (e.g., a script) at any stage before continuing.
- It works with a company's actual live backlog via JIRA API/JQL, CSV, or JSON export, and explicitly warns that ticket contents become public once deployed — surfacing a confidentiality/data-exposure consideration for using real enterprise data in generative pipelines.
- The creator frames this as low-effort automation: roughly 18 Claude calls and ~12 minutes of generated speech (about 11,000 characters of TTS) to build a full playable "station" from 15–60 tickets, via a single CLI command.
- An optional QA step automatically transcribes generated audio and flags mismatches against the original script, pointing to a built-in verification/check layer for AI-generated output fidelity.

## Quote

> Every log is adapted from a ticket in a perfectly ordinary backlog.
