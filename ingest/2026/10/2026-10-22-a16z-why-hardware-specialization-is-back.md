---
title: Why Hardware Specialization is Back
source: a16z
source_id: a16z
source_url: https://www.a16z.news/p/why-hardware-specialization-is-back
author: Zain Asgar
date_published: '2026-10-21'
date_captured: '2026-10-22'
ingest_method: feed
model: claude-sonnet-5
---

# Why Hardware Specialization is Back

## Insights

- In the 1990s, general-purpose microprocessors beat specialized chips (vector processors, MPPs, Lisp machines) even on the specialized chips' own target workloads, via a virtuous cycle: generality drove volume, volume drove performance, performance drove further generality.
- That cycle broke down as Dennard scaling ended (~2005, voltage scaling stalled) and transistor cost-per-gate flattened (~2012), removing the "free" generational speedups that let generalist chips out-invest specialists.
- GPUs are reframed as the prior era's specialist survivor that became the new de facto generalist: GPU sales now exceed CPU sales, and GPUs have progressively absorbed specialized inference features (tensor cores in 2017, MXFP4/NVFP4 in 2024) the way CPUs once absorbed vector processing.
- Nvidia's single-GPU inference speedup of 1000x over ten years broke down mostly as: ~16x from lower-precision number formats, ~12.5x from new instructions, 2x from sparsity, and only ~2.5x from process node improvements — process scaling is no longer the dominant performance lever.
- The "memory wall" (compute scaling with chip area, bandwidth scaling with perimeter) is cited as a binding constraint, especially for memory-bandwidth-bound inference decode phases, pushing interest toward near-memory/SRAM-centric architectures like Groq (now Nvidia's LPU), Cerebras, and d-Matrix.
- Author argues current conditions differ from the 1990s in ways favoring specialization's durability: AI coding agents make it easier to write kernels/design chips, fabless models lower the barrier to building new chip companies, and power/performance-per-watt scarcity (token demand to grow 24x by 2030 vs. ~2x power growth) rewards workload-specific hardware.
- Frames this as a cyclical "pendulum" (per Tsugio Makimoto) between generalized and specialized hardware, predicting continued heterogeneity and cross-accelerator orchestration (GPUs, LPUs, TPUs, Trainium, etc.) for inference workloads in the near term, with eventual reconsolidation into generalist architectures likely but not immediate.

## Quote

> …ultimately these things were just going to be boxes of microprocessors.
