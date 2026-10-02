---
title: Claim 4 is about monitorability. Evaluating the first three claims hinges on
  und
source: X (brianmaddenai home timeline)
source_id: x-timeline
source_url: https://x.com/ApolloResearch/status/2105739269876703458
author: '@ApolloResearch'
date_published: '2026-10-01'
date_captured: '2026-10-02'
ingest_method: x
model: claude-sonnet-5
---

# Claim 4 is about monitorability. Evaluating the first three claims hinges on und

## Insights

- Frames "monitorability" as a precondition claim: assessing whether a model is behaving safely (claims 1-3) depends on being able to understand *why* it acts as it does, not just *what* it does.
- Notes that legible reasoning — the ability to read a model's rationale — is fragile and can degrade either through training pressure or through architecture changes.
- Because of that fragility, the monitorability claim can't be checked once and trusted; it needs re-verification any time training or architecture shifts.
- On internal deployment monitoring (claim 3), argues that an absence of detected incidents is only meaningful evidence if the monitoring actually covers high-stakes situations and is capable of catching scheming behavior from the specific model in use.
- Recommends evaluators actively red-team the monitoring setup itself and audit its coverage, rather than taking a clean incident record at face value.

## Quote

> Legible reasoning can be lost through training pressure or architecture changes, so this claim must be re-checked whenever either changes.
