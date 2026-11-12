---
title: Semantic diffing of formal policies with anti-unification
source: AWS Machine Learning Blog
source_id: aws-ml-blog
source_url: https://aws.amazon.com/blogs/machine-learning/semantic-diffing-of-formal-policies-with-anti-unification/
author: Ferhat Erata
date_published: '2026-11-11'
date_captured: '2026-11-12'
ingest_method: feed
model: claude-sonnet-5
---

# Semantic diffing of formal policies with anti-unification

## Insights

- The engine addresses a specific LLM reliability problem: when an LLM (autoformalization) translates natural-language requirements into formal policy languages (SMT-LIB, Cedar, Dogwood, OpenShell YAML, CEL), repeated runs can produce different, non-verifiable outputs with no ground truth — semantic diffing shows where candidates agree/disagree rather than scoring a single correctness number.
- Uses anti-unification (an older formal-methods technique, Plotkin 1970) over e-graphs to compute a "most specific common pattern" between two formal expressions, producing a merged term where shared structure appears once and genuine disagreements are isolated in explicit "Variants" nodes.
- Explicitly distinguishes syntactic noise (reordering, equivalent predicates) from actual semantic/behavioral differences (e.g., an "Or" where a policy requires "and") — in a worked AWS S3-replication policy example, 18 of 28 lines showed as changed in a plain text diff, but after algebraic normalization only 2 of 5 differences were real bugs.
- Positioned as a complement, not a replacement, for other verification methods: it doesn't validate schemas, run SMT solvers, or replay policies against event logs itself — those are separate steps used to resolve the flagged disagreements (e.g., Dogwood schema validation caught an invalid field reference).
- Frames this as a formal-methods analogue to "semantic entropy" (Farquhar et al., Nature 2024) for natural-language LLM outputs, but argues it's more informative because it preserves the actual structural disagreement rather than collapsing to a single consistency score.
- Includes caveats about system maturity: core e-graph persistence is formally verified (via Verus), but the full anti-unification solver lacks an end-to-end proof, and generated "justifications" aren't yet independently replay-checked as certificates — framed transparently in the project's own claims inventory.
- Proposes a concrete pipeline use case: generate many LLM candidate policy formalizations, cluster equivalent ones, diff cluster representatives, and route only the small number of recurring real disagreements to human review, SMT solving, or replay — intended to reduce reviewer workload rather than fully automate policy correctness.

## Quote

> A real change in behavior, such as an Or where the requirement says and, can get lost in that noise.
