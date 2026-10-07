---
title: Manage Amazon SageMaker HyperPod Spaces directly from SageMaker Studio
source: AWS Machine Learning Blog
source_id: aws-ml-blog
source_url: https://aws.amazon.com/blogs/machine-learning/manage-amazon-sagemaker-hyperpod-spaces-directly-from-sagemaker-studio/
author: Giuseppe Angelo Porcelli
date_published: '2026-10-06'
date_captured: '2026-10-07'
ingest_method: feed
model: claude-sonnet-5
---

# Manage Amazon SageMaker HyperPod Spaces directly from SageMaker Studio

## Insights

- AWS now lets data scientists create, start, stop, and open SageMaker HyperPod "Spaces" (JupyterLab/Code Editor dev environments on EKS clusters) through a GUI in SageMaker Studio, removing the prior requirement to use HyperPod CLI or kubectl — explicitly targeting non-infrastructure users.
- This is a self-service layer on top of shared GPU/accelerator clusters: admins retain control via IAM policies, namespace-based Task Governance (compute quotas/queues via Kueue), and per-user identity propagation that attributes every cluster action to a specific user for auditing (CloudTrail).
- Supports fractional GPU allocation (NVIDIA MIG) so interactive dev work can run alongside training/inference jobs on the same hardware — framed as maximizing utilization of expensive GPU infrastructure rather than siloing it per workload type.
- A documented cold-start problem (5–7 minutes to launch a new environment) is addressed via a Kubernetes "over-provisioning" pattern using low-priority placeholder pods that pre-pull container images onto warm nodes; this cuts startup to ~30–40 seconds but costs extra for idle running nodes.
- Local VS Code can connect directly to cluster compute via SSH-over-SSM (no exposed port 22, no SSH key management), billed per-hour through AWS Systems Manager Advanced Instance pricing — compute/storage otherwise billed as standard HyperPod usage.
- Idle shutdown and task governance are positioned as cost-control guardrails for organizations opening up shared GPU clusters to broader, less infrastructure-savvy user bases.

## Quote

> Managing HyperPod Spaces with SageMaker Studio bridges the gap between data scientists and high-performance compute infrastructure.
