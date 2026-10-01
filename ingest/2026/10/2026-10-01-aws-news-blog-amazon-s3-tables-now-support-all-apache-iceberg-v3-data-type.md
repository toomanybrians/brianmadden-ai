---
title: Amazon S3 Tables now support all Apache Iceberg V3 data types
source: AWS News Blog
source_id: aws-news-blog
source_url: https://aws.amazon.com/blogs/aws/amazon-s3-tables-now-support-all-apache-iceberg-v3-data-types/
author: Daniel Abib
date_published: '2026-09-30'
date_captured: '2026-10-01'
ingest_method: feed
model: claude-sonnet-5
---

# Amazon S3 Tables now support all Apache Iceberg V3 data types

## Insights

- Amazon S3 Tables now support the full Apache Iceberg V3 spec, including deletion vectors, row lineage, and new types (variant, nanosecond timestamps, geometry, geography, unknown) — framed as closing common V2 pain points (slow deletes, JSON-as-string workarounds, imprecise timestamps).
- Deletion vectors replace V2's positional delete files with a compact binary format, meant to sharply cut compaction overhead — e.g., a 50,000-row compliance delete against a 2-billion-row table now writes one deletion vector file instead of thousands of delete files.
- Row lineage auto-adds `_row_id` and `_last_updated_sequence_number` to records, letting downstream pipelines query only changed rows (via sequence number checkpoints) instead of full-table scans — targeted at incremental pipeline efficiency.
- The variant type stores semi-structured data (e.g., clickstream JSON payloads) in a schema-flexible column that's shredded into hidden columns at write time, enabling statistics-based file pruning at query time without upfront schema design.
- V2-to-V3 upgrades are presented as atomic and backward-compatible for existing readers, but the migration is explicitly one-way — Iceberg's spec has no V3-to-V2 downgrade path, so AWS recommends confirming all engines support V3 before upgrading.
- New V3 data types require Spark 4.0+ engines (AWS Glue 6.0+, EMR 8.1+) and Parquet-format tables only; these special-type columns also can't be used in sort/Z-order compaction strategies, a notable constraint for storage optimization.
- AWS positions this within a broader claim of having "the broadest native Apache Iceberg support of any major cloud provider," spanning ingestion (EMR), catalog (Glue, Iceberg REST Catalog API), storage (S3 Tables), and analytics (Redshift).

## Quote

> AWS offers the broadest native Apache Iceberg support of any major cloud provider, with Iceberg-compatible services at every layer of the data stack.
