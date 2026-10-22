---
title: Solving a 31-year-old grand challenge in mathematics – the KLS conjecture
source: Microsoft Research Blog
source_id: microsoft-research-blog
source_url: https://www.microsoft.com/en-us/research/blog/solving-a-31-year-old-grand-challenge-in-mathematics-the-kls-conjecture/
author: Xinzhi Zhang
date_published: '2026-10-21'
date_captured: '2026-10-22'
ingest_method: feed
model: claude-sonnet-5
---

# Solving a 31-year-old grand challenge in mathematics – the KLS conjecture

## Insights

- The proof came from a human-directed "agentic search" process: multiple AI agents explored variations of an idea in parallel, researchers inspected intermediate results, pruned unpromising directions, and fed the best ones into the next round — roughly 100 research trajectories were explored before the key breakthrough.
- A controlled comparison was built into the project: a separate track gave several leading AI models the same total token budget to attempt the problem unguided (without human pruning/direction), and that approach failed to reach the result — suggesting the human judgment layer, not just raw AI capability, was decisive.
- AI's role was specifically in exploring candidate approaches, carrying out detailed derivations, drafting the manuscript, and performing internal proof checks — while humans set mathematical direction, selected ideas, assembled the final argument, and verified it.
- The result was independently corroborated fast: another research group posted a full independent proof the same day (building directly on the first version of this paper), a third unrelated proof appeared the same day via a related idea, and a formal Lean 4 verification followed shortly after.
- Framed explicitly as a case study in a particular mode of human-AI collaboration — not "ask AI to solve it end-to-end," but iterative human-guided pruning across many parallel AI-generated attempts.

## Quote

> Human-AI guidance... demonstrates the power of having researchers direct AI rather than simply asking AI to solve a complex problem through a single end-to-end run.
