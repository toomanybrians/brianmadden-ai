---
title: Not a Good Week for American AI
source: brain@ inbox (curated newsletters)
source_id: brain-inbox
source_url: https://evalsignal.xyz/campaign/d14575ba-55c3-4bd9-9db4-74071ace6978/ff779425-3a22-47e4-965d-bf0e1f18a567
author: EvalSignal <newsletter@evalsignal.xyz>
date_published: '2026-10-29'
date_captured: '2026-10-30'
ingest_method: email
model: claude-sonnet-5
---

# Not a Good Week for American AI

## Insights

- On Artificial Analysis's Intelligence Index, Chinese models lead the current snapshot (DeepSeek V4.1 Flash 1017 at 45, Qwen3.8 Flash-Next at 40), while new US open-weight releases trail (Meta Muse Spark Open 39, Reflection Beam 30, NVIDIA Nemotron 3.5 Super VL 26).
- Open weights are not the same as open source: Meta's Muse Spark Open carries its own custom license (Muse Model License), meaning practical usage rights vary by model even when weights are downloadable.
- DeepSeek open-sourced DeepInfer, the inference framework behind its production serving stack, including optimized kernels and distributed-inference features for NVIDIA and Huawei hardware — though key production pieces (KV-cache system, prefill/decode disaggregation, load balancing) remain unreleased.
- Benchmark results from vendors (DeepSeek, MiniMax, Spark-X2.6, Recursive) are repeatedly distinguished from independent verification; several efficiency and cost-reduction claims (e.g., MiniMax's 70% cost cut, Spark-X2.6-4B matching larger 9B models) are self-reported and unreproduced.
- Recursive's Flint model, built using an automated "Eureka Machine" self-improving research loop, shows a mixed benchmark profile (near Qwen3.8-27B on SWE-bench Verified, but behind on Terminal-Bench 2.1 and LiveCodeBench) — framed as promising but not evidence that self-improving AI research is solved.
- Agent reliability and security remain weak points: top models scored as low as 3-8% on Terminal-Bench 4.0 despite stronger showings elsewhere, and separate incidents (an OpenCode credential breach, a malicious-JavaScript investigation tied to a browser-agent project) highlight that credentials, repos, and integrations are part of an agent's security surface, not just model capability.

## Quote

> Chinese labs are shipping capable open-weight models and pushing down the cost of agent work; US teams have credible releases... but have not established a lead across the board.
