---
title: 'The Iron(wood) Throne: Google''s TPU Stakes Its Claim on Inference'
source: SemiAnalysis
source_id: semianalysis
source_url: https://newsletter.semianalysis.com/p/tpu-strikes-the-king
author: Bryan Shan
date_published: '2026-11-05'
date_captured: '2026-11-06'
ingest_method: feed
model: claude-sonnet-5
---

# The Iron(wood) Throne: Google's TPU Stakes Its Claim on Inference

## Insights

- Google's TPUv7 (Ironwood) is now winning or competitive on realistic agentic inference benchmarks (AgentX/InferenceX) against NVIDIA's GB300/B300 and AMD's MI355X, with gains of 1.2x–2.7x tokens-per-dollar on some models, though NVIDIA's FP4 chips still lead in other cases — the competitive picture is workload- and precision-dependent, not a clean win for either side.
- A new benchmark category (AgentX) has emerged specifically to measure "agentic" inference workloads — multi-turn sessions, long context, high prefix reuse, and bursty sub-agent spawning — as distinct from simple chatbot-style benchmarking, reflecting industry recognition that agentic usage patterns are now the dominant real-world inference cost driver.
- Google is pursuing an explicit ecosystem strategy to challenge NVIDIA's software moat: partnering directly with open-source maintainers (PyTorch, vLLM, SGLang, llm-d, Ray) and giving them early/Day-0 chip access, mirroring the playbook NVIDIA historically used to build CUDA lock-in.
- The piece alleges NVIDIA's internal bureaucracy (e.g., legal review blocking driver feature additions for months) is now a competitive liability, with AMD and Google moving faster on community contributions and feature merges — framed as a meaningful risk to NVIDIA's ecosystem dominance.
- Frontier AI labs with large TPU allocations (Anthropic, Google DeepMind, soon OpenAI) are reportedly co-designing model architectures (e.g., attention head dimensions) specifically to run efficiently on TPU hardware, suggesting model design and hardware procurement are becoming intertwined decisions at the lab level.
- Major customers already buying/using TPUs for inference include Oracle, OpenAI, Anthropic, and Meta, with Meta specifically deploying TPUv7 in production via SGLang-TorchTPU for its Muse Spark Open model.

## Quote

> There needs to be an cultural shift in massively reducing bureaucracy at NVIDIA.
