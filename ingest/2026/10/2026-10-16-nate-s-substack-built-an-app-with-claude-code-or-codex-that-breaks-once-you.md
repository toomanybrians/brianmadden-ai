---
title: Built an app with Claude Code or Codex that breaks once you use it? I'll walk
  you through setting up Reverse Engineer Anything (REA) and show you where to point
  it first.
source: Nate’s Substack
source_id: nate-s-substack
source_url: https://natesnewsletter.substack.com/p/rea-reverse-engineer-anything
author: Nate
date_published: '2026-10-15'
date_captured: '2026-10-16'
ingest_method: feed
model: claude-sonnet-5
---

# Built an app with Claude Code or Codex that breaks once you use it? I'll walk you through setting up Reverse Engineer Anything (REA) and show you where to point it first.

## Insights

- REA (Reverse Engineer Anything) is an open-source tool that lets AI coding agents (Codex, Claude Code) inspect existing software's code and runtime behavior — including apps without available source — to explain how a feature actually works.
- The tool's surge in popularity (200,000+ GitHub stars, top of trending) is framed as evidence of demand for this kind of AI-assisted reverse engineering, not just novelty.
- A case study (Ledger Reborn) shows a developer using REA to investigate QuickBooks Desktop's internals and then build an independent local accounting app with its own transaction engine, validated against the original.
- The core argument: AI-built apps often "unravel" in use because a convincing UI reveals little about underlying logic — what records must persist, how values are calculated, what happens on edits. Reverse-engineering existing software surfaces these hidden decisions before you build.
- The piece positions REA as useful for both developers and non-coders, treating reverse engineering as a way to turn observed behavior into a concrete spec (e.g., a business rule or calculation) that an AI can then implement correctly.
- Suggested starting method: pick one narrow, answerable question about a specific behavior, confirm the tool is working with a small test, then use the findings to define a spec with a verifiable check.

## Quote

> A convincing screen gives you very little information about what should happen next, what needs to be remembered, or which numbers have to agree.
