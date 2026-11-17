---
title: Learn SWE-2 Flash by Fixing a Report
source: Super Intelligence School
source_id: super-intelligence-school
source_url: https://sischool.substack.com/p/learn-swe-2-flash-by-fixing-a-report
author: Super Intelligence School
date_published: '2026-11-16'
date_captured: '2026-11-17'
ingest_method: feed
model: claude-sonnet-5
---

# Learn SWE-2 Flash by Fixing a Report

## Insights

- The demo illustrates a subtle statistical error: running the same spreadsheet comparison against different baselines (one experimental group vs. all remaining groups, labeled REST, versus that same group vs. a control group, CTRL) changes whether a result clears a significance threshold — the data is identical, only the question asked of it changes.
- This type of error is harder to catch than a technical failure (e.g., a missing software package), because it produces a clean, presentable result rather than an error message, so a colleague receiving the output has no obvious reason to suspect the underlying comparison was wrong.
- The exercise uses SWE-2 Flash (a faster, cheaper coding model newly available in Devin) to find and fix a flawed build report claiming an engineering team saved 120 seconds, when the actual saved time was 30 seconds — the discrepancy traced to a step that was never re-timed.
- A side-by-side terminal comparison of SWE-2 Flash (200 tokens/sec) versus the larger SWE-2 model (60 tokens/sec) is noted as simulated for the replay, and explicitly does not capture full real-world task time (file opening, installs, waiting on commands, result-checking).
- The underlying task posed to learners: use Flash to locate the missing measurement, correct the calculation, and verify the fix against three unseen tests to determine what time savings the data actually supports.

## Quote

> A missing Python package gives you an error and a reason to investigate. Choose the wrong comparison and you can get a table clean enough to send to a colleague.
