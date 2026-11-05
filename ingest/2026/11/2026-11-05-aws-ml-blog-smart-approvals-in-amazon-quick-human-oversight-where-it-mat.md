---
title: 'Smart Approvals in Amazon Quick: Human oversight where it matters'
source: AWS Machine Learning Blog
source_id: aws-ml-blog
source_url: https://aws.amazon.com/blogs/machine-learning/smart-approvals-in-amazon-quick-human-oversight-where-it-matters/
author: Steve Vinsik
date_published: '2026-11-04'
date_captured: '2026-11-05'
ingest_method: feed
model: claude-sonnet-5
---

# Smart Approvals in Amazon Quick: Human oversight where it matters

## Insights

- Smart Approvals is a feature in Amazon Quick (AWS's AI agent product) that uses a separate "classifier" model to automatically approve routine agent actions that already fall within existing permission settings, rather than prompting a human every time — aimed at countering "approval fatigue," where repeated prompts cause human attention/adherence to decline.
- The system layers on top of existing permission controls (Custom Permissions, Quick Guardrails, connector action permissions) rather than replacing them — it only reviews actions already eligible under "ask each time" settings where no other control mandates human sign-off; denials and mandatory approvals remain enforced regardless.
- The classifier evaluates proposed actions against the user's original request and a bounded conversation context, including a knowledge graph of the user's working relationships (e.g., detecting if a recipient is a senior leader or outside the org), to catch actions that technically match a request but warrant review (external sends, access changes, deletions, payments).
- Each automatic approval is single-use and scoped to exact parameters reviewed — it cannot be reused if an agent later tries to expand scope (e.g., an email sent to additional unauthorized recipients found in a document).
- The design explicitly treats retrieved content as "information, not instructions" to harden against indirect prompt injection attacks where embedded text tries to redirect agent behavior.
- AWS frames this as an auditable governance feature: CloudTrail and CloudWatch Logs record permission events, chat context, and agent metadata, but the vendor explicitly cautions that logged "approval" events are not proof an action executed — actual confirmation requires checking destination systems.
- AWS's own rollout guidance recommends piloting with a limited team, defining success metrics (fewer prompts without weakening oversight on consequential actions) before expanding — positioning this as a cautious, evidence-based adoption process rather than a plug-and-play autonomy upgrade.

## Quote

> The measure of effective oversight isn't how often an agent asks for approval, but whether people retain control over consequential decisions.
