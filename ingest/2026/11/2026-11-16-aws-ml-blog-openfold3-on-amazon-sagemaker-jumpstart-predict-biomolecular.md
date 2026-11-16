---
title: 'OpenFold3 on Amazon SageMaker JumpStart: Predict biomolecular structures'
source: AWS Machine Learning Blog
source_id: aws-ml-blog
source_url: https://aws.amazon.com/blogs/machine-learning/openfold3-on-amazon-sagemaker-jumpstart-predict-biomolecular-structures/
author: Malav Shastri
date_published: '2026-11-13'
date_captured: '2026-11-16'
ingest_method: feed
model: claude-sonnet-5
---

# OpenFold3 on Amazon SageMaker JumpStart: Predict biomolecular structures

## Insights

- OpenFold3 (open source, Apache 2.0, from OpenFold Consortium/Columbia's AlQuraishi Lab) is now deployable via SageMaker JumpStart as a managed endpoint, predicting 3D structures for proteins, DNA, RNA, ligands, and their complexes in a single inference call.
- AWS frames the core infrastructure pain point for scientific ML as GPU setup, CUDA/PyTorch stacks, large checkpoints, and request latency (minutes, not milliseconds) — positioning managed JumpStart deployment as abstracting that complexity away.
- Because folding jobs can take minutes to an hour, the endpoint uses asynchronous inference (S3-staged requests, up to 1-hour timeout) rather than AWS's typical real-time endpoint pattern, with built-in request queuing and scale-to-zero for idle cost savings.
- A key enterprise/privacy angle: the endpoint runs with network isolation and never calls external MSA (multiple sequence alignment) servers — customers must generate and supply their own MSAs, keeping proprietary sequences inside their AWS account rather than sending them to public tools.
- AWS's own benchmark shows MSAs matter enormously for accuracy: on a carbonic anhydrase/zinc/drug complex, adding an MSA raised average pLDDT confidence from 30 to 98 and cut backbone deviation from experimental structure from 22 Å to 0.2 Å, with no added prediction time.
- Multi-GPU instances don't speed up a single prediction but allow parallel concurrent predictions (one per GPU), useful for high-throughput screening pipelines in drug discovery workflows.

## Quote

> Treat this example as a demonstration of the workflow... not as a benchmark of accuracy on novel targets.
