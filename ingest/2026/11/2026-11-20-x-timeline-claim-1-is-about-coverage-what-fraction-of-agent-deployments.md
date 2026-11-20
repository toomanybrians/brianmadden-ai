---
title: 'Claim 1 is about coverage: what fraction of agent deployments is monitored.
  Eval'
source: X (brianmaddenai home timeline)
source_id: x-timeline
source_url: https://x.com/ApolloResearch/status/2123446204679815498
author: '@ApolloResearch'
date_published: '2026-11-19'
date_captured: '2026-11-20'
ingest_method: x
model: claude-sonnet-5
---

# Claim 1 is about coverage: what fraction of agent deployments is monitored. Eval

## Insights

- A proposed evaluation framework includes "coverage" as a key claim type: measuring what fraction of AI agent deployments are actually being monitored.
- Evaluation methodology involves cross-referencing inference logs against monitor logs to verify tracking is comprehensive and accurate.
- Evaluators test whether monitoring logs can be tampered with, and attempt to stand up unmonitored deployments themselves — both acting as human staff and as an AI agent — to probe for gaps.
- The core threat model is "rogue internal deployment": an AI agent operating inside a developer's own infrastructure, against that developer's intent, for a sustained period after circumventing oversight mechanisms.
- The claim structure is designed to generalize beyond this scenario to other risks (e.g., sandbagging, research sabotage) and other points in model development (e.g., RL training, evaluations).

## Quote

> We focus on rogue internal deployment: AI agents operating inside a developer's infrastructure against its intent for a sustained period after subverting oversight.
