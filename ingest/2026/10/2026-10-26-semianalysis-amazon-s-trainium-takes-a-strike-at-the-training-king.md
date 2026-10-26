---
title: Amazon’s Trainium Takes a Strike at the Training King
source: SemiAnalysis
source_id: semianalysis
source_url: https://newsletter.semianalysis.com/p/amazons-trainium-takes-a-strike-at
author: Kimbo Chen
date_published: '2026-10-23'
date_captured: '2026-10-26'
ingest_method: feed
model: claude-sonnet-5
---

# Amazon’s Trainium Takes a Strike at the Training King

## Insights

- Amazon's Trainium chip has shifted strategy toward native PyTorch support (TorchNeuron), replacing the older PyTorch/XLA approach that required bespoke execution models and out-of-tree APIs — making it far more accessible to researchers used to CUDA/PyTorch workflows rather than just frontier-lab kernel engineers.
- In benchmark testing, Trainium3 showed competitive or superior matrix-multiplication efficiency (MFU) versus Nvidia's GB300/B200 in mid-range compute workloads, though Nvidia still leads in a narrower band of very large operations.
- A major weakness remains compile time: first-step compilation took 30-55x longer than average training steps, and one test (gpt-oss 20B) took over 27 minutes to compile — a significant friction point for researchers iterating on model architecture, though AWS claims upcoming fixes targeting two-orders-of-magnitude reduction.
- AWS's Neuron Explorer profiler is described as superior to Nvidia's and AMD's equivalents, with fine-grained, hardware-co-designed event timelines, dependency visualization, and memory throughput views not available in Nvidia's Nsight tools.
- AWS is running large-scale automated quality assurance against 100k+ Hugging Face models to test numerical parity, performance, and architecture coverage — the piece contrasts this favorably with other chip vendors' internal reporting practices, where QA failures were reportedly obscured before reaching senior leadership.
- Anthropic is already running production inference and RL rollouts on Trainium2/Trainium3, and its performance engineering team has reportedly praised Trainium's profiling capabilities over Nvidia's.

## Quote

> It is easy to get decent MFU%, but it is hard to get decent MFU% while not introducing numeric issues.
