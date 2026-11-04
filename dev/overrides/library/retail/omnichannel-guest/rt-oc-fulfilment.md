---
id: rt-oc-fulfilment
domain: Retail
l1: Omnichannel & Guest
l2: Omnichannel order fulfilment
summary: One online order routed to the best source: ship from DC, ship from store, buy online pick up in store, same-day.
systems: OMS, ERP, Store fulfilment app, WMS
tags: BOPIS, ship from store, same day, sourcing, order routing, ecommerce
order: 401
---
# Omnichannel order fulfilment

## What omnichannel order fulfilment covers
### Purpose
- Meet the guest's promise at the lowest cost
- Use store stock to save the sale
### In scope
- Order capture, sourcing and routing
- Ship from DC or store, pick-up, same-day
### Outcome
- More orders filled complete and on time
- Lower split shipments and cancellations

## Orders route automatically, stores pick
Layout: swimlane handoffs
- Guest: Places the order online
- Order management: Picks the best source
- Order management: In stock nearby?
- Order management: If yes, send to the store
- Order management: If no, ship from the DC
- Store team: Picks and stages the order
- Guest: Collects or receives it

## The systems and data it runs on
| Step | What the system does | Records it keeps |
|---|---|---|
| Order capture | The order management system takes the online order | Customer order |
| Sourcing | Rules pick the DC or store with stock | Sourcing decision |
| Store picking | Store associates pick and stage on an app | Pick tasks, pickup status |
| Ship from DC | The WMS picks and ships the parcel | Shipment, tracking number |
| Settle | Payment captured when the order ships or is collected | Invoice, payment capture |

## An online order reaches guests four ways
Layout: retail omnichannel-fulfilment

## Controls and exceptions
| Control | How it works | Owner |
|---|---|---|
| Safety stock for online | Store stock below a buffer is not offered | Omnichannel planning |
| Pick time limit | Orders not picked in two hours re-route | Store operations |
| Payment capture on ship | Cards captured only when shipped | Payments team |
| Cancellation reasons | Every cancel carries a reason | Customer care |

## KPIs that show it works
| KPI | What it measures | Data source |
|---|---|---|
| Fill rate | Units shipped vs ordered | Ordered vs shipped |
| Click-to-ready time | Order to ready for pick-up | Order and pick times |
| Split shipment rate | Orders shipped in more than one parcel | Shipments per order |
| Cost per order | Fulfilment cost per online order | Labour, freight, packaging |

## Today and target
### Today
- Online orders ship only from the DC
- Store stock invisible to the website
### Target
- Real-time sourcing across DCs and stores
- Pick-up ready in hours, not days
