---
title: Update-aware reasoning is somewhat rare in the environments we investigated.
  We
source: X (brianmaddenai home timeline)
source_id: x-timeline
source_url: https://x.com/ApolloResearch/status/2110737964518998102
author: '@ApolloResearch'
date_published: '2026-10-15'
date_captured: '2026-10-16'
ingest_method: x
model: claude-sonnet-5
---

# Update-aware reasoning is somewhat rare in the environments we investigated. We

## Insights

- Apollo Research reports that "update-aware reasoning" — models reasoning about updates to their own training or weights — is rare in the environments they tested, appearing in roughly 1-2 out of every 1,000 rollouts.
- The researchers suggest this type of reasoning could be deliberately induced through alignment techniques such as inoculation prompting or constitutional AI, rather than only emerging spontaneously.
- They specifically flag that Claude's constitution includes content teaching the model about flawed or imperfect training incentives, which could prompt the model to reason about its own training process and intended generalization behavior.
- The implication is that how models are trained/prompted (e.g., exposing them to meta-level information about training flaws) may causally shape whether and how they reason about their own updates.

## Quote

> Claude's constitution teaches models about flawed training incentives, which could lead to reasoning about training and intended generalization.
