---
title: How skills and agents work in AWS Quick
source: AWS Machine Learning Blog
source_id: aws-ml-blog
source_url: https://aws.amazon.com/blogs/machine-learning/how-skills-and-agents-work-in-aws-quick/
author: Jed Lechner
date_published: '2026-11-10'
date_captured: '2026-11-10'
ingest_method: feed
model: claude-sonnet-5
---

# How skills and agents work in AWS Quick

## Insights

- AWS Quick's architecture separates three concepts: agents (configurable AI with instructions/connectors/knowledge sources), skills (reusable task instructions), and data (spaces, knowledge bases, datasets, dashboards) — agents load skills dynamically and ground answers in connected data.
- Skills follow Anthropic's open Agent Skills specification (SKILL.md files with frontmatter), not an AWS-proprietary format — a folder with name/description metadata plus optional scripts, loaded via "progressive disclosure" (agent sees only name/description until a request triggers full instruction loading).
- Agents run in a managed "harness" using the ReAct (reasoning and acting) loop, and the post notes other agent frameworks like Strands Agents SDK use the same model-driven loop pattern — suggesting a convergence around this architecture across vendors.
- The piece frames skill-building explicitly as software engineering: recommends README documentation, failure-handling instructions (what the agent should do if an email send fails, etc.), versioned release notes, checksums for drift detection, input parameterization instead of hardcoded values, and structural "linting" after changes.
- A key governance/access gotcha: agents run with the access permissions of whoever is using them, so a shared agent can return inconsistent or incomplete results depending on each user's own data/connector permissions — sharing an agent doesn't share the underlying data access.
- AWS Quick ships a pre-built "Skill Architect" skill that automates applying these engineering best practices, and an "official catalog" of vetted (tested/scanned) skills spanning sales, HR, legal, engineering, and vertical industries like healthcare and finance.
- Product timeline noted: AWS Quick desktop launched in preview April 2026, went GA September 2026.

## Quote

> Skills are like code, and many engineering best practices can help any knowledge worker build them.
