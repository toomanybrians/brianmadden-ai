---
title: Pretraining progress is mostly coming from data
source: brain@ inbox (curated newsletters)
source_id: brain-inbox
source_url: https://dwarkesh.substack.com/p/pretraining-progress-is-mostly-data
author: Dwarkesh Patel <dwarkesh+blog@substack.com>
date_published: '2026-09-08'
date_captured: '2026-09-09'
ingest_method: email
model: claude-sonnet-5
---

# Pretraining progress is mostly coming from data

## Insights

- A controlled experiment training year-representative model recipes (2019–2025) against year-representative data corpuses found data quality improvements drove ~12x compute efficiency gains vs. ~3.7x from model/architecture improvements over that period — roughly 3.24x more of the gain came from data.
- Gains from data and model improvements were found to be largely independent/additive (88% of variance in eval scores explained by additive effects), suggesting better data doesn't require specific architectures and vice versa.
- The paper argues model-side research (MoEs, sparse attention, stability fixes, kernel optimizations like FlashAttention) mattered less for raw compute efficiency and more for making larger training runs feasible at all — removing bottlenecks rather than boosting quality per FLOP.
- Small models benefit disproportionately from careful data curation (limited capacity means garbage-in hurts more), while large, heavily overtrained frontier models may benefit more from just scaling up data volume than from aggressive filtering — implying the data-quality lesson may not transfer to frontier scale.
- Raises an open concern about a "data wall": since most gains studied came from curating existing internet scrapes rather than genuinely new data sources, and synthetic data's effectiveness at expanding usable corpora remains untested, future pretraining progress could stall if data curation runs out of room.
- Notes that RL post-training, not pretraining, has driven most AI progress in the last two years — meaning even if pretraining gains slow, that's not necessarily the most important bottleneck for overall AI advancement.

## Quote

> Now that we have more capacious and sturdy container ships, we don't have to fret about exactly what we load on board.
