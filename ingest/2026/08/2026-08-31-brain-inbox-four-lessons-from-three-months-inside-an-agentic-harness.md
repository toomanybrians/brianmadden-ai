---
title: Four Lessons From Three Months Inside An Agentic Harness
source: brain@ inbox (curated newsletters)
source_id: brain-inbox
source_url: ''
author: Tomasz Tunguz <blog@tomtunguz.com>
date_published: '2026-08-30'
date_captured: '2026-08-31'
ingest_method: email
model: claude-sonnet-5
---

# Four Lessons From Three Months Inside An Agentic Harness

## Insights

- Author restructured a personal agentic workflow around an email inbox rather than a task list, because an inbox surfaces "waiting on you" items with a one-line reason instead of letting failures rot silently under a label.
- A single model was reconfigured as a router across tiers — fast local worker, local reasoner, cloud fallback — trading off cost (local, ~4-6 min) against reliability (cloud, ~39 sec), with a rule that the router must record the true reason for escalating to cloud rather than fabricating a local failure.
- Enabling self-healing (auto-redrive with jittered backoff, dead-lettering, auto-reverting bad deploys) caused the visible error rate to spike from 0% to 34% — not because the system got worse, but because it stopped silently hiding failures that previously required manual SQL recovery.
- The system now auto-reverts bad deploys (65 times, 42 due to failed unit tests) and catches broken code pre-deploy, but certain failure classes — auth token refresh, memory limits, a model that narrates instead of acting — still require human intervention.
- Work shifted from one monolithic prompt to a graph of contracted nodes: a model emits a narrow JSON intent (action, domain, reason, confidence), deterministic code executes the write, and a separate node verifies — enforcing that the same agent never grades its own output.
- Despite full automation of routing and error-handling, a human "quarterback" is still required to decide which tasks escalate, which failures need people, and which deploys get reverted.

## Quote

> Surfacing an error is not the same as fixing it.
