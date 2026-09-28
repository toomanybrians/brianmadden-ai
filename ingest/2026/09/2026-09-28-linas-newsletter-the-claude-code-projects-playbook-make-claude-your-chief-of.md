---
title: 'The Claude Code Projects Playbook: Make Claude Your Chief of Staff 🧠'
source: Linas's Newsletter
source_id: linas-newsletter
source_url: https://linas.substack.com/p/claude-code-projects-playbook
author: Linas Beliūnas
date_published: '2026-09-25'
date_captured: '2026-09-28'
ingest_method: feed
model: claude-sonnet-5
---

# The Claude Code Projects Playbook: Make Claude Your Chief of Staff 🧠

## Insights

- Anthropic redesigned Claude Code "Projects" (beta since Sept 17) so a single ongoing conversation acts as a coordinator, splitting work into parallel threads that run as independent Claude Code sessions on separate branches, sharing repositories, instructions, and memory.
- Anthropic frames the intended usage model explicitly as briefing Claude like a Chief of Staff: give it work as it arises, and it scopes, delegates to threads, reviews results, and assembles output; users can steer from a phone.
- Outcomes diverge sharply based on setup discipline: successful users provide a clear brief, named workstream owners, a shared decision file, standing rules, review gates, and a budget — vague-goal users get overlapping pull requests and threads that silently exhaust usage windows (auto-resuming when limits reset).
- Internal Anthropic staff reaction is enthusiastic (one engineer says it unlocked "a totally different mode of working"; another shifted fully from command line to Claude Desktop), while external commentary is more skeptical.
- External critiques: The Register framed it as paying for parallel work; a Windows Forum analysis noted persistent merge conflicts and incompatible pull requests, making human review the bottleneck.
- In Anthropic's own compiler experiment, 16 parallel agents repeatedly hit the same bug and overwrote each other's fixes until the work was restructured differently — illustrating a concrete failure mode of naive parallelization.

## Quote

> It felt, he said, like "having a chief of staff dedicated to each thing you're working on."
