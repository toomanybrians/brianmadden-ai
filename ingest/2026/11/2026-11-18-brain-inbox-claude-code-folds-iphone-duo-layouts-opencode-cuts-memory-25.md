---
title: 📱 Claude Code folds iPhone Duo layouts; OpenCode cuts memory 25x
source: brain@ inbox (curated newsletters)
source_id: brain-inbox
source_url: ''
author: AlphaSignal <news@alphasignal.ai>
date_published: '2026-11-17'
date_captured: '2026-11-18'
ingest_method: email
model: claude-sonnet-5
---

# 📱 Claude Code folds iPhone Duo layouts; OpenCode cuts memory 25x

## Insights

- AI coding agents are expanding beyond code generation into controlling development tooling itself: Claude Code can now drive the iOS simulator directly, folding/unfolding Apple's foldable iPhone Duo to test layouts across device states without manual Xcode interaction.
- Claude Code can install Apple's "App Resizability skill" to scan existing apps for layout problems, propose fixes, apply them on approval, and verify visually in the simulator — collapsing editing, building, and visual QA into one agent session.
- OpenCode's browser tool was rewritten in Rust, cutting memory use ~25x (190MB to 5.6MB per session) and binary size ~23x, while removing Node.js/Playwright dependencies — framed as a cost/efficiency story (reported at ~$60 to rebuild).
- The rewrite exposes browser actions directly as MCP (Model Context Protocol) tools, letting agents open URLs, scrape, loop, and chain actions using the user's real logged-in browser rather than a separate headless browser setup.
- Separately, Liquid AI released small "decision models" (d1.2, d1.2-ultra) designed not for chat but for structured extraction/classification across text, image, and audio, with calibrated confidence scores intended to route low-confidence outputs to human review.
- A listed signal item notes an OpenAI study finding ChatGPT nearly doubled productivity for 1,800 academic scientists, and a separate item flags silent numerical bugs found in KL/JSD divergence calculations affecting training pipeline gradients.

## Quote

> "We're watching the IDE become the agent. That's a big deal." — Lior Alexander, AlphaSignal
