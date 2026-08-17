---
title: Qwen 3.8 27B is excellent, but it defaults to wildly overthinking things
source: Simon Willison's Newsletter
source_id: simon-willison
source_url: https://simonw.substack.com/p/qwen-38-27b-is-excellent-but-it-defaults
author: Simon Willison
date_published: '2026-08-17'
date_captured: '2026-08-17'
ingest_method: feed
model: claude-sonnet-5
---

# Qwen 3.8 27B is excellent, but it defaults to wildly overthinking things

## Insights

- Qwen 3.8 27B (Alibaba, Apache 2.0) is a 17GB open-weight model that runs on consumer hardware (MacBook, DGX Spark) yet performs vision tasks, bounding-box detection, and coding-agent work competitively with proprietary models — but its default "xhigh" reasoning setting causes extreme over-thinking, e.g. 21 minutes and 22,276 reasoning tokens to draw a simple SVG, versus 2 minutes with reasoning disabled.
- Local/open models are closing the gap with frontier proprietary models faster than expected — a model this capable would have been "competitive with the best and most expensive proprietary models" a year ago, and now runs on a laptop, reducing dependence on datacenter-scale infrastructure.
- The main bottleneck for local models is inference speed, not capability: Qwen 3.8 27B ran at only 15-30 tokens/sec versus 74-184 tokens/sec for hosted models like GPT-5.6; architecture tricks like Multi-Token Prediction can boost local inference speed by ~72%.
- Anthropic made "auto mode" the default in Claude Code, arguing it reduces risk versus human approval fatigue: in one eval, humans only refused a swapped-in dangerous command 13.6% of the time, while auto mode would have blocked 89% of such actions — leaving an acknowledged 11% gap.
- Despite Anthropic's claims of blocking all 720 tested prompt-injection attacks, the author remains skeptical that agent "auto mode" can defend against supply-chain-style attacks (e.g. malicious packages instructing an agent to fetch and run additional tools), and advocates limiting agent access to sensitive data/tools as a more reliable mitigation.
- A separate piece by Sophie Alpert argues there are no lossless transformations of natural-language text — every AI rewrite changes meaning — so writers using AI to edit remain fully responsible for standing behind every sentence in a document.

## Quote

> The thing that will work is actually curing cancer.

— Dario Amodei
