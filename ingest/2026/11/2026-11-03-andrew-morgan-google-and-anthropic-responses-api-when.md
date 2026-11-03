---
title: Google and Anthropic, Responses API when?
source: Andrew Morgan
source_id: andrew-morgan
source_url: https://andrewmorgan.ai/p/the-state-of-llm-apis-can-we-agree
author: Andrew Morgan
date_published: '2026-11-03'
date_captured: '2026-11-03'
ingest_method: feed
model: claude-sonnet-5
---

# Google and Anthropic, Responses API when?

## Insights

- There is still no universal wire format for LLM APIs: OpenAI has Responses, Anthropic has Messages, Google has Content/Parts, and Chat Completions remains the only broadly shared format despite being designed for a simpler 2024-era exchange.
- Chat Completions creates "false comfort" — it looks portable because endpoints and SDKs connect, but breaks down once an application needs structured reasoning, hosted tools, multimodal content, or complex execution semantics that Chat Completions wasn't built for.
- Translating between provider APIs is harder than it looks: reasoning items, tool-call lifecycles, streaming events, citations, and turn boundaries aren't equivalent across contracts, so gateways/routers that promise a single interface face constant risk of silent, hard-to-test failures even when both providers behave correctly.
- Web search is cited as a concrete example of fragmentation already happening at a "table stakes" feature level — OpenAI, Anthropic, and Google each implement it with different configuration, execution, and citation models despite identical user intent.
- Responses-API compatibility is spreading beyond OpenAI (Mistral, DeepSeek, xAI, Moonshot, Z.ai, MiniMax, ByteDance) and self-hosted runtimes (Ollama, vLLM, llama.cpp, partially SGLang) are doing significant interoperability work, but "supporting" an endpoint often doesn't mean full protocol parity (e.g., stateful continuation, WebSocket transport).
- Open Responses joined the Linux Foundation's Agentic AI Foundation (Oct 22) alongside Anthropic's MCP/Agent Skills contributions, giving the industry a vendor-neutral convergence point — but Anthropic hasn't publicly committed to adopting or maintaining it, and Google continues pushing its own proprietary format.

## Quote

> Chat Completions is everywhere, but in 2026 that is increasingly an indictment of the industry's interoperability story rather than an achievement.
