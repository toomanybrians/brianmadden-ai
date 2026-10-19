---
title: I created a new system of measuring work output called Deeds that addresses
  this
source: X (brianmaddenai home timeline)
source_id: x-timeline
source_url: https://x.com/DanielMiessler/status/2111220310829900110
author: '@DanielMiessler'
date_published: '2026-10-16'
date_captured: '2026-10-19'
ingest_method: x
model: claude-sonnet-5
---

# I created a new system of measuring work output called Deeds that addresses this

## Insights

- Proposes "Deeds" as an alternative to pull requests for measuring software work, arguing PRs measure collaboration (code review) rather than value delivered, and that this mismatch worsens as more code is written solo by individuals working with AI agents and pushing straight to production.
- Classifies every commit into three categories judged from the diff itself (never commit messages): "cap" (a new or deepened capability), "fix" (something moved from broken to working, including security fixes), and "tend" (invisible upkeep like refactors, dependency bumps, tests).
- The system uses a two-stage pipeline: deterministic code-parsing extracts factual signals from a diff, then an AI model ("Clef") answers a structured set of yes/no questions, which feed into ~112 ordered rules (first match wins) that assign the final cap/fix/tend classification — explicitly designed so ambiguous cases default to "no deed" rather than being guessed.
- Applied to 90 days of Go's commit history (1,065 commits), the tool found 146 caps, 494 fixes, and 887 tends — illustrating that raw commit/PR counts obscure how much of that activity was actual new capability versus repair versus maintenance.
- Frames the motivating question as: if AI models can already catch bugs as well as human reviewers, the traditional justification for PR-based code review (catching mistakes) weakens, strengthening the case for a different measurement unit for AI-driven work.
- Positions Deeds as an open, self-hosted proposal (Claude Code plugin, runs via a user's own Cloudflare account, no telemetry) rather than a finished or authoritative standard — explicitly inviting critique of where it may be wrong.

## Quote

> Pull requests show that code changed. Deeds tries to show what got better.
