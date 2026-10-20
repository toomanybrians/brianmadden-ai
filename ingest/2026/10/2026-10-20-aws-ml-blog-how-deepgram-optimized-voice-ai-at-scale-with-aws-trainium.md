---
title: How Deepgram optimized voice AI at scale with AWS Trainium
source: AWS Machine Learning Blog
source_id: aws-ml-blog
source_url: https://aws.amazon.com/blogs/machine-learning/how-deepgram-optimized-voice-ai-at-scale-with-aws-trainium/
author: Pierre Lienhart
date_published: '2026-10-19'
date_captured: '2026-10-20'
ingest_method: feed
model: claude-sonnet-5
---

# How Deepgram optimized voice AI at scale with AWS Trainium

## Insights

- Deepgram ported its Nova-3 speech-to-text model from standard PyTorch to AWS Trainium2 for offline batch workloads (contact-center analytics, medical transcription), working with AWS's Forward Deployed Engineering team over several months.
- The optimized setup (8 model replicas per trn2.3xlarge instance) delivered 11–70% more audio processed per dollar versus Deepgram's prior compute options, based on pricing at time of evaluation — a wide, workload-dependent range rather than a single clean number.
- Hand-tuned kernels produced large layer-level gains: 2x lower latency on FFN layers (fixing memory-bandwidth-bound weight reloading), 1.5x speedup on depthwise conv1d (rewritten for the Vector Engine), and up to 50x on conv2d at batch sizes ≤32 (unblocking a compilation bottleneck that previously capped batch size).
- Because Deepgram's production serving stack is Rust-based, the team built a custom Rust runtime calling AWS's Neuron Runtime API directly (bypassing Python/PyTorch in the serving path), yielding a 7.5% throughput gain over a Python multiprocessing baseline, with larger gains at low batch sizes.
- The work relied on AWS's Neuron software stack (TorchNeuron, NKI kernel library, Neuron Explorer profiler, and an "agentic" NAD toolkit that uses AI to help analyze profiles and write kernel code) — suggesting AWS is positioning Trainium adoption as increasingly tool-assisted rather than purely manual low-level engineering.
- Framed as a case study validating Trainium as a cost-competitive alternative inference chip for large-scale, throughput-oriented (not necessarily latency-critical) voice AI workloads; gains reported are specific to batch/offline processing, not real-time serving.

## Quote

> Our setup demonstrated cost savings in offline, throughput-oriented scenarios, validating AWS Trainium as a viable and efficient option for Deepgram's inference workloads.
