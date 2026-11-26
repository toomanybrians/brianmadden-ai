---
title: Evaluating Recent Model Releases on GDPx
source: SemiAnalysis
source_id: semianalysis
source_url: https://newsletter.semianalysis.com/p/evaluating-recent-model-releases
author: Max Kan
date_published: '2026-11-26'
date_captured: '2026-11-26'
ingest_method: feed
model: claude-sonnet-5
---

# Evaluating Recent Model Releases on GDPx

## Insights

- SemiAnalysis's GDPx benchmark deliberately narrows to 11 domains judged most economically consequential for frontier AI (chip design, cybersecurity, biology, finance, legal, quant trading, RSI, hardware design, materials science, alignment, software engineering), explicitly rejecting GDP-weighted or O*NET-based task selection used by benchmarks like GDPVal — arguing AI's economic impact is highly concentrated, not evenly spread.
- The benchmark is intentionally very hard: top model (Opus 5.5 at launch) scored only 12%, leaving large headroom versus saturated benchmarks like Terminal Bench, which the authors argue is necessary to actually discriminate between successive model releases.
- Safety classifiers materially distort scores in cyber/bio/alignment domains — "sandbagging" some models' totals — which creates two defensible leaderboards (with/without those domains), raising a live measurement question about whether refusals should count against model "intelligence."
- GPT-6.2 Astra tops the main leaderboard (19.3%) and excels at reasoning-heavy domains (chip/hardware design, materials science, RSI, finance, alignment) yet is weak at software engineering and widely perceived as unpleasant to use — suggesting a gap between raw capability and public/developer sentiment, which the authors attribute to aggressive RL with weak SFT data.
- Gemini 4 Neon's strongly positive public reception is attributed mainly to likeable conversational style and more lenient safety filters (hence its bio lead), not superior underlying capability — GDPx shows it still trailing OpenAI and Anthropic broadly; Google's inference stack (prompt caching) also lags competitors, inflating run costs.
- Fable 5.2 dominates software engineering and ties on finance but is the most expensive model to run per task (more output tokens, more subagent spawning), illustrating a cost/capability tradeoff where higher scores don't always mean better cost-efficiency; domain-specific post-trained/abliterated cyber models mostly underperformed vanilla open-source models in this early test.

## Quote

> We believe Twitter vibes are more a reflection of how pleasant models are to work with, rather than raw model IQ.
