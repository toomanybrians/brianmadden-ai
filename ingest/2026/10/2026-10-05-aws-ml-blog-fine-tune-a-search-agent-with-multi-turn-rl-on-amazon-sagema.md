---
title: Fine-tune a search agent with multi-turn RL on Amazon SageMaker AI
source: AWS Machine Learning Blog
source_id: aws-ml-blog
source_url: https://aws.amazon.com/blogs/machine-learning/fine-tune-a-search-agent-with-multi-turn-rl-on-amazon-sagemaker-ai/
author: Huibin Shen
date_published: '2026-10-02'
date_captured: '2026-10-05'
ingest_method: feed
model: claude-sonnet-5
---

# Fine-tune a search agent with multi-turn RL on Amazon SageMaker AI

## Insights

- AWS positions multi-turn reinforcement learning (MTRL) as a third path between costly supervised fine-tuning (needs expert demonstration data) and single-turn RL (RLVR), which can't capture interdependent decisions across a multi-step agent trajectory.
- The pitch is explicitly economic: fine-tuning a small model via MTRL aims to match a frontier model's reliability on a narrow task while keeping the speed/cost profile of a small model — a direct alternative to just prompting GPT-class models for agentic tool use.
- SageMaker AI MTRL is framed as a managed, serverless, low-configuration RL service (per-token pricing, no GPU cluster management, resumable multi-day jobs, built-in algorithm library) — lowering the expertise bar needed to do production agentic RL.
- Case study: fine-tuning Qwen3.6-27B as an enterprise search agent (BM25 + vector search tools) using nDCG@10 as a direct trajectory-level reward, with a -1 penalty for hitting turn/token limits to explicitly discourage runaway or failed searches.
- Reported results: nDCG@10 improved on 3 of 4 held-out benchmarks (BrowseComp-Plus +23.7%, WixQA +18.4%, Wands +6%), with a slight regression on FreshStack; the more notable change was reliability — BrowseComp-Plus failure rate dropped from 22.89% to 0.68%.
- Only three hyperparameters were tuned from defaults (epochs, batch size, rollout concurrency), per AWS's framing — a claim of low setup friction that should be read as a vendor convenience narrative rather than a neutral technical benchmark.

## Quote

> That's the whole setup. The choices that usually demand RL expertise... all run on defaults.
