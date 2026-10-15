---
title: Amazon S3 is now available on the Vercel Marketplace and v0 by Vercel
source: AWS News Blog
source_id: aws-news-blog
source_url: https://aws.amazon.com/blogs/aws/amazon-s3-vercel-marketplace-v0/
author: Daniel Abib
date_published: '2026-10-14'
date_captured: '2026-10-15'
ingest_method: feed
model: claude-sonnet-5
---

# Amazon S3 is now available on the Vercel Marketplace and v0 by Vercel

## Insights

- AWS is distributing S3 (including S3 Tables for Iceberg-based analytics and S3 Vectors for embedding storage) directly through third-party developer platforms like Vercel, rather than requiring developers to provision via the AWS Console — collapsing a traditional onboarding/config step.
- The integration uses short-lived OIDC-to-STS credential exchange (no static keys), provisioned automatically when a developer creates a storage resource in Vercel's dashboard or CLI.
- S3 Vectors is positioned explicitly as infrastructure for AI workloads — RAG and semantic search — claiming up to 90% cost reduction versus typical vector storage/query approaches, but it only stores/queries vectors; embedding generation is left to the developer's own model.
- v0 (Vercel's AI app-builder) can provision the correct S3 resource type (general bucket, Tables, or Vectors) directly from a natural-language prompt describing the desired app (e.g., "a support bot that answers questions from my PDFs"), then wires up the connection and generates code.
- All AWS services available through Vercel (S3, Aurora, DynamoDB, OpenSearch Serverless) share one AWS account/billing and authentication model, enabling combined stacks (e.g., metadata in Aurora + files in S3, or text in DynamoDB + embeddings in S3 Vectors) without extra setup.
- New AWS accounts created through the Vercel integration get $100 in credits (six months); existing linked AWS accounts retain native billing but Vercel can only manage new buckets created through the platform, not pre-existing ones.

## Quote

> S3 Vectors ... reducing the cost of uploading, storing, and querying vectors by up to 90%.
