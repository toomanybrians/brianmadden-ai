---
title: '⚙️ Data: Agents fail an average of 40% of their tasks'
source: brain@ inbox (curated newsletters)
source_id: brain-inbox
source_url: https://archive.thedeepview.com/p/why-jensen-huang-proved-to-be-too-big-to-fire
author: The Deep View <newsletter@thedeepview.co>
date_published: '2026-11-24'
date_captured: '2026-11-25'
ingest_method: email
model: claude-sonnet-5
---

# ⚙️ Data: Agents fail an average of 40% of their tasks

## Insights

- OpenClaw Foundation's new ShellBench benchmark (built with Hugging Face, Red Hat, UC Berkeley, Parsewave) tested 13 leading AI models across 5 agent harnesses on 100 realistic tasks set in messy, real-world contexts (emails, spreadsheets, receipts, PDFs) rather than clean benchmark environments — and found agents fail roughly 40% of tasks on average.
- Even top-tier models (GPT-6 Astra, GPT-6.1 Sol, Claude Fable 5.2, Gemini 4 Carbon) only completed tasks successfully 6 out of 10 times; weaker models (Meta Muse Wonder, DeepSeek v4.1 Flash, Claude Sonnet) succeeded only about 4 out of 10 times.
- A major failure mode wasn't inaccurate information retrieval but omission: 51% of failures involved leaving out important details, even though the agent had actually collected the relevant info in 87% of those cases — suggesting a synthesis/completeness gap rather than a knowledge gap.
- Model performance was inconsistent across repeated runs (one model dropped from 75% to 49% accuracy on repeat trials), and higher cost per run did not reliably correlate with better performance — a cheaper model (17¢/run) nearly matched a pricier one ($1.01/run).
- Open-source agent harnesses (Hermes, OpenClaw, Pi, Codex CLI) slightly outperformed the proprietary Claude Code harness in this benchmark.
- Separately, a consumer anecdote illustrates agentic commerce working well in a narrow, well-scoped task: ChatGPT connected to Instacart via a sign-in flow, built and refined a 16-item Thanksgiving grocery cart from two recipes (including substitutions and quantity verification), and completed checkout — delivery arrived within hours, with total interaction time under 20 minutes.

## Quote

> "These systems may not be as reliable as common benchmarks make them seem."
