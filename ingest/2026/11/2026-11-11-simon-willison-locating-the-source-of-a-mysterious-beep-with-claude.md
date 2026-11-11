---
title: Locating the source of a mysterious beep with Claude
source: Simon Willison's Newsletter
source_id: simon-willison
source_url: https://simonw.substack.com/p/locating-the-source-of-a-mysterious
author: Simon Willison
date_published: '2026-11-10'
date_captured: '2026-11-11'
ingest_method: feed
model: claude-sonnet-5
---

# Locating the source of a mysterious beep with Claude

## Insights

- Willison used Claude Code (and later Claude Fable 5.2) to build a full working system — "Beep Locator" — that coordinates multiple networked devices (phones, laptops, iPads) via WebSockets and WebAudio to triangulate a sound source in physical space, demonstrating agentic coding applied to a real-world, non-software problem.
- The agent independently researched and applied a 2007 academic acoustic-ranging paper (BeepBeep) to inform the system's design, suggesting coding agents can surface and operationalize relevant prior research without being pointed to it directly.
- A "hot-swap" code deployment mechanism let Willison modify running software live and remotely without needing physical/manual interaction with each device — treating the agent as a semi-autonomous collaborator that could keep iterating while he stepped away.
- Willison frames this as giving an AI coding agent "ears": since models lack native audio input, hooking a code-writing agent up to microphone-capturing devices let it perceive and reason about an acoustic environment indirectly — he draws a parallel to another engineer using a webcam feed to let an agent "see" hardware test results.
- Separately, he describes a workflow adjustment for AI-generated pull request descriptions: because agent-written PR text is thorough but reads as "slop," he now hides the full AI-authored detail behind a collapsible `<details><summary>` block and writes a short human-curated summary himself, preserving human editorial judgment on top of AI verbosity.
- Notes that AI agents (tested on Claude Fable 5.2) respond measurably differently to ownership framing in prompts — telling a model the codebase is "its own" roughly quintupled the rate at which it meaningfully refactored/merged code rather than just bolting on new structure.

## Quote

> In Anthropic's testing... the model merged repeated code in about half of the tries with this sentence, and in under a tenth of the tries without it.
