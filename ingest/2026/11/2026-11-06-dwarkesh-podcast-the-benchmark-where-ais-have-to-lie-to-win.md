---
title: The benchmark where AIs have to lie to win
source: Dwarkesh Podcast
source_id: dwarkesh-podcast
source_url: https://www.dwarkesh.com/p/clocktower
author: Dwarkesh Patel
date_published: '2026-11-05'
date_captured: '2026-11-06'
ingest_method: feed
model: claude-sonnet-5
---

# The benchmark where AIs have to lie to win

## Insights

- A custom benchmark built on the social-deception game Blood on the Clocktower measures capabilities no standard benchmark captures: sustained multi-agent deception, coalition-building, bluffing under questioning, and detecting lies from incomplete/adversarial information.
- Models improved sharply within 2026: GPT-6 Astra (Sept) beats the Feb flagship Claude Opus 4.6 in ~92% of matchups, a ~430 Elo gap in a matter of months — evidence of fast gains in long-horizon coherence and multi-agent strategic reasoning.
- OpenAI's recent models pulled far ahead of Anthropic's specifically on the "good" (truth-seeking) side, because they treat individual pieces of evidence skeptically and reason holistically across the game's history, while Anthropic's models tend to accept reported information at face value and get fooled by staged "proof."
- Game transcripts show models executing genuinely sophisticated deception: coordinated bluffing, engineered self-sacrifice, fabricated roles, and real-time adaptive lying consistent across multiple players — capabilities the author found more striking than the raw leaderboard numbers.
- Intelligence gains don't clearly favor either the deceptive or truth-seeking side — evil's win rate drifts only slightly down as both sides get smarter, suggesting the benchmark resists saturation since the bar is set by competing frontier models rather than a fixed ceiling.
- Building the benchmark itself became a case study in AI-driven engineering: Claude largely designed, tested, and iteratively rebalanced the game environment autonomously (over 20 revision cycles, often unsupervised), which the author argues is a proxy for AI's growing ability to construct and refine its own RL training environments.
- Mixed-model teams (half Opus, half GPT) performed no better (if anything slightly worse) than single-model teams, suggesting model diversity didn't yield a coordination advantage; models also never attempted to identify teammates by writing style.

## Quote

> I’m just stunned that the models are this good at doing it themselves.
