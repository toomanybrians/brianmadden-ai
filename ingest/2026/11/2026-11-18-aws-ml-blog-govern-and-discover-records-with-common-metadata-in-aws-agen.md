---
title: Govern and discover records with common metadata in AWS Agent Registry
source: AWS Machine Learning Blog
source_id: aws-ml-blog
source_url: https://aws.amazon.com/blogs/machine-learning/govern-and-discover-records-with-common-metadata-in-aws-agent-registry/
author: Sana Iqbal
date_published: '2026-11-17'
date_captured: '2026-11-18'
ingest_method: feed
model: claude-sonnet-5
---

# Govern and discover records with common metadata in AWS Agent Registry

## Insights

- AWS Agent Registry now supports admin-defined "custom metadata schemas" — organization-specific key-value fields (text, enum, URL, boolean) that every registered agent, MCP server, or skill record must carry, enforced via validation at creation/update time.
- The registry distinguishes compliance from approval: a record can be schema-"COMPLIANT" without being approved — approval remains a separate human or automated decision layered on top of validated metadata.
- Records without metadata are saved as "NON_COMPLIANT" and can't be submitted for approval, and schema changes are additive only (no renaming/removing/retyping fields), so older records can lag behind schema updates without losing their approved status.
- The design supports a governance pipeline: publishers submit draft values, external systems (security scanners, CMDB sync jobs) enrich records via API before approval, and an approval function (e.g., AWS Lambda triggered by EventBridge) checks structured evidence (scan status, classification, CMDB ID) to auto-approve or reject.
- Metadata fields are indexed for discovery, letting both human consumers and AI agents combine natural-language search with structured filters (e.g., environment=prod AND businessUnit=payments AND securityScanStatus=PASSED); only approved records surface in results.
- Agents can query the registry directly through an MCP endpoint exposing search/list/get as tools, enabling an LLM-based agent (demoed via Strands + Amazon Bedrock) to translate plain-language requests into filtered registry searches.

## Quote

> Schema changes are additive: you can add fields... but you can't rename, remove, or retype a field.
