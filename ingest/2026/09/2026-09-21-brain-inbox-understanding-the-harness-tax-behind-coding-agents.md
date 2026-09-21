---
title: 🧩 Understanding the “harness tax” behind coding agents
source: brain@ inbox (curated newsletters)
source_id: brain-inbox
source_url: ''
author: AlphaSignal <news@alphasignal.ai>
date_published: '2026-09-20'
date_captured: '2026-09-21'
ingest_method: email
model: claude-sonnet-5
---

# 🧩 Understanding the “harness tax” behind coding agents

## Insights

- A new study ("HarnessTax") finds that the "harness" — the surrounding software layer that governs instructions, tools, memory, and execution for a coding agent — can change inference cost by up to 5x for the same model on the same task, without a comparable change in success rate.
- Tested across 21 model-harness combinations (7 models × 3 harnesses: Claude Code, Codex CLI, Pi) on SWE-bench Lite and Terminal-Bench 2.0 tasks, measuring both task success and token cost.
- A minimal harness (Pi, with just four tools: read, write, edit, bash) reached the cost-success "Pareto frontier" on both benchmarks — cost-competitive with richer, feature-heavy harnesses, though the study didn't test other reasons developers pick richer tools (integrations, permissions, hooks, memory).
- Models frequently perform better outside their own vendor's harness: across 12 model/benchmark comparisons, an alternative harness beat the native one in 9 cases (e.g., GPT-5.6 Sol scored higher and cheaper with Pi than with OpenAI's own Codex CLI).
- Harness overhead is driven largely by context size — Claude Code's initial context averaged over 10x Pi's, from longer instructions and tool definitions, meaning cost differences stem from harness design, not just model choice.
- The researchers argue developers should treat "model × harness × workload" as a single unit to evaluate, using their own representative tasks and tracking cost-per-success (not cost-per-attempt), since harness/model choice today is often driven by preference or word of mouth rather than measurement.
- Improving the harness is framed as one of few levers available to developers/researchers without frontier-model resources to meaningfully affect agent performance and cost.

## Quote

> "Harness effort is one of the few ways that people can improve performance without touching the model." — Melissa Pan, HarnessTax co-author
