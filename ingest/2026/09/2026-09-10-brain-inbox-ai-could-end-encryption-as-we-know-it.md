---
title: AI Could End Encryption as We Know It
source: brain@ inbox (curated newsletters)
source_id: brain-inbox
source_url: https://aifrontiersmedia.substack.com/p/ai-could-end-encryption-as-we-know
author: AI Frontiers <aifrontiersmedia@substack.com>
date_published: '2026-09-09'
date_captured: '2026-09-10'
ingest_method: email
model: claude-sonnet-5
---

# AI Could End Encryption as We Know It

## Insights

- AI models are increasingly solving previously intractable math problems (Jacobian conjecture, Navier-Stokes) and have begun succeeding at cryptanalysis specifically — Anthropic's Claude Mythos Preview found new attacks against two cryptographic algorithms, including one under NIST evaluation for post-quantum standardization.
- The core risk isn't AI breaking one algorithm but AI potentially proving that *all* public-key encryption is fundamentally breakable — a mathematical possibility per complexity theorist Russell Impagliazzo's "five worlds" framework (we may live in "Minicrypt" rather than "Cryptomania," meaning public-key encryption may not really be secure at all).
- AI may excel at cryptanalysis for the same structural reason it excels at math/coding: solutions are easy to verify (attack succeeds or fails), which is ideal for reinforcement learning; labs can also generate custom-difficulty weakened ciphers to train progressively stronger AI cryptanalysts.
- Even without a fundamental mathematical breakthrough, AI could generate enough incremental algorithm-specific breaks (as seen with SIKE and McEliece) to functionally end public-key encryption's usefulness, since replacing broken standards historically takes 10-20 years.
- If public-key encryption is broken, practical consequences include the end of true end-to-end encryption, a return to something like the 1990s Clipper chip model (trusted intermediaries who can decrypt communications), and new leverage points for government surveillance, deplatforming, and identity verification.
- Historically, intelligence agencies that discover an algorithm is broken keep this secret rather than disclosing it — meaning a frontier AI lab making this discovery could be compelled to withhold it from the public.
- Proposed mitigation: build "Minicrypt-ready" infrastructure now (standardized key-distribution protocols, split trust across multiple independent intermediaries via secret-sharing) so society isn't caught unprepared if/when public-key encryption fails.

## Quote

> Public-key cryptography is all number theory, and potentially vulnerable to more mathematically inclined aliens. — Bruce Schneier
