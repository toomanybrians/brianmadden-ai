---
title: What if the inside of an AI turns out to be readable after all? New research
  suggests it might be, and that could make AI mistakes easier to catch.
source: Nate’s Substack
source_id: nate-s-substack
source_url: https://natesnewsletter.substack.com/p/mechanistic-interpretability-explained
author: Nate
date_published: '2026-10-22'
date_captured: '2026-10-23'
ingest_method: feed
model: claude-sonnet-5
---

# What if the inside of an AI turns out to be readable after all? New research suggests it might be, and that could make AI mistakes easier to catch.

## Insights

- Goodfire's research reconsiders a long-standing explanation for "polysemantic" neurons (ones that seem to respond to unrelated concepts) — Nick Cammarata argues the issue is often that our semantic categories obscure a real underlying commonality (e.g., a "cat and car" neuron actually responding to a shared V-shaped visual pattern), not that the neuron is inherently uninterpretable.
- The two headline numbers — 99–100% interpretability on the final layer of a vision model, and roughly 90% of neuron "poles" in Qwen3-32B having one main job — are narrow, preliminary technical measurements, not indicators of overall AI safety.
- A real tested example (neuron 127 in Goodfire's model microscope) shows a neuron with strong positive activation on ladybugs but its most decision-relevant (highest-attribution) activity on toy terrier images — demonstrating that what a neuron responds to and what it actually contributes to the model's output can be entirely different things.
- Researchers distinguish observation (recorded activation), inference (a hypothesis like "ladybug detector"), and testing (ablation — zeroing a component and measuring the actual output change) as three different confidence levels; only ablation/intervention establishes causal explanation.
- Anthropic's sparse-autoencoder approach (extracting millions of discrete features from Claude 3 Sonnet) is presented as a different strategy from Goodfire's — building a second, more interpretable model of the original's activity rather than reinterpreting the original neurons directly.
- Leo Gao's response to Goodfire proposes a stricter bar: use a neuron's explanation to simulate its activity, substitute the simulated values into the model, and measure resulting behavior change — Cammarata disputes over-reliance on a single simulation score in favor of multiple investigative methods.
- Practical upside argued: if individual neurons are more tractable than assumed, researchers gain a direct way to interrogate specific AI errors — testing a suspected cause and checking whether altering it fixes or breaks other behavior — which asking a chatbot to "explain itself" cannot provide.

## Quote

> A neuron's response and the network's use of that response are separate questions.
