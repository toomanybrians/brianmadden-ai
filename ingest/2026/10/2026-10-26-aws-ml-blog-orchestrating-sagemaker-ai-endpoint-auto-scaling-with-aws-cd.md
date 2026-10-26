---
title: Orchestrating SageMaker AI endpoint auto scaling with AWS CDK
source: AWS Machine Learning Blog
source_id: aws-ml-blog
source_url: https://aws.amazon.com/blogs/machine-learning/orchestrating-sagemaker-ai-endpoint-auto-scaling-with-aws-cdk/
author: Lauren Eterno
date_published: '2026-10-23'
date_captured: '2026-10-26'
ingest_method: feed
model: claude-sonnet-5
---

# Orchestrating SageMaker AI endpoint auto scaling with AWS CDK

## Insights

- Updating a SageMaker real-time endpoint's configuration (instance type, count, env vars) via CloudFormation/CDK natively fails or silently breaks auto scaling, because SageMaker requires deregistering the Application Auto Scaling scalable target before an endpoint update, but CloudFormation can't track resources once deregistered outside its control.
- Three documented failure modes: CloudFormation blocks the update outright; a manual workaround succeeds but silently leaves the endpoint without auto scaling (no error surfaced); or a parameter change triggers a CloudFormation error referencing a resource that "was not found," which can cascade into an unrecoverable `UPDATE_ROLLBACK_FAILED` stack state requiring manual console intervention.
- The proposed fix replaces native CloudFormation auto-scaling resources with three custom resources (Deregister, Register Scalable Target, Attach Scaling Policy) sequenced via explicit CDK dependency ordering, using an async "wait until endpoint is InService" polling pattern bounded by provider timeouts (1 hour / 15 minutes) rather than single Lambda invocation limits.
- A single `ConfigHash` property spanning both endpoint and auto-scaling config is used to force CloudFormation to re-invoke the orchestration whenever either changes, since the two concerns are coupled across the deployment lifecycle.
- The author notes a hidden infrastructure cost: what looks like three custom resources in the construct actually deploys twelve Lambda functions and two Step Functions state machines once CDK's provider framework generates its supporting boilerplate — a complexity/overhead tradeoff worth tracking when reviewing deployed stacks.
- This is an open-source reference implementation (linked GitHub repo) intended to be dropped into existing CDK stacks, positioning it as a reusable pattern rather than a managed AWS feature — the underlying SageMaker/CloudFormation limitation itself remains unaddressed at the service level.

## Quote

> SageMaker AI blocks the endpoint update before CloudFormation reaches the auto scaling resources.
