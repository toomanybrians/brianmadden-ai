---
title: 'Import AI 479: Spacewar; low-latency tasks versus LLMs; Genie 4'
source: Import AI
source_id: import-ai
source_url: https://importai.substack.com/p/import-ai-479-spacewar-low-latency
author: Jack Clark
date_published: '2026-11-02'
date_captured: '2026-11-03'
ingest_method: feed
model: claude-sonnet-5
---

# Import AI 479: Spacewar; low-latency tasks versus LLMs; Genie 4

## Insights

- A new benchmark, Realtime-Bench, tests AI models on 50 time-sensitive interactive tasks (30 web tasks like travel/e-commerce/security, 20 games) where delayed actions directly cause failure — probing temporal awareness, adaptive deliberation, and timed action selection.
- Current frontier models perform poorly under real-world latency constraints: the best model (GPT-6 Astra, high reasoning) only achieved a 36% pass rate on the "wall clock" condition, versus 70-80% when given unlimited time (paused clock) — showing a large gap between raw reasoning capability and real-time execution.
- Metis, a startup, published a position paper proposing to add an explicit, persistent "epistemic state" (claims/hypotheses with evidential status) plus a reasoning policy and value function to AI systems, aiming to make reasoning auditable and reduce hallucination by requiring claims to pass "warrant assessment" before being accepted — explicitly modeled on DeepMind's AlphaGo-style approach applied to open-domain problems.
- Google DeepMind released Genie 4, a world-model system that lets users generate and interactively modify simulated environments in real time (natural language scene edits, physics/human-motion simulation, native audio generation, and an embedded Gemini 3.8 Flash agent that plans and verifies multi-step goals within the simulation).
- A DIA report on space security describes escalating anti-satellite capabilities (co-orbital kill vehicles, directed-energy weapons, satellite-stalking, space-based nuclear EMP concepts) among the US, China, and Russia, framed as relevant to the future given growing interest in space-based data center infrastructure.

## Quote

> "Model-generated content cannot enter the accepted epistemic state merely by being plausible; it must pass warrant assessment, which lowers hallucinations." — Metis
