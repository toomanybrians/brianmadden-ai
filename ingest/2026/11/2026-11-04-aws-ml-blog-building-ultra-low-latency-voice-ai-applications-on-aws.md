---
title: Building ultra-low-latency voice AI applications on AWS
source: AWS Machine Learning Blog
source_id: aws-ml-blog
source_url: https://aws.amazon.com/blogs/machine-learning/building-ultra-low-latency-voice-ai-applications-on-aws/
author: Nolan Chen
date_published: '2026-11-03'
date_captured: '2026-11-04'
ingest_method: feed
model: claude-sonnet-5
---

# Building ultra-low-latency voice AI applications on AWS

## Insights

- Cartesia (AWS Partner) built voice AI models — Sonic (text-to-speech) and Ink (speech-to-text) — on State Space Models (SSMs) rather than transformers, claiming sub-100ms latency (Sonic: ~90ms to first audio byte) because SSMs process sequences step-by-step with constant memory, avoiding the quadratic compute cost of transformer attention.
- Ink performs native turn detection and semantic end-pointing (distinguishing mid-sentence pauses from true conversational boundaries) without a separate voice-activity-detection model — pitched as removing a common source of awkward AI-conversation pauses.
- Sonic supports voice cloning from just 10 seconds of audio and covers 44+ languages, positioning it for contact centers, telehealth, gaming NPCs, accessibility tools, and sales agents.
- AWS offers two deployment paths: a managed SageMaker/AWS Marketplace endpoint (minutes to deploy, in-VPC, AWS-managed scaling) versus self-managed EC2 GPU deployment (hours/days, full control over networking/scaling/cost, suited to teams with existing GPU infra or compliance needs) — a concrete illustration of the managed-vs-self-hosted tradeoff AWS is pushing for AI infrastructure generally.
- Cartesia's models are already integrated into Amazon Connect (AWS's contact center product), used for live transcription/agent-assist and multilingual real-time voice handling at claimed production scale ("millions of customer interactions daily").
- The piece frames SSMs as a distinct architectural alternative to transformers specifically advantageous for streaming/real-time audio workloads, not just a speed optimization of existing transformer TTS/STT models.

## Quote

> To feel natural, AI-generated speech must arrive within the same temporal window as human turn-taking.
