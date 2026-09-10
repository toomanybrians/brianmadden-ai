---
title: GPT-6 Astra, Looped Transformers, and Hidden Reasoning
source: brain@ inbox (curated newsletters)
source_id: brain-inbox
source_url: https://sebastianraschka.substack.com/p/gpt-6-astra-looped-transformers-and
author: '"Sebastian Raschka, PhD from Ahead of AI" <sebastianraschka@substack.com>'
date_published: '2026-09-09'
date_captured: '2026-09-10'
ingest_method: email
model: claude-sonnet-5
---

# GPT-6 Astra, Looped Transformers, and Hidden Reasoning

## Insights

- GPT-6 Astra's standout capability relative to prior models is computer use — operating GUIs directly (mouse/keyboard) via the Codex/ChatGPT app harness, not just CLI/API-based tool use, which the author expects to be a major focus area for both open-source and proprietary harnesses in coming months.
- OpenAI reportedly trained Astra's computer-use skills using tens of thousands of Mac Minis/Studios as an interaction environment (screenshots in, actions out, RL on success/failure) while the model itself trains on ~100,000 GPUs — the Macs simulate the OS, not run the model.
- A practical workflow note: as models get better at inferring context, existing AGENTS.md/SKILL.md instruction files may over-constrain newer models; the author suggests periodically pruning or regenerating such instruction files rather than assuming more hand-holding is always better.
- "Looped transformers" (reusing the same transformer block weights across multiple passes) are likely part of Astra's architecture per reporting, and research shows they can modestly improve model quality per unit of training compute (one study estimates 6.8–18% less compute needed for equivalent performance) versus adding more distinct blocks.
- Shorter reasoning traces in newer models (fewer tokens at matched accuracy) are argued to reflect greater capability/fewer mistakes rather than deliberately obscured chain-of-thought — a pattern already seen across model sizes within a family, not a new architectural risk.
- OpenAI's chief scientist publicly clarified that Astra's computation depth is within 2x of GPT-4 and that any reduced chain-of-thought monitorability is a separate, non-architecture-driven trend the company is actively trying to counteract.

## Quote

> The depth of the computation graph for our present frontier models, including Astra, is within a factor of two of GPT-4.
