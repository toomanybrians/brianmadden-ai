---
title: 'The Super-Agent Blueprint: Building an Always-On, Production-Grade AI Agent
  🤖'
source: Linas's Newsletter
source_id: linas-newsletter
source_url: https://linas.substack.com/p/deepseek-super-agent-blueprint
author: Linas Beliūnas
date_published: '2026-11-03'
date_captured: '2026-11-03'
ingest_method: feed
model: claude-sonnet-5
---

# The Super-Agent Blueprint: Building an Always-On, Production-Grade AI Agent 🤖

## Insights

- DeepSeek's "Harness" team published a paper ("Exploring Super-agent Design") describing an internal agent architecture that monitors team chat, autonomously spots unreported bugs, and opens pull requests to fix them.
- A "Super-agent" is defined as a single always-on agent with continuous memory across channels, parallel task execution, unprompted event-driven action, and self-recovery from failures — distinct from today's single-session chat agents.
- Human attention is framed as the current bottleneck on agent productivity: a person can realistically track only 3-5 active agent sessions at once.
- In DeepSeek's tests, the Super-agent architecture completed tasks ~40% faster at the median than a standard single-session agent, nearly halved worst-case (slowest 5%) task time, and became more efficient under load (per-decision inference time dropped 75% as traffic rose 40x).
- Delegation to subagents didn't occur reliably through prompting alone — a single-session agent given a neutral prompt never delegated in five runs, and even a strongly pushed prompt failed once — suggesting effective delegation requires architectural changes, not just better prompts.
- The architecture is described as model-agnostic, applicable across DeepSeek, Claude, ChatGPT, Grok, or open-source models, since it concerns the system layer wrapped around the model rather than the model itself.

## Quote

> So agent productivity is now basically capped by human attention.
