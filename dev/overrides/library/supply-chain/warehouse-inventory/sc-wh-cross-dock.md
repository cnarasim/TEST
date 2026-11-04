---
id: sc-wh-cross-dock
domain: Supply Chain
l1: Warehouse & Inventory
l2: Cross-dock and flow-through
summary: Vendor freight pre-labelled by store crosses the dock to outbound trucks without being stored.
systems: WMS, Allocation, EDI
tags: cross-dock, flow-through, pre-distributed, merchandise distribution
order: 403
---
# Cross-dock and flow-through

## What cross-dock and flow-through covers
### Purpose
- Move freight to stores without storing it
- Cut handling and days on hand
### In scope
- Pre-distributed and pick-by-line flows
- Sorting, staging and outbound loading
### Outcome
- Cartons in, cartons out within a day
- No putaway, no second pick

## Cartons cross the dock in one shift
Layout: swimlane handoffs
- Vendor: Labels cartons by store
- Receiver: Scans cartons at the door
- Sorter: Routes cartons to store lanes
- Sorter: Label readable?
- Sorter: If yes, send to the store lane
- Problem solver: If no, relabel by hand
- Loader: Loads store routes

## The systems and data it runs on
| Step | What the system does | Records it keeps |
|---|---|---|
| Distribution plan | Store quantities are known before the freight arrives | Allocation plan |
| Flow-through set-up | Pre-labelled or pick-by-line flows | Distribution orders |
| Receive at door | Cartons scanned by carton-level ASN | Carton receipts |
| Cross-dock routing | The WMS sends each carton to its store lane | Sortation tasks |
| Ship | Store loads leave the outbound doors | Store deliveries |

## Cartons cross the dock, never stored
Layout: retail cross-dock

## Controls and exceptions
| Control | How it works | Owner |
|---|---|---|
| Label compliance | Vendors fined for unreadable labels | Vendor compliance |
| Dwell time alert | Cartons on the dock beyond a shift alert | DC lead |
| Store lane audit | Sample cartons checked per lane | Quality lead |
| ASN by carton | Carton-level ASN required | Integration team |

## KPIs that show it works
| KPI | What it measures | Data source |
|---|---|---|
| Dock dwell time | Hours from inbound scan to load | Carton scan times |
| Cross-dock share | Volume that never goes to storage | Flow-through vs stocked volume |
| Mis-sort rate | Cartons at the wrong store | Store receiving differences |
| Vendor label compliance | Cartons with a readable store label | Sorter exceptions |

## Today and target
### Today
- Most freight put away then picked again
- Store labels applied in the DC
### Target
- Pre-labelled freight crosses the dock
- Only exceptions touched by hand
