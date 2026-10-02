---
title: Building better evals for knowledge work
source: Future-Proof Your Career with AI
source_id: khe-hy
source_url: https://khemaridh.substack.com/p/building-better-evals-for-knowledge
author: Khe Hy
date_published: '2026-10-01'
date_captured: '2026-10-02'
ingest_method: feed
model: claude-sonnet-5
---

# Building better evals for knowledge work

## Insights

- Describes a concrete workflow for building "evals" (systematic evaluation of LLM outputs) for a knowledge-work task: scanning Twitter/X for Claude/Anthropic updates relevant to investment-management clients, then drafting a monthly client summary.
- Moved the eval process from spreadsheets to Claude Code, using sub-agents and an interactive dashboard to tag a development set (25 tweets) and a held-out "Golden Set" (25 tweets) with include/exclude/maybe labels and reasons.
- The dashboard workflow: label a test set, run a skill (prompt) against it, score and surface disagreements with the model's reasoning, then iteratively refine the prompt based on labeled mistakes — improving scores from an initial baseline to 96% on the development set.
- When the refined skill was run on the untouched Golden Set, performance degraded significantly, revealing that iterating directly against the dev set had caused overfitting ("cheating") rather than genuine generalization.
- The final production prompt example shows detailed rule-based classification logic (official accounts only, product-change categories vs. excluded categories like pricing, research, or developer-only features) as the actual artifact being tested/evaluated.
- Key methodological takeaway: a eval score looking good against the set you tuned on doesn't mean the skill generalizes — a true held-out set is needed to catch overfitting, and after degradation the author had to rebuild the Golden Set entirely.

## Quote

> there's always the risk that you overfit... The Golden Set tests against "never seen before" tweets
