---
title: Preview web apps live as your coding agent builds them with Amazon Bedrock
  AgentCore runtime
source: AWS Machine Learning Blog
source_id: aws-ml-blog
source_url: https://aws.amazon.com/blogs/machine-learning/preview-web-apps-live-as-your-coding-agent-builds-them-with-amazon-bedrock-agentcore-runtime/
author: Sundar Raghavan
date_published: '2026-10-30'
date_captured: '2026-11-02'
ingest_method: feed
model: claude-sonnet-5
---

# Preview web apps live as your coding agent builds them with Amazon Bedrock AgentCore runtime

## Insights

- AWS adds "Session endpoints" to Amazon Bedrock AgentCore runtime, letting developers watch a coding agent's web app update live in a browser as it edits files, rather than waiting on a deploy cycle to review changes.
- Each agent session runs in an isolated microVM; Session endpoints are authenticated URLs (SigV4 or JWT) that forward HTTP/1.1, HTTP/2, and WebSocket traffic only to explicitly allowlisted ports, with all other ports/requests rejected (403/404/502 depending on cause).
- AWS distinguishes this from existing "runtime endpoints": runtime endpoints are for production invocation (versioned, promotable/rollback-able), while session endpoints are ephemeral, scoped to one dev/preview session, and die when the session ends.
- Because browsers can't attach AWS-signed credentials themselves, a local proxy ("local endpoint") runs on the developer's machine to inject credentials — a workaround highlighting that this is a developer/reviewer tool, not an end-user-facing app serving mechanism.
- Security caveats noted by AWS itself: no AWS PrivateLink support for inbound session traffic (public HTTPS only), agent and website share the same permission boundary within a session, and file edits don't persist beyond the session unless persistent storage is separately configured.
- Demo uses Claude Haiku 5.5 as the underlying model for the coding agent's file-editing decisions.

## Quote

> The URL needs credentials on every request and lasts only as long as the session, so use it to build, test, and review what your agent produces.
