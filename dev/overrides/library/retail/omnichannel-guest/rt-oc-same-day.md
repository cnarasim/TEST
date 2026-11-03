---
id: rt-oc-same-day
domain: Retail
l1: Omnichannel & Guest
l2: Same-day delivery
summary: Orders delivered from a nearby store within hours by a courier partner: zones, cut-off, pick, driver dispatch, hand-off and proof of delivery.
systems: OMS, Store fulfillment app, Courier partner integration, Payments
tags: same-day delivery, courier, last mile, delivery partner, store fulfillment, proof of delivery
order: 405
---
# Same-day delivery

## What same-day delivery covers
### Purpose
- Deliver the order within hours of the click
- Win on speed using the store network
### In scope
- Delivery zones, eligible items, cut-off times
- Driver dispatch, hand-off, proof of delivery
### Outcome
- Orders at the door the same day
- A known cost per delivery, by store

## The store picks, the courier delivers
Layout: swimlane handoffs
- Guest: Orders before the cut-off
- OMS: Picks a store in range
- Store team: Picks and bags the order
- Courier partner: Dispatches a nearby driver
- Store team: Driver here on time?
- Store team: If yes, verify and hand over
- Courier partner: If no, send a new driver
- Courier partner: Delivers with photo proof

## Systems and data for same-day delivery
| Step | What the system does | Records it keeps |
|---|---|---|
| Eligibility | Address, items and cut-off checked at checkout | Delivery zone, cut-off time |
| Dispatch | The OMS books a driver through the courier API | Delivery request, driver ETA |
| Hand-off | The store scans the bag to the driver | Hand-off scan and time |
| Proof of delivery | The courier sends status and a photo back | Delivery status, photo, fee |

## A same-day order runs on the clock
Layout: process numbered
- Order: before the store's cut-off
- Pick: within [n] minutes
- Book: a driver timed to the pack
- Hand off: bag scanned to the driver
- Deliver: photo proof to the guest

## Controls and exceptions
| Control | How it works | Owner |
|---|---|---|
| Delivery zone | Only addresses in a store's radius see the option | Ecommerce team |
| Order cut-off | Orders after the cut-off move to the next day | Omnichannel operations |
| Hand-off check | Driver and order code checked before release | Store team |
| Undelivered orders | Bags not delivered return to the store that day | Courier partner |

## KPIs that show it works
| KPI | What it measures | Data source |
|---|---|---|
| Delivered same day | Orders delivered by the promised time | Order and delivery times |
| Driver wait time | Driver arrival to hand-off | Courier events, hand-off scan |
| First-try delivery | Orders delivered on the first attempt | Courier status |
| Cost per delivery | Courier fee and store labor per order | Courier invoices, labor hours |

## Today and target
### Today
- Drivers wait while the order is still picked
- Delivery status checked on the courier's site
### Target
- Drivers booked to arrive as packing ends
- Courier events in the OMS and the guest's app
