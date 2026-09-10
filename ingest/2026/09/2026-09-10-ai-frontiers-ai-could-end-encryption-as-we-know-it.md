---
title: AI Could End Encryption as We Know It
source: AI Frontiers
source_id: ai-frontiers
source_url: https://newsletter.ai-frontiers.org/p/ai-could-end-encryption-as-we-know
author: AI Frontiers
date_published: '2026-09-09'
date_captured: '2026-09-10'
ingest_method: feed
model: claude-sonnet-5
---

# AI Could End Encryption as We Know It

## Insights

- Frontier AI models are increasingly solving major open math problems (Jacobian conjecture in 3D, Navier-Stokes) and, more consequentially, finding new cryptanalytic attacks — including against a post-quantum algorithm under NIST evaluation and a near-50-year-old scheme (McEliece) that had survived all prior attacks.
- Public-key encryption's security has never been mathematically proven — it rests on the unverified assumption that certain operations are hard to reverse. Unlike symmetric encryption/one-way functions (many diverse hard-to-invert options), public-key crypto relies on only a few structured mathematical problems, making it a narrower and more fragile target.
- The author argues AI may be particularly suited to cryptanalysis because attacks are easily verifiable (key recovery succeeds or fails), which is exactly the clean reward signal RL training needs — plus AI can grind through exhaustive "schlep work" at a scale the small (~thousands) global cryptography research community cannot match.
- If public-key encryption collapses, the world reverts to "Minicrypt": symmetric encryption, signatures, and hashes still work, but true end-to-end encryption between strangers becomes impossible without a pre-shared channel — requiring trusted intermediaries (analogous to SIM cards/Clipper chip) that could decrypt traffic and become surveillance/deplatforming chokepoints.
- Historically, governments and intelligence agencies have kept discovered cryptographic breaks secret rather than disclosing them (harvest-now-decrypt-later precedent from quantum computing), raising the possibility that an AI lab could privately break public-key crypto without public knowledge.
- Proposed mitigation: proactively build "Minicrypt-ready" infrastructure now (standardized key-distribution protocols, multi-jurisdictional trusted intermediaries requiring threshold cooperation, e.g. 3-of-5 providers) so society isn't caught unprepared if/when AI-assisted math breaks current encryption assumptions.

## Quote

> Public-key cryptography is all number theory, and potentially vulnerable to more mathematically inclined aliens.
