---
id: da-an-data-product
domain: Data and AI
l1: Analytics
l2: Data product design
summary: Designing a data product people can rely on: its users and questions, sources, owner, quality and freshness promises, and access.
systems: Data platform, Data catalog, BI dashboards, Data quality tool
tags: data product, data mesh, data contract, service level, semantic layer, self-service analytics
order: 201
---
# Data product design

## What a data product is
### Purpose
- A trusted, reusable data set with an owner
- Answers to a known set of business questions
### In scope
- Users, questions, sources and the model
- Quality, freshness, access and support
### Outcome
- Analysts start from data, not from extracts
- One definition used by every report

## Six parts of every data product
Layout: hexagons
- Users: who relies on it, for which decisions
- Questions: what it must answer
- Sources: systems of record it draws from
- Contract: fields, meanings and freshness
- Quality: rules checked on every load
- Owner: named, with a support route

## Example: store sales data product
| Part | Design | Owner |
|---|---|---|
| Questions | Sales, margin and traffic by store and day | Retail analytics |
| Sources | POS, ecommerce orders, store calendar | Data platform team |
| Freshness | Loaded by [time] each morning | Data platform team |
| Quality | Totals match finance within [n]% | Data steward |
| Access | All store leaders; margin by role | Data owner |

## From request to published product
Layout: swimlane handoffs
- Business team: Brings the questions
- Data owner: Agrees scope and access
- Data platform team: Builds model and checks
- Data platform team: Contract met in testing?
- Data platform team: If yes, publishes it
- Data platform team: If no, fixes and retests

## KPIs that show it works
| KPI | What it measures | Data source |
|---|---|---|
| Active users | People using it each month | Platform usage logs |
| On-time loads | Loads meeting the freshness promise | Pipeline monitoring |
| Quality passes | Loads passing every rule | Data quality tool |
| Reports built on it | Reports reusing the product | BI catalog |
