---
title: 'Mistral Large 4: Where Did the 41 Go?'
source: The AI Realist
source_id: ai-realist
source_url: https://www.airealist.ai/p/mistral-large-4-terminal-bench-41-removed
author: Julien Simon
date_published: '2026-11-11'
date_captured: '2026-11-12'
ingest_method: feed
model: claude-sonnet-5
---

# Mistral Large 4: Where Did the 41 Go?

## Insights

- Mistral's headline claim that Large 4 scored 41% on Terminal-Bench 4.0 (and led open-weight models) was traced to a specific Artificial Analysis (AA) benchmark row that was later quietly deleted from AA's public page, with a different, lower-scoring row (26%) relabeled to take its place — with no changelog entry or public explanation from AA.
- The deleted run and its replacement differ materially: the removed "High" run used ~293,637 output tokens per task (matching Mistral's own published 8.5M tokens/task figure), while the surviving row relabeled "High" used far fewer tokens (~193,504), matching what Mistral's own release chart had called "Medium."
- As of the time of writing, Mistral's release page, Hugging Face model card, and technical report still display the original 41%/48% figures sourced to AA, with no update acknowledging that AA's own page no longer shows that data — and a direct user question about the discrepancy on Hugging Face went unanswered for a week.
- Independent reproductions (Vals AI) show far more modest, mixed results for the release vs. preview model: gains on some benchmarks, losses on others, mostly within margin of error — suggesting the main verified improvement is efficiency (fewer output tokens, lower cost), not raw coding capability.
- A related confusion: Mistral's Vibe coding agent offered a "Max" reasoning effort level for ten days that the underlying API didn't actually support, muddying which benchmark run corresponds to which real-world deployable configuration.
- The piece frames this as a case study in the fragility of public AI benchmarking infrastructure — benchmark data can be silently edited or removed by the grading organization, and a lab can continue citing a vanished number without correction, undermining the practical ability of outside parties to verify claims.

## Quote

> A benchmarker that deletes a published run, relabels another... owes its readers one line. AA wrote none.
