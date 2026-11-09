---
title: Serverless MCP server for AI agent data lake access on Amazon ECS Fargate
source: AWS Machine Learning Blog
source_id: aws-ml-blog
source_url: https://aws.amazon.com/blogs/machine-learning/serverless-mcp-server-for-ai-agent-data-lake-access-on-amazon-ecs-fargate/
author: Aishwarya Pawar
date_published: '2026-11-06'
date_captured: '2026-11-09'
ingest_method: feed
model: claude-sonnet-5
---

# Serverless MCP server for AI agent data lake access on Amazon ECS Fargate

## Insights

- Amazon's internal case study: an MCP (Model Context Protocol) server built on serverless ECS Fargate acts as a single gateway between AI agents and the enterprise data lake, replacing a pattern where each agent independently wired its own SQL generation, schema knowledge, and access control — causing schema-change breakage and fragmented permissions.
- Core design move is metadata-driven onboarding: adding a new dataset requires only a JSON file (schema, business description, column semantics, sample values, engine-specific query hints) rather than custom integration code; the system auto-indexes it into a vector-searchable metadata catalog on the next pipeline sync.
- Architecture separates client, MCP server, tools, and knowledge-base-refresh layers so each scales and deploys independently; security is layered (Cognito auth, private-subnet MCP server, WAF, SELECT-only enforcement at the tool level, CloudWatch audit logging) rather than enforced at one choke point.
- The same server supports multiple agents/clients simultaneously (any MCP-compatible client can connect via a standard `/mcp` endpoint) and can combine structured SQL queries with unstructured document/policy search in a single response turn.
- Reported end-to-end query latency is 15–20 seconds; stated future work includes column-level restricted-access permissions and a feedback loop that surfaces suggested metadata/query-hint improvements when queries fail or return low-confidence results.
- Framing emphasizes that tool/data-access layers should be built to "outlive" any specific agent implementation, treating extensibility as a configuration problem rather than a code problem.

## Quote

> Agents evolve rapidly, but data access patterns should outlive any single agent implementation.
