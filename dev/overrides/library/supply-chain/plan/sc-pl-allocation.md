---
id: sc-pl-allocation
domain: Supply Chain
l1: Plan
l2: Allocation (push to stores)
summary: New and seasonal merchandise split across stores by rule, then turned into store orders and deliveries.
systems: Allocation, ERP, WMS
tags: allocation table, push, launch, seasonal, store grades
order: 102
---
# Allocation (push to stores)

## What allocation (push to stores) covers
### Purpose
- Put new product where it sells first
- Ship launch quantities from one plan
### In scope
- Allocation rules, store grades, pack sizes
- Follow-on documents: POs, transfers, deliveries
### Outcome
- Every store has its launch quantity on day one
- Remaining stock held at the DC to chase

## Allocation splits a buy across stores
Layout: swimlane handoffs
- Merchant: Confirms buy and launch date
- Allocator: Builds the allocation table
- Allocator: Quantities fit store grades?
- Allocator: If yes, release the table
- Allocator: If no, adjust rules or pack size
- DC: Receives and splits the delivery
- DC: Ships the store deliveries
- Stores: Receive and set the launch

## The systems and data it runs on
| Step | What the system does | Records it keeps |
|---|---|---|
| Allocation rule | Rules split a buy by store grade, climate and pack size | Rule, store grades, shares |
| Allocation plan | The allocation tool proposes a quantity per store | Allocation header and lines |
| Follow-on orders | The plan creates purchase orders and DC-to-store transfers | Purchase orders, transfer orders |
| Ship to stores | The WMS picks and ships each store delivery | Outbound deliveries, goods issue |
| Store receipt | Stores confirm the delivery on a handheld | Goods receipt |

## From buy to store shelf
Layout: process numbered
- Buy: quantity and launch date
- Rules: grades and pack sizes
- Table: quantity per store
- Documents: POs and transfers
- Ship: DC to stores
- Chase: reorder what sells

## Controls and exceptions
| Control | How it works | Owner |
|---|---|---|
| Pack-size rounding | Store quantities round to the vendor pack | Allocator |
| Launch date gate | Deliveries cannot arrive before the set date | DC planning |
| Reserve hold-back | A share of the buy stays at the DC | Merchant |
| Grade review | Store grades refreshed every season | Planning manager |

## KPIs that show it works
| KPI | What it measures | Data source |
|---|---|---|
| Sell-through at week 4 | Share of the allocation sold in four weeks | Sales vs allocated quantity |
| Allocation accuracy | Stores that sold within plus or minus 20 percent | Allocated vs sold by store |
| Store-to-store transfers | Units moved after launch to fix the split | Store-to-store transfer volume |
| On-time launch | Stores set on the launch date | Receipt date vs launch date |

## Today and target
### Today
- Allocations built in spreadsheets and keyed by hand
- One rule for every store, whatever it sells
### Target
- Rules by store grade and climate in the allocation tool
- Follow-on documents created in one run
