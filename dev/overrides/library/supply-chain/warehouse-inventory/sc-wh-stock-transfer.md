---
id: sc-wh-stock-transfer
domain: Supply Chain
l1: Warehouse & Inventory
l2: Stock transfers between sites
summary: Stock moved between DCs and stores on a transfer order: delivery, goods issue, in-transit and receipt.
systems: ERP inventory, WMS, Transportation
tags: stock transfer, transfer order, transfer, in transit, intercompany
order: 405
---
# Stock transfers between sites

## What this process covers
### Purpose
- Move stock to where it sells
- Know what is in transit and who owns it
### In scope
- DC-to-store, store-to-store and DC-to-DC
- Same company and cross-company transfers
### Outcome
- Stock in transit visible and valued
- Receipt closes the transfer every time

## The sending site ships, the receiving site closes the loop
Layout: swimlane handoffs
- Planner: Creates the transfer order
- Sending site: Creates the delivery
- Sending site: Picks and posts goods issue
- Receiving site: Receives the shipment
- Receiving site: Quantity matches?
- Receiving site: If yes, post goods receipt
- Inventory control: If no, investigate the difference

## The systems and data it runs on
| Step | What the system does | Records it keeps |
|---|---|---|
| Transfer order | Says what moves where, and when | Transfer document |
| Delivery | The sending site creates the delivery | Outbound delivery |
| Goods issue | Stock moves into in-transit | Goods issue, in-transit stock |
| In transit | In-transit stock is visible and valued | In-transit list |
| Goods receipt | The receiving site posts the receipt | Goods receipt, ledger posting |

## Four documents move stock between sites
Layout: retail document-flow
- Transfer order: what moves where (Planner)
- Delivery: what is picked (Sending site)
- Goods issue: stock in transit (Sending site)
- Goods receipt: stock at the receiver (Receiving site)

## Controls and exceptions
| Control | How it works | Owner |
|---|---|---|
| In-transit ageing | Transfers in transit beyond a week alert | Inventory control |
| Receipt against delivery | Receipts reference the delivery | Receiving site |
| Cross-company pricing | Transfer price from the price agreement | Finance |
| Approval for store-to-store | Manager approval above a value | Store operations |

## KPIs that show it works
| KPI | What it measures | Data source |
|---|---|---|
| In-transit days | Goods issue to goods receipt | Goods issue vs goods receipt dates |
| Transfer accuracy | Receipts that match the shipment | Shipped vs received |
| Open transfers | Transfers not received after a week | In-transit list |
| Transfer cost per unit | Freight and handling per unit moved | Freight cost and volume |

## Today and target
### Today
- Transfers by e-mail, received without reference
- In-transit stock invisible to planners
### Target
- Every move on a transfer order
- In-transit stock in the plan and the balance sheet
