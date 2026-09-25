---
title: Thinking in Systems, Shipping in Loops
source: brain@ inbox (curated newsletters)
source_id: brain-inbox
source_url: ''
author: Tomasz Tunguz <blog@tomtunguz.com>
date_published: '2026-09-24'
date_captured: '2026-09-25'
ingest_method: email
model: claude-sonnet-5
---

# Thinking in Systems, Shipping in Loops

## Insights

- The author argues software engineering has shifted from writing code to designing systems that let AI write code correctly at scale — framed as the "new" definition of software engineering.
- Cited example: Artemis Security engineers went from merging 2 pull requests/day (Jan 2026) to 6 (May) to 16 (Aug), totaling 30,000 PRs in eight months; their CTO says every line of platform code is now written by AI agents, with engineers designing systems, setting constraints, and reviewing outputs.
- Second example: a Grok team engineer ships ~2,000 PRs/month (nearly 100/working day), attributing this not to model choice but to verification loops that let AI validate its own work.
- The piece names three properties of good system design, borrowed loosely from systems-thinking literature (Meadows): resilience (multiple layers of self-checking — tests, reviewer agents, production observability, not one single gate), self-organization (failures become reusable learned skills), and hierarchy (composable, verified skills/tools/sandboxes layered together).
- DHH (37signals) is quoted predicting that by end of 2026, hand-writing code will be economically unproductive across virtually all programmers, domains, and companies.
- Frames the shift as a new occupational identity: not "chiseling code by hand" but "steering intelligence" as a "professional maker of things."

## Quote

> Writing code by hand is no longer an economically productive enterprise for the vast majority of programmers.
