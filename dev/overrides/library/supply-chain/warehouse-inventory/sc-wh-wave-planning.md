---
id: sc-wh-wave-planning
domain: Supply Chain
l1: Warehouse & Inventory
l2: Wave planning and release
summary: How the DC groups store, online and transfer orders into waves sized to labour, stock and carrier cut-offs, and releases them.
systems: WMS, OMS, Labor management, TMS
tags: wave planning, wave release, cut-off, pick release, labour plan, order pooling, waveless
order: 407
---
# Wave planning and release

## What wave planning covers
### Purpose
- Orders released in the right groups and order
- Labour and equipment busy all shift, not idle
### In scope
- Store, online and transfer orders
- Waves, priorities and carrier cut-offs
### Outcome
- Orders out before every truck and carrier
- Fewer short picks and waiting pickers

## Five steps from order pool to the dock
Layout: process numbered
- Pool: orders by carrier, route and due time
- Check: stock in the pick faces
- Build: waves sized to labour and cut-off
- Release: tasks to pickers and automation
- Monitor: progress against each cut-off

## The planner builds, the WMS releases
Layout: swimlane handoffs
- Wave planner: Builds waves for the next cut-off
- WMS: Checks stock in the pick faces
- WMS: Enough stock to pick in full?
- WMS: If yes, releases the wave
- WMS: If no, replenishes the faces first
- Pickers: Pick and send totes to packing
- Shipping: Loads before the cut-off

## Each order type has its own wave rule
| Order type | Wave rule | Cut-off |
|---|---|---|
| Store replenishment | By route, in stop order | Truck departure |
| Online standard | Every [n] minutes, sorted by carrier | Carrier pickup |
| Online express | Released as orders arrive | Express pickup |
| Transfers between DCs | Full loads, off-peak shifts | Load schedule |

## Systems and data for waves
| Step | What the system does | Records it keeps |
|---|---|---|
| Pool | Collects released orders | Order pool, due times |
| Plan | Sizes waves to labour and doors | Wave plan |
| Release | Creates pick tasks | Tasks, totes, cartons |
| Track | Shows progress by wave | Wave status, backlog |

## KPIs that show it works
| KPI | What it measures | Data source |
|---|---|---|
| Shipped by cut-off | Orders out before their cut-off | Ship confirms vs cut-offs |
| Wave completion | Time from release to packed | Wave status history |
| Pick rate | Units picked per labour hour | Labor management |
| Short picks | Lines picked short | Pick confirmations |

## Today and target
### Today
- Waves sized by habit, not by cut-off
- Late waves push orders to the next day
### Target
- Waves sized to labour and each cut-off
- Every order out on its planned truck
