---
title: Where Does a Robot Think – On-Device vs Datacenter Inference
source: SemiAnalysis
source_id: semianalysis
source_url: https://newsletter.semianalysis.com/p/where-does-a-robot-think-on-device
author: Ivan Chiam
date_published: '2026-09-09'
date_captured: '2026-09-10'
ingest_method: feed
model: claude-sonnet-5
---

# Where Does a Robot Think – On-Device vs Datacenter Inference

## Insights

- Robotics inverts the LLM design pattern: instead of building hardware to serve an already-trained model, robot builders must first determine what fits real-time, cost-constrained on-robot hardware, then design the model to match — capping model capability against latency and unit economics rather than pure scaling.
- Frontier robot models remain small (5–14B parameters, e.g. Physical Intelligence's π0.7, NVIDIA's DreamZero) compared to trillion-parameter LLMs, though early evidence suggests scaling laws may still apply once data constraints (via world models and embodied data collection) ease.
- Companies are diverging on where cognition runs: Figure runs its Helix model fully onboard; Physical Intelligence and NVIDIA run policies off-robot on datacenter GPUs (H100s, dual GB200s) — the author argues a hybrid "cascade" is inevitable, with hierarchical models splitting a slow planning layer (offloadable to datacenter) from a fast local action/control layer.
- Practical constraints push heavy cognition off-robot: onboard chips (Jetson Thor) have roughly 1/10th to 1/14th the compute of a single datacenter GPU, robot batteries can't power datacenter-class chips, and offloading requires substantial local investment in image compression, uplink bandwidth, antenna placement, and network handover engineering.
- Supply-chain analysis: NVIDIA's silicon output and margins heavily favor datacenter GPUs over Jetson edge chips, and both wafer-efficiency and DRAM-efficiency calculations show that shared datacenter GPUs become more resource-efficient than onboard chips once fleets exceed roughly 5–7 robots per GPU.
- A TCO test (running DreamZero on a B300) found one B300 server could time-multiplex cognition for 7 robots while staying under a 1.6-second motion-latency budget, framing a scenario comparison of one B300 NVL8 server (56 robots) versus 56 individually-equipped Jetson Thor robots.

## Quote

> So the real question is not whether robots can get wafers. It is silicon efficiency.
