---
title: A Brain Too Big to Carry — On-Device vs Datacenter Inference
source: SemiAnalysis
source_id: semianalysis
source_url: https://newsletter.semianalysis.com/p/a-brain-too-big-to-carry-on-device
author: Ivan Chiam
date_published: '2026-09-14'
date_captured: '2026-09-15'
ingest_method: feed
model: claude-sonnet-5
---

# A Brain Too Big to Carry — On-Device vs Datacenter Inference

## Insights

- Robotics inverts the LLM development pattern: instead of scaling a model and fitting hardware to it, robot manufacturers must fix affordable, real-time hardware first and design models to fit within that budget, since they (not end users) bear the capital cost of compute per unit.
- Frontier robot models remain in the billions of parameters (vs. trillions for LLMs) largely because of two hard constraints: real-time control loops that can't tolerate latency, and the cost of building compute into every physical unit at scale.
- A layered architecture is emerging in generalist robots: high-frequency action/servo control (100+ Hz) must stay on-device because network round-trips consume the entire latency budget, while lower-frequency planning/reasoning layers (5-20 Hz) have enough time headroom to be offloaded to datacenter GPUs — jitter, not average latency, is the harder problem to solve for offloading.
- Analysis of silicon/DRAM supply and TCO modeling suggests offloading robot "cognition" to shared datacenter GPUs (e.g., B300) is more efficient than embedding chips in every robot once fleets exceed roughly 5-12 robots per GPU, and datacenter offload reaches ~46% of on-device TCO per FLOP in industrial settings (and better in home settings) — though real-world utilization rates for robots are still very low (4-40%), which is the biggest swing factor.
- Companies are actually split by strategy today, largely based on network reliability at their deployment site: Boston Dynamics splits reasoning (cloud, via Google DeepMind/TPUs) from motor control (onboard Jetson) for factory generalist work; Agility Robotics, Verne, and Sunday Robotics keep inference fully onboard because home/factory WiFi jitter and safety requirements make offloading impractical today.
- The "network wall" blocking wider offload isn't the AI model — it's that WiFi/5G infrastructure was built for downlink-heavy stationary consumer use, not for uplink-heavy, moving, metal robotic clients; fixing this requires robot-aware scheduling, location-aware beamforming, multi-link operation, and mainboard/access-point co-design.

## Quote

> Intelligence becomes something you ration against latency and unit economics.
