---
title: Capabilities research expands the safety-usefulness Pareto frontier too
source: Redwood Research blog
source_id: redwood-research
source_url: https://blog.redwoodresearch.org/p/capabilities-research-expands-the
author: Alex Mallen
date_published: '2026-10-02'
date_captured: '2026-10-05'
ingest_method: feed
model: claude-sonnet-5
---

# Capabilities research expands the safety-usefulness Pareto frontier too

## Insights

- Argues that defining "safety research" as anything that lets developers deploy more safely without sacrificing usefulness is flawed, because nearly all capabilities research technically qualifies under that definition (e.g., inference optimization lets weaker/safer models be used more, which counts as "safer").
- Proposes a more useful model: safety research expands the safety-usefulness frontier mainly rightward (new safety options, little new usefulness), while capabilities research expands it upward-and-left (new usefulness, at safety's expense) — and developers choose a point on that frontier, they don't automatically take the safer option.
- Key mechanism: technological improvements can change developers' incentives such that they choose to sacrifice more safety for usefulness gains — the existence of an option for more safety doesn't mean it will be chosen, especially under competitive/race pressure.
- Gives concrete examples: building more RLVR training environments mostly just makes more capable/dangerous models possible (minor safety upside via better filtering); faster inference lets developers use weaker, more controllable models with more compute instead of one stronger less-aligned model, a more substantial safety gain; pretraining-heavy (vs. RL-heavy) approaches may reward-hack and misalign less at a given capability level.
- Identifies a specific future scenario where capabilities research becomes genuinely safety-positive: once a developer has "fully automated AI R&D" and is robustly committed to not pushing usefulness further (e.g., deliberately "burning their lead"), further capabilities gains free up resources to redirect toward safety rather than being used to push riskier deployment.
- Explicitly cautions that none of this currently applies — frontier developers are in active competitive races with no credible commitment to slow down, so doing capabilities research at a frontier AI company today is "probably bad," and raises countervailing risks like capability overhangs if safety-paced research is later stolen or exploited by a rival project.

## Quote

> AI safety research should actually enable improved safety without much sacrifice from the developers after taking into account all new options created on the Pareto frontier.
