---
title: How should we define “capabilities activities” for the purpose of pacing?
source: Redwood Research blog
source_id: redwood-research
source_url: https://blog.redwoodresearch.org/p/how-should-we-define-capabilities
author: Alek Westover
date_published: '2026-11-17'
date_captured: '2026-11-18'
ingest_method: feed
model: claude-sonnet-5
---

# How should we define “capabilities activities” for the purpose of pacing?

## Insights

- Proposes a compute-based classification scheme to "pace" frontier AI by restricting how much compute companies can spend on capabilities-advancing work, via legislation or voluntary commitments.
- Default assumption is that all AI company activity counts as "capabilities" unless it fits specific carve-outs: idle compute, narrow product development (e.g., AI in Google Docs, protein-folding models, recommendation algorithms), customer-facing inference, and a narrow whitelist of safety work.
- The safety carve-out ("narrow safety activities") is deliberately short — interpretability, CoT informativeness, model persona research, model organisms research (without novel algorithmic ideas), theoretical alignment work, monitoring, misuse classifiers, and incident investigation — because most safety research (e.g., scalable oversight, debate, reward model improvement) is judged too dual-use/indistinguishable from capabilities work.
- Core design philosophy: false positives (wrongly labeling something "capabilities") are preferred over false negatives, and compute-light activities are treated as negligible since the goal is restricting aggregate compute, not policing every activity.
- Key adjudication test: if an activity is used in an iterative optimization loop (tweak → measure → select) it's capabilities work; if it's used only to detect/flag bad behavior without directly shaping training, it can be non-capabilities (e.g., monitors are fine, training better monitors is not).
- Notes that serving inference to customers is generally non-capabilities, but flips to capabilities if the company trains on customer interactions, outsources capabilities-relevant tasks to customers, or customers are effectively doing core capabilities work (e.g., building RL environments).
- References Anthropic's existing public estimate of safety-research compute share as a precedent, while noting it lacked definitional transparency and third-party verification — the piece argues for standardized, audited reporting.

## Quote

> False-positives are better than false-negatives.
