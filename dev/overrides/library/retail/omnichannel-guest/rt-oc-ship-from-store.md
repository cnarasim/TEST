---
id: rt-oc-ship-from-store
domain: Retail
l1: Omnichannel & Guest
l2: Ship from store
summary: Online orders picked, packed and shipped from store stock: store eligibility, routing, pick and pack, carrier pickup and short picks.
systems: OMS, Store fulfillment app, Parcel shipping system, Store inventory
tags: ship from store, store fulfillment, parcel, carrier pickup, short pick, split shipment
order: 404
---
# Ship from store

## What ship from store covers
### Purpose
- Sell store stock to online guests anywhere
- Ship from closer to the guest, faster
### In scope
- Store eligibility, routing, pick and pack
- Labels, carrier pickup, tracking, short picks
### Outcome
- Fewer online cancels when the DC is out
- Store stock that sells before markdown

## The store packs, the carrier collects
Layout: swimlane handoffs
- OMS: Routes to the best store
- Store team: Accepts on the store app
- Store team: Picks every unit
- Store team: All units found?
- Store team: If yes, pack and print the label
- OMS: If no, re-route the short items
- Carrier: Collects at the daily pickup
- Guest: Tracks and receives the parcel

## Systems and data for ship from store
| Step | What the system does | Records it keeps |
|---|---|---|
| Eligibility | Rules set which stores and items can ship | Store and item eligibility |
| Routing | The OMS picks the store by stock, distance and cost | Sourcing decision, store order |
| Pick and pack | The store app guides the pick and suggests a carton | Pick task, carton, weight |
| Ship | A carrier label prints and tracking goes to the guest | Shipment, tracking number |

## Six steps from store shelf to doorstep
Layout: process arrow
- Route: the OMS picks the store
- Accept: the store confirms capacity
- Pick: every unit scanned
- Pack: carton, fill and packing slip
- Label: carrier label and tracking
- Hand off: at the daily carrier pickup

## Controls and exceptions
| Control | How it works | Owner |
|---|---|---|
| Store capacity | Each store takes orders up to its daily limit | Omnichannel operations |
| Hazmat rules | Polish, aerosols, fragrance: trained packers, ground only | Environmental compliance |
| Pick scan | Every unit scanned against the order | Store team |
| Carrier scan | Parcels the carrier did not scan are chased next day | Store manager |

## KPIs that show it works
| KPI | What it measures | Data source |
|---|---|---|
| Ship-from-store share | Online units shipped from stores | OMS shipments by source |
| Pick-to-ship time | Store order received to carrier scan | Store app and carrier scans |
| Short-pick rate | Units the store could not find | Pick exceptions |
| Cost per parcel | Labor, packaging and freight per parcel | Labor hours, carrier invoices |

## Today and target
### Today
- Stores ship only when the DC is out of stock
- Short picks re-routed by hand, orders slip
### Target
- Routing on stock, distance, cost and capacity
- Short picks re-routed by the OMS at once
