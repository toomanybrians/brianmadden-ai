---
title: 'Spark-X2.5 vs the small-model field: who picks the right tool?'
source: brain@ inbox (curated newsletters)
source_id: brain-inbox
source_url: https://evalsignal.xyz/campaign/35fa915f-4fb6-4059-a676-7ad8b16e66e0/ff779425-3a22-47e4-965d-bf0e1f18a567
author: EvalSignal <newsletter@evalsignal.xyz>
date_published: '2026-10-03'
date_captured: '2026-10-05'
ingest_method: email
model: claude-sonnet-5
---

# Spark-X2.5 vs the small-model field: who picks the right tool?

## Insights

- Benchmark leaderboard performance didn't translate directly to practical task accuracy: Spark-X2.5 posts strong published agent scores (e.g., 65.1 BFCL-V4, 75.1 tau2-bench) but underperforms on a local, controlled test of actual next-action selection.
- A model can be highly reliable at producing syntactically valid tool calls (Spark-X2.5-4B: 96/100 structured) while being substantially worse at choosing the *correct* action/arguments (only 11/89 strict matches) — format compliance and judgment are separable capabilities.
- Smaller "class" labels (2B, 4B) often don't reflect actual parameter counts — e.g., Gemma 4 E4B is actually 7.5B total, Gemma 4 E2B is 4.6B — which complicates fair small-model comparisons and deployment decisions.
- Across multiple compact models, a shared failure pattern emerged: models default to a cautious "inspect the page first" action (get_accessibility_tree) rather than the specific next action requested, suppressing exact-match scores even when tool-calling infrastructure works fine.
- "Loose" match metrics (name-only or prose mapped to intent) can be misleading proxies for real task success — Gemma's leading loose scores and Spark-1.7B's loose score (partly from prose-only answers) overstate actual completed-action accuracy.
- The evaluators frame this as a broader caution about relying on official model-card benchmarks: independent, narrowly-scoped reproduction testing surfaced a materially different ranking (Qwen3.5 leading strict routing) than the vendor's published results implied.

## Quote

> Spark is exceptionally willing and able to produce structured tool calls, but Qwen remains better at strict action selection in both size classes.
