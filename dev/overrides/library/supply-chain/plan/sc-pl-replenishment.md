---
id: sc-pl-replenishment
domain: Supply Chain
l1: Plan
l2: Store replenishment (pull)
summary: Automatic store orders from forecast, stock on hand and presentation minimums, sourced from the DC or the vendor.
systems: Replenishment, ERP, WMS, POS
tags: replenishment, auto-replenishment, reorder point, store orders, pull
order: 103
---
# Store replenishment (pull)

## What store replenishment (pull) covers
### Purpose
- Keep shelves full without overstock
- Order what sold, every day
### In scope
- Replenishment parameters, run and order release
- DC-sourced and direct-store-delivery orders
### Outcome
- Store orders created without a person
- Stock in line with sales and shelf capacity

## The system orders, people work exceptions
Layout: swimlane handoffs
- POS: Posts yesterday's sales
- Replenishment run: Calculates the order quantity
- Replenishment run: Quantity above the limit?
- Inventory analyst: If yes, review and approve
- Inventory analyst: If no, release automatically
- DC: Picks and ships store orders
- Store team: Receives and fills the shelf

## The systems and data it runs on
| Step | What the system does | Records it keeps |
|---|---|---|
| Parameters | Each store-item keeps its target stock, safety stock and shelf minimum | Replenishment parameters |
| Stock and sales | POS sales and receipts update store stock every night | Store stock, sales |
| Replenishment run | The engine compares forecast, stock and on-order | Order proposals |
| Store orders | Approved proposals become transfer or vendor orders | Transfer orders, purchase orders |
| Ship and receive | The DC ships; the store receives against the ASN | Deliveries, goods receipts |

## Six steps keep store shelves full
Layout: retail store-replenishment

## Controls and exceptions
| Control | How it works | Owner |
|---|---|---|
| Presentation minimum | Shelf minimums keep the display full | Space planning |
| Order limit | Orders above a quantity or value wait for review | Inventory analyst |
| Stock accuracy first | Sites with poor count accuracy are reviewed | Inventory control |
| Parameter review | Target and safety stock reviewed each season | Replenishment manager |

## KPIs that show it works
| KPI | What it measures | Data source |
|---|---|---|
| In-stock rate | Store-SKUs with stock on the shelf | Store stock, daily |
| Weeks of supply | Stock in weeks of forecast sales | Stock and forecast |
| Auto-order share | Store orders released with no touch | Proposals released vs changed |
| Store order fill rate | Units shipped vs ordered | Ordered vs shipped |

## Today and target
### Today
- Store teams order by eye on a handheld
- Overstock in slow stores, gaps in fast ones
### Target
- Automatic orders from forecast and stock
- People manage the exceptions only
