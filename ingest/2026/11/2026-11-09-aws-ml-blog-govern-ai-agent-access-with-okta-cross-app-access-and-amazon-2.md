---
title: Govern AI agent access with Okta Cross App Access and Amazon Bedrock AgentCore
  – Part 1
source: AWS Machine Learning Blog
source_id: aws-ml-blog
source_url: https://aws.amazon.com/blogs/machine-learning/govern-ai-agent-access-with-okta-cross-app-access-and-amazon-bedrock-agentcore-part-1/
author: Hammad Ausaf
date_published: '2026-11-06'
date_captured: '2026-11-09'
ingest_method: feed
model: claude-sonnet-5
---

# Govern AI agent access with Okta Cross App Access and Amazon Bedrock AgentCore – Part 1

## Insights

- Okta Cross App Access (XAA) registers AI agents as identities in the IdP and evaluates policy per-request, so admins can revoke a user's access to a specific agent — in testing, new requests were refused within ~1 second of unassignment, though already-issued tokens remained valid up to their 5-minute expiry.
- The architecture separates governance from execution: Okta decides "which agent may act for which user," while Amazon Bedrock AgentCore Identity holds credentials, redeems Okta's decision for a short-lived access token, and keeps that token invisible to the agent's own code.
- Three distinct tokens carry three distinct decisions in each request chain: an ID token (who the user is), an ID-JAG (Okta's authorization decision, single-use, 5-minute life), and an access token (what the downstream resource accepts, carrying both user and agent identity plus group claims).
- Per-user authority is carried via group claims rather than OAuth scopes, since scopes are fixed per agent-resource connection — meaning fine-grained permission differences between users must be enforced by checking group membership in the resource/tool code itself, not assumed from the token grant alone.
- Comparison testing showed plain OAuth token exchange (without XAA) leaks broader authority than intended — e.g., scopes silently widened and revoked users' stale tokens still worked — whereas XAA tokens carried an explicit agent identity claim and were properly refused after revocation.
- Operational gaps were measured, not just claimed: deleting a resource connection acts as an immediate kill switch, but deactivating an agent through Okta's agent API queued for 86 minutes in testing with no cancel option — a real latency gap in incident response.
- The added latency cost of the governance layer was measured at roughly 0.6 seconds within an end-to-end ~30 second request, suggesting the security/identity overhead is a minor fraction of total agent response time.

## Quote

> Which agent might act for which user in which application, and how you stop it.
