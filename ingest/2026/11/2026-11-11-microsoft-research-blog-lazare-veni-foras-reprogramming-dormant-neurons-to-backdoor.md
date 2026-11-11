---
title: 'Lazare, veni foras: Reprogramming Dormant Neurons to Backdoor AI Agents'
source: Microsoft Research Blog
source_id: microsoft-research-blog
source_url: https://www.microsoft.com/en-us/research/blog/lazare-veni-foras-reprogramming-dormant-neurons-to-backdoor-ai-agents/
author: Dimitris Papailiopoulos
date_published: '2026-11-10'
date_captured: '2026-11-11'
ingest_method: feed
model: claude-sonnet-5
---

# Lazare, veni foras: Reprogramming Dormant Neurons to Backdoor AI Agents

## Insights

- Microsoft researchers (with Claude Code/Opus 4.5 assisting discovery) found that reprogramming fewer than 10 "dormant" (rarely-firing) neurons in an LLM, with no retraining, is enough to install a backdoor — "Lazarus" — that triggers malicious tool/terminal commands on a hidden cue (e.g., a date change) while passing standard safety evals.
- The attack works because pretraining organizes internal representations so cleanly that a linear classifier trained on ~50 examples can detect a trigger pattern and repurpose dormant neurons into trigger detectors that force specific tokens into the model's output stream.
- Only inference-level compute is needed (no training infrastructure), and the attack requires only write access to model weights — meaning internally developed/closed models are just as exposed as open-weight ones; the core vulnerability is weight integrity, not openness.
- Detection is possible (frontier agents can be prompted to spot anomalous weight edits) but not provable — reliable detection requires diffing against original unmodified weights, making provenance and tamper-evident audit trails essential rather than optional.
- Microsoft's current mitigations (Foundry) focus on provenance verification, publisher trust-tying, and environment scanning for open-weight models onboarded via Azure/Hugging Face; planned additions include AI-assisted weight scanning, red-teaming harnesses, and cryptographic model signing.
- Framed explicitly as a known class of threat (compromised software / insider risk) rather than a novel category — the recommended posture is standard security hygiene applied to models: don't trust implicitly, limit agent permissions, monitor behavior.

## Quote

> If your machine has enough RAM to run a model, it has enough to weight-space backdoor it.
