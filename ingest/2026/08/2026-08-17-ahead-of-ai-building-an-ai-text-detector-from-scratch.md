---
title: Building an AI Text Detector From Scratch
source: Ahead of AI
source_id: ahead-of-ai
source_url: https://magazine.sebastianraschka.com/p/ai-detector-from-scratch
author: Sebastian Raschka, PhD
date_published: '2026-08-15'
date_captured: '2026-08-17'
ingest_method: feed
model: claude-sonnet-5
---

# Building an AI Text Detector From Scratch

## Insights

- Motivated by Substack's newly launched built-in AI detector feature, which the author identifies as likely built on a Pangram-style model.
- Project builds an AI text detector from scratch (fine-tuning a DistilBERT classifier) both to explain how such detectors work and as a case study in building a scorer/verifier for LLM applications.
- The same detector doubles as a verifier to train a small language model to generate text that evades AI detection — framed as an educational exploration of detector limitations.
- Raises a practical risk: using grammar/polish tools (including general-purpose LLMs) on human-written text can inadvertently make it read as "AI-generated" and get flagged as spam, even though the author wrote it themselves.
- Frames AI detection as an inherent cat-and-mouse dynamic — detectors learn to flag patterns, new models learn to avoid them, and detectors must continually update, with false positives (human text flagged as AI) an ongoing risk.
- Notes detection approaches broadly fall into categories: supervised classifiers, perturbation-based probability tests, perplexity measures, and watermarking; the project's detector outputs a 0-100 score representing classifier-estimated probability, not a definitive judgment.

## Quote

> AI checkers are essentially a cat-and-mouse game.
