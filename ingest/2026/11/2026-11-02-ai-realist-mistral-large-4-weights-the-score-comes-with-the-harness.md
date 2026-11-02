---
title: 'Mistral Large 4 Weights: The Score Comes With the Harness'
source: The AI Realist
source_id: ai-realist
source_url: https://www.airealist.ai/p/mistral-large-4-weights-score-comes-with-harness
author: Julien Simon
date_published: '2026-11-01'
date_captured: '2026-11-02'
ingest_method: feed
model: claude-sonnet-5
---

# Mistral Large 4 Weights: The Score Comes With the Harness

## Insights

- Mistral's headline claim that Large 4 improved 13 points to 41% on Terminal-Bench 4.0 refers to a score measured inside Mistral's own coding agent (Vibe), not a generic harness; independent boards (Artificial Analysis, Vals AI) show no gain over the preview when the model is run in a minimal, model-agnostic agent, where it scores 25-26%.
- The author defines an "agent premium" (own-agent score minus generic-harness score) and finds Large 4's premium is +16 points, far outside the range of twelve comparable models (-4 to +7, median 0), suggesting the harness itself — not the weights — is driving most of the improvement.
- Mistral's open-weight license is a modified MIT with a "Model as a Service" condition requiring a separate commercial license for anyone giving third parties inference or post-training access with meaningful control over inputs/parameters — and unlike competitor licenses (Kimi K3, GLM-5.3), it has no revenue floor, making it the most restrictive of the four compared.
- Architecturally, Large 4's config diverges from Large 3 (which matched DeepSeek-V3's settings exactly) — different width, depth, expert count, and vocabulary — while still retaining DeepSeek-derived design elements like latent attention and a sparse-attention indexer, despite the model card saying "trained from scratch" with no DeepSeek mention.
- The piece argues that published benchmark comparisons across open-weight coding models (Mistral, GLM-5.3) are inconsistent because each lab reports scores using a different agent harness, making cross-model and cross-version comparisons unreliable without knowing which agent produced the number.
- No independent run of the released Large 4 weights outside Mistral's own Vibe harness exists yet, so whether the capability gain is in the weights, the harness, or training optimized for the harness remains unresolved.

## Quote

> When a lab hands you a benchmark, ask which agent was driving.
