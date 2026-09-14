---
title: 'Long Live the Short King: Why 4-hi HBM Wins'
source: SemiAnalysis
source_id: semianalysis
source_url: https://newsletter.semianalysis.com/p/long-live-the-short-king-why-4-hi
author: Myron Xie
date_published: '2026-09-13'
date_captured: '2026-09-14'
ingest_method: feed
model: claude-sonnet-5
---

# Long Live the Short King: Why 4-hi HBM Wins

## Insights

- HBM stack height (4-hi vs 8-hi vs 12-hi) delivers identical per-cube bandwidth, since I/O pins are fixed at 2048 per stack and split across dies — meaning shorter stacks give better $/bandwidth at no bandwidth cost, only less capacity.
- Nvidia's Rubin Ultra is cutting HBM per GPU to 192GB from 288GB (down from an earlier expectation of 1TB), driven both by HBM wafer scarcity/cost and by a recognition that excess capacity is often "stranded" and not worth its BOM cost.
- The compute mix has shifted from capacity-hungry pre-training toward bandwidth-bound inference/RL, and rack-scale systems (e.g., GB300 NVL72, Rubin Ultra NVL576) now provide so much aggregate memory that model weights (even quantized to 4-bit) consume a small fraction of it, easing pressure for taller HBM stacks.
- Modeling on Kimi K3 shows that above certain interactivity thresholds, 8-hi and 12-hi HBM produce only modest throughput gains (8% and 10% over 4-hi) that don't offset their 12.1% and 26.3% cost premiums — making 4-hi the lower cost-per-token option at current HBM prices.
- Real InferenceX benchmark testing (85% vs 92% HBM utilization) showed throughput held steady until high concurrency, where restricted HBM caused a ~30% throughput drop once KV cache occupancy hit 100%, with over 10x more DRAM offload reads — indicating KV cache offloading can meaningfully cushion reduced HBM capacity.
- Counter-considerations: future models could be much larger (justifying more capacity), but trends like looped transformers (reportedly used in GPT-6 Astra), heavier RL/reasoning-time scaling, and hardware/software co-design pressure from frontier labs' own hardware teams are cited as reasons model architectures may adapt to smaller-capacity chips rather than vice versa.
- Frames 4-hi as optimizing "tokens per HBM wafer" — analogous to tokens/watt — since it can roughly double or triple harvestable bandwidth per wafer versus 8-hi/12-hi, potentially freeing DRAM wafer capacity for other starved uses like server DRAM.

## Quote

> Silicon and hardware teams at frontier labs see 4-hi HBM as the optimal SKU for many inference workloads.
