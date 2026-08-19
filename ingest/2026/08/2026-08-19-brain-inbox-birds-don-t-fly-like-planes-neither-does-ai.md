---
title: Birds Don't Fly Like Planes. Neither Does AI.
source: brain@ inbox (curated newsletters)
source_id: brain-inbox
source_url: ''
author: Tomasz Tunguz <blog@tomtunguz.com>
date_published: '2026-08-18'
date_captured: '2026-08-19'
ingest_method: email
model: claude-sonnet-5
---

# Birds Don't Fly Like Planes. Neither Does AI.

## Insights

- A small local model (Qwen3.8-27B, dense) ranked #1 of 135 models on Artificial Analysis's Intelligence Index (score 52), edging out GLM-5.2, a 753B-parameter frontier open-source model — despite being roughly 1/28th the size.
- The author's theory: larger models store more memorized knowledge and can jump straight to answers; smaller models compensate for sparser knowledge by reasoning more extensively token-by-token to reach comparable quality.
- In a head-to-head benchmark (25 real VC workflow tasks: research, summarization, transcription), a cloud model (DeepSeek V4 Flash) and two local models (Qwen3.8-27B, Qwen3.6-35B-A3B) produced equal-quality outputs, judged blind on a 9-point scale, but took very different computational paths.
- The cloud model answered fast with little deliberation (159 avg tokens, 1.1s); the dense local model used more "thinking" tokens (369, 7.2s); a sparse mixture-of-experts local model deliberated even more heavily (1,143 tokens, 10.0s) despite high raw token throughput.
- Model efficiency claims can diverge sharply depending on the metric: the top-ranked model by intelligence score ranked only #23 of 135 on token-efficiency (verbosity), suggesting intelligence and efficiency rankings move independently.
- Practical implication for local/on-device deployment: local models can match cloud-model output quality on real work tasks, but they achieve it via longer, more token-heavy internal reasoning rather than by "knowing more" directly.

## Quote

> Local models can achieve the same result as cloud models, but they'll take a different flight path to get there.
