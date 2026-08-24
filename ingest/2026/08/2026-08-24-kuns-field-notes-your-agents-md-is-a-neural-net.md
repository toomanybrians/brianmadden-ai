---
title: Your AGENTS.md is a Neural Net
source: Kun's Field Notes
source_id: kuns-field-notes
source_url: https://blog.kunchenguid.com/p/your-agentsmd-is-a-neural-net
author: Kun Chen
date_published: '2026-08-23'
date_captured: '2026-08-24'
ingest_method: feed
model: claude-sonnet-5
---

# Your AGENTS.md is a Neural Net

## Insights

- Agent memory files (AGENTS.md/CLAUDE.md) typically decay into one of four failure states: empty (never populated), bloated (rules accumulate forever, diluting instruction-following as the file grows), stale (describes outdated systems), or drifted (inconsistent across files/tools).
- Proposes splitting memory into two tiers with different treatment: a small, handwritten, rarely-changed user-level file for personal preferences (never edited by tools or agents), versus a project-level file that should be actively "trained" like a model.
- Frames the project-level file as analogous to neural net weights: each agent session is a "forward pass" (file used as-is), the gap between desired and actual agent behavior is "loss," and updating the file based on transcript evidence is a "backward pass" — with the file's token budget acting like model size (capacity vs. inference cost tradeoff).
- Argues the raw data needed to improve these files already exists in session transcripts (what was asked, what the agent did, where it violated or correctly followed rules) but most people never mine it — they only do "forward passes," never backward ones.
- Recommends disciplined update practices: rely only on transcript evidence (not memory/anecdote), require patterns across a batch of sessions before editing (avoid one-off overreactions), make small bounded edit sets per pass, and enforce a strict token budget where additions require corresponding removals; narrow triggerable rules get extracted into separate "skills" rather than bloating the main file.
- Describes an open-source tool (backpass) built to automate this loop: it pulls transcripts from common agent harnesses, extracts loss-relevant signal via cheap model calls requiring verbatim quotes as evidence, aggregates gradients deterministically across sessions, proposes a capped number of edits via one higher-reasoning model call, and requires human review/approval before any write occurs.

## Quote

> Thinking of AGENTS.md this way also leans into the reality - most people will not actually carefully read the content very often.
