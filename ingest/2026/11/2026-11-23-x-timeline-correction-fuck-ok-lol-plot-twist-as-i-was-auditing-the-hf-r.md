---
title: 'CORRECTION: fuck ok lol *plot twist* — as I was auditing the HF repo after
  uploa'
source: X (brianmaddenai home timeline)
source_id: x-timeline
source_url: https://x.com/elder_plinius/status/2124637991436173436
author: '@elder_plinius'
date_published: '2026-11-22'
date_captured: '2026-11-23'
ingest_method: x
model: claude-sonnet-5
---

# CORRECTION: fuck ok lol *plot twist* — as I was auditing the HF repo after uploa

## Insights

- Original claim: changing roughly 10 words in a model's vocabulary/dictionary ("Vocab Surgery") could "abliterate" refusal behavior in a model called Inkling-2-Mini, dropping refusal rates to near-zero across 800+ tested prompts.
- The author later retracted/corrected this finding after auditing the Hugging Face repo post-upload.
- The real cause, per the correction, was a short prefill accidentally baked into the chat template from an earlier experiment — not the vocabulary edit itself.
- When variables were isolated, the prefill (not "Vocab Surgery") appeared to account for most of the effect on refusal rates.
- This is a live example of a safety/alignment technique (refusal suppression via small vocab or template changes) being tested, claimed, and then partially debunked through self-audit.

## Quote

> WOAH! turns out you can effectively "abliterate" models ... simply by changing 10 words in the dictionary 🤯
