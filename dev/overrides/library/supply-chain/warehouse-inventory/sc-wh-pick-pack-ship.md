---
id: sc-wh-pick-pack-ship
domain: Supply Chain
l1: Warehouse & Inventory
l2: DC operations: pick, pack, ship
summary: Inside the DC from wave to truck: waves, picking, packing, staging, loading and goods issue for stores and e-commerce.
systems: WMS, Labour management, Transportation
tags: wave, picking, packing, loading, WMS, store orders, ecommerce
order: 402
---
# DC operations: pick, pack, ship

## What this process covers
### Purpose
- Turn store and online orders into loaded trucks
- Ship complete orders at the lowest cost per unit
### In scope
- Waves, picking, packing, staging and loading
- Store replenishment and e-commerce flows
### Outcome
- Every route loaded before its cut-off
- Units picked once, checked once

## Waves keep the floor busy and trucks on time
Layout: swimlane handoffs
- Wave planner: Releases waves by route
- Picker: Picks to tote or cart
- Packer: Packs, weighs and labels
- Packer: Weight within tolerance?
- Packer: If yes, send to staging
- Problem solver: If no, audit the carton
- Loader: Loads by stop and closes the trailer

## The systems and data it runs on
| Step | What the system does | Records it keeps |
|---|---|---|
| Waves | Orders grouped by route and cut-off | Wave plan |
| Picking | RF or voice picking to totes and carts | Pick tasks |
| Packing | Pack stations weigh, label and manifest | Cartons, labels |
| Loading | Cartons loaded by stop and door | Load, trailer |
| Goods issue | Shipped stock leaves the books | Goods issue, ASN to the customer |

## Five zones turn vendor trailers into store deliveries
Layout: retail dc-operations

## Controls and exceptions
| Control | How it works | Owner |
|---|---|---|
| Weight check | Carton weight compared with expected | Packing lead |
| Cut-off control | Waves released to meet route cut-offs | Wave planner |
| Short-pick handling | Shorts trigger an immediate bin count | Inventory control |
| Seal and manifest | Trailer sealed with the manifest attached | Shipping lead |

## KPIs that show it works
| KPI | What it measures | Data source |
|---|---|---|
| Units per hour | Picking productivity | Pick confirmations |
| Order fill rate | Units shipped vs ordered | Shipped vs ordered quantity |
| On-time trailer departure | Trailers leaving by cut-off | Trailer departure vs plan |
| Cost per unit shipped | DC cost divided by units | Cost and volume |

## Today and target
### Today
- Waves released by hand from spreadsheets
- Carton errors found by stores
### Target
- Waves released automatically by route and cut-off
- Weight and scan checks catch errors before loading
