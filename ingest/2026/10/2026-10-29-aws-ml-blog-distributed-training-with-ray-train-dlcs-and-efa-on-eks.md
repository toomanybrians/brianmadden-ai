---
title: Distributed training with Ray Train DLCs and EFA on EKS
source: AWS Machine Learning Blog
source_id: aws-ml-blog
source_url: https://aws.amazon.com/blogs/machine-learning/distributed-training-with-ray-train-dlcs-and-efa-on-eks/
author: Sunita Koppar
date_published: '2026-10-28'
date_captured: '2026-10-29'
ingest_method: feed
model: claude-sonnet-5
---

# Distributed training with Ray Train DLCs and EFA on EKS

## Insights

- AWS's Ray Train Deep Learning Container (DLC) bundles CUDA, PyTorch, NCCL, EFA networking libraries, the AWS OFI NCCL plugin, and Ray into a single pre-tested, pre-published image, eliminating the version-alignment work teams otherwise face when assembling distributed training stacks themselves.
- The post frames container/networking misconfiguration as a silent failure mode: a mismatch in the EFA/NCCL stack doesn't error out, it silently falls back to slower TCP sockets, which AWS positions as the main problem the DLC is designed to prevent.
- KubeRay (an open-source Kubernetes operator) is used to manage Ray clusters on EKS via a single RayCluster manifest, with one container image serving both head and worker roles — all job-specific variation (hardware, transport, packages, versions) is pushed into external configuration rather than image rebuilds.
- The worked example fine-tunes Qwen2.5-1.5B using PyTorch FSDP across 8 L4 GPUs (two g6.12xlarge instances) and reports EFA networking roughly doubling throughput versus TCP fallback, with no changes to training code.
- Infrastructure automation scripts handle capacity-finding across AWS regions/zones (since GPU instance availability shifts daily), idempotent cluster deployment, and teardown — presented as a reproducible, CI-gateable pipeline rather than a one-off demo.
- The piece is explicitly scoped as sample/reference architecture (random synthetic training data), with suggested next steps toward production use: real datasets, S3/FSx checkpointing, failure recovery config, and scaling to larger GPUDirect RDMA instance families like p5.
