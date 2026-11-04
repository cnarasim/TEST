---
id: ea-ds-ai-architecture
domain: Enterprise Architecture
l1: Design and Standards
l2: AI solution architecture
summary: The building blocks of an AI solution: governed data and retrieval, models behind one gateway, tools, guardrails, evaluation and monitoring.
systems: AI gateway, Data platform, Search and retrieval, Monitoring platform
tags: AI architecture, generative AI, retrieval, agents, guardrails, evaluation, model gateway
order: 612
---
# AI solution architecture

## What AI architecture covers
### Purpose
- AI solutions that are useful, safe and affordable
- Models that can be swapped without a rebuild
### In scope
- Data, models, tools and guardrails
- Evaluation, monitoring and cost
### Outcome
- Faster, safer releases of AI features
- Quality, cost and risk visible per use case

## Six building blocks of every AI solution
Layout: process list
- Data: governed sources, answers that cite them
- Models: behind one gateway, swappable
- Tools: least-privilege access to our systems
- Guardrails: input and output checks, human approval
- Evaluation: test sets before and after release
- Monitoring: quality, cost, speed and drift

## Choose the simplest pattern that works
| Pattern | When to use it | Example |
|---|---|---|
| Prompt and model | Drafting and summaries | Product description drafts |
| Retrieval | Answers grounded in our documents | Store policy assistant |
| Agent with tools | Multi-step tasks in our systems | Order status and returns help |
| Fine-tuned model | Only when the others fall short | A narrow classification task |

## Standards for every AI solution
| Standard | Rule | Owner |
|---|---|---|
| One gateway | Every model call goes through it | AI platform team |
| Evaluation gate | Release only above the agreed score | Product owner |
| Human approval | People approve irreversible actions | Business owner |
| Data protection | No personal data without approval | Privacy |
| Tracing | Each call logged: cost, speed, outcome | AI platform team |

## Evaluation decides each release
Layout: swimlane handoffs
- Product team: Proposes the AI use case
- AI platform team: Reviews the design
- AI platform team: Passes the evaluation?
- AI platform team: If yes, releases a pilot
- AI platform team: If no, improves data or prompts
- Business owner: Approves wider release

## KPIs that show it works
| KPI | What it measures | Data source |
|---|---|---|
| Task success | Cases the solution gets right | Evaluation sets |
| Cost per task | Model and tool cost per task | AI gateway |
| Response time | Slowest 5% of responses | AI gateway |
| Guardrail blocks | Inputs or outputs stopped | AI gateway logs |
