---
id: sc-wh-kitting
domain: Supply Chain
l1: Warehouse & Inventory
l2: Kitting and value-added services
summary: Building gift sets, gift-with-purchase bags, tester packs and store display kits in the DC, from work order to a sellable kit item.
systems: WMS, ERP, Planning system, Labor management
tags: kitting, value-added services, VAS, gift sets, gift with purchase, work order, bill of materials
order: 409
---
# Kitting and value-added services

## What kitting and VAS cover
### Purpose
- Kits and sets ready for events and seasons
- Components used exactly as planned
### In scope
- Gift sets, bonus bags and tester packs
- Labels and store display kits
### Outcome
- Every kit ready before its launch date
- No surplus components after the season

## From work order to stock in five steps
Layout: process numbered
- Order: a work order with its bill of materials
- Reserve: components held for the order
- Build: assembled at the VAS station
- Check: quality sample against the kit standard
- Receive: the kit item into sellable stock

## Merchandising sets it, the DC builds it
Layout: swimlane handoffs
- Merchandising: Sets the kit and quantity
- Supply planning: Releases the work order
- WMS: All components in stock?
- WMS: If yes, picks components to VAS
- WMS: If no, holds the work order
- VAS team: Builds, checks and labels
- Inventory control: Receives the kit item

## Services the DC offers
| Service | Example | Planned from |
|---|---|---|
| Kit assembly | Holiday gift sets | Season plan |
| Gift with purchase | Bonus bags for beauty events | Promotion calendar |
| Labelling | Price or compliance labels | Item and channel rules |
| Tester packs | Testers for new launches | Launch calendar |
| Display kits | Fixture packs for store resets | Store reset plan |

## Systems and data for kitting
| Step | What the system does | Records it keeps |
|---|---|---|
| Work order | Holds the kit, quantity and due date | Work order, bill of materials |
| Components | Reserves and issues components | Component consumption |
| Build | Records units built and labour | Build confirmations |
| Receipt | Creates the kit in stock | Kit item inventory |

## KPIs that show it works
| KPI | What it measures | Data source |
|---|---|---|
| Kits on time | Work orders done by the due date | Work orders |
| Component accuracy | Components used vs planned | Consumption vs bill |
| Cost per kit | Labour and materials per kit | Labor management, ERP |
| Rework rate | Kits rebuilt after the check | Quality records |

## Today and target
### Today
- Kits built late, components short
- Leftover components after every season
### Target
- Work orders released with stock reserved
- Kits ready a week before each launch
