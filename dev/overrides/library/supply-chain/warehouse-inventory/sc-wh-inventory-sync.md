---
id: sc-wh-inventory-sync
domain: Supply Chain
l1: Warehouse & Inventory
l2: Inventory reconciliation between systems
summary: Keeping one stock number across ERP, WMS and OMS: daily snapshots, compared by item and status, differences explained and fixed at the cause.
systems: ERP inventory, WMS, OMS, Integration platform
tags: inventory reconciliation, stock sync, ERP WMS variance, interface errors, available to sell, inventory accuracy
order: 413
---
# Inventory reconciliation between systems

## What reconciliation covers
### Purpose
- One stock number in ERP, WMS and OMS
- Differences found and fixed every day
### In scope
- DC, store and in-transit stock
- Snapshots, variances and their causes
### Outcome
- Accurate available-to-sell online
- A clean inventory value at month end

## Five steps run every night
Layout: process chevrons
- Snapshot: each system at the same cut-off
- Compare: by item, location and status
- Explain: messages still in flight
- Correct: adjust with a reason code
- Prevent: fix the cause, not the number

## Inventory control owns the difference
Layout: swimlane handoffs
- Integration: Sends the nightly snapshots
- Inventory control: Compares by item and status
- Inventory control: Over the tolerance?
- Inventory control: If yes, researches the cause
- Inventory control: If no, closes the item
- Finance: Reviews adjustment value

## Where differences come from
| Cause | Example | Fix |
|---|---|---|
| Messages in flight | Receipt posted in WMS only | Compare at one cut-off |
| Failed messages | An interface error not resent | Resend and alert on failure |
| Status mismatch | On hold in WMS, available in ERP | Map statuses one to one |
| Unit of measure | Cases in one system, eaches in another | Fix the item master |
| One-sided changes | Adjusted in one system only | Adjust through one system |

## KPIs that show it works
| KPI | What it measures | Data source |
|---|---|---|
| Matched items | Items equal in every system | Reconciliation report |
| Variance value | Value of open differences | Reconciliation report |
| Failed messages | Interface errors per day | Integration monitoring |
| Time to resolve | Days a difference stays open | Variance log |

## Today and target
### Today
- Differences found at month end
- Fixes made in whichever system is open
### Target
- Compared nightly, fixed within a day
- Every adjustment through one system
