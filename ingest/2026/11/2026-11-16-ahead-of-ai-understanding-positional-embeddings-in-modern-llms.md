---
title: Understanding Positional Embeddings in Modern LLMs
source: Ahead of AI
source_id: ahead-of-ai
source_url: https://magazine.sebastianraschka.com/p/understanding-positional-embeddings
author: Sebastian Raschka, PhD
date_published: '2026-11-15'
date_captured: '2026-11-16'
ingest_method: feed
model: claude-sonnet-5
---

# Understanding Positional Embeddings in Modern LLMs

## Insights

- Positional encoding in LLMs has moved through three main approaches: learned absolute position vectors (GPT-2), fixed sinusoidal absolute encodings (original Transformer), and RoPE (relative, rotation-based), with RoPE now the de facto standard since the original LLaMA model.
- RoPE encodes position by rotating query/key vector pairs inside attention rather than adding a position vector to embeddings; because only the relative angle between rotated query/key pairs affects the dot product, attention scores stay stable even when a long prefix (e.g., a system prompt) shifts all absolute positions equally.
- Learned absolute embeddings (GPT-2-style) don't generalize past their trained context length and become disproportionately expensive to scale (e.g., ~22% of total weights at 100k context vs 0.3% at 1,024).
- 2026-era architectures are diverging from "full RoPE everywhere": partial RoPE (rotating only a subset of head features, e.g., MiniMax-M3 rotates half) saves memory on positional tables, but cited research found no consistent benefit over full RoPE, leading the author to call partial RoPE "hardly worth it."
- Some newer models (e.g., SmolLM3) deliberately skip RoPE in a subset of transformer layers (NoPE layers), relying on causal masking alone to implicitly carry positional signal in those layers — reportedly improving long-context performance.
- An alternative to RoPE, learned relative position bias (used by "Thinky's Inkling," echoing T5's 2019 approach), adds a learned, hidden-state-dependent bias term to attention scores based on the distance between query and key tokens, rather than rotating vectors.

## Quote

> So, in my opinion, partial RoPE is hardly worth it.
— Sebastian Raschka
