---
title: Train Qwen3 on AWS Trainium with torchtitan
source: AWS Machine Learning Blog
source_id: aws-ml-blog
source_url: https://aws.amazon.com/blogs/machine-learning/train-qwen3-on-aws-trainium-with-torchtitan/
author: Josh Longenecker
date_published: '2026-10-21'
date_captured: '2026-10-22'
ingest_method: feed
model: claude-sonnet-5
---

# Train Qwen3 on AWS Trainium with torchtitan

## Insights

- AWS is positioning Trainium as a drop-in PyTorch training target: TorchNeuron registers it as a native device, so existing torchtitan workflows, launch commands, and config structures work unchanged — the pitch is minimal migration friction from GPU-based training stacks.
- The walkthrough demonstrates three distinct paths to training Qwen3 on Trainium2 hardware: via Hugging Face Transformers v5 (loading/saving standard safetensors directly), via torchtitan's native model implementation, and via custom Neuron Kernel Interface (NKI) kernels for mixture-of-experts layers.
- Checkpoint compatibility is emphasized as a concrete capability, not just a claim: fine-tuned weights exported from Trainium training reload cleanly into standard Hugging Face `AutoModelForCausalLM` with no missing/unexpected keys (aside from an expected tied-embedding exception).
- Custom kernel integration is positioned as a differentiator — engineers can write or adapt NKI kernels (e.g., from `nkilib`) and attach them via an "override registry" to replace specific PyTorch ops (like rotary embeddings) without modifying the broader model code, with a demonstrated near-zero numerical difference versus the native PyTorch implementation.
- Scale tested is modest and specific: a single trn2.48xlarge instance (16 Trainium2 accelerators, 64 logical NeuronCores) training a 4B model and a reduced 4-layer, 64-expert MoE variant of Qwen3-30B-A3B — this is a tutorial-scale proof of capability, not a production training benchmark.
- The piece is a technical enablement post aimed at developers already in the PyTorch/Hugging Face ecosystem, signaling AWS's continued effort to reduce switching costs from GPU-based LLM training to its own Trainium silicon.

## Quote

> AWS Trainium works as a supported torchtitan device across all three configurations in this walkthrough.
