---
title: 'AWS Weekly Roundup: AgentCore Runtime V2, Amazon DynamoDB bulk put items,
  and more (November 9, 2026)'
source: AWS News Blog
source_id: aws-news-blog
source_url: https://aws.amazon.com/blogs/aws/aws-weekly-roundup-agentcore-runtime-v2-amazon-dynamodb-bulk-put-items-and-more-november-9-2026/
author: Daniel Abib
date_published: '2026-11-09'
date_captured: '2026-11-10'
ingest_method: feed
model: claude-sonnet-5
---

# AWS Weekly Roundup: AgentCore Runtime V2, Amazon DynamoDB bulk put items, and more (November 9, 2026)

## Insights

- AWS's new AgentCore Runtime (V2) targets agent-hosting cost and latency: it dynamically scales memory to actual usage rather than peak, and uses environment snapshotting to cut cold starts to ~2 seconds regardless of container image size (200MB–2GB), versus the original runtime's cold starts ballooning from ~5.4s to ~30s as images grow — positioned as usage-based pricing that should lower total cost despite a higher per-unit rate.
- "Web Answer" is a new managed tool on Bedrock AgentCore Gateway that gives an agent a single tool call returning a synthesized, cited answer to a natural-language question — AWS is explicitly packaging the search/retrieval/citation pipeline so developers don't build it themselves, with filtering by domain and publish date.
- The piece frames this week's launches around a common pattern: enabling adoption/migration without stopping existing systems — e.g., Hive-to-Iceberg table migration (S3 Tables) that keeps the source writable except for a few minutes at cutover, and DynamoDB bulk-loading into *existing* tables from S3.
- DynamoDB's new bulk put-items feature loads line-delimited JSON/Ion files from S3 as an async managed job, supports per-record condition expressions (mixing plain/insert-only/version-guarded writes), and offers an "Accelerated" tier claiming under 1 hour for 100M 1KB items — but cancellation does not roll back already-written items.
- Lambda now supports Kafka "queue mode" (via Kafka share groups, requiring Kafka 4.2+), allowing many parallel invocations per partition instead of capping parallelism at partition count — trade-off is loss of ordering guarantees in favor of at-least-once delivery.
- Security Hub added an SBOM-based software inventory across EC2/ECR/Lambda (built on existing Inspector-generated SBOMs), aimed at rapid vulnerability-exposure lookups, included at no extra cost in Security Hub Essentials.

## Quote

> The per-unit rate is higher, but you use far fewer GB-hours, so the team expects most agents to see a lower bill, though that isn't guaranteed.
