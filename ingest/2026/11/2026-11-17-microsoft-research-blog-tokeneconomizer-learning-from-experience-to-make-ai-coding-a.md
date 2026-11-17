---
title: 'TokenEconomizer: Learning from Experience to Make AI Coding Agents More Efficient'
source: Microsoft Research Blog
source_id: microsoft-research-blog
source_url: https://www.microsoft.com/en-us/research/blog/tokeneconomizer-learning-from-experience-to-make-ai-coding-agents-more-efficient/
author: Aaron J. Li, Weijia Xu, Chandan Singh, Jeevana Priya Inala, Bin Yu, Ion Stoica,
  Michel Galley, Jianfeng Gao
date_published: '2026-11-16'
date_captured: '2026-11-17'
ingest_method: feed
model: claude-sonnet-5
---

# TokenEconomizer: Learning from Experience to Make AI Coding Agents More Efficient

## Insights

- Profiling of Claude Code on 60 SWE-Bench tasks found three recurring sources of waste: 30% of tool calls repeated earlier-session actions (vs. 7% cross-repo), 16 of 23 loaded tool descriptions were never used, and the 17% of failed tasks consumed 32% of total spending.
- TokenEconomizer is a black-box plugin layered on top of existing coding agents (no model/agent modification) that learns from a repo's session history via three mechanisms: "micro-skills" (confirmed repo-specific notes added to context), tool pruning (removing rarely-used tools while keeping core ones), and failure-loop intervention (a judge model detects stuck agents and injects a redirect note).
- Across 277 real bug-fix tasks in six repositories and five agent-model combinations, it cut average cost 18.4–30.9% with no performance loss in any of the 30 pairings; cumulative costs dropped below baseline by the sixth task in every repo.
- Comparison point: reducing model reasoning effort achieved similar or larger savings but caused "substantial performance degradation," whereas TokenEconomizer's savings came without that tradeoff — in fact Pass@1 rose in four of five combinations.
- Savings generalized beyond the original benchmark: 16.0–21.2% lower cost on sequential web-dev tasks (Web-Bench), and 6.4–19.6% lower even on security-auditing tasks where every task occurs in a new, unseen repository.
- The tool treats existing fixed-strategy cost-saving plugins as inconsistent — each helped in some repos and not others — framing the core design insight as: effective cost control must adapt per-repository rather than apply one universal strategy.

## Quote

> Together, these findings suggest that effective cost control must adapt to the repository, rather than apply the same strategy everywhere.
