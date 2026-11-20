---
title: Claim 2 is about capability. Evaluators red-team monitoring from first-pass
  filt
source: X (brianmaddenai home timeline)
source_id: x-timeline
source_url: https://x.com/ApolloResearch/status/2123446204985975197
author: '@ApolloResearch'
date_published: '2026-11-19'
date_captured: '2026-11-20'
ingest_method: x
model: claude-sonnet-5
---

# Claim 2 is about capability. Evaluators red-team monitoring from first-pass filt

## Insights

- Evaluators propose two distinct claims for assessing AI agent monitoring systems: "coverage" (what fraction of deployments are actually monitored) and "capability" (whether the monitoring, when active, actually catches problems).
- For coverage claims, evaluators are expected to cross-check inference logs against monitor logs, verify logs can't be tampered with, and actively attempt to launch unmonitored agent deployments — testing both as human staff and as an agent itself.
- For capability claims, evaluators red-team the full monitoring pipeline, from first-pass automated filtering through to human review stages.
- "Detected" is defined narrowly as detection confirmed by a human, not just flagged by an automated system.
- Red-teaming alone cannot prove a monitor is effective, so evaluators are expected to also report on the rigor behind their testing: how much elicitation effort was applied, and how realistic and diverse the test scenarios were.

## Quote

> Red-teaming can't prove a monitor works, so evaluators should report the effort behind every result: elicitation, realism and diversity.
