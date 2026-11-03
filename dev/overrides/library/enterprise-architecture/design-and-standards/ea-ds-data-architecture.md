---
id: ea-ds-data-architecture
domain: Enterprise Architecture
l1: Design and Standards
l2: Data architecture
summary: How data moves from the systems of record into governed data products for reports, apps and AI, with owners, zones and quality rules.
systems: Data platform, Data catalog, ERP, OMS, WMS, CRM
tags: data architecture, data platform, data products, data zones, system of record, data catalog, lineage
order: 607
---
# Data architecture

## What data architecture covers
### Purpose
- Trusted data for reports, apps and AI
- One copy of each data set, with an owner
### In scope
- Sources, platform zones and data products
- Ownership, quality, lineage and access
### Outcome
- Faster answers from data people trust
- Fewer copies and conflicting numbers

## Data moves in five steps
Layout: process chevrons
- Capture: in the system of record
- Ingest: to the platform by stream or batch
- Model: into governed data products
- Serve: to reports, apps and AI
- Govern: owners, quality and access

## Zones on the data platform
| Zone | What it holds | Who uses it |
|---|---|---|
| Raw | Data as it arrived, kept for replay | Data engineers |
| Clean | Checked, standardized and joined | Analysts, data scientists |
| Curated | Data products with owners and service levels | Business teams, apps |
| Sandbox | Short-lived space to explore | Data scientists |

## Each data domain has an owner
| Domain | System of record | Data owner |
|---|---|---|
| Product | Merchandising system and PIM | Merchandising |
| Guest | CRM and loyalty platform | Marketing |
| Inventory | WMS and ERP inventory | Supply chain |
| Orders | OMS | Ecommerce operations |
| Financials | ERP | Finance |

## A new data product follows one path
Layout: swimlane handoffs
- Business team: Requests a data product
- Data owner: Approves meaning and access
- Data platform team: Builds the pipeline
- Data platform team: Quality checks pass?
- Data platform team: If yes, publishes it
- Data platform team: If no, fixes at the source

## KPIs that show it works
| KPI | What it measures | Data source |
|---|---|---|
| Owned data products | Products with a named owner | Data catalog |
| Quality checks passed | Checks passing each day | Data quality tool |
| Freshness | Products updated on schedule | Pipeline monitoring |
| Copies retired | Duplicate data sets removed | Data catalog |
