---
title: How Airbnb uses cost per task to operate coding agents on Amazon Bedrock
source: AWS Machine Learning Blog
source_id: aws-ml-blog
source_url: https://aws.amazon.com/blogs/machine-learning/how-airbnb-uses-cost-per-task-to-operate-coding-agents-on-amazon-bedrock/
author: Alan Yao
date_published: '2026-11-18'
date_captured: '2026-11-19'
ingest_method: feed
model: claude-sonnet-5
---

# How Airbnb uses cost per task to operate coding agents on Amazon Bedrock

## Insights

- Airbnb evaluates every new coding model on its own task suites before rollout, scoring both quality and "cost per task" (total list-price token cost to complete one task) rather than trusting vendor benchmarks, which don't reflect real engineering work.
- Reasoning-effort settings create steep cost/quality tradeoffs: raising effort from low to high on one model gained 0.8 points of eval score but cost 2.5x as much — Airbnb uses eval results to cap allowed effort levels per model.
- Eval scores didn't predict production cost: a model that scored 3+ points higher and had similar eval cost-per-task ended up costing several times more per user in production, because its ability to sustain long autonomous sessions led engineers to use it differently (more requests, more re-read cached context), not because output tokens were expensive.
- Swapping that expensive model for a newer, higher-scoring, ~6x-cheaper-per-task alternative cut the heavy-user group's weekly spend to about a seventh with roughly the same request volume — illustrating that model churn/capacity planning requires watching production telemetry (token mix, cache reads/writes, requests-per-user) alongside eval numbers.
- Airbnb maintains "equivalent" backup models across model families (validated via the same evals) so it can rebalance traffic when quota/capacity gets tight, treating multi-model redundancy as an operational necessity, not just a cost play.
- Practical operational details flagged: Bedrock's token-per-minute quota math (burndown multipliers, cache-read exemption from quota) can make a dashboard look like there's quota headroom while requests are actually being throttled; lowering max_tokens can meaningfully increase admittable request volume without changing final cost.

## Quote

> The eval measured the model on a task. Production measured how people chose to work with it.
