---
title: 'Multi-Turn Reinforcement Learning on Amazon SageMaker AI: A hands-on guide'
source: AWS Machine Learning Blog
source_id: aws-ml-blog
source_url: https://aws.amazon.com/blogs/machine-learning/multi-turn-reinforcement-learning-on-amazon-sagemaker-ai-a-hands-on-guide/
author: Daniel Quang
date_published: '2026-10-23'
date_captured: '2026-10-26'
ingest_method: feed
model: claude-sonnet-5
---

# Multi-Turn Reinforcement Learning on Amazon SageMaker AI: A hands-on guide

## Insights

- AWS launched Multi-Turn Reinforcement Learning (MTRL) on SageMaker AI, a managed, serverless RL training service specifically for agentic, multi-step tasks (not single-prompt fine-tuning) — the model is scored only on whether an entire action sequence succeeds, not on imitating a "correct" trajectory.
- The architecture splits responsibilities: SageMaker AI owns training/the policy model, while the agent, environment, and reward function run externally (demoed on Bedrock AgentCore, but also EKS/EC2/Fargate are supported) — meaning the reward/environment logic is fully custom code supplied by the user, not an AWS primitive.
- Using a small open-weight model (GPT-OSS-20B) as the example, AWS reports moving solve rate on a Wordle benchmark from 61% to 84% (at default reasoning effort) for about $339 in training tokens plus ~$79 in agent runtime costs — positioned as evidence that small/cheap models can be made competent at narrow, business-specific multi-step workflows "that public models were never trained on."
- The post stresses reward-design as the hard, failure-prone part of this technique: naive reward summation produced perverse incentives (e.g., a lost game scoring higher than some wins), fixed only by separating a dominant outcome term from a small bounded shaping term — a cautionary note about how fragile and labor-intensive RL reward engineering is in practice.
- Several non-trivial operational failure modes are disclosed: authentication/credential throttling under concurrency, jobs silently failing if a rollout never reaches the model, and models drifting from tool-calls into plain text under too-high a learning rate — signaling this is still an early, rough, engineer-intensive capability, not a turnkey product.
- Notably, evaluation settings matter enormously: the model's own training-reported validation accuracy (37%) dramatically understated its real performance at actual serving settings (84%), highlighting a gap between benchmark/validation metrics and deployed behavior — a broader caution about trusting in-training metrics.

## Quote

> Evaluate at the settings you will serve at. The training curve says this adapter ends at 37 percent. At serving settings it solves 84 percent.
