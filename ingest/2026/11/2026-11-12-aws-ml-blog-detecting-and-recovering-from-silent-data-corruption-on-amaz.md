---
title: Detecting and recovering from silent data corruption on Amazon SageMaker HyperPod
source: AWS Machine Learning Blog
source_id: aws-ml-blog
source_url: https://aws.amazon.com/blogs/machine-learning/detecting-and-recovering-from-silent-data-corruption-on-amazon-sagemaker-hyperpod/
author: Siddharth Senger
date_published: '2026-11-11'
date_captured: '2026-11-12'
ingest_method: feed
model: claude-sonnet-5
---

# Detecting and recovering from silent data corruption on Amazon SageMaker HyperPod

## Insights

- Silent data corruption (SDC) — GPUs returning wrong-but-plausible numbers with no error raised — is a real, measured problem at scale: Meta attributed 6 of 419 unexpected training job interruptions to SDC during a 54-day Llama 3 405B pretraining run on up to 16K H100s, and that undercounts cases that didn't interrupt the job.
- Existing hardware/infrastructure safeguards (ECC memory, GPU Xid errors, DCGM health checks, network/storage checksums) all guard different boundaries and structurally cannot catch SDC, because the fault is in the compute path itself, which has no error-correction mechanism — detection has to be built into the training loop.
- The proposed solution adds three in-loop checks to PyTorch DDP: a non-finite gradient check (catches NaN/Inf), a "ring replay audit" where GPUs recompute each other's micro-batches and compare bit-for-bit, and a post-update weight fingerprint comparison across replicas — each targeting a different point where corruption can land.
- Once a corrupt rank is named, SageMaker HyperPod's Kubernetes node-naming scheme lets the team map rank → node → instance ID directly, enabling automated cordon, correlation against GPU telemetry, and node replacement/recovery from a prior checkpoint.
- Testing on a 953M-parameter model across 32 H100 GPUs found real tradeoffs: deterministic audits every 10 steps added ~35% step-time overhead vs. plain DDP, while audits every 100 steps cost only ~10% but allow up to 99 corrupted updates before detection; some backward-only faults with default (non-deterministic) kernels went completely uncaught in 50 test steps.
- The piece is explicit that detection is probabilistic, not proof: fingerprint comparisons and clean hardware telemetry don't guarantee a node is fault-free, and the authors recommend keeping human approval in the loop before replacing nodes in production.

## Quote

> SDC is in the compute path, and every integrity check you already have guards a different boundary.
