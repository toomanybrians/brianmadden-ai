---
title: Write your own training loop — without managing GPUs — with Amazon SageMaker
  training session APIs
source: AWS Machine Learning Blog
source_id: aws-ml-blog
source_url: https://aws.amazon.com/blogs/machine-learning/write-your-own-training-loop-without-managing-gpus-with-amazon-sagemaker-training-sessions/
author: Nicolas Jourdan
date_published: '2026-10-22'
date_captured: '2026-10-23'
ingest_method: feed
model: claude-sonnet-5
---

# Write your own training loop — without managing GPUs — with Amazon SageMaker training session APIs

## Insights

- AWS launched "training session APIs" within SageMaker AI, a new abstraction layer that exposes GPU-backed training as live, stateful API calls (forward_backward, optim_step, sample) rather than abstracting away the whole algorithm — users write the training loop in Python locally while AWS manages GPU allocation, distributed execution, fault recovery, and checkpointing.
- This sits as a middle tier in SageMaker's model customization spectrum: more algorithmic control than fully-managed "Serverless Model Customization" (pick-a-model-and-data), but far less operational burden than SageMaker Training Jobs or HyperPod clusters.
- Billing is per-token-processed rather than per-GPU-hour, meaning local computation (reward scoring, data loading, multi-tool agentic rollouts, human-in-the-loop evaluation) runs "off the clock" — a notable economic shift for workloads with heavy non-GPU compute like RL reward functions.
- Targets a specific user segment: post-training/alignment researchers, teams needing custom losses or RL reward functions, and "ML engineers who've outgrown config-driven fine-tuning" — explicitly framed as AWS trying to capture custom/novel-algorithm fine-tuning work that previously required either sacrificing control (managed services) or owning infrastructure (self-managed clusters).
- Demonstrated results are modest-scale but concrete: a GRPO loop on GSM8K math problems took held-out accuracy from 56% to 75% in 10 training steps on 40 problems; a competitive-programming RL recipe (multi-turn, tool-using, sandbox-graded) raised accuracy from 40% to 50.5% over 50 steps.
- The "cookbook" release (ready-made SFT/RL recipes including preference optimization, KTO alignment, multi-turn tool use) signals AWS is trying to lower the barrier to advanced fine-tuning techniques (RL, reward shaping, agentic rollouts) becoming standard enterprise practice rather than research-lab-only work.

## Quote

> Instead of abstracting away the algorithm, they abstract away the compute.
