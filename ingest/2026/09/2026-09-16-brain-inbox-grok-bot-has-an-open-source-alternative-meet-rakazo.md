---
title: Grok Bot has an open-source alternative. Meet Rakazo.
source: brain@ inbox (curated newsletters)
source_id: brain-inbox
source_url: https://evalsignal.xyz/campaign/608c4090-c0e9-446c-b052-d547733538a6/ff779425-3a22-47e4-965d-bf0e1f18a567
author: EvalSignal <newsletter@evalsignal.xyz>
date_published: '2026-09-15'
date_captured: '2026-09-16'
ingest_method: email
model: claude-sonnet-5
---

# Grok Bot has an open-source alternative. Meet Rakazo.

## Insights

- Rakazo is an Apache-2.0 open-source alternative to Grok Bot's "persistent AI coworker" model: bots with memory, conversation history, standing routines, and cross-application access (browser, terminal, files, GUI desktop), available via web, Electron desktop, and Expo mobile clients.
- Scheduled/recurring work is backed by durable database state (prompts, schedules, timezones, next-run times), a transactional claim mechanism for scheduled runs, and a separate reconciliation process to recover stranded jobs — addressing the reliability gap between a cron-like UI and actual dependable recurring execution.
- The architecture separates the model/agent runtime (Pi) from the "computer" layer (execution environment), with pluggable computer providers (Docker, E2B, Daytona, Box) — letting users mix local and remote infrastructure and swap models/infra independently.
- Human-in-the-loop states are made explicit in the run lifecycle (running, waiting for input, waiting for takeover, completed, failed), with approvals tied to specific run/tool/argument combinations — creating an inspectable boundary for human oversight, though this doesn't guarantee safety.
- The "computer" (working environment) is treated as part of the product: workspace files and browser profiles can persist and migrate to replacement machines, though system-level packages don't automatically transfer — reducing lock-in as a bot accumulates context and history.
- Practical constraints in current beta: requires Docker for local setup, user supplies model credentials, an idle/sleeping laptop can't run scheduled jobs (needs an always-on server), managed cloud hosting is not yet available, and shared "Team Computers" mean isolation across workloads must be deliberately managed.
- The piece frames the real open question as measurable ROI — useful work completed per dollar and per minute of human correction — rather than demo quality, and calls for identical-task benchmarking against proprietary alternatives like Grok Bot.

## Quote

> Open source gives us the freedom to choose the machinery. Reliable execution will determine how much work we entrust to it.
