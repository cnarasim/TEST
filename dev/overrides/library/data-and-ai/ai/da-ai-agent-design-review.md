---
id: da-ai-agent-design-review
domain: Data and AI
l1: AI
l2: AI agent design review
summary: Reviewing an AI agent before it acts in our systems: its tools and permissions, guardrails, human approvals, evaluations, limits and tracing.
systems: AI gateway, Identity platform, Evaluation tooling, Monitoring platform
tags: AI agents, agent design review, tools, permissions, human in the loop, prompt injection, evaluation
order: 304
---
# AI agent design review

## What an agent review covers
### Purpose
- Agents that act safely in our systems
- Clear limits on what an agent may do alone
### In scope
- Tools, permissions, data and approvals
- Evaluation, limits, tracing and rollback
### Outcome
- Agents released with known behaviour
- Every action traceable to a request

## Six questions for every agent
Layout: process list
- Goal: the task and when it is done
- Tools: few, named, least-privilege access
- Approvals: people confirm irreversible actions
- Inputs: documents and web content treated as data
- Limits: steps, time and cost caps, stop rules
- Evidence: evaluation results and full tracing

## Actions are tiered by risk
| Action | Example | Rule |
|---|---|---|
| Read | Look up an order's status | Allowed with the user's access |
| Draft | Prepare a refund or a message | Allowed, a person sends it |
| Change | Update an address or a booking | Allowed within limits, logged |
| Irreversible | Issue a refund, cancel an order | Human approval every time |

## The review decides the release
Layout: swimlane handoffs
- Product team: Submits design and evaluations
- AI platform team: Reviews tools and limits
- AI platform team: Passes every check?
- AI platform team: If yes, approves a pilot
- AI platform team: If no, lists the changes
- Business owner: Signs off the pilot scope

## Checks before release
| Check | Pass when | Owner |
|---|---|---|
| Evaluation | Task success above [target] on real cases | Product owner |
| Injection tests | Planted instructions are ignored | Security |
| Permissions | Tools limited to the task | Identity team |
| Tracing | Every step and tool call logged | AI platform team |
| Kill switch | The agent can be stopped at once | AI platform team |

## KPIs that show it works
| KPI | What it measures | Data source |
|---|---|---|
| Task success | Tasks completed correctly | Evaluation and audits |
| Approvals overridden | Actions people reject | Approval logs |
| Cost per task | Model and tool cost | AI gateway |
| Incidents | Unsafe or wrong actions | Incident log |
