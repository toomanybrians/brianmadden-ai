---
title: Where an AI Watermark Can Hide in Plain Text
source: Daniel Miessler
source_id: daniel-miessler
source_url: https://danielmiessler.com/blog/where-watermarks-hide-in-text?utm_source=rss&utm_medium=feed&utm_campaign=website
author: daniel@danielmiessler.com (Daniel Miessler)
date_published: '2026-08-11'
date_captured: '2026-08-12'
ingest_method: feed
model: claude-sonnet-5
---

# Where an AI Watermark Can Hide in Plain Text

## Insights

- Anthropic announced (Aug 2026) that Claude watermarks all output — signed C2PA metadata for files/images, and an undisclosed "imperceptible" watermark for plain text that survives copy-paste — but published no algorithm or detector.
- Text watermarks can't live in raw ASCII bytes (no spare encoding room); they most plausibly work by biasing word-choice probabilities via a secret key, a technique with public analogues (Kirchenbauer's green-list method, Google's SynthID-Text/tournament sampling).
- Watermarks sort into four layers by depth — encoding, formatting, word choice, meaning — and deeper layers are harder to strip; shallow encoding/formatting tricks are trivially destroyed by converting to plain ASCII.
- Word-choice watermarks survive copying but degrade as text is edited or paraphrased; a thorough human rewrite removes enough signal to defeat detection, while an AI-generated rewrite just swaps in a different model's watermark.
- Full removal requires two passes: a canonicalization step (strip to clean ASCII) to kill surface-layer marks, plus genuine rewriting to kill word-choice-level signal.
- Anthropic itself cautions that a detected mark only proves Claude "touched" the text at some stage (e.g., a grammar fix), not that it authored the content — and a clean result proves nothing, since short/edited/older-model text also reads clean.

## Quote

> Complete sanitized regeneration of the text using a separate method that produces the canonicalized ASCII-only pure text format with validation.
