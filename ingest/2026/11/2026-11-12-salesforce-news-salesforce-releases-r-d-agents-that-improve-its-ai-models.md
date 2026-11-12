---
title: Salesforce Releases R&D Agents That Improve Its AI Models
source: Salesforce News
source_id: salesforce-news
source_url: https://www.salesforce.com/news/stories/agents-that-improve-ai-models/
author: Salesforce News
date_published: '2026-11-11'
date_captured: '2026-11-12'
ingest_method: feed
model: claude-sonnet-5
---

# Salesforce Releases R&D Agents That Improve Its AI Models

## Insights

- Salesforce AI Research built SFR-AutoR&D, a system of two agents (AutoR&D-Engineer and TrainForge) that autonomously runs the ML research loop — forming hypotheses, implementing methods, and testing them against baselines — retaining changes only when evidence supports measurable improvement.
- The system has already improved real production infrastructure: it optimized SFR-Embedding V3 (Salesforce's Data Cloud retrieval model) and took the open-source EmbeddingGemma 2 model to produce SFR-Embedding v4, with gains in both quality and latency.
- It previously demonstrated gains on heavily-optimized, years-old open-source codebases (pandas, hnswlib, USearch), suggesting the agents can find real optimization headroom even in mature, expert-tuned software.
- Quantified results: a research cycle that would traditionally take "several weeks" of human work was completed in ~80 hours; a follow-up efficiency run took ~9 hours and yielded 36% more throughput and 17% lower latency with minimal quality loss; initial retrieval quality improved nDCG@10 by 6.13 points on MTEB benchmarks.
- Autonomy is explicitly bounded: humans set the goal, compute budget, evaluation criteria, and data constraints (including ethical/legal review of training data); the system only explores within those limits and an unverified improvement means the model doesn't change.
- A related system, CodeEvolve, uses evolutionary search with LLMs to improve Java and Salesforce Apex code quality — mentioned as upcoming coverage, not detailed here.

## Quote

> "We used to count progress in weeks of human work. Now we count it in hours of compute." — Shafiq Joty, Senior Research Director, Salesforce
