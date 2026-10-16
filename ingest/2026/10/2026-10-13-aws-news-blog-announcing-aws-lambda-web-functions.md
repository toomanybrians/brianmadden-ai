---
title: Announcing AWS Lambda Web Functions
source: AWS News Blog
source_id: aws-news-blog
source_url: https://aws.amazon.com/blogs/aws/announcing-aws-lambda-web-functions-for-fast-consistent-web-app-performance-anywhere/
author: Micah Walter
date_published: '2026-10-12'
date_captured: '2026-10-13'
ingest_method: feed
model: claude-sonnet-5
---

# Announcing AWS Lambda Web Functions

## Insights

- AWS Lambda now has three distinct "form factors" sharing Firecracker isolation: Event Functions (classic event-handler model, wall-clock billing), Web Functions (new, HTTP-native, multi-concurrent, active-CPU billing), and MicroVMs (stateful sandboxes for untrusted/user-generated code).
- Web Functions let developers deploy standard port-listening HTTP servers (Express, Hono, Fastify, Next.js, etc.) unmodified — no adapters or event-handler rewrites — directly via a single CLI command.
- Each execution environment can handle up to 128 concurrent requests, and billing meters active CPU time rather than wall-clock time, so I/O-wait (DB calls, API calls, streaming token responses) costs little — explicitly framed as beneficial for AI inference endpoints that stream tokens.
- Built-in multi-region deployment with automatic latency-based routing via a single global URL, plus revision/endpoint primitives for canary-style weighted traffic shifting without extra tooling.
- Integrates with CloudFront as an origin, including origin access control (OAC) support so Web Function endpoints can be locked to a specific CloudFront distribution, mirroring the private-origin pattern already used with S3.
- Launch scope is limited: five AWS regions, Node.js 24 on Arm64 only, with VPC connectivity support.

## Quote

> No adapters, no infrastructure to manage, and no framework lock-in.
