---
title: 'Talorys – A self-hosted personal AI agent on Cloudflare.


  https://t.co/93526lWSS'
source: X (brianmaddenai home timeline)
source_id: x-timeline
source_url: https://x.com/DanielMiessler/status/2108986793437831614
author: '@DanielMiessler'
date_published: '2026-10-10'
date_captured: '2026-10-12'
ingest_method: x
model: claude-sonnet-5
---

# Talorys – A self-hosted personal AI agent on Cloudflare.

https://t.co/93526lWSS

## Insights

- Talorys is an open-source personal AI agent designed to run entirely inside a user's own Cloudflare account, avoiding any third-party server, database, or developer-operated backend.
- It's deployed with a single CLI command and relies exclusively on free-tier Cloudflare services (Pages, Workers, Durable Objects with SQLite, Workers AI), explicitly avoiding paid add-ons like R2, D1, or Vectorize.
- Core features — chat, persistent memory, tasks/notes/projects, and scheduled reminders/automations — are designed to keep working even without AI access, decoupling basic productivity functions from model availability.
- Memory handling includes versioning logic (tracking facts as "current" vs. "past" when they change) and optional semantic recall, pointing to deliberate design around how personal context persists and evolves over time.
- The architecture enforces strict privacy/security boundaries: the agent Worker has no public URL, auth happens server-side, and the system has no telemetry or tracking sent to developers.
- Positioned explicitly as single-user, no-signup, no-teams software — a sharp contrast to multi-tenant SaaS AI assistant models.

## Quote

> Your personal AI agent. Your own cloud.
