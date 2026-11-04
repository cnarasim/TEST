---
id: ea-ds-target-state
domain: Enterprise Architecture
l1: Design and Standards
l2: Current and target state architecture
summary: Where the architecture is today, where it needs to be, the gaps between, and the order in which to close them.
systems: Architecture repository, Application inventory
tags: target state, current state, gap analysis, transition architecture, roadmap, future state
order: 603
---
# Current and target state architecture

## What this view covers
### Purpose
- A shared picture of where we are and where we go
- Projects that move toward one target
### In scope
- Integration, data, applications and hosting
- Gaps, transition steps and their order
### Outcome
- Investment aimed at the biggest gaps
- Fewer projects that add complexity

## The shift in one view
### Today
- Point-to-point files between systems
- Data copied into many stores
### Target
- APIs and events on one platform
- Governed data products with owners

## Gaps between today and target
| Area | Today | Target |
|---|---|---|
| Integration | Point-to-point files | APIs and events on one platform |
| Data | Copies in many places | One platform, owned data products |
| Orders | Separate per channel | One order management for all channels |
| Hosting | Own data centres | Cloud first, managed services |
| Identity | Many logins | Single sign-on for every app |

## Transition in three stages
Layout: timeline phases
- Foundations: Jan 2027 to Dec 2027 (Year 1)
- Scale: Jan 2028 to Dec 2028 (Year 2)
- Optimize: Jan 2029 to Dec 2029 (Year 3)
- Integration platform live: Jun 30, 2027 (Year 1)
- Every channel on one order view: Dec 31, 2028 (Year 2)
> Notes: example dates; set each stage from the funded roadmap.

## Where to move first
Layout: matrix
- Quick wins: high value, low effort - retire duplicate reports
- Big moves: high value, high effort - one order management
- Fill-ins: lower value, low effort - single sign-on for small apps
- Later: lower value, high effort - replace stable back-office tools

## KPIs that show progress
| KPI | What it measures | Data source |
|---|---|---|
| Interfaces on the platform | Share of interfaces off point-to-point | Interface inventory |
| Systems retired | Applications switched off | Application inventory |
| Data products live | Owned, governed data products | Data catalog |
| Gap closure | Gaps closed vs planned | Architecture roadmap |
