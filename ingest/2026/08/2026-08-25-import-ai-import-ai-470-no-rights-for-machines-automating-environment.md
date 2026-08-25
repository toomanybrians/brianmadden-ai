---
title: 'Import AI 470: No rights for machines; automating environment generation with
  SPADE; and building better GPU kernels with Hawkeye'
source: Import AI
source_id: import-ai
source_url: https://importai.substack.com/p/import-ai-470-no-rights-for-machines
author: Jack Clark
date_published: '2026-08-24'
date_captured: '2026-08-25'
ingest_method: feed
model: claude-sonnet-5
---

# Import AI 470: No rights for machines; automating environment generation with SPADE; and building better GPU kernels with Hawkeye

## Insights

- A METR analysis finds AI's acceleration effect on science is uneven: major acceleration in cybersecurity vulnerability discovery, minor/hard-to-measure acceleration in mathematics, and no measurable acceleration yet in AI research optimization itself — suggesting AI capability gains hit "phase changes" in some domains before others, with coding (2025) and cyber (2026) cited as examples.
- SPADE (multi-university research group) is a self-play framework where an LLM alternates between designing executable training environments and solving them, using the gap in performance with/without "privileged hints" as a reward signal — a way to cheaply generate diverse training data, though the authors note it can't push a model meaningfully beyond the imaginative range of the base model used to generate environments.
- Hawkeye (Harvard/Stanford/Together AI/Caltech) shows that a small, well-curated taxonomy of unit tests (pairing human-authored solution kernels with profiling metrics) lets coding agents write GPU kernels that match or beat expert-tuned vendor libraries and, in some emerging hardware/attention cases, exceed expert-authored kernels by up to 18.9x — evidence that minimal, high-quality human scaffolding can let AI systems surpass specialist human work.
- Researcher Julian Togelius published a personal essay describing "dread" that AI success could make human talent and understanding irrelevant — "abundance... at the price of redundance" — joining Hinton and Bengio in publicly wrestling with AI's implications for human meaning.
- A published essay by Taylor Belrose argues against granting AI systems rights, contending AI cannot be conscious because it lacks properties of biological cognition (asynchronous neuron firing, chemical signaling, mixed memory/computation, sensitivity to physical state) and warns that treating AI as persons risks a "slippery slope" toward human replacement.
- DeepMind and academic collaborators improved the matrix multiplication exponent bound by combining a new gradient-descent optimization approach with AlphaEvolve, which iteratively evolved the optimization code itself — framed as a proof point that AI can now meaningfully assist on frontier theoretical science problems, not just applied engineering.

## Quote

> "I sometimes wake up at 3 am, heart pounding, from the dread of a future where human talent, knowledge, and even genius does not matter." — Julian Togelius
