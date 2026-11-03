---
id: sc-wh-returns
domain: Supply Chain
l1: Warehouse & Inventory
l2: DC returns processing
summary: Guest and store returns at the DC: receipt against the order, grading, the disposition decision and the refund and stock records.
systems: WMS, OMS, ERP, Returns portal
tags: returns, reverse logistics, disposition, grading, restock, refund, returns to DC
order: 410
---
# DC returns processing

## What DC returns cover
### Purpose
- Refunds on time for guests who return by mail
- The most value recovered from each return
### In scope
- Mail returns and store returns to the DC
- Grading, disposition and refunds
### Outcome
- Faster refunds and fewer guest contacts
- Sellable items back in stock within days

## Returns flow back through the network
Layout: retail returns

## Every return gets one disposition
Layout: swimlane handoffs
- Receiving: Scans returns to their orders
- Returns team: Grades the item
- Returns team: Sellable as new?
- Returns team: If yes, restocks it
- Returns team: If no, sends to RTV or disposal
- Finance: Posts the refund and write-off

## Condition decides the disposition
| Condition | Disposition | Owner |
|---|---|---|
| Unopened, undamaged | Restock to sellable stock | Returns team |
| Damaged packaging | Repack or return to the vendor | Returns team |
| Opened or used | Destroy or donate per policy | Returns lead |
| Defective | Return to the vendor for credit | Vendor compliance |
| Recalled | Quarantine for the recall | Quality |

## Systems and data for returns
| Step | What the system does | Records it keeps |
|---|---|---|
| Authorize | Issues the return label | Return authorization |
| Receive | Matches the parcel to the order | Return receipt |
| Grade | Records condition and disposition | Grade, reason code |
| Refund | Releases the guest refund | Refund, payment record |
| Stock | Restocks or writes off the item | Inventory movement |

## KPIs that show it works
| KPI | What it measures | Data source |
|---|---|---|
| Dock to refund | Days from receipt to refund | Return receipts, refunds |
| Restock rate | Returned units restocked | Dispositions |
| Return backlog | Parcels waiting to be graded | Return receipts |
| Write-off value | Value destroyed or donated | Inventory movements |

## Today and target
### Today
- Returns wait weeks before grading
- Guests chase refunds by phone
### Target
- Graded and refunded within [n] days
- Clear rules for every condition
