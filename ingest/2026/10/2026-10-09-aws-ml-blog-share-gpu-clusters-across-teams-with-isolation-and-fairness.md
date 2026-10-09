---
title: Share GPU clusters across teams with isolation and fairness using Amazon SageMaker
  HyperPod
source: AWS Machine Learning Blog
source_id: aws-ml-blog
source_url: https://aws.amazon.com/blogs/machine-learning/share-gpu-clusters-across-teams-with-isolation-and-fairness-using-amazon-sagemaker-hyperpod/
author: Giuseppe Angelo Porcelli
date_published: '2026-10-08'
date_captured: '2026-10-09'
ingest_method: feed
model: claude-sonnet-5
---

# Share GPU clusters across teams with isolation and fairness using Amazon SageMaker HyperPod

## Insights

- The architecture explicitly targets multi-team sharing within a single trusted organization, not multi-customer isolation between untrusted tenants — Kubernetes namespaces are described as a logical/accidental-interference boundary, not a hard security boundary against a determined malicious actor.
- The design stacks several AWS primitives to solve GPU cost/governance problems at the enterprise level: IAM Identity Center (federated auth via Entra ID/Okta/Ping with SCIM sync), per-team SageMaker AI domains, EKS namespaces + access entries, HyperPod Task Governance (built on Kueue) for quotas/priority/preemption, and Kubecost for namespace-level chargeback.
- Fair-share compute is handled via priority classes — e.g., production inference workloads can be configured to preempt experimental training jobs when GPU capacity is constrained, reflecting a real operational tension between research flexibility and production reliability.
- Cost attribution (chargeback/showback) is treated as a first-class architectural concern, not an afterthought, with per-team namespace cost visibility enabling budgets/alerts — signaling that GPU cost accountability is now a packaged enterprise requirement, not just infrastructure plumbing.
- The piece notes this is a "flexible, composable" reference pattern requiring assembly of multiple AWS services rather than a single turnkey product, and acknowledges it extends to Slurm-based clusters too — suggesting multi-tenant GPU governance is still an integration challenge, not a solved/packaged offering even from AWS itself.
- Network isolation is called out as a gap by default: Kubernetes pods across namespaces can reach each other unless explicit NetworkPolicies are added, underscoring that "isolation" claims in shared-cluster setups require deliberate additional configuration.

## Quote

> Namespaces are an isolation boundary, not a hard security boundary.
