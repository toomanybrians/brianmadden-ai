---
title: 'New paper: Emerging trends in AI agent evaluation'
source: AI as Normal Technology
source_id: ai-as-normal-technology
source_url: https://www.normaltech.ai/p/new-paper-emerging-trends-in-ai-agent
author: Sayash Kapoor
date_published: '2026-10-19'
date_captured: '2026-10-20'
ingest_method: feed
model: claude-sonnet-5
---

# New paper: Emerging trends in AI agent evaluation

## Insights

- Agent evaluation is fundamentally harder than model evaluation: evaluators must scrutinize entire trajectories (not just outcomes) to detect shortcuts, and attributing performance changes to specific agent components is difficult.
- Rigorous agent evaluation is becoming very expensive — some agents on the ExploitBench benchmark cost tens of thousands of dollars in credits to evaluate, not counting the engineering effort to build and maintain evaluation infrastructure.
- Evaluators increasingly rely on other AI agents to monitor/inspect agent traces at scale (e.g., investigating the OpenAI-HuggingFace incident), an approach with acknowledged limitations and biases, since the monitoring tools themselves require evaluation.
- Evaluation results don't reliably transfer across levels of scope: METR's RCT found that using agent tools for software development actually increased task completion time despite expectations from lab-level capability demonstrations.
- The paper distinguishes two evaluation framings — "automation" (can an agent replace a task) vs. "augmentation" (can an agent improve human work) — noting these are complementary but yield different research agendas.
- Meaningful independent evaluation is constrained by funding access, model access, and shrinking transparency (e.g., frontier labs now release only summarized Chain-of-Thought traces rather than raw ones).

## Quote

> An agent might demonstrate capability in the lab, but face limits when placed in a specific use case.
