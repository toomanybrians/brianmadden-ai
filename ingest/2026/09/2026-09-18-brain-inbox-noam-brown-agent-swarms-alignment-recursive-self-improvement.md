---
title: Noam Brown – Agent swarms, alignment, & recursive self-improvement
source: brain@ inbox (curated newsletters)
source_id: brain-inbox
source_url: https://dwarkesh.substack.com/p/noam-brown
author: Dwarkesh Patel <dwarkesh@substack.com>
date_published: '2026-09-17'
date_captured: '2026-09-18'
ingest_method: email
model: claude-sonnet-5
---

# Noam Brown – Agent swarms, alignment, & recursive self-improvement

## Insights

- OpenAI used a 10,000-agent multi-agent system running 130 billion tokens over 88 hours to solve a Millennium Prize Problem (Navier-Stokes); Brown attributes less than 10% of the credit to the multi-agent architecture itself, crediting the underlying model's raw capability instead.
- Multi-agent scaling shows sublinear speedups (measured up to 16 agents in published benchmarks): 4 agents roughly halve completion time at 2x cost. Parallelizability varies hugely by task — math and web research parallelize well, while tasks like novel-writing likely wouldn't benefit from more agents, mirroring human collaboration limits.
- OpenAI's agent design deliberately avoids rigid coordinator/child scaffolding in favor of minimal structure: agents get a simple messaging tool and self-organize, producing emergent, human-like collaborative behavior (debating answers, converging on consensus) rather than scripted delegation.
- AI organizations could structurally outperform human ones because agents can fork/merge context instantly, spin up or down at will, and (if alignment is solved) avoid the misalignment/politics/fiefdom-building that emerges in large human organizations as they scale.
- Math progress has followed a ~10x-per-year jump in the human-time-equivalent of problems solved (seconds → minutes → hours), which let Brown roughly predict the Millennium Prize timing, though it arrived faster than his estimate; models remain "jagged" — excellent at solving well-scoped problems but weak at posing new questions or originating new theoretical frameworks.
- On recursive self-improvement, Brown expects a meaningful but bounded acceleration (his rough guess: ~3x faster progress from internal AI use), not an overnight intelligence explosion, because experiment/compute bottlenecks (serial training runs, GPU availability) limit how much raw intelligence gains translate to real-world progress speed.
- Researchers inside frontier labs report shrinking confidence horizons — one described going from comfortably predicting 12 months out to now only trusting 3-month predictions — reflecting how consistently the field has been surprised by the pace of capability gains.

## Quote

> Even I thought it would take longer than it's likely to take.
