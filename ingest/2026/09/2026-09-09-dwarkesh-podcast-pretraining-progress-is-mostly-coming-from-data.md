---
title: Pretraining progress is mostly coming from data
source: Dwarkesh Podcast
source_id: dwarkesh-podcast
source_url: https://www.dwarkesh.com/p/pretraining-progress-is-mostly-data
author: Dwarkesh Patel
date_published: '2026-09-08'
date_captured: '2026-09-09'
ingest_method: feed
model: claude-sonnet-5
---

# Pretraining progress is mostly coming from data

## Insights

- A controlled experiment training small models (up to 1e19 FLOPs) with year-representative recipes (2019 GPT-2 to 2025 OLMo-2) and year-representative data corpuses (2019 OpenWebText to 2025 UltraFineWeb) found data improvements delivered ~3.24x more compute-efficiency gains than model/architecture improvements (12.0x vs 3.7x).
- Data and model improvements were found to be largely independent — 88% of variance in capability scores was explained by additive effects, suggesting exploiting a model improvement doesn't require specific data engineering and vice versa.
- The authors argue this doesn't mean architectural research was unimportant — its real contribution was making larger compute budgets usable at all (preventing instability, memory/bandwidth limits) rather than raw efficiency gains, likening it to building sturdier "container ships" vs. faster "sailboats."
- Small models benefit more from careful data curation because they lack capacity, while large/overtrained frontier models may benefit more from throwing in larger, noisier datasets since SGD can extract signal — implying data curation strategy differs by scale.
- Measured year-over-year compute efficiency gains here (1.57x) were notably lower than a separately cited industry estimate of ~3x/year, attributed to the small experimental scale missing scale-dependent gains, inference-efficiency innovations, and tokenizer improvements.
- The piece flags an open, high-stakes question: since most gains so far exploited curation of a finite Common Crawl-based stock, future pretraining progress depends heavily on whether synthetic data can meaningfully expand usable data beyond this fixed supply.

## Quote

> "the container ship doesn't necessarily go faster, but it can lug thousands of tons of cargo... and won't be toppled by choppy waters"
