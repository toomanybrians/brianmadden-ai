---
title: 💸 Claude Code cuts subagent costs 99%, 6% more prompts
source: brain@ inbox (curated newsletters)
source_id: brain-inbox
source_url: https://app.alphasignal.ai/c?uid=1Aj1bhaMRbIkU3CpB&amp;cid=12a32fd5eeb939c4&amp;lid=h7zp4D58907KKN9A&amp;mid=6e596da1-c2cd-49ab-bfc1-af6396fb3954
author: AlphaSignal <news@alphasignal.ai>
date_published: '2026-11-05'
date_captured: '2026-11-06'
ingest_method: email
model: claude-sonnet-5
---

# 💸 Claude Code cuts subagent costs 99%, 6% more prompts

## Insights

- Anthropic's Claude Code (v2.1.316) cut background subagent token costs by 99% by having a smaller model (Haiku 5.5) generate status updates from short notes instead of re-reading the full conversation history every 30 seconds.
- The fix is architectural/operational rather than a new capability — it addresses a cost inefficiency that scaled with session length (the longer the multi-agent session, the worse the waste).
- Practical effect for users: roughly 5% less usage-limit consumption and about 6% more prompts available before hitting plan limits, with no configuration changes required.
- OpenAI shipped ChatGPT Images 2.6 the same day, emphasizing speed (6-second generation via a "Flare" API model) and reusable reference images for consistent characters/products across generations — also framed around efficiency (50% faster overall).
- Moonshot AI released open-weight Kimi K3.1 Pro (2.8T parameters, 1M token context, MoE architecture), positioned as capable of full-project coding and reduced hallucination in finance tasks, ranked #1 among open-weight models on Agent Arena.
- The newsletter frames the day's releases as a shift in competitive focus among AI labs from raw capability toward "cost per useful output."

## Quote

> We're past the era of raw capability. The race is now about cost per useful output.
