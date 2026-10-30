---
title: Build a repeatable PHP-to-Java migration engine with Kiro
source: AWS Machine Learning Blog
source_id: aws-ml-blog
source_url: https://aws.amazon.com/blogs/machine-learning/build-a-repeatable-php-to-java-migration-engine-with-kiro/
author: Sarat Guttikonda
date_published: '2026-10-29'
date_captured: '2026-10-30'
ingest_method: feed
model: claude-sonnet-5
---

# Build a repeatable PHP-to-Java migration engine with Kiro

## Insights

- AWS positions "Kiro" (an AI IDE/agent) and "AWS Transform" (an agentic migration service) as two execution modes for the same codified methodology, stored as versioned Markdown "skill files" rather than locked into one tool — framing migration knowledge as a portable, reusable asset rather than tribal/tacit knowledge.
- The core methodology insight is process discipline over raw code generation: a mechanical discovery scanner must inventory the legacy system before any translation happens, and ambiguous cases are explicitly flagged for human review rather than guessed at by the AI.
- A "parity harness" (automated testing legacy vs. new output) is built *before* any new code is written and must be proven to catch deliberately injected bugs — the AI-generated port isn't considered correct until this referee validates behavioral equivalence, not just structural similarity.
- The stated failure-correction principle is "fix the loop, not the code" — when the AI makes a systemic error across files, the human updates the rulebook/prompts and regenerates, rather than hand-patching individual outputs, aiming for compounding improvement across future migrations.
- The provided demo example is partial and self-admittedly incomplete (only 4 of 37 models migrated, and the critical parity harness was never actually built for the walkthrough) — a notable gap in a post whose thesis is built around rigor/verification.
- Framed as generalizable beyond PHP/Java: the vendor suggests the same "old system as specification, scanner + harness + rulebook" pattern applies to other legacy-to-modern migrations.

## Quote

> Don't read, guess at, or hand-translate a model or entity file until the scanner has run.
