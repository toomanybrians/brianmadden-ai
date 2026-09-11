---
title: What is So Hard About Behind-The-Meter Power For Datacenters? Part 1
source: SemiAnalysis
source_id: semianalysis
source_url: https://newsletter.semianalysis.com/p/what-is-so-hard-about-behind-the
author: Ellie Holbrook
date_published: '2026-09-10'
date_captured: '2026-09-11'
ingest_method: feed
model: claude-sonnet-5
---

# What is So Hard About Behind-The-Meter Power For Datacenters? Part 1

## Insights

- SemiAnalysis tracks 75GW of firm, binding behind-the-meter (BTM) power orders for AI datacenters, with ~20GW ordered in Q2 2026 alone — up from what was seen as a fringe/"science experiment" approach (originally an Elon Musk/xAI tactic) to now standard practice across all major AI labs and hyperscalers.
- The economics driving this: a 1GW power plant costs ~$5B, but inference API revenue can reach $100B/GW/year at 90%+ margins — meaning labs can pay back a power plant's cost in ~20 days of revenue, making speed of power deployment far more valuable than cost efficiency.
- Major named deployments: Microsoft (5GW+ BTM in 2026 YTD), Google (930MW off-grid turbines + 900MW Bloom fuel cells in Wyoming), Anthropic/Meta (deals with Enchanted Rock; Anthropic's Texas campus backstopped by Google), and OpenAI (1.4GW Texas site + 1.3GW New Mexico site, part of $150B+ Oracle contracts).
- Six real-world bottlenecks stand between an equipment order and an operating plant: contract/financing (bankability), permitting (can take a year+, varies drastically by state/jurisdiction), fuel/gas supply and pipeline buildout, equipment procurement (turbines sold out past 2030, driving a recip-engine boom and a secondary turbine market with 16-46% price premiums), skilled labor shortages (projected 288,000-worker gap by 2027), and the physics of running an "island" grid (inertia, fault current, load fluctuation issues) without benefit of the main grid.
- A new category of "BTM utility" / Energy-as-a-Service vendors (e.g., VoltaGrid, Williams, Solaris, Bloom Energy) has emerged to solve the chicken-and-egg financing problem by selling guaranteed power delivery rather than just equipment, resembling utility-like long-term contracts.
- Real execution cracks are visible: permitting fights forced Oracle's Project Jupiter and Nebius NJ to pivot from turbines to Bloom fuel cells; pipeline delays hit Jupiter's gas supply; reliability/uptime issues and labor shortages are increasingly reported; some developers are overbuilding permitted capacity as a hedge against gas contracts not yet secured.

## Quote

> Anthropic and its peers can pay back the value of a power plant in 20 days of inference revenue.
