---
id: sc-tr-parcel
domain: Supply Chain
l1: Deliver
l2: Parcel shipping and carriers
summary: Shipping online orders by parcel: choosing the carrier and service, labels and manifests, pickups, tracking and delivery exceptions.
systems: Parcel shipping system, WMS, OMS, TMS
tags: parcel, carrier selection, rate shopping, label, manifest, tracking, delivery promise
order: 503
---
# Parcel shipping and carriers

## What parcel shipping covers
### Purpose
- Every order delivered on its promise
- The lowest cost service that keeps it
### In scope
- Carrier and service choice, labels, manifests
- Pickups, tracking and delivery exceptions
### Outcome
- On-time delivery guests can track
- Lower cost per package

## The service is chosen at the pack bench
Layout: swimlane handoffs
- Pack station: Packs and weighs the carton
- Shipping system: Rates every eligible service
- Shipping system: Meets the delivery promise?
- Shipping system: If yes, prints the cheapest
- Shipping system: If no, upgrades the service
- Carrier: Scans at pickup and delivers

## What decides the carrier and service
| Factor | What it decides | Source |
|---|---|---|
| Delivery promise | The slowest service that still arrives | Order promise date |
| Weight and size | Rate and dimensional weight | Pack station scale |
| Destination | Zone and carrier coverage | Address and zone tables |
| Dangerous goods | Ground only, limited quantity marks | Item hazmat flag |
| Carrier capacity | Daily volume each carrier accepts | Carrier agreements |

## Systems and data for parcel
| Step | What the system does | Records it keeps |
|---|---|---|
| Rate | Compares services and costs | Rate quotes |
| Label | Prints the carrier label | Tracking number |
| Manifest | Closes the day by carrier | Manifest, pickup record |
| Track | Reads carrier scan events | Tracking history |
| Exception | Flags late or lost parcels | Exception cases |

## KPIs that show it works
| KPI | What it measures | Data source |
|---|---|---|
| On-time delivery | Parcels delivered by the promise | Tracking vs promise |
| Cost per package | Freight cost per parcel | Carrier invoices |
| Pickups on time | Scheduled pickups made | Carrier scans |
| Damage and loss | Claims per [n] parcels | Claims log |

## Today and target
### Today
- One carrier for most parcels by habit
- Late parcels found when guests call
### Target
- Service chosen per parcel on promise and cost
- Exceptions flagged before the guest asks
