---
title: Introducing workload recovery and expanded infrastructure checks on Amazon
  SageMaker HyperPod
source: AWS Machine Learning Blog
source_id: aws-ml-blog
source_url: https://aws.amazon.com/blogs/machine-learning/introducing-workload-recovery-and-expanded-infrastructure-checks-on-amazon-sagemaker-hyperpod/
author: Roy Allela
date_published: '2026-11-18'
date_captured: '2026-11-19'
ingest_method: feed
model: claude-sonnet-5
---

# Introducing workload recovery and expanded infrastructure checks on Amazon SageMaker HyperPod

## Insights

- AWS distinguishes three failure modes that node-level hardware health checks miss: silent numerical corruption (GPU passes diagnostics but computes wrong values), hung jobs (process stalls but keeps holding GPU resources while scheduler still shows it as running), and cluster-level/Kubernetes failures (crash-looping plugins, missing DaemonSets) that don't surface as node hardware errors.
- New "MultiNodeTrainingValidation" deep health check runs a small fixed training workload (Tiny Megatron/Megatron test) on and across instances specifically to catch GPUs that pass stress tests but produce NaN/infinite loss — treating "trains correctly" as a distinct property from "hardware passes diagnostics."
- A new Kubernetes Resource Monitoring Agent only observes and reports (via K8s events + CloudWatch) — it does not auto-remediate, because root cause may be in the workload itself rather than infrastructure; separates detection from recovery responsibility.
- Hung job detection for Slurm clusters is a new capability requiring customers to opt in per-job via environment variable and a rules file; default detection watches stdout staleness + idle-but-memory-holding GPU state, while custom regex-based rules can catch progress markers or error strings faster.
- AWS frames the value proposition in economic terms via a worked example: an undetected 8-hour hang on 256 H100 GPUs costs ~$16,900, reduced to ~$530 with 15-minute detection — explicitly tying reliability tooling to "goodput" (useful compute time) rather than raw uptime.
- Note that Meta's own Llama 3 405B training paper is cited as evidence that silent data corruption is a real, non-hypothetical failure mode (6 of 419 interruptions in a 54-day run), used to justify the new validation check.

## Quote

> A GPU with a subtle fault can pass its stress tests and still return wrong values.
