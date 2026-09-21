---
title: My Early Thoughts on Jev
source: Daniel Miessler
source_id: daniel-miessler
source_url: https://danielmiessler.com/blog/early-thoughts-on-jev?utm_source=rss&utm_medium=feed&utm_campaign=website
author: daniel@danielmiessler.com (Daniel Miessler)
date_published: '2026-09-19'
date_captured: '2026-09-21'
ingest_method: feed
model: claude-sonnet-5
---

# My Early Thoughts on Jev

## Insights

- Jev is described as a decision engine rather than an LLM: it outputs choices, scores, or yes/no judgments instead of generating text, at roughly the intelligence level of Sol or Opus.
- Its appeal rests on two factors: a large share of real-world AI work (classification, labeling, routing, spam/churn detection, security triage) reduces to exactly these discrete decision types, and Jev performs them nearly instantly (~200ms round-trip) and nearly free ($42 per billion input tokens, no output-token charge).
- The suggested workflow is to audit any AI pipeline or application, decompose it into judgment/classification sub-tasks, and route those through a decision layer like Jev before or after handing off to an LLM — architectures can be LLM-first-then-Jev or Jev-first-then-LLM.
- Proposed use within AI harnesses includes hook systems (pre/post tool-use, user-prompt-submit checks) and model-routing decisions.
- Eval systems are framed as a prime beneficiary: evals split into deterministic asserts and judgment (rubrics and tournaments), and rubrics/tournaments — traditionally slow, costly LLM tasks — map closely onto what a fast, cheap decision engine like Jev can do, enabling multi-staged evals that only escalate to an LLM when necessary.
- The author frames this as a potential new foundational layer ("cornerstone") for AI systems generally, since so much AI work is decision-making at scale rather than text generation.

## Quote

> This system, or a system like it, is likely to be a new cornerstone for all AI work being done anywhere.
