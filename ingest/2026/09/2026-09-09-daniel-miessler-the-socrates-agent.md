---
title: The Socrates Agent
source: Daniel Miessler
source_id: daniel-miessler
source_url: https://danielmiessler.com/blog/the-socrates-agent?utm_source=rss&utm_medium=feed&utm_campaign=website
author: daniel@danielmiessler.com (Daniel Miessler)
date_published: '2026-09-08'
date_captured: '2026-09-09'
ingest_method: feed
model: claude-sonnet-5
---

# The Socrates Agent

## Insights

- Miessler released a full AI agent system prompt ("Socrates") designed to tutor by only asking questions, never supplying answers, deliverables, fact-lookups, or confirmations — built as a hard-constrained Claude Code subagent (disallowed tools include Edit, Write, Bash, WebSearch, WebFetch).
- The design explicitly closes workaround loopholes (e.g. "just show me yours to compare," narrowing an answer to a range, confirming one digit of a multi-choice answer) — all are treated as functionally equivalent to giving the answer.
- Underlying motivation: a fear that AI's answer-giving fluency is causing both kids and adults to silently lose the capacity to sit with hard questions — framed as "skipping a rep," with the risk being invisible because no one notices a skipped rep.
- Frames this as an extension of an earlier "Job vs. Gym" distinction — tasks you want done (job) vs. tasks you want to personally develop through doing (gym) — arguing AI should be kept out of the gym category.
- Argues the strategic stakes rise as average AI capability increases: the value of retained personal thinking ability grows, so people who keep practicing hard thinking will separate from those who outsource it — for both a ten-year-old and an adult.
- Practical distribution: single markdown file, install via curl into Claude Code, but portable to any system-prompt-taking tool (ChatGPT project, Gemini gem), positioned as directly handoff-able to a student or to oneself.

## Quote

> "The better AI gets at average, the more your own thinking is worth."
