---
title: 🔥 Cursor Just Made GitHub Optional
source: brain@ inbox (curated newsletters)
source_id: brain-inbox
source_url: https://link.mail.beehiiv.com/v2/c/188d4c01dcf382c68ea4bd596c2f6b56c382295fdf66be940c8dfadbace4db2b4c615837b62b90a1271a1996530535acbe0ca7e7ffb63cf49823f146322e43220decf58c76ffa9c3804ff743d41e901afcbc49c85378b602deb9c9ff40192a36f478d57a2a464cabf3961b00b01085900e7d75562f67b9bf7d32d9295c6f11327c6b5c635e61a9b941e2ba6a1dff8a8f31bd15f38011a21c75723005e8452442/591c4edc0c266c6f
author: Superintelligence <superintel@mail.beehiiv.com>
date_published: '2026-08-18'
date_captured: '2026-08-19'
ingest_method: email
model: claude-sonnet-5
---

# 🔥 Cursor Just Made GitHub Optional

## Insights

- Cursor launched "Origin," its own native code hosting platform (repos, PRs, agents in one place), directly competing with GitHub rather than just integrating with it — a shift from AI coding assistant as guest to platform as owner of the codebase itself.
- The underlying logic: as more code in a repo comes from agents rather than humans, the repository stops being a place people "visit" and becomes the runtime environment the agent operates in — whoever hosts that runtime controls what agents are permitted to do within it.
- Practical mechanics: agents working against external forges (like GitHub) waste cycles on auth, cloning, polling, and translating between systems; collapsing hosting into the same platform as the agent removes that overhead.
- Origin syncs bidirectionally with existing GitHub repos and integrates CI/deployment tooling (Vercel, Depot, Buildkite) directly into the platform, but lacks enterprise-grade features so far (issue tracking, org-wide permissions, compliance attestations) and is still an early beta.
- Risk flagged: companies are being asked to move their most sensitive asset (source code) onto a vendor's infrastructure, with two-way GitHub sync potentially narrowing over time — a classic lock-in concern.
- Broader newsletter framing (context, not primary story): major AI companies are simultaneously outgrowing shared infrastructure they don't control — Cursor vs. GitHub, OpenAI signing a 20-year, ~8GW compute lease on a former uranium site, Anthropic hitting a $65B run rate ahead of a possible IPO — each trading a dependency for something it owns outright.

## Quote

> "Your code, PRs, and agents are now in the same place." — Cursor, on Origin
