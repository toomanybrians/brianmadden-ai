---
title: Cost-optimizing AssemblyAI speech-to-text inference on AWS with Amazon EC2
  Spot
source: AWS Machine Learning Blog
source_id: aws-ml-blog
source_url: https://aws.amazon.com/blogs/machine-learning/cost-optimizing-assemblyai-speech-to-text-inference-on-aws-with-amazon-ec2-spot/
author: Belair Albahagwi
date_published: '2026-11-13'
date_captured: '2026-11-16'
ingest_method: feed
model: claude-sonnet-5
---

# Cost-optimizing AssemblyAI speech-to-text inference on AWS with Amazon EC2 Spot

## Insights

- AssemblyAI runs its speech-to-text inference fleet (thousands of GPU instances) on a mix of EC2 Spot and On-Demand instances via Amazon ECS capacity providers, reporting 70% cost savings on inference compute versus pure On-Demand pricing.
- Resilience against Spot interruptions (2-minute reclaim notice) comes from decoupling job submission/execution with SQS queues: in-flight jobs either finish within the window or get requeued for pickup by another healthy instance, with a dead-letter queue for jobs that exhaust retries.
- Interruption recovery is sped up via custom AMIs that bundle model artifacts and container images, enabling new instances to warm up and rejoin the pool in about 2 minutes.
- The core cost/reliability lever is diversification across three GPU instance families (g4dn/T4, g5/A10G, g6/L4) and Availability Zones, which taps independent Spot capacity pools so pressure on one family doesn't starve the whole fleet; EC2's "price-capacity optimized" allocation strategy picks pools with highest capacity at lowest price.
- Separate, fully independent regional deployments (US West Oregon, Europe London) are used specifically to satisfy data residency requirements for regulated customers (healthcare, finance, legal), not just for latency/performance reasons.
- Compute demand grew ~4x year-over-year, and the Spot/queue-retry architecture was credited with keeping unit economics sustainable through that growth.

## Quote

> Designing fault tolerance from day one with queue-based retries and fast warm-up turns Spot interruptions into routine events while maintaining SLA commitments.
