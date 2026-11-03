---
id: sc-sp-drop-ship
domain: Supply Chain
l1: Source & Procure
l2: Drop ship from vendors
summary: Vendors ship online orders straight to the guest: the stock feed, order routing, ship confirmation, invoicing and returns.
systems: OMS, Vendor portal, EDI, ERP, Ecommerce platform
tags: drop ship, vendor direct, extended assortment, inventory feed, ship confirm, EDI 856, endless aisle
order: 206
---
# Drop ship from vendors

## What drop ship covers
### Purpose
- A wider assortment online without DC stock
- The same promise as items we ship ourselves
### In scope
- Stock feeds, order routing and ship confirms
- Vendor invoices, returns and scorecards
### Outcome
- More items for guests, no inventory risk
- Vendors held to one service standard

## The vendor ships, the guest sees one order
Layout: swimlane handoffs
- Guest: Orders on ulta.com or the app
- OMS: Routes the line to the vendor
- Vendor: Can ship within the promise?
- Vendor: If yes, ships and sends tracking
- Vendor: If no, rejects the line
- OMS: Updates the guest, refunds if needed

## Systems and data for drop ship
| Step | What the system does | Records it keeps |
|---|---|---|
| Stock feed | Loads vendor stock every [n] hours | Available quantity by item |
| Route | Sends the order line to the vendor | Vendor order, EDI 850 |
| Ship confirm | Reads tracking from the vendor | EDI 856, tracking number |
| Invoice | Matches the bill to the ship confirm | Vendor invoice, EDI 810 |
| Returns | Sends returned items back or to stock | Return record, credit |

## The standard every drop-ship vendor signs
| Rule | Standard | Owner |
|---|---|---|
| Stock feed | Updated at least every [n] hours | Vendor |
| Ship time | Shipped within [n] business days | Vendor |
| Packing | Ulta packing slip, no vendor marketing | Vendor |
| Tracking | Sent the same day the order ships | Vendor |
| Returns | Accepted at stores and by mail | Ecommerce operations |

## KPIs that show it works
| KPI | What it measures | Data source |
|---|---|---|
| On-time ship | Orders shipped within the standard | Ship confirms vs order date |
| Vendor cancel rate | Lines the vendor rejects | OMS order lines |
| Feed accuracy | Stock feed vs what ships | Feed vs rejects |
| Guest contacts | Questions per drop-ship order | Guest care cases |

## Today and target
### Today
- Stock feeds daily, so items oversell
- Each vendor follows its own rules
### Target
- Feeds near real time, few rejected lines
- One scorecard for every drop-ship vendor
