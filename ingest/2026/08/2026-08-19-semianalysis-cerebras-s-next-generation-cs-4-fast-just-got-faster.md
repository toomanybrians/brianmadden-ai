---
title: 'Cerebras''s Next Generation CS-4: Fast Just Got Faster'
source: SemiAnalysis
source_id: semianalysis
source_url: https://newsletter.semianalysis.com/p/cerebrass-next-generation-cs-4-fast
author: Myron Xie
date_published: '2026-08-19'
date_captured: '2026-08-19'
ingest_method: feed
model: claude-sonnet-5
---

# Cerebras's Next Generation CS-4: Fast Just Got Faster

## Insights

- Cerebras's CS-4 doubles token throughput per user over CS-3 by increasing power and clock speed on the same 5nm WSE-3 wafer, rather than a new chip generation — memory bandwidth (not just compute) is the metric driving this gain.
- The system keeps the same 44GB SRAM capacity per wafer as CS-3, which remains the core constraint of Cerebras's architecture — low memory capacity relative to HBM-based GPU systems, pushing customers toward disaggregated setups to compensate.
- Cerebras is redesigning its rack ("backpack" modular design, split power/compute) to simplify manufacturing and deployment, and is betting on open, heterogeneous, disaggregated inference architectures — positioning itself as the "decode" specialist chip paired with HBM systems (AMD, AWS Trainium) handling prefill.
- Claimed real-world interactivity gain is "up to 30-40x" versus GPUs (not the flashier 2,000x memory-bandwidth marketing number), with estimates of ~4,000 tok/sec/user for CS-4 versus ~100-200 tok/sec/user realistic ceiling for Blackwell GPUs.
- Running large frontier models (e.g., a 1.6T-parameter model) at long context and real concurrency requires significant Cerebras hardware investment — estimated ~40 systems, $20M+ CAPEX, 1MW power just to serve one frontier model at scale, per the piece's tokenomics analysis.
- Disaggregated inference (fixed hardware ratios of prefill:decode resources) is inherently less flexible than GPU/TPU fleets that can dynamically reallocate as workload profiles shift — a tradeoff the piece flags as a real risk over a 5+ year hardware lifespan.

## Quote

> One P:D ratio to rule them all is unlikely to be perfectly optimal for the 5+ year lifespan of these systems.
