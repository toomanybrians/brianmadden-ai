---
title: How Claude Watermarks AI-Generated Text
source: Ahead of AI
source_id: ahead-of-ai
source_url: https://magazine.sebastianraschka.com/p/claude-watermarking
author: Sebastian Raschka, PhD
date_published: '2026-08-22'
date_captured: '2026-08-24'
ingest_method: feed
model: claude-sonnet-5
---

# How Claude Watermarks AI-Generated Text

## Insights

- Anthropic's Claude watermarking is applied at the token-sampling stage, not inside the model itself — meaning no retraining is needed; a secret key plus recent context tokens deterministically bias which token gets selected at certain "coin-flip" positions where multiple next-words are near-equally plausible.
- Because watermarking only manipulates sampling, Anthropic claims (and the mechanism supports) that it shouldn't degrade text quality — it acts like fixing a random seed rather than altering the model's outputs.
- Detection can't be done by end users: it requires the same secret key and a set of "watermarking functions" plus a threshold score, and Anthropic has not yet made a detection API broadly available.
- The scoring/detection method draws on Google's SynthID-Text (tournament sampling: candidate tokens are scored via random bit-generating functions and matched in knockout rounds), designed specifically so text can be scored later without needing to rerun the original LLM.
- Watermarks are only embedded at positions with genuinely interchangeable token choices — removal requires editing multiple positions, but since outsiders can't identify which words carry the watermark, removal effectively requires random or blind edits.
- Predicted consequence: parties wanting unwatermarked AI text will likely add a secondary local-model editing pass on top of watermarked output, which may make the final text worse due to arbitrary, awkward edits — a plausible driver being EU regulation requiring AI-content labeling.

## Quote

> "The watermarking is not as complicated as it might seem." — Sebastian Raschka
