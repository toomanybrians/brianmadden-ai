---
title: Announcing SOCI-indexed images for faster SageMaker AI jobs
source: AWS Machine Learning Blog
source_id: aws-ml-blog
source_url: https://aws.amazon.com/blogs/machine-learning/announcing-soci-indexed-images-for-faster-sagemaker-ai-jobs/
author: Kanwaljit Khurmi
date_published: '2026-10-27'
date_captured: '2026-10-28'
ingest_method: feed
model: claude-sonnet-5
---

# Announcing SOCI-indexed images for faster SageMaker AI jobs

## Insights

- AWS introduces SOCI (Seekable OCI) indexing for SageMaker AI training/processing jobs, letting containers lazy-load only the files needed to start, streaming the rest in the background — cutting job-start image download time from minutes to seconds.
- Benchmarks across eight container images (1.8–35.4 GB) showed 8x to ~38x faster download times, with lazy loading holding at 3–11 seconds regardless of image size, while standard downloads scaled linearly with size (up to 7+ minutes for the largest image).
- The speedup held consistently across 13 instance type/size combinations, suggesting the benefit is independent of compute configuration and purely tied to image size and loading method.
- There's a measured trade-off: the first training epoch is slower (3–16 seconds, or minutes if a large model is baked into the image) as deferred files get fetched; net effect across tested workloads was still 1–6 minutes saved per job.
- Adoption requires no changes to job definitions or APIs — just using a pre-indexed AWS Deep Learning Container (tag suffix "-soci") or generating an index for custom images via open-source tooling (containerd, SOCI snapshotter, Finch/nerdctl); jobs fall back to standard download if indexing fails.
- Limitations disclosed: only works with Amazon ECR private repositories (not other registries or VPC-mode private registries), gains shrink for images under ~4GB, and containerd-based runtime can break Docker-specific assumptions in entry-point scripts (e.g., Docker socket access, cgroup-based IDs).

## Quote

> Container image download is pure overhead: billable job time that produces no model progress.
