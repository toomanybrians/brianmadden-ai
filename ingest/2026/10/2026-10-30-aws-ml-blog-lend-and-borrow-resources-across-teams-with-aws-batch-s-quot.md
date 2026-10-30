---
title: Lend and borrow resources across teams with AWS Batch’s quota management for
  SageMaker Training jobs
source: AWS Machine Learning Blog
source_id: aws-ml-blog
source_url: https://aws.amazon.com/blogs/machine-learning/lend-and-borrow-resources-across-teams-with-aws-batchs-quota-management-for-sagemaker-training-jobs/
author: Michelle Goodstein
date_published: '2026-10-29'
date_captured: '2026-10-30'
ingest_method: feed
model: claude-sonnet-5
---

# Lend and borrow resources across teams with AWS Batch’s quota management for SageMaker Training jobs

## Insights

- AWS Batch now supports "quota management" for SageMaker Training jobs: administrators can carve shared GPU capacity into per-team/project "quota shares," each with its own capacity limit and sharing strategy, aimed at reducing manual coordination overhead as ML orgs scale.
- Three sharing strategies are offered: RESERVE (hold idle capacity until the owning team needs it), LEND (give up idle capacity to others but reclaim automatically when needed), and LEND_AND_BORROW (both lend idle capacity and borrow from others when busy).
- Two preemption mechanisms exist: cross-share preemption automatically reclaims capacity from borrowers when the lending team submits new jobs, and optional in-share preemption lets higher-priority jobs bump lower-priority running/queued jobs within the same quota share.
- Job priority is configurable per submission and can be updated after submission via an UpdateServiceJob API, which can trigger preemption of already-running lower-priority jobs.
- The feature is positioned as pairing with SageMaker AI "training plans" for capacity reservation, suggesting AWS is building a fuller GPU-capacity-allocation/utilization layer on top of raw reserved compute.
- Framed explicitly as a utilization/cost-optimization and admin-time-saving tool rather than a new ML capability — it's scheduling/infrastructure plumbing, not a model or workflow advance.

## Quote

> AWS Batch with quota management can help your organization increase compute utilization and more effectively prioritize your teams and workloads.
