---
title: 'Making Amazon Quick enterprise-ready: Automated, auditable cross-account resource
  promotion'
source: AWS Machine Learning Blog
source_id: aws-ml-blog
source_url: https://aws.amazon.com/blogs/machine-learning/making-amazon-quick-enterprise-ready-automated-auditable-cross-account-resource-promotion/
author: Keshav Ganesh
date_published: '2026-10-05'
date_captured: '2026-10-06'
ingest_method: feed
model: claude-sonnet-5
---

# Making Amazon Quick enterprise-ready: Automated, auditable cross-account resource promotion

## Insights

- Amazon Quick's agentic resources (chat agents, action connectors, knowledge bases, flows, spaces) previously had no native way to move from a dev AWS account to production — teams manually rebuilt instructions, re-attached connectors, and re-provisioned S3 buckets, which was slow and error-prone and undermined enterprise governance claims.
- AWS built the "Quick Resource Migrator," a sample MCP server hosted on Amazon Bedrock AgentCore, that automates cross-account promotion via the existing Quick/QuickSight API (create/read/update/delete/list) rather than requiring a new product feature.
- The tool is explicitly designed around enterprise governance concerns: idempotent upserts (safe to re-run), permission fidelity (replays identical permission grants via Describe*Permissions APIs rather than hardcoding), least-privilege roles (read-only source, scoped read-write target), and versioned S3 backups before every update with a restore/rollback tool.
- Secrets/credentials for action connectors are never copied across accounts — connectors are recreated with placeholder credentials requiring re-authentication in the target, and knowledge base documents (S3 objects) themselves are not migrated, only configuration and permissions.
- The MCP server exposes five tools (preview_migration, migrate_resources, list_backups, get_backup, restore_backup) and can be invoked via natural language inside Quick or through a generated point-and-click "Quick App" built from a provided prompt template.
- Positioned as closing a gap AWS frames as "a baseline expectation for enterprise software" — i.e., an admission that basic dev/prod promotion tooling was missing from Quick until this sample solution.

## Quote

> Cross-account promotion is a baseline expectation for enterprise software, and until now it has been the missing piece for Amazon Quick.
