---
title: 'Flint-interactive: A language for creating interactive data visualizations'
source: Microsoft Research Blog
source_id: microsoft-research-blog
source_url: https://www.microsoft.com/en-us/research/blog/flint-interactive-a-language-for-creating-interactive-data-visualizations/
author: Chenglong Wang, Yuwei  Xiao, Alper Sarikaya, Michel Galley, Chris Quirk, Jianfeng
  Gao
date_published: '2026-10-22'
date_captured: '2026-10-23'
ingest_method: feed
model: claude-sonnet-5
---

# Flint-interactive: A language for creating interactive data visualizations

## Insights

- Flint-interactive is a new language/compiler layer on top of Flint for specifying interactive data visualizations, aimed at letting AI agents (not just human developers) generate charts with click, filter, zoom, highlight, and cross-chart behaviors.
- The core technical move is separating "visual logic" (handled automatically by the compiler: hit testing, rendering, low-level updates) from "interaction logic" (specified at a high semantic level by the user or agent, e.g., mapping a click event to a highlight or annotation operator).
- The authors frame the current problem explicitly: generating interactive visualizations with frontier models today is costly (multiple rounds of reasoning/coding/debugging) and unreliable (expressive interactivity easily produces broken layouts or interactions), and existing viz libraries' built-in interactions aren't expressive enough for bespoke needs.
- The stated goal is to collapse that gap by giving agents a high-level language instead of requiring them to write low-level, renderer-specific code, reducing token/time cost and improving reliability of agent-generated interactive charts.
- The system is designed to connect beyond single charts — linking visualizations to tables, text, widgets, and application state, enabling interactive data stories and dashboards where selections in one element update others.
- Access is offered at multiple levels: end users via chat/MCP integration (agent generates chart + interaction spec in conversation), app builders via a programming API/canvas, and "interaction designers" who can propose new reusable interaction presets via GitHub.

## Quote

> These challenges are results of the lack of an expressive yet high-level language to specify visual interactions.
