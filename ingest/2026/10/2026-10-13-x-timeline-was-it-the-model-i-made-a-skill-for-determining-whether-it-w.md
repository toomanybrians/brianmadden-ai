---
title: 'Was It the Model?


  I made a skill for determining whether it was your prompting'
source: X (brianmaddenai home timeline)
source_id: x-timeline
source_url: https://x.com/DanielMiessler/status/2109865473152274631
author: '@DanielMiessler'
date_published: '2026-10-13'
date_captured: '2026-10-13'
ingest_method: x
model: claude-sonnet-5
---

# Was It the Model?

I made a skill for determining whether it was your prompting

## Insights

- The skill is built to answer a specific, recurring ambiguity in AI-assisted coding: when something goes wrong, was it the model underperforming, or the user's prompting/harness setup?
- It requires two independent, time-overlapping signals (e.g., provider status incident + API error spike) before attributing blame to either side; otherwise it reports "unclear" rather than guessing.
- An earlier version of the tool was wrong in a telling way: it used a loose 48-hour coincidence window and concluded "mostly the model," but stricter time-alignment found that none of 145 frustration episodes since mid-July could actually be pinned on the model.
- The tool has to filter out false signals of "frustration," including automated/headless job runs misread as user frustration, and Codex's own system-generated summary text that gets mistakenly tagged as user messages (694 of 738 flagged instances in one case were this artifact).
- It also normalizes for noise in harness changes (config files churn almost daily, so only unusually large changes count) and filters provider status incidents to only those relevant to the specific model/product actually in use.
- Reflects an emerging practice: builders creating dedicated diagnostic/meta-tooling to audit AI agent reliability and attribute failures correctly, rather than relying on gut feeling about "the model being bad today."

## Quote

> Day-level coincidence is not evidence.
