---
id: da-an-kpi-definitions
domain: Data and AI
l1: Analytics
l2: KPI definitions and catalog
summary: One agreed definition for every business KPI: formula, source, owner and grain, kept in a catalog and used by every report.
systems: Data catalog, Semantic layer, BI dashboards, Data platform
tags: KPI definitions, metrics catalog, business glossary, semantic layer, single source of truth, comparable sales
order: 203
---
# KPI definitions and catalog

## What the KPI catalog covers
### Purpose
- One definition for each KPI, used everywhere
- Numbers that match across every report
### In scope
- Formula, source, grain and owner
- Changes, versions and certification
### Outcome
- Meetings spent on actions, not on numbers
- Faster, consistent reports

## Every KPI has one card
| Field | What it holds | Example |
|---|---|---|
| Name and meaning | Plain-language definition | Units per transaction |
| Formula | How it is calculated | Units sold / transactions |
| Source | The data product it uses | Store sales data product |
| Grain | The lowest level it is valid at | Store and day |
| Owner | Who approves changes | Retail analytics |

## Changes are approved once
Layout: swimlane handoffs
- Requester: Proposes a new or changed KPI
- KPI owner: Reviews the definition
- KPI owner: Conflicts with another KPI?
- KPI owner: If yes, takes it to the council
- KPI owner: If no, approves and versions it
- Analytics team: Updates the semantic layer

## Five steps to a certified KPI
Layout: process numbered
- Define: name, meaning and formula
- Source: a governed data product
- Test: matches finance or the agreed baseline
- Certify: owner signs and the catalog marks it
- Publish: in the semantic layer for every report

## KPIs that show it works
| KPI | What it measures | Data source |
|---|---|---|
| Certified KPIs | KPIs with an approved card | KPI catalog |
| Reports on certified KPIs | Reports using the semantic layer | BI catalog |
| Definition conflicts | Disputes raised each quarter | Council log |
| Change time | Days to approve a change | KPI catalog |

## Today and target
### Today
- Each team defines its own version
- Leaders argue about whose number is right
### Target
- One card per KPI in the catalog
- Every report uses the certified definition
