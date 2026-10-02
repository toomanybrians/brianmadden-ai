---
title: Announcing AWS Well-Architected Agent, an AI-powered intelligence to optimize
  your cloud environment (preview)
source: AWS News Blog
source_id: aws-news-blog
source_url: https://aws.amazon.com/blogs/aws/announcing-aws-well-architected-agent-an-ai-powered-intelligence-to-optimize-your-cloud-environment-preview/
author: Channy Yun (윤석찬)
date_published: '2026-10-01'
date_captured: '2026-10-02'
ingest_method: feed
model: claude-sonnet-5
---

# Announcing AWS Well-Architected Agent, an AI-powered intelligence to optimize your cloud environment (preview)

## Insights

- AWS Well-Architected Agent (preview) is a genAI service that analyzes a customer's actual AWS environment — utilization metrics, resource configs, application topology — against Well-Architected best practices across 65+ AWS services, rather than relying on static checklists.
- Recommendations are goal-aligned: customers declare business objectives per pillar (cost, performance, resilience, security), and the agent prioritizes findings by impact and effort against those stated goals rather than producing flat, undifferentiated output.
- Output operates at three levels of granularity — individual resource findings with dollar-impact estimates, consolidated cross-resource findings scoped to an application, and broader architectural/IaC-level pattern recommendations — with remediation deliverable via console walkthroughs, updated IaC code, or CLI commands.
- Supports pre-deployment review by letting users upload Terraform/CloudFormation/CDK projects for analysis against a chosen Well-Architected lens, extending the tool beyond live-environment auditing.
- Programmatic access is available via API and an AWS MCP Server/plugins, enabling integration into existing dev/ops workflows and AI coding tools.
- AWS explicitly flags that genAI-generated recommendations "may contain errors or incomplete information" and places evaluation/oversight responsibility on the customer; the legacy manual Well-Architected Tool remains available in parallel.
- Preview is region-limited (N. Virginia, Ohio, Oregon) and gated behind having an AWS Support plan, signaling this is positioned as a support-tier/enterprise offering rather than a self-serve free tool.

## Quote

> Generative AI capabilities produce this recommendation, which may contain errors or incomplete information.
