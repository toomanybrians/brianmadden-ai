---
title: 'Import AI 469: Science AI; RSI simulator; and Zuck''s technological pessimism'
source: Import AI
source_id: import-ai
source_url: https://importai.substack.com/p/import-ai-469-science-ai-rsi-simulator
author: Jack Clark
date_published: '2026-08-17'
date_captured: '2026-08-17'
ingest_method: feed
model: claude-sonnet-5
---

# Import AI 469: Science AI; RSI simulator; and Zuck's technological pessimism

## Insights

- DiG-bench (from Oxford, Princeton, MIT, Schmidhuber and others) is a new 70-game text-based benchmark measuring whether AI systems can infer hidden rules and objectives through exploration rather than being told them — framed as a proxy for creativity and discovery ability.
- Current frontier models (Opus 5, Fable 5, GPT-5.5) struggle badly on the hardest tiers of DiG-bench (only ~20% success on Tier 7 vs. 100% for humans); the author predicts human parity by mid-2027, which he ties to a potential kickoff point for recursive self-improvement.
- Paradigm Research released an "RSI Simulator" browser game modeling the tradeoffs of running an AI lab pursuing recursive self-improvement (compute vs. researchers, data licensing, etc.), intended to build public intuition about frontier AI development dynamics.
- Startup Inherent built "Faraday," a small 27B supervisory model (post-trained on Qwen-3.6, using OpenAI Codex as a tool) that directs larger frontier models to do science — outperforming standalone Opus 4.8 and GPT-5.5 on 73% of in-distribution and 60% of held-out AI-for-science replication tasks.
- Faraday's training approach: a "Replica" dataset of 100 papers with results stripped out, used to generate 310 replication tasks graded by rubric, with a Codex-based judge providing rewards to train the supervisory model via modified GRPO.
- Mark Zuckerberg's Meta essay "The Future is for Everyone" argues for proliferating superintelligence to prevent power concentration, but the author argues it never addresses whether a superhuman-invention-capable system would actually stay subordinate to individual human empowerment as Zuckerberg assumes.

## Quote

> The skills that allow Faraday to fill in vaguely-specified details may be the very same skills that would allow it to advance the state of the art.
