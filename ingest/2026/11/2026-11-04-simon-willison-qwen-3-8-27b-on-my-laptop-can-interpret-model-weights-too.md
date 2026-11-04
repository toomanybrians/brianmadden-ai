---
title: Qwen 3.8 27B on my laptop can interpret model weights, too
source: Simon Willison's Newsletter
source_id: simon-willison
source_url: https://simonw.substack.com/p/qwen-38-27b-on-my-laptop-can-interpret
author: Simon Willison
date_published: '2026-11-03'
date_captured: '2026-11-04'
ingest_method: feed
model: claude-sonnet-5
---

# Qwen 3.8 27B on my laptop can interpret model weights, too

## Insights

- A new paper ("Sparks of Weight-Space Programming") claims frontier models like GPT-6 Astra can read and even edit raw neural network weights without writing code — identifying what a network does and fixing performance issues via direct weight edits (e.g., raising a model's MATH-500 score from 7.9% to 48.1% by editing 0.016% of weights). Critics argue the paper conflates "no-tools weight reading" with "code-assisted model editing," overstating the no-tools capability.
- Smaller open-weight models (Qwen 3.8 27B, running locally) could also partially replicate the weight-interpretation trick, correctly identifying games (Breakout, Pong, Pac-Man) a neural network was trained to play purely from its weight values, with reasoning traces taking 45+ minutes and tens of thousands of tokens — suggesting this isn't an exotic frontier-only capability, though it still failed on a more obscure case (Freeway).
- The U.S. Census Bureau's biweekly business AI-adoption survey changed its core question wording in Dec 2025 from "AI in producing goods or services" to "AI in any business functions," making before/after comparisons invalid — and reported adoption among large (250+ employee) firms jumped from ~12% to ~40% over roughly a year under the new framing.
- As of an Executive Order (14434), the Census Bureau's survey instrument was updated starting Oct 19, 2026 to replace "Artificial Intelligence (AI)" with "Super Intelligence (SI)" in official government survey language, with examples like "SI-powered data analysis" and "virtual SI agents for customer service."
- GitHub's Octoverse 2026 report shows agentic engineering driving large infrastructure-level shifts: merged pull requests tripled to 220M/month, commits tripled to 7.38B/month, and new repo creation doubled to 30.3M/month within the year.
- A case study (Spawn, an AI-driven multiplayer game company) describes near-fully-autonomous software development: AI agents detect, triage, and ship fixes to production within an hour of bug reports with no human in the loop, treating "an hour without a ship" as a severe incident; the company reportedly spends 30x its payroll on AI tokens (~$3M/month).

## Quote

> The use of LLMs erodes trust in documentation, in software, and in the organizations which produce them.
