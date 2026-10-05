---
title: Sweep thousands of leases for compliance using Amazon Quick and the Adjudicated
  Query pattern
source: AWS Machine Learning Blog
source_id: aws-ml-blog
source_url: https://aws.amazon.com/blogs/machine-learning/sweep-thousands-of-leases-for-compliance-using-amazon-quick-and-the-adjudicated-query-pattern/
author: Anand Komandooru
date_published: '2026-10-02'
date_captured: '2026-10-05'
ingest_method: feed
model: claude-sonnet-5
---

# Sweep thousands of leases for compliance using Amazon Quick and the Adjudicated Query pattern

## Insights

- The "Adjudicated Query" pattern deliberately keeps AI models out of decision-making: an LLM only translates natural-language questions into calls on a fixed set of typed operations and narrates results, while a deterministic (non-AI) rules engine performs the actual pass/fail determinations.
- The pattern is positioned as a response to specific failure modes of RAG and text-to-SQL in high-stakes compliance work: similarity search can't prove it covered "all" records, and model-generated SQL queries carry a risk of silently narrowing the population while still looking exact.
- A "completeness receipt" (compliant + in-breach + ambiguous + unreadable = total scanned) is asserted computationally before any sweep result persists, intended to prevent records from being silently dropped from compliance checks.
- The architecture explicitly treats the summarization/narration model as "an untrusted renderer" — the vendor reports real observed failures (a model stripping a caveat label and presenting an invented citation as statute; a model extrapolating a population-wide range from a 20-row sample) and layers redundant, paraphrase-resistant safeguards to mitigate them.
- The vendor frames this as a general pattern applicable beyond lease compliance — sanctions screening, insurance claims adjudication, export control, clinical trial monitoring — wherever records are enumerable, rules are externally owned, and a missed record constitutes real liability.
- The post is explicit about the pattern's limits: it's inappropriate when rules require genuine subjective judgment (forcing them into deterministic logic "hides the subjectivity"), when completeness isn't actually needed, or when the record population itself is ill-defined.

## Quote

> A model stripped a caveat prefix... and the model presented an invented citation as statute.
