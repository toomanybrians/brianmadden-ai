---
title: Managed Agents Are Changing How We Build AI Agents
source: Emerging AI
source_id: emerging-ai
source_url: https://emergingai.substack.com/p/managed-agents-are-changing-how-we
author: Opinion AI
date_published: '2026-08-12'
date_captured: '2026-08-12'
ingest_method: feed
model: claude-sonnet-5
---

# Managed Agents Are Changing How We Build AI Agents

## Insights

- Anthropic's Managed Agents feature (public beta ~4 months old) added four capabilities at once: hard spending limits, advisor models, inference-location controls, and automatic loading of Skills from GitHub repos.
- The framing is that the "machine around the model" — not the model itself — is becoming the product: persistent execution environments, scheduling, memory across jobs, and multi-agent delegation are now handled by the runtime rather than custom-built by developers.
- Anthropic's architecture breaks agents into four core objects: Agent (model, instructions, tools, MCP servers, Skills), Environment (the computer it runs in), Session (a single job run), and Events (the interface for applications to monitor/communicate with the agent).
- A key emerging split: the managed/runtime layer should own infrastructure concerns (sandboxing, execution, orchestration, session persistence), while the developer's own layer should still own judgment calls — what counts as good work, what needs verification, what data is private, and when a task is actually done.
- Basic agent loops (model → choose tool → run tool → inspect result → repeat) are simple, but scaling them to long-running, interruption-tolerant, multi-agent, scheduled workers previously required significant custom infrastructure that Managed Agents now abstracts away.

## Quote

> The model is still important. The machine around the model is becoming a product.
