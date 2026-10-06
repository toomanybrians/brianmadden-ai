---
title: OpenAI DevDay 2026 live blog
source: Simon Willison's Newsletter
source_id: simon-willison
source_url: https://simonw.substack.com/p/openai-devday-2026-live-blog
author: Simon Willison
date_published: '2026-10-05'
date_captured: '2026-10-06'
ingest_method: feed
model: claude-sonnet-5
---

# OpenAI DevDay 2026 live blog

## Insights

- OpenAI's DevDay 2026 centered on "dots," a personal AI agent product with plans for vertical-specific versions (legal, finance), alongside "ChatGPT Space," a collaboration platform resembling Google Drive/Docs — both signal OpenAI's push toward embedding agents into organizational workflows beyond chat.
- New "Sign in with ChatGPT" lets third-party apps authenticate users via their existing ChatGPT account/tokens, pointing toward ChatGPT becoming an identity and billing layer across the AI app ecosystem.
- An OpenAI security staffer described being caught off guard by sudden jumps in model capability around "cyber," "swarming," and coordinated messaging behaviors, arguing organizations need incident response plans specifically for unexpected AI capability jumps — not just hardened systems but cultural/process readiness.
- Security research (Anthropic) found newer models (GLM-5.3, Claude Mythos Preview) crossing a capability threshold in binary exploitation tasks that earlier models (Opus 4.6, GLM-5.2) could not achieve at all, suggesting a step-change in offensive-cyber capability rather than gradual improvement.
- A separate piece warns that autonomous/personal agents sharing common channels (package caches, email, Slack, shared docs) create conditions for "worm"-like propagation, where one compromised agent leaves instructions that hijack others — a novel security risk unique to multi-agent systems.
- The piece argues coding/personal agents' low friction for spinning up usage-metered services creates financial risk, and that hard (not just warning-based) budget caps should become default-on for usage-based cloud/API products; AWS and Google Cloud have both recently shipped spend-limit features responding to this need.

## Quote

> Do my teams know what to do when something goes wrong? Do I have the right incident response?
