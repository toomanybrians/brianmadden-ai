---
title: Modernizing mainframe Assembler to Java using Amazon Bedrock and AWS Transform
source: AWS Machine Learning Blog
source_id: aws-ml-blog
source_url: https://aws.amazon.com/blogs/machine-learning/modernizing-mainframe-assembler-to-java-using-amazon-bedrock-and-aws-transform/
author: Abhishek Ashish
date_published: '2026-11-16'
date_captured: '2026-11-17'
ingest_method: feed
model: claude-sonnet-5
---

# Modernizing mainframe Assembler to Java using Amazon Bedrock and AWS Transform

## Insights

- AWS proposes a five-phase AI-assisted pipeline for modernizing mainframe Assembler: business rules extraction, spec-driven functional documentation, Assembler-to-COBOL conversion, validation/equivalence testing, then COBOL-to-Java (Spring Boot) via AWS Transform.
- The methodology deliberately inserts an intermediate COBOL stage rather than converting Assembler directly to Java, on the claim that this is more reliable and lets human SMEs validate business logic in a readable format before final transformation.
- Business rules extraction is framed as the highest-leverage, highest-risk phase — AI (Amazon Bedrock via Kiro IDE or Bedrock console) generates structured JSON documenting rules and data mappings, but is explicitly positioned as draft output requiring SME review, not a final artifact.
- The piece emphasizes human-in-the-loop validation checkpoints at every phase (not just extraction) as essential to transformation quality, citing SME review as catching domain logic and edge cases AI tools may miss.
- Equivalence testing between Assembler and COBOL is scored via a weighted rubric (syntax, structure, logic, data flow, business-rule coverage, spec compliance) with a 0.7 threshold to "pass," suggesting a fairly formalized QA gate structure rather than ad hoc testing.
- Underlying business problem framed explicitly: critical batch jobs run for decades, understood by few remaining experts nearing retirement, making this as much a workforce/knowledge-continuity problem as a technical migration problem.

## Quote

> Amazon Bedrock and AWS Transform change that equation.
