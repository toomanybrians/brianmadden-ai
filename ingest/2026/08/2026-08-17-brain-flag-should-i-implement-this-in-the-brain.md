---
title: should I implement this in the brain?
source: emergingai.substack.com
source_id: brain-flag
source_url: https://emergingai.substack.com/p/graph-engineering-the-next-step-after
author: Brian Madden (flagged)
date_published: '2026-08-15'
date_captured: '2026-08-17'
ingest_method: brain-flag
model: claude-sonnet-5
---

# should I implement this in the brain?

## Insights

- Proposes a three-stage progression in AI agent design: prompt engineering (telling a model what to do), loop engineering (keeping one agent working via goal-act-test-repeat cycles), and now "graph engineering" (coordinating multiple agents/processes across a whole operation).
- Argues loops solve single-task persistence but break down once work involves multiple sub-goals (e.g., a launch needing research, copy, code, legal review, approval) — a human still has to manually connect the separate loops, decide sequencing, and judge trustworthiness of outputs.
- Describes a practical three-agent pattern for serious tasks: a "worker" (does the task), an "invigilator" (independently critiques the output for weak reasoning, missing evidence, fake completion), and an "evaluator" (judges whether both worker and invigilator did their jobs and whether the result is ready).
- Defines graph engineering structurally: nodes (agents, scripts, APIs, tests, human review) do work; edges carry data/dependencies/permissions/failure routes; state persists across the process; gates control continuation; cycles allow failed work to loop back without full restart; terminal states mark done/rejected/expired/needs-human.
- References Anthropic's "evaluator-optimizer" pattern (one model generates, another evaluates/corrects) as the established shape underlying the loop stage, which graph engineering is positioned to extend.
- Piece originates from a question posed by Peter Steinberger (July 17) that reportedly spread because builders recognized the coordination gap between multiple working agent loops.

## Quote

> A prompt produces an answer. A loop pursues a pass condition. A graph runs the operation.
