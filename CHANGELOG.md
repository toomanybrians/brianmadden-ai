# Changelog

This isn't every commit. Those are in `git log`, same as any repo. This is the short version: the headline moments in how brianmadden.ai actually got built, curated by hand and updated when something is genuinely a milestone, not on a schedule.

Two repos feed this timeline. Content, frameworks, and the pipeline that reads and writes them live in [brianmadden-ai](https://github.com/toomanybrians/brianmadden-ai), the repo this file lives in. The Cloudflare Worker that actually serves the MCP endpoint any AI connects to lives in a second repo, [brianmadden-ai-server](https://github.com/toomanybrians/brianmadden-ai-server). Milestones from both show up here, because "the brain" means both to anyone actually using it.

## August 9, 2026—Day Zero

Brian decides to rebuild the public brain from the ground up: flip the architecture so this repo becomes the base layer, not an export of something kept privately, organized into three tiers (quarantined raw material, canonical thinking, generated output), with a private Citrix-side overlay reading from it downstream and never the other way around. No code yet. Just the decision to build it.

## August 10—First build day

The three-tier structure gets scaffolded (`ingest/`, `outputs/`, `sources/`). `MAINTAINER.md` and `BUILD.md` get written so the next session doesn't have to start from scratch. The ingest skill goes from nothing to a first real batch the same day: 96 notes pulled from 55 sources, written in Brian's own words rather than reprinted.

## August 11—The brief writes itself

The briefing skill lands: the part of the pipeline that reads a whole day's ingest notes together, not one at a time, against Brian's actual frameworks and current thinking, and decides what's worth flagging. Same day, the first real post goes out on Substack end to end—generated, edited by Brian, pasted in by hand.

## August 15—The brain learns to orient itself

`/maintain` ships—a skill that syncs with GitHub, reads the operating rules and the last couple of days of the build journal, and reports back on real state before doing anything else. Every session since starts the same way, without re-explaining the project from a blank slate.

## August 19—Launch day

`v2` merges to `main`. `daily-pipeline.yml` goes live: ingest, brief, publish, and email, unattended, every weekday morning. Proven for real the same day with a manual trigger before it was trusted to run on its own.

## August 20—The domain goes live

`brianmadden.ai` and `mcp.brianmadden.ai` finish cutting over, confirmed with a real request rather than a cached check. The MCP endpoint any AI can connect to is now running in production, not just a local dev server.

## August 24—A second publication, at a slower clock speed

Weekly Wrap Up (launched as "Deeper Thinking," renamed by Brian two days later once it was actually live) starts running: a lower-frequency companion to the Daily Brief that steps back and looks at the week instead of the day.

## September 2—Brian uses his own brain for real, and the podcast comes home

A week after a Citrix ASEAN business webcast on knowledge factories and second brains, Brian owed the audience the leftover Q&A. Instead of writing up answers, he recorded himself doing the thing the webcast was actually about: opened a fresh, incognito Claude instance, connected it live to his own public second brain, on camera, and asked it the leftover questions one at a time. Nine exchanges, unedited. This is the one that actually landed for him—the first time the brain stopped being something that technically worked and became something he'd actually used himself, for real, and watched hold up. Partway through, still running on plain keyword search, he notes on camera that he should eventually switch the server over to a vector database—two days before that became true. [Watch the demo](https://www.youtube.com/watch?v=8XC3UJsfIFE) · [full narration + transcript](talks/2026-09-02-citrix-asean-webcast-followup-second-brain-demo.md)

Same day: Episode 5 of the Citrix AI Hotsheet becomes the first episode drafted natively inside the public brain instead of privately and mirrored over afterward—Brian's own call that a podcast that's public the moment it's recorded has no private-first step to justify.

## September 4—Vector database

`semantic_search` ships in the server repo: a Cloudflare Vectorize index over Brian's published canon, re-embedded on an hourly schedule. For the first time, an AI connecting to brianmadden.ai can ask a genuinely open-ended question in its own words, not just search for a phrase it already has to know, and get back the right passage, ranked by meaning rather than exact wording. The full story, including what actually went wrong along the way: [outputs/essays/2026-09-04-semantic-search.md](outputs/essays/2026-09-04-semantic-search.md).

---

*Curated by hand, headline milestones only. For the complete record, `git log` in either repo has every commit—[brianmadden-ai](https://github.com/toomanybrians/brianmadden-ai/commits/main) and [brianmadden-ai-server](https://github.com/toomanybrians/brianmadden-ai-server/commits/main).*
