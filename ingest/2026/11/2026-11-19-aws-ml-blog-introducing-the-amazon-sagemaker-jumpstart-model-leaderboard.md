---
title: Introducing the Amazon SageMaker JumpStart Model Leaderboard
source: AWS Machine Learning Blog
source_id: aws-ml-blog
source_url: https://aws.amazon.com/blogs/machine-learning/introducing-the-amazon-sagemaker-jumpstart-model-leaderboard/
author: Dan Ferguson
date_published: '2026-11-18'
date_captured: '2026-11-19'
ingest_method: feed
model: claude-sonnet-5
---

# Introducing the Amazon SageMaker JumpStart Model Leaderboard

## Insights

- AWS launched a leaderboard inside SageMaker Studio that ranks 70+ open-weight foundation models (from Meta, Google, Qwen, IBM, Arcee, etc.) on quality, speed, and cost side by side, addressing the problem of comparing benchmark numbers published under inconsistent conditions across vendors.
- Quality scores use three fixed benchmarks (BIG-Bench Hard, GPQA Diamond, MMLU-Pro) run by AWS itself with identical methodology for every model, explicitly kept separate rather than blended into a composite score.
- Performance/cost metrics (time to first token, throughput, hourly instance cost) are measured by AWS sending a standardized workload to actual SageMaker endpoints, and change depending on selected "use case profile" and "optimization goal" (Balanced, Cost optimized, Latency optimized, Throughput optimized) — meaning the same model can show very different numbers depending on deployment configuration.
- Cost figures only reflect on-demand SageMaker instance pricing — excluding data transfer, storage, inference-component costs, or discount plans — so AWS flags that real bills will differ.
- AWS's own guidance frames the leaderboard as a shortlisting tool, not a decision-maker: it explicitly warns that close scores should be treated as ties, reasoning vs. non-reasoning models use different evaluation parameters (making cross-type comparison "approximate"), and users should still validate top candidates on their own data before production deployment.
- Coverage is partial at launch (LLMs only, not all JumpStart models benchmarked yet), with stated future plans for private-hub leaderboards and expansion into other task types like object detection, embeddings, and image understanding.

## Quote

> A model without a score is not a weak model. It simply has not been benchmarked yet.
