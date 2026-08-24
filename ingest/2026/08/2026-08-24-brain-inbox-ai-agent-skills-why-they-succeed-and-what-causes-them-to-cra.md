---
title: '🧠 AI agent skills: Why they succeed—and what causes them to crash'
source: brain@ inbox (curated newsletters)
source_id: brain-inbox
source_url: ''
author: AlphaSignal <news@alphasignal.ai>
date_published: '2026-08-23'
date_captured: '2026-08-24'
ingest_method: email
model: claude-sonnet-5
---

# 🧠 AI agent skills: Why they succeed—and what causes them to crash

## Insights

- A study analyzing 8,135 trial records across benchmarks (Terminal-Bench 2.0, SkillsBench) found agent "skills" mainly work by stabilizing execution during complex workflows, not by supplying missing facts — procedural anchoring accounted for 65.7% of successful skill cases vs. only 4.5% for explicit knowledge injection.
- Distilling raw execution logs into clean, standardized procedural summaries ("skills") outperformed feeding agents raw workflow memory by 6.06 percentage points on task success — format of experience matters as much as having the experience.
- Skills sharply reduce environment/infrastructure failure rates (from 5.3% in raw execution to 0.2% with distilled skills), suggesting their main value is execution robustness rather than higher-level reasoning improvement.
- Distilling skills without annotating which past trajectories succeeded vs. failed is dangerous: in a controlled test, success rate dropped from 74.6% (with success/failure hints) to 40.0% (without hints), baking hallucinations into the skill library.
- Growing a skill catalog from 5 to 100 options crashes retrieval precision (29.6% → 3.3%), yet downstream task success stayed roughly stable (~36–39%) because related "wrong" skills still offer enough partial procedural guidance — exact skill retrieval is "neither sufficient nor necessary" for success.
- Recommended mitigation for large skill libraries: a two-level gating system — an LLM router first assigns tasks to a domain bucket, then a strict, rule-based trigger (e.g., matching a specific error string) selects the skill, avoiding "semantic confusability" in flat vector search.

## Quote

> Skill use should be understood as a lifecycle problem rather than a single memory-injection mechanism.
