---
title: 'From Ancient Claude to Modern Claude: Model Migration Guide'
source: Opinion AI
source_id: opinion-ai-2
source_url: https://opinionai.substack.com/p/from-ancient-claude-to-modern-claude
author: Opinion AI
date_published: '2026-09-28'
date_captured: '2026-09-29'
ingest_method: feed
model: claude-sonnet-5
---

# From Ancient Claude to Modern Claude: Model Migration Guide

## Insights

- Anthropic released Opus 5.5 (costing ~40% less than Opus 5 for typical token-billed work) and Sonnet 5.5 (running 30%+ faster than Sonnet 5, up to 30% cheaper per task), released six days apart.
- On the Terminal-Bench 4.0 agentic coding benchmark, Sonnet 5.5 scored 70.6% versus Opus 5.5's 66.4%, an unusual case of the smaller/cheaper model outperforming the larger one on this test.
- The core friction in adopting new models isn't capability — it's the sunk cost of having customized an old model's behavior (writing style, project context, instruction preferences) and dreading redoing that work.
- Key reframe: personalization mostly lives outside the model weights themselves — in Memory, Projects (files/instructions/chats), Skills, CLAUDE.md/Claude Code memory, and API system prompts/tool descriptions — meaning migration doesn't require starting over.
- Proposed migration approach: have the old model help prepare the new one by identifying what the existing setup depends on, before making any changes.
- Framed as an increasingly necessary skill given the pace of model releases ("every time Anthropic adds .5 to the name"), implying settling-in periods of weeks/months are no longer sustainable.

## Quote

> Learn how to leave a model.
