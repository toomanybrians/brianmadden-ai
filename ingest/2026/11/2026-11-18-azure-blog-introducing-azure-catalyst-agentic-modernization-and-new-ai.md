---
title: Introducing Azure Catalyst agentic modernization and new AI infrastructure
  innovations
source: Azure Blog
source_id: azure-blog
source_url: https://azure.microsoft.com/en-us/blog/introducing-azure-catalyst-agentic-modernization-and-new-ai-infrastructure-innovations/
author: Jeremy Winter
date_published: '2026-11-17'
date_captured: '2026-11-18'
ingest_method: feed
model: claude-sonnet-5
---

# Introducing Azure Catalyst agentic modernization and new AI infrastructure innovations

## Insights

- Azure Catalyst is positioned as an agent-led modernization tool that analyzes legacy code, maps dependencies, and plans/executes migrations across applications, data, and infrastructure (Java, .NET, VMware, Hyper-V, physical servers, BizTalk-to-Logic Apps), integrated into GitHub Copilot and Microsoft Security for vulnerability remediation.
- New AI infrastructure features for AKS/Azure include: Agent Sandbox (VM-level isolated execution for agent-generated code), Agent Grid (authenticated/encrypted agent-to-agent and agent-to-tool networking with default-deny isolation), context caching to avoid GPU recomputation on long-running agent tasks, and AKS AI Manager (workload-aware GPU/VM placement across the fleet).
- A new "connected path" links Microsoft Foundry (managed model/agent experience) to AKS (customizable infrastructure), with open-weight models/agents meant to move seamlessly from cloud to edge with consistent security/governance; flex nodes for AKS extend this to GPU environments beyond Azure.
- Cited adoption figures include 1.4 million applications modernized via Catalyst, Levi Strauss deploying 1,000+ agents, Microsoft Quantum/Xbox reporting 80% faster modernization, Intune 75% faster library upgrade, and GitHub porting 800,000 lines of Copilot's agentic harness from TypeScript to Rust — presented as internal "customer zero" proof points, not independently verified.
- Edge/on-prem AI extension is addressed via Azure Local, Windows Server 2028 (public preview, AI inference alongside business apps), and Windows PCs (local processing), all governed through Azure Arc for consistent management across distributed environments.
- The piece frames open-source commitment (Kubernetes, vLLM, Ray) as central to flexibility, claiming customers can run open models "everywhere they operate," though this coexists with deep Azure-specific tooling (Catalyst, AI Manager) that creates platform lock-in incentives.

## Quote

> Running our factory-level AI applications on Azure gives us one foundation for different AI workloads in production. — Justin Litherland, Rockwell Automation
