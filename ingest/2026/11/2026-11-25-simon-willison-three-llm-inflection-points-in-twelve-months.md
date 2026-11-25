---
title: Three LLM inflection points in twelve months
source: Simon Willison's Newsletter
source_id: simon-willison
source_url: https://simonw.substack.com/p/three-llm-inflection-points-in-twelve
author: Simon Willison
date_published: '2026-11-24'
date_captured: '2026-11-25'
ingest_method: feed
model: claude-sonnet-5
---

# Three LLM inflection points in twelve months

## Insights

- Willison identifies three "inflection points" in coding-agent capability over 12 months: Claude Opus 4.5 / GPT-5.1 (Nov 2025, agents became reliably correct by default rather than needing frequent correction), "Fable class" models (June/July 2026, defined by proactive, autonomous tool-use to solve open-ended problems without hand-holding), and a leap in 3D modeling/game-design "taste" (Sept/Oct 2026, where models like Opus 5.5 could iteratively make software genuinely "fun," not just functional).
- "Fable class" models are characterized by relentless proactivity — e.g., spinning up custom tooling (screenshot mechanisms, logging servers) unprompted to solve a debugging task, or triangulating a physical sound source using multiple microphones given only a goal and tools.
- A real-world example (Ladybird browser) shows coding agents producing a concrete, measurable leap: ~75,650 new passing web-platform-tests in one month, with ~60,000 of those gained in a single five-day window by pointing agents directly at the test suite and having them fill gaps — surpassing Safari's pass rate.
- Software supply chains are seeing agent-driven rewrites (e.g., C-to-Rust conversions) that critics argue produce large volumes of new code without matching the bug-fixing/security rigor of actively maintained original projects (curl maintainer pushback cited).
- Emerging architectural trend: "looped transformers" (GLM-5.4, Inkling 2 Mini) that re-run middle layers multiple times per token to deepen reasoning without increasing parameter count, aimed at improving agentic coding performance per token.
- A historian used GPT-6.2 Astra to autonomously identify the creator of an anonymous 1808 sketchbook in 22 minutes by locating an obscure archival source and forming a testable hypothesis — raising questions about an impending "crisis of confidence" in historical research, though expected to be less disruptive than in mathematics since history isn't about converging on single provable truths.

## Quote

> Give it a goal, give it the right tools, and watch it cook.
