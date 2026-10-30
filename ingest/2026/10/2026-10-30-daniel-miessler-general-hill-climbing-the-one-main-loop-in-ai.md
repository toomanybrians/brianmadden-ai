---
title: 'General Hill-Climbing: The One Main Loop in AI'
source: Daniel Miessler
source_id: daniel-miessler
source_url: https://danielmiessler.com/blog/general-hill-climbing?utm_source=rss&utm_medium=feed&utm_campaign=website
author: daniel@danielmiessler.com (Daniel Miessler)
date_published: '2026-10-29'
date_captured: '2026-10-30'
ingest_method: feed
model: claude-sonnet-5
---

# General Hill-Climbing: The One Main Loop in AI

## Insights

- Miessler frames a single recurring loop underlying all effective AI-driven work ("General Hill-climbing"): define desired state, articulate it clearly, measure progress, do/test the work, then iterate.
- He argues most AI failures today aren't execution failures — AI largely does what's asked — but articulation failures: users give incomplete or self-contradicting pictures of what they want.
- He describes a three-layer information loss model: the true idea in one's head → its capture in an artifact (text/voice) → the AI's build from that artifact. AI only ever has access to the second layer, never the first, making high-quality capture (even hours of dictation) critical.
- Evals are positioned as the measurement/instrumentation layer that used to be software-specific but is becoming universal — applicable to reports, marketing, sales, design, any knowledge work — and are ranked as the second most critical component after ideal-state articulation.
- He catalogs eval types (binary checks, pairwise comparisons, rubric scoring, tournaments, reference-matching, reproducibility testing, personalized AI judges) and recommends running cheap deterministic checks before expensive AI-judge evals.
- Both the ideal-state description and the evals themselves are treated as iterative/evolving artifacts — a result that passes all evals but still "feels wrong" signals a missing or flawed eval criterion, not just a bad output.
- The loop is pitched as a generalized problem-solving mechanism beyond AI specifically — applicable to personal improvement, enterprise work, and "AI harnesses" broadly.

## Quote

> The problem is often us either: a. Not giving a complete picture of what we wanted b. Giving an incorrect / conflicting picture
