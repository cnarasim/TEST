---
id: sc-wh-cycle-count
domain: Supply Chain
l1: Warehouse & Inventory
l2: Cycle count
summary: Continuous counting by ABC class instead of a wall-to-wall count: plan, count, recount, post differences, find root cause.
systems: WMS, ERP inventory, Handheld scanning
tags: cycle count, physical inventory, ABC, shrink, inventory accuracy, count
order: 404
---
# Cycle count

Count a little every day, so the books are always right and the year-end count goes away.

## What cycle count covers
### Purpose
- Keep book stock equal to physical stock
- Find and fix the cause of every difference
### In scope
- ABC classes and count frequency
- Count, recount, approval and posting
### Outcome
- Inventory accuracy above the agreed target
- Shrink explained by cause, not written off

## Counters count, inventory control approves
Layout: swimlane handoffs
- Inventory control: Creates the day's count documents
- Counter: Counts every listed bin
- Counter: Difference over tolerance?
- Counter: If yes, recount the bin
- Counter: If no, confirm the count
- Inventory control: Approves the differences
- Finance: Reviews the value posted

## Systems and data for cycle count
| Step | What the system does | Records it keeps |
|---|---|---|
| ABC classes | Items classed by value and velocity; class sets the count frequency | Item classification |
| Count lists | A daily count list by location from the plan | Count document |
| Count entry | Counters scan every bin on a handheld | Counted quantity by bin |
| Recount | Differences over tolerance create a recount task | Recount result |
| Post differences | Approved differences adjust stock and the ledger | Inventory adjustment, ledger posting |
| Root cause | Each large difference gets a cause code | Difference reason |

## Five steps turn counts into accurate stock
Layout: retail inventory-count

## Controls and exceptions
| Control | How it works | Owner |
|---|---|---|
| Book stock frozen | Postings blocked for the bin while it is counted | Inventory control |
| Blind count | Counters do not see the book quantity | DC lead |
| Recount threshold | Differences over value or percent are recounted | Inventory control |
| Approval by value | Large differences need a manager to post | Inventory manager |

## KPIs that show it works
| KPI | What it measures | Data source |
|---|---|---|
| Inventory record accuracy | Bins whose count matched the book | Count results by bin |
| Net difference value | Value of gains and losses posted | Inventory adjustments |
| Count plan compliance | Planned counts done on time | Count lists created vs counted |
| Shrink rate | Loss as a share of sales | Adjustment value vs sales |

## Today and target
### Today
- One wall-to-wall count a year closes the DC
- Differences written off without a cause
### Target
- A daily ABC count: A items monthly, C items yearly
- Every large difference has a root cause code
