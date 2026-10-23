---
title: What will computer chips look like in 2045?
source: Dwarkesh
source_id: dwarkesh
source_url: https://www.dwarkesh.com/p/intel-tour
author: Dwarkesh Patel
date_published: '2026-10-22'
date_captured: '2026-10-23'
ingest_method: feed
model: claude-sonnet-5
content_basis: transcript
---

# What will computer chips look like in 2045?

## Fit with Brian's work

**Fit: partial.** Most of the episode is transistor physics and fab engineering with no bearing on Brian's work, but the closing stretch on AI compute demand outstripping chip-manufacturing supply is hard evidence for his developing "compute scarcity and token governance" thread and the "control your own destiny" compute-availability argument.

- Directly extends **compute scarcity and token governance**: Intel's CTO states AI compute demand has grown 3x/year for a decade, but even with unlimited capital, existing global tool stock could only ~2x leading-edge wafer output — a hard physical ceiling Brian's thread has so far argued mostly from token-pricing and lab-behavior evidence.
- Confirms the **compute-availability / "control your own destiny" note**: Elon Musk's decision to build his own fab (Terrafab) because guaranteed supply through another foundry wasn't reliable enough is a real-world instance of the exact "reserved capacity beats pay-as-you-go" lesson Brian drew from cloud computing.
- New evidence for the **bubble-pop / planning-floor thinking**: the CTO's admission that tool lead times (~18 months) plus new fab construction push any meaningful capacity increase to "end of the decade," regardless of capital deployed now — a concrete timeline constraint Brian's bubble-pop and compute-scarcity notes currently lack.
- Adds a economic data point worth filing under token/compute economics: roughly $2B of Intel capex is described as enabling chips that generate ~$100B of AI-company revenue — extreme leverage that explains why labs are described as moving to "buy everything," reinforcing Brian's view that compute remains the structural bottleneck underneath enterprise AI strategy.

## Insights

- Intel's CTO (Pushkar Arande, spelling unverified) states AI compute demand has grown roughly 3x per year for a decade, but with today's global stock of chipmaking tools, leading-edge wafer production could only be roughly doubled, not increased 10x.
- ASML produces fewer than 100 EUV lithography tools per year and has no plans to significantly exceed that by the end of the decade; this single supplier bottleneck is shared across Intel, TSMC, and memory makers like SK Hynix.
- Once a company locks into a process node (e.g., 18A), it is locked into a specific tool from a specific supplier — there's no substitute tool, which removes flexibility even where alternative equipment vendors exist.
- A high-NA EUV scanner system costs roughly $400 million; litho tool costs have been doubling roughly every four to five years, a trajectory the CTO says "doesn't make sense" if extrapolated.
- The CTO estimates that even a large investment order today for new tools (roughly 18-month lead time) plus new fab construction pushes meaningfully higher capacity to around 2028–2030 — production could rise faster next year than forecast, but end-of-decade output won't be dramatically higher than current projections unless the entire supply chain (tool suppliers and their sub-suppliers) scales up.
- Roughly $2 billion of Intel capex is estimated to produce enough leading-edge chip logic to generate about $100 billion in annual revenue for AI model companies — framed as evidence the industry could see AI labs "just buy everything" and guarantee future fab capacity.
- The CTO describes an industry shift from vertically integrated (decades ago) to horizontal (foundries, equipment makers, fabless designers) and now toward a "virtually vertically integrated" structure, where individual hyperscalers and model companies are large enough to consume an entire fab's output on their own and have the capital to fund it directly.
- Elon Musk is pursuing a fab partnership/project ("Terrafab") with Intel, reportedly because he concluded his own businesses' silicon demand was large enough that guaranteed access required building capacity himself rather than relying on another foundry's supply.
- Fab economics are described as having roughly 80% fixed costs, making capacity utilization and yield improvements disproportionately valuable — every extra percentage point of yield or utilization adds far more than linear revenue, which the CTO cites as a driver of industry consolidation.
- Memory supply (not just compute/logic) is described as facing an even larger supply crunch than leading-edge compute, according to the CTO.
- Fab inputs beyond tools — power, water, consumables, clean-room space — are also cited as scaling constraints, though some (unlike specialized tools) can in principle be built out faster.
- The CTO states plainly, in hindsight, "had we known what we know today, we would have invested more like a year ago," and says Intel is now investing more going forward given current demand signals.

## Not captured

The bulk of the transcript — gate-all-around transistor mechanics, backside power, CFET stacked transistors, ruthenium interconnects, hybrid bonding pitch scaling, Intel's 10nm/EUV delay history, and PDK/foundry-customer process details — is semiconductor engineering detail with no bearing on Brian's enterprise-AI or knowledge-work focus and was omitted.
