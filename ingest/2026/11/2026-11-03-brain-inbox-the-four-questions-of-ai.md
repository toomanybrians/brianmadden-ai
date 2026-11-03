---
title: The Four Questions of AI
source: brain@ inbox (curated newsletters)
source_id: brain-inbox
source_url: ''
author: Tomasz Tunguz <blog@tomtunguz.com>
date_published: '2026-11-02'
date_captured: '2026-11-03'
ingest_method: email
model: claude-sonnet-5
---

# The Four Questions of AI

## Insights

- The AI stack splits into four layers (application, harness/context, model, data center), each facing a distinct unresolved question about durability of advantage, and the layers are coupled: a shift in one (e.g., GPU prices or new architectures) can swing economics across the whole stack.
- At the application layer, thin wrappers are vulnerable to being absorbed by model updates; durable moats require brand, pricing disruption, proprietary models, or outpacing competitors — and if agents fully automate work, UI-based apps may collapse entirely into middleware/harnesses.
- The harness (runtime context/tool layer around a model) increasingly matters more than the model itself: benchmarks show both OpenAI and Anthropic models performed better inside Cursor's harness than their own native ones, and since input context is up to 98% of tokens, smarter context handling can cut costs ~71% and lift gross margins from 38% to 75%. Enterprises are also building their own "sovereign" harnesses to keep data/context in-house while swapping underlying models.
- At the model layer, frontier training costs (billions per run) aren't clearly paying off — AI writes 75% of Google DeepMind's production code with no measurable research speedup — and SOTA models are losing token share to smaller fine-tuned or domain-specific models (~83% of agent tasks now route to these), even as Anthropic's S-1 shows cost-per-task reductions driving accelerated revenue growth (Jevons paradox). New architectures (diffusion models, JEPA) are also bypassing brute-force scaling with far less data/compute.
- At the data-center layer, physical and financial constraints (tripled concrete costs, turbine/generator backlogs, grid strain, $4T in projected AI-related debt, rising CDS spreads on companies like CoreWeave) are currently outpacing GPU demand, with open questions about debt duration matching cash flows, GPU hardware lifespan, and future GPU-hour pricing direction.

## Quote

> Like a double pendulum, the four layers form a coupled system: simple in each part, yet complex, chaotic, & unpredictable in motion.
