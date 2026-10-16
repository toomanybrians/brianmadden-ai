---
title: Meta’s Muse Spark Open now available in Amazon SageMaker JumpStart
source: AWS Machine Learning Blog
source_id: aws-ml-blog
source_url: https://aws.amazon.com/blogs/machine-learning/metas-muse-spark-open-now-available-in-amazon-sagemaker-jumpstart/
author: Aris Tsakpinis
date_published: '2026-10-15'
date_captured: '2026-10-16'
ingest_method: feed
model: claude-sonnet-5
---

# Meta’s Muse Spark Open now available in Amazon SageMaker JumpStart

## Insights

- Meta's Muse Spark Open is a large mixture-of-experts coding/agentic model (816B total parameters, 42B active per token) now deployable via Amazon SageMaker JumpStart, giving enterprises a self-hosted alternative to API-based coding assistants.
- It supports a 1M-token context window specifically aimed at ingesting entire codebases (dependencies, legacy code, thousands of files) without manual chunking — a direct response to the "context limits" pain point in enterprise coding agents.
- Meta designed it as an agentic model from the ground up: it plans, acts, observes results, and self-corrects over long horizons, and can coordinate subagents and operate across desktop/mobile/browser environments (though the host app must supply the actual tools/browser/compute environment).
- It's multimodal (text, image, document, audio, audio-video in; text out) and positioned for workflows like turning a screen recording or bug report with audio/video into a reproduction plan or draft fix.
- Deployment economics hinge on quantization: the NVFP4 4-bit variant needs ~1/4 the memory of BF16, letting it run on a smaller instance (ml.p5e.48xlarge vs ml.p6-b300.48xlarge) — framed as the natural "try first" option for cost-conscious evaluation.
- Enterprise control pitch: because it's open-weight and self-hosted, the model runs in the customer's own AWS account/VPC with KMS encryption and network isolation, keeping source code and prompts off third-party infrastructure — a direct enterprise-security differentiator versus hosted coding-assistant APIs.

## Quote

> Meta says the model plans, acts, observes the result, and corrects itself over long horizons, rather than making single tool calls.
