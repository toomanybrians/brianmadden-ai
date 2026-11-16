---
title: Route coding agent requests to the right model on Amazon Bedrock with NVIDIA
  NeMo Switchyard
source: AWS Machine Learning Blog
source_id: aws-ml-blog
source_url: https://aws.amazon.com/blogs/machine-learning/route-coding-agent-requests-to-the-right-model-on-amazon-bedrock-with-nvidia-nemo-switchyard/
author: Aswath Ram A Srinivasan
date_published: '2026-11-13'
date_captured: '2026-11-16'
ingest_method: feed
model: claude-sonnet-5
---

# Route coding agent requests to the right model on Amazon Bedrock with NVIDIA NeMo Switchyard

## Insights

- The core economic argument: for agentic coding tasks, price-per-token is a misleading metric because total task cost depends on number of model turns, how much conversation history is replayed each turn, and retry/failure rates — so the proposed metric is "cost per solved task" (total run cost ÷ runs that passed tests).
- NVIDIA NeMo Switchyard is an open-source routing library (integrated via LiteLLM) that lets a gateway dynamically pick between models per-request for agent traffic; it ships two usable strategies in this integration — "Stage" (reads recent tool-call/result history to choose between a "capable" and "efficient" model) and "Random" (weighted traffic splitting for A/B tests). More advanced classifier-based strategies (Task/Composite routing) aren't supported in this integration because they'd require extra model calls.
- The reference architecture routes requests through LiteLLM on ECS/Fargate to Amazon Bedrock (Claude Opus 5.5 and NVIDIA Nemotron 3 Super 120B tested as capable/efficient pair), with the routing logic making the default choice send new/ambiguous requests to the cheaper model and escalate only on detected failure signals in tool-call history.
- AWS and NVIDIA explicitly flag this as non-production, experimental sample code (switchyard-server 0.3.0 documented by NVIDIA as a "demo and evaluation component," APIs subject to change) — a caveat that undercuts any claim this is a mature, battle-tested routing solution.
- The post includes a benchmarking methodology (bench/run.py, bench/multiturn.py) for measuring cost-per-solved-task and cost-per-conversation across routed vs. single-model baselines, with explicit warnings that small sample sizes, turn limits, output truncation, and prompt caching can all distort the measured numbers — treat results as estimates, not bills.
- A structural caution: escalating a task mid-conversation (from efficient to capable model) replays the entire failed attempt's history, which can make recovery via escalation more expensive than simply starting the hard task on the capable model directly.

## Quote

> You pay for every attempt, including attempts on tasks that never finish.
