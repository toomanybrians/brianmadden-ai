---
title: 'Murshid: an open-source browser for the AI you already pay for'
source: brain@ inbox (curated newsletters)
source_id: brain-inbox
source_url: https://evalsignal.xyz/campaign/62631aa9-416a-4c37-8b06-6f45ae6fa417/ff779425-3a22-47e4-965d-bf0e1f18a567
author: EvalSignal <newsletter@evalsignal.xyz>
date_published: '2026-11-16'
date_captured: '2026-11-16'
ingest_method: email
model: claude-sonnet-5
---

# Murshid: an open-source browser for the AI you already pay for

## Insights

- Murshid is an open-source (GPL-3.0) Chromium/Electron browser that embeds an AI agent (WebBrain) directly in the browsing surface, rather than operating as a separate tool alongside it.
- Architecture separates three layers: the browser shell, the WebBrain agent (reads pages, answers questions, can click/type), and a Companion app that handles model connections — letting the model provider be swapped without changing the browsing workflow.
- The Companion connects existing paid subscriptions (Claude, ChatGPT, Gemini) via supported sign-ins, avoiding manual API key setup, and separately tracks provider quotas; it can also expose a local model endpoint.
- Local model support includes PrismML's Bonsai 2 27B and a separate "d1" decision model for structured agent decisions; local runtime/config (context size, vision support) varies by available machine memory.
- Agent actions execute within the user's own signed-in browser tabs/sessions (not a sandboxed instance), with a "Plan before Act" mode showing proposed steps before execution — raising both capability and oversight/security considerations.
- Explicit caveats: connecting a "local" model endpoint isn't the same as local inference (cloud-selected models still receive prompts/page context); local inference reduces data sent to providers but doesn't make browsing private/offline. Product is a development preview with unsigned/non-notarized installers and missing capabilities (e.g., no Chrome Web Store install).

## Quote

> The real test will be reliable task completion and clear control over what the agent can access, not another chat box beside a page.
