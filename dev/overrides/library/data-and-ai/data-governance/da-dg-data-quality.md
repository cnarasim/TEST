---
id: da-dg-data-quality
domain: Data and AI
l1: Data Governance
l2: Data quality management
summary: Measuring and fixing data quality at the source: quality dimensions, rules and scorecards, and the loop from issue to root cause.
systems: Data quality tool, Data platform, Data catalog, Ticketing tool
tags: data quality, completeness, accuracy, validity, timeliness, data quality rules, scorecard
order: 102
---
# Data quality management

## What data quality covers
### Purpose
- Data good enough for the decisions it feeds
- Problems fixed at the source, not in reports
### In scope
- Rules, scores and thresholds
- Issue triage and root-cause fixes
### Outcome
- Fewer wrong orders, prices and reports
- Trust in the numbers leaders use

## Six ways data can be wrong
Layout: process list
- Complete: every required field is filled
- Accurate: matches the real world
- Valid: in the right format and range
- Consistent: the same in every system
- Timely: there when it is needed
- Unique: one record per real thing

## Quality runs as a loop
Layout: process cycle
- Define: rules for the data that matters most
- Measure: scores every day
- Alert: owners when a score drops
- Fix: at the source, not downstream
- Prevent: change the process or the system

## Example rules for retail data
| Data | Rule | Dimension |
|---|---|---|
| Item | Every active item has a size and weight | Complete |
| Price | No price below cost without approval | Valid |
| Vendor | One vendor record per tax number | Unique |
| Inventory | Stock matches between WMS and ERP | Consistent |
| Store sales | Loaded by [time] each morning | Timely |

## Owners fix the source
Layout: swimlane handoffs
- Data quality tool: Flags the failed rule
- Data steward: Finds the root cause
- Data steward: Source system to blame?
- Data steward: If yes, fixes it with the owner
- Data steward: If no, fixes the pipeline
- Data owner: Approves the prevention step

## KPIs that show it works
| KPI | What it measures | Data source |
|---|---|---|
| Quality score | Records passing their rules | Data quality tool |
| Rules in place | Key data with active rules | Rule catalog |
| Time to fix | Days from alert to fix | Issue log |
| Repeat issues | Issues with the same root cause | Issue log |
