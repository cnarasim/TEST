---
id: sc-pl-inventory-policy
domain: Supply Chain
l1: Plan
l2: Safety stock and inventory policy
summary: How much stock to hold where: service targets by item class, safety stock from demand and lead-time variability, regular review.
systems: Planning system, ERP inventory, BI dashboards
tags: safety stock, inventory policy, service level, ABC, XYZ, reorder point, days of supply
order: 105
---
# Safety stock and inventory policy

## What inventory policy covers
### Purpose
- The right stock to meet the service target
- No more cash in stock than the target needs
### In scope
- Service targets by item class and channel
- Safety stock, reorder points, review cycle
### Outcome
- In stock on the items guests buy most
- Less excess and slow-moving stock

## Targets follow item value and demand
Layout: matrix
- High value, steady demand: high service, lean safety stock
- High value, erratic demand: high service, buffer reviewed weekly
- Low value, steady demand: standard service, reorder in bulk
- Low value, erratic demand: lower service, order on demand or drop

## Planners set targets, rules do the math
Layout: swimlane handoffs
- Inventory planning: Sets service targets by class
- Planning system: Calculates safety stock
- Inventory planning: Change over tolerance?
- Inventory planning: If yes, reviews and approves it
- Inventory planning: If no, accepts it automatically
- Planning system: Updates reorder points
- Finance: Reviews inventory value vs plan

## Systems and data for inventory policy
| Step | What the system does | Records it keeps |
|---|---|---|
| Classify | Ranks items by value and variability | ABC and XYZ class |
| Target | Applies a service level by class | Service targets |
| Calculate | Safety stock from demand and lead time | Safety stock, reorder point |
| Monitor | Tracks stock against the policy | Days of supply, excess |
| Review | Flags items to change or retire | Policy changes |

## Safety stock in four steps
Layout: process numbered
- Measure: demand variability by item and location
- Add: lead time and its variability
- Apply: the service factor for the class
- Review: monthly, and after big lead-time changes

## KPIs that show it works
| KPI | What it measures | Data source |
|---|---|---|
| In-stock rate | Items on shelf when guests look | Store stock snapshots |
| Days of supply | Stock divided by daily demand | Inventory and forecast |
| Excess inventory | Stock above the policy maximum | Inventory vs policy |
| Service level achieved | Demand filled from stock | Orders and sales |

## Today and target
### Today
- One safety stock rule for every item
- Excess builds while fast sellers run out
### Target
- Targets set by item class and channel
- Policy reviewed monthly with finance
