---
title: 'Vera Rubin NVL72 Agentic Inference: 67x better Performance per Dollar'
source: SemiAnalysis
source_id: semianalysis
source_url: https://newsletter.semianalysis.com/p/vera-rubin-nvl72-agentic-inference
author: Bryan Shan
date_published: '2026-09-14'
date_captured: '2026-09-15'
ingest_method: feed
model: claude-sonnet-5
---

# Vera Rubin NVL72 Agentic Inference: 67x better Performance per Dollar

## Insights

- SemiAnalysis's benchmarking (AgentX/InferenceX) claims NVIDIA's new Rubin platform delivers up to 67x more total throughput per TCO dollar than the prior-generation GB300 at matched token-speed targets, with the gap narrowing to 1.4–3x at realistic serving speeds (60-100 TPS).
- The piece argues NVIDIA has a pattern of underselling ("sandbagging") its own generational performance claims at GTC — citing GB200 NVL72 being measured at 98x Hopper's performance versus Jensen's claimed 30x, and now Rubin showing up to 7x performance-per-megawatt gains versus a claimed 3x.
- Per-gigawatt economics are framed as the real constraint on scaling AI infrastructure: since powered datacenter capacity is limited, more tokens generated per GW directly translates to more revenue/profit without needing additional utility power — Rubin is modeled to generate ~39% more revenue and ~42% more profit per GW than the best GB300 configuration.
- A new feature called "DSX MaxLPS" enables dynamic power-shifting across a GPU cluster based on real workload power draw (rather than provisioning for max TDP + oversubscription), allowing more GPUs to fit within the same power footprint.
- The efficiency advantage also creates strategic pricing flexibility: an operator could reportedly cut prices ~28% while still matching a competitor's revenue per GW, using the efficiency gain either as pure profit or as a competitive pricing lever.
- Agentic AI workloads are characterized as structurally different from chatbot workloads — multi-turn, long-context, high KV-cache prefix reuse, and bursty sub-agent calls — which is why hardware co-designed specifically for these patterns (rather than general LLM inference) shows outsized gains.

## Quote

> Jensen needs to stop sandbagging his performance claims at GTC.
