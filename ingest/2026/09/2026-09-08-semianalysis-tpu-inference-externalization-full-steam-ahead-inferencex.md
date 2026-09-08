---
title: TPU Inference Externalization Full Steam Ahead - InferenceX
source: SemiAnalysis
source_id: semianalysis
source_url: https://newsletter.semianalysis.com/p/tpu-inferencex-full-steam
author: Alec Ibarra
date_published: '2026-09-07'
date_captured: '2026-09-08'
ingest_method: feed
model: claude-sonnet-5
---

# TPU Inference Externalization Full Steam Ahead - InferenceX

## Insights

- Google's TPUv7 (Ironwood) is now being benchmarked by third parties against Nvidia's B200/B300, showing up to 50% better performance-per-dollar in aggregated FP8 serving — signaling Google's shift from purely internal use toward actively competing for external inference workloads.
- Anthropic is described as TPU's largest external customer, having committed to over one million chips (~400k+ purchased, 600k+ rented via GCP), used mainly for training but increasingly for inference.
- A new software stack, TorchTPU, is replacing the older TorchAX/JAX-translation approach, letting PyTorch treat TPUs as native devices; this is expected to substantially lower the engineering cost of bringing new open-weight models to TPUs and could bring TPU support to "day-0" status in vLLM/SGLang alongside Nvidia.
- Google's per-chip economics advantage is attributed to systemic co-design (compute die, interconnect, compiler) rather than raw single-chip performance — TPU still trails Nvidia GPUs on raw throughput/latency in many scenarios but wins on cost-adjusted throughput.
- Model architecture choices (attention head dimensions, KV head counts, MoE expert widths) now carry real performance costs on TPU's wide 256x256 systolic array, meaning some popular open models are structurally expensive to optimize for TPUs regardless of software maturity — a hidden constraint shaping which models get supported first.
- Disaggregated prefill/decode serving, speculative decoding, and KV-cache offloading (for long-context, multi-turn "agentic" workloads) are flagged as the next major frontier for TPU externalization, with Google having run these internally for years but only recently begun open-sourcing the tooling.

## Quote

> Google's cost-per-token advantage on inference is a result of co-design.
