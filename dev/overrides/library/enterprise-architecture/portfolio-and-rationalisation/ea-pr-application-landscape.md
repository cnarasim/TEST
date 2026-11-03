---
id: ea-pr-application-landscape
domain: Enterprise Architecture
l1: Portfolio and Rationalisation
l2: Application landscape
summary: A one-page view of the applications by business capability, with owner, lifecycle state, health and cost, kept current for portfolio decisions.
systems: Application inventory, Architecture repository, Contract register
tags: application landscape, application inventory, portfolio, capability, ownership, health check, rationalisation
order: 407
---
# Application landscape

## What the landscape view gives
### Purpose
- One current list of what we run and why
- Facts for every portfolio decision
### In scope
- Applications by capability and owner
- Lifecycle state, health, cost and usage
### Outcome
- Overlaps and gaps visible at a glance
- Retirements chosen on evidence

## Applications by capability
| Capability | Main applications | Lifecycle |
|---|---|---|
| Sell in store | POS, store systems | Adopt |
| Sell online | Ecommerce platform, app | Adopt |
| Fulfil orders | OMS, WMS | Adopt |
| Plan and buy | Planning system, ERP | Contain |
| Run finance | ERP, close tools | Adopt |
> Notes: illustrative states; fill each row from the application inventory.

## Every application has one record
Layout: hub
- Application record: one per application
- Owner: business and technical
- Capability: what it supports
- Lifecycle: adopt, contain or retire
- Cost: licence, hosting and support
- Interfaces: what it connects to

## Four questions in every health check
| Measure | Question | Source |
|---|---|---|
| Business fit | Does it support the process well? | Owner survey |
| Technical health | Supported, secure and maintainable? | Architecture review |
| Cost | What does it cost to run each year? | Finance and contracts |
| Usage | Who uses it, and how often? | Sign-in data |

## Owners keep the landscape current
Layout: swimlane handoffs
- Application owner: Updates the record quarterly
- Enterprise architecture: Reviews health and cost
- Enterprise architecture: Overlap or poor health?
- Enterprise architecture: If yes, proposes a change
- Enterprise architecture: If no, keeps the plan
- Portfolio leadership: Funds the changes

## Today and target
### Today
- Lists in several spreadsheets, out of date
- Overlaps found during projects
### Target
- One inventory, updated every quarter
- Rationalisation decided on the facts
