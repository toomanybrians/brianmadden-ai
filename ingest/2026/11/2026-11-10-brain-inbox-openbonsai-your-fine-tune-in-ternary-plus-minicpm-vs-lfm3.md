---
title: 'OpenBonsai: your fine-tune, in ternary. Plus MiniCPM vs. LFM3.'
source: brain@ inbox (curated newsletters)
source_id: brain-inbox
source_url: https://evalsignal.xyz/campaign/cd37c6bb-dd9f-40f1-974a-5a281110ef58/ff779425-3a22-47e4-965d-bf0e1f18a567
author: EvalSignal <newsletter@evalsignal.xyz>
date_published: '2026-11-09'
date_captured: '2026-11-10'
ingest_method: email
model: claude-sonnet-5
---

# OpenBonsai: your fine-tune, in ternary. Plus MiniCPM vs. LFM3.

## Insights

- OpenBonsai offers an open, Apache-2.0 alternative to Prism ML's proprietary ternary quantization recipe, letting users compress their own BF16 fine-tunes (not just base models) into ~2GB ternary checkpoints compatible with Prism's runtime — a workflow aimed at deploying specialized models on consumer hardware (one RTX 5090, ~5 hours).
- The compression pipeline uses the original model's own reasoning traces (via an "Attend to Your Own Thoughts" technique) to calibrate which activation pathways to preserve, rather than naive weight rounding, in an effort to retain task-specific behavior through extreme compression.
- The released checkpoint is a research preview that still trails both the original BF16 model and Prism's own ternary release on math/coding, and requires a non-standard llama.cpp fork since upstream doesn't support the format — illustrating current practical friction in deploying ultra-compressed models.
- Independent benchmarking of two small multimodal models (MiniCPM-V 4.7 at 1B params vs. LFM3-VL-2B) shows a capability tradeoff: LFM3 scores higher on broad tool-routing/agent tasks, while MiniCPM produces faster, richer screenshot descriptions but initially scored near-zero on a vision benchmark due to a formatting quirk (dropped numbering) rather than actual content failure.
- Rescoring MiniCPM's same outputs with a more tolerant header parser raised its vision pass rate from 0/100 to 37/100, underscoring how benchmark/grader design can dramatically misrepresent a small model's real capability — a methodological caution for evaluating compact AI systems.
- Both evaluated models still have very low "exact action" tool-use accuracy (1-2 correct out of ~89), suggesting that even when small models pick a plausible tool, getting arguments right remains a major unsolved gap for autonomous agent reliability.

## Quote

> Its pipeline also distills scaling factors against the original model's outputs.
