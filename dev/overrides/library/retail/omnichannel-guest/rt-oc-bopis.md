---
id: rt-oc-bopis
domain: Retail
l1: Omnichannel & Guest
l2: Buy online, pick up in store
summary: Online orders picked from store stock and collected at the counter or the curb: route, pick, stage, notify, hand over, restock no-shows.
systems: OMS, Store fulfillment app, POS, Store inventory
tags: BOPIS, buy online pick up in store, curbside, click and collect, store pickup, ready for pickup
order: 403
---
# Buy online, pick up in store

## What store pickup and curbside cover
### Purpose
- Get the order to the guest the same day
- Turn store stock into online sales
### In scope
- Store routing, pick, staging and ready notice
- Counter, curbside and locker hand-over
### Outcome
- Orders ready inside the promised time
- Add-on sales when guests come in to collect

## Stores pick and stage, guests collect
Layout: swimlane handoffs
- Guest: Orders online for pickup
- OMS: Routes to the chosen store
- Store team: Picks on the store app
- Store team: Every item found?
- Store team: If yes, stage and notify the guest
- Store team: If no, cancel the short item
- Guest: Arrives in store or curbside
- Store team: Verifies and hands over

## Systems and data for store pickup
| Step | What the system does | Records it keeps |
|---|---|---|
| Order and route | The OMS sends the order to the pickup store | Customer order, store order |
| Pick and stage | The store app guides the pick and the staging bin | Pick task, staging location |
| Notify | Ready and reminder messages by text, e-mail and app | Ready notice, reminders |
| Hand over | The order code is scanned at the counter or the curb | Pickup confirmation, payment capture |

## Six steps from click to collect
Layout: process chevrons
- Order: the guest picks a store and pays
- Route: the OMS checks store stock
- Pick: on the store app, by promise time
- Stage: bagged, labeled and binned
- Notify: a ready message with a code
- Collect: counter, curbside or locker

## Controls and exceptions
| Control | How it works | Owner |
|---|---|---|
| Pick time limit | Orders not picked by the promise time escalate | Store manager |
| Safety stock | Store stock under a buffer is not offered for pickup | Omnichannel planning |
| Pickup verification | Order code or ID checked before hand-over | Store team |
| Unclaimed orders | Orders not collected in [n] days are canceled and restocked | Store operations |

## KPIs that show it works
| KPI | What it measures | Data source |
|---|---|---|
| Order-to-ready time | Order placed to ready for pickup | OMS order and pick times |
| On-time ready rate | Orders ready inside the promised time | Promise vs ready time |
| Fill rate | Units handed over vs units ordered | Ordered vs picked units |
| Curbside wait | Guest check-in to hand-over, in minutes | Check-in and hand-over scans |

## Today and target
### Today
- Pick lists printed, orders staged by hand
- Curbside guests call the store to say they arrived
### Target
- App-guided picks with promise-time alerts
- App check-in on arrival, hand-over in minutes
