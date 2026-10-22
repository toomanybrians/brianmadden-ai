---
title: Securing Quick access from corporate networks with AWS PrivateLink
source: AWS Machine Learning Blog
source_id: aws-ml-blog
source_url: https://aws.amazon.com/blogs/machine-learning/securing-quick-access-from-corporate-networks-with-aws-privatelink/
author: Rahul Kulkarni
date_published: '2026-10-21'
date_captured: '2026-10-22'
ingest_method: feed
model: claude-sonnet-5
---

# Securing Quick access from corporate networks with AWS PrivateLink

## Insights

- Amazon Quick is positioned as an "AI-powered workspace" unifying search, analytics, research, and automation into one conversational interface — the piece treats agentic data access (via Quick Agents, Flows, Automate) as requiring the same enterprise network/security architecture as traditional BI tools.
- AWS frames enterprise AI adoption as gated by data-access security: the core tension is letting AI agents query sensitive on-prem/behind-firewall data without exposing it to the public internet, driven by compliance regimes (HIPAA, FedRAMP, PCI-DSS) as well as attack-surface and audit concerns.
- Notable gap disclosed: Quick's knowledge-base "VPC connections" (private network access) currently only support Amazon Redshift as a private source — common enterprise content repositories (Confluence, SharePoint, Box, Google Drive, OneDrive, S3) cannot use this private connectivity path today, limiting how much of an enterprise's knowledge the AI index can touch privately.
- VPC connections and endpoint restrictions require Quick "Enterprise edition" — private/secure data access for the AI agents is an edition-gated, not default, capability, implying a deliberate upsell/tiering strategy for security-conscious enterprise buyers.
- Identity and network controls are explicitly presented as interdependent: role-based access (Admin/Author/Reader), Space-level segmentation, and row/column-level security all govern what the AI agents can see and surface in natural-language answers — the same security policies that restrict dashboards are said to restrict what AI can reference when generating responses.
- Several AI-specific features (action connector and flow management APIs) are *not* available through the private VPC API endpoint, meaning automation that manages connectors/flows programmatically still needs a path to the public API — private-networking coverage for the AI/automation layer is partial, not total.

## Quote

> The AI capabilities are unchanged. The exposure is removed.
