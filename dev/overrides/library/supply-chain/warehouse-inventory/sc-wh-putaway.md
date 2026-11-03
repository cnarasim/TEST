---
id: sc-wh-putaway
domain: Supply Chain
l1: Warehouse & Inventory
l2: Putaway and slotting
summary: Received stock directed to the right location, and pick faces slotted by velocity, size and handling so picking stays fast.
systems: WMS, Slotting tool, ERP inventory, Handheld scanning
tags: putaway, slotting, re-slot, location, golden zone, velocity, reserve, pick face
order: 406
---
# Putaway and slotting

## What putaway and slotting covers
### Purpose
- Every pallet and case in a known, scanned location
- Fast sellers where picking is quickest
### In scope
- Directed putaway to reserve and pick faces
- Slotting by velocity, size and handling
### Outcome
- Stock ready to pick within hours of receipt
- Less travel and fewer touches per pick

## The WMS directs, the operator confirms
Layout: swimlane handoffs
- Receiver: Releases the received pallet
- WMS: Suggests a location by rule
- Putaway operator: Suggested location usable?
- Putaway operator: If yes, scans it to confirm
- Inventory control: If no, clears the location issue
- WMS: Releases the stock for picking

## Systems and data for putaway
| Step | What the system does | Records it keeps |
|---|---|---|
| Putaway rules | Rules by size, velocity, hazard | Putaway strategy, location types |
| Directed task | A location set for each pallet | Putaway task |
| Scan to confirm | Item, pallet and bin scanned | Stock by location |
| Slotting review | Velocity and cube rank pick faces | Slotting proposals |
| Re-slot moves | Agreed changes become move tasks | Move tasks, new pick faces |

## Velocity and size decide the pick face
Layout: matrix
- Fast and small: Carton flow in the golden zone
- Fast and bulky: Pallet pick near the shipping docks
- Slow and small: Static shelving further out
- Slow and bulky: Case pick from the lower rack levels
> Notes: the golden zone is waist to shoulder height. Re-slot fast movers into it before each season and after big resets.

## Controls and exceptions
| Control | How it works | Owner |
|---|---|---|
| Scan to confirm | Putaway closes only when the location is scanned | DC lead |
| Hazard segregation | Aerosols and flammables go to approved zones only | Safety lead |
| Location capacity | The WMS will not overfill a location by cube | Inventory control |
| Re-slot window | Re-slots done in quiet weeks, never at peak | Operations manager |

## KPIs that show it works
| KPI | What it measures | Data source |
|---|---|---|
| Dock-to-stock time | Receipt to stock available to pick | Receipt vs putaway confirmed |
| Putaway accuracy | Stock found in the location scanned | Cycle count results |
| Putaways per labor hour | Putaway productivity | Tasks and labor hours |
| Pick travel per line | Walking time between picks | Pick task times |

## Today and target
### Today
- Operators choose locations from memory
- Pick faces set at opening, never revisited
### Target
- Every putaway directed and scan-confirmed
- Fast movers re-slotted each season from data
