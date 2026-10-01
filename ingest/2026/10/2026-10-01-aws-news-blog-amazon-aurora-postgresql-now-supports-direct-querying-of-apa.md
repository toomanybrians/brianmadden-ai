---
title: Amazon Aurora PostgreSQL now supports direct querying of Apache Iceberg and
  Parquet data in your data lake
source: AWS News Blog
source_id: aws-news-blog
source_url: https://aws.amazon.com/blogs/aws/amazon-aurora-postgresql-now-supports-direct-querying-of-apache-iceberg-and-parquet-data-in-your-data-lake/
author: Esra Kayabali
date_published: '2026-09-30'
date_captured: '2026-10-01'
ingest_method: feed
model: claude-sonnet-5
---

# Amazon Aurora PostgreSQL now supports direct querying of Apache Iceberg and Parquet data in your data lake

## Insights

- Aurora PostgreSQL can now directly query Apache Iceberg and Parquet data lake files (via S3, S3 Tables, or AWS Glue Data Catalog) using standard PostgreSQL foreign tables, without ETL pipelines to replicate data into the operational database.
- The capability is powered by embedding DuckDB directly inside Aurora PostgreSQL, following AWS's acquisition of DuckLabs (the team maintaining DuckDB); AWS frames this as a channel for open-source DuckDB improvements to flow into its managed services.
- AWS explicitly motivates this with AI agents: agents that "reason over both live and archived data" make it impractical to pre-replicate every dataset they might need, so direct cross-store querying removes a data-access bottleneck for agentic applications.
- Supports federated queries across external Iceberg REST Catalog (IRC)-compatible catalogs via Glue Data Catalog federation, letting a single query join Aurora data with Iceberg tables registered in multiple catalogs without migrating or duplicating data.
- Includes performance optimizations (predicate pushdown, column pruning, caching) and a materialization path (CREATE TABLE AS SELECT, MERGE INTO) for promoting lake data into native Aurora tables when sub-millisecond latency is required.
- Available at no additional feature charge (standard Aurora compute and S3 request costs apply) across commercial and GovCloud regions, on Aurora PostgreSQL 17.11+ and 18.6+.

## Quote

> This challenge only grows as you increasingly embed AI agents into your applications, where it is impractical to predict and pre-replicate every dataset an agent might need.
