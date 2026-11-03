---
id: sc-wh-lot-expiry
domain: Supply Chain
l1: Warehouse & Inventory
l2: Lot and expiry control
summary: Capturing lot and expiry at receipt, holding minimum shelf life, picking first-expiring first and pulling stock before it expires.
systems: WMS, ERP inventory, Quality system
tags: lot control, expiry, FEFO, shelf life, batch, traceability, sunscreen
order: 412
---
# Lot and expiry control

## What lot and expiry control covers
### Purpose
- Guests get products with life left to use
- Any lot traced in minutes, not days
### In scope
- Lot and expiry capture at receipt
- FEFO picking and near-expiry pulls
### Outcome
- Less expired stock written off
- Recalls narrowed to the affected lots

## Shelf life is protected in five steps
Layout: process numbered
- Capture: lot and expiry date at receipt
- Check: remaining shelf life against the rule
- Store: stock kept apart by lot
- Pick: first expiring, first out (FEFO)
- Pull: near-expiry stock before it reaches stores

## Receiving checks life before putaway
Layout: swimlane handoffs
- Receiving: Scans the lot and expiry date
- WMS: Checks the remaining shelf life
- WMS: Enough life left?
- WMS: If yes, directs putaway by lot
- WMS: If no, holds it for the vendor
- Inventory control: Reviews near-expiry stock

## Shelf-life rules
| Rule | Standard | Owner |
|---|---|---|
| Receipt minimum | At least [n]% of shelf life left | Quality |
| Store shipment minimum | At least [n] days of life left | Quality |
| Pick order | First expiring, first out | WMS |
| Near-expiry pull | Pulled [n] days before expiry | Inventory control |
| Lot trace | Lot recorded on every move | DC operations |

## KPIs that show it works
| KPI | What it measures | Data source |
|---|---|---|
| Expired write-offs | Value of stock that expired | Inventory adjustments |
| Short-life receipts | Receipts held for low shelf life | Receiving holds |
| FEFO compliance | Picks from the first-expiring lot | Pick confirmations |
| Lot trace time | Minutes to locate every unit of a lot | Recall drills |

## Today and target
### Today
- Expiry checked by eye, if at all
- A recall means pulling every lot
### Target
- Lot and expiry scanned on every receipt
- Any lot located in under [n] minutes
