---
title: Proof-based general-purpose computing with Magnetar
source: Microsoft Research Blog
source_id: microsoft-research-blog
source_url: https://www.microsoft.com/en-us/research/blog/proof-based-general-purpose-computing-with-magnetar/
author: Srinath Setty
date_published: '2026-10-15'
date_captured: '2026-10-16'
ingest_method: feed
model: claude-sonnet-5
---

# Proof-based general-purpose computing with Magnetar

## Insights

- Zero-knowledge proofs let a program's execution be verified via a short, fast-to-check cryptographic proof rather than through trust in the operator, vendor, or counterparty — shifting correctness from "who ran it" to "what accompanies the result."
- Magnetar is a new zkVM (zero-knowledge virtual machine) from Microsoft Research that proves execution of RISC-V programs written in ordinary Rust, Go, or C, removing the need for developers to hand-build cryptographic circuits.
- It claims 10–39x speedup over the fastest comparable prior systems (up to 300x on some benchmarks), proving millions of processor instructions per second on a laptop, with proof verification around 12 milliseconds.
- Its security relies solely on standard hash functions (e.g., SHA-256/SHA-3) rather than elliptic curves, lattices, or novel unproven cryptographic assumptions — intended to hold up against future quantum computing and avoid a future "cryptographic migration."
- Stated use cases include AI agents attaching proofs that their actions complied with given policy, and regulated financial institutions proving correct transaction processing without disclosing transaction data.
- Framed as the culmination of over a decade of Microsoft Research work (Spartan, Phalanx, Nova family, Brakedown, Jolt, BinarySpartan, etc.), each solving one piece of a three-part problem: proving speed, general-purpose usability, and long-term-trustworthy cryptography.

## Quote

> We expect that technology leaders will stop asking whether proofs of execution are practical and focus instead on which results would they prefer to verify rather than taking on trust.
