---
id: sc-tr-transportation
domain: Supply Chain
l1: Deliver
l2: Transportation planning and freight
summary: Loads planned, tendered and tracked: routes to stores, carrier tendering, tracking and freight settlement.
systems: Transportation, Carrier portal, Accounts payable
tags: transportation, freight, carrier, routing, tendering, TMS
order: 501
---
# Transportation planning and freight

## What this process covers
### Purpose
- Deliver on time at the lowest freight cost
- Know where every load is
### In scope
- Route and load planning, tendering, tracking
- Freight cost calculation and settlement
### Outcome
- Loads tendered and accepted before cut-off
- Freight invoices paid as calculated

## Planners build loads, carriers accept and deliver
Layout: swimlane handoffs
- Transport planner: Builds loads from deliveries
- Transport planner: Tenders to the carrier
- Carrier: Accepts the tender?
- Carrier: If yes, confirm the pickup
- Transport planner: If no, tender to the next carrier
- Carrier: Sends tracking events
- Freight audit: Settles the freight cost

## The systems and data it runs on
| Step | What the system does | Records it keeps |
|---|---|---|
| Freight to plan | Deliveries become loads to plan | Freight units |
| Planning | Routes and loads built by an optimiser | Planned loads |
| Tendering | Loads offered to carriers through a portal | Tenders, acceptances |
| Tracking | Carrier events update every stop | Tracking events, proof of delivery |
| Freight settlement | Rate table cost, invoice matched | Freight cost, carrier invoice |

## Six steps from delivery to settled freight
Layout: process arrow
- Collect: deliveries to ship
- Plan: routes and loads
- Tender: carrier accepts
- Load: at the DC door
- Track: events to the store
- Settle: freight cost

## Controls and exceptions
| Control | How it works | Owner |
|---|---|---|
| Rate from contract | Freight cost calculated from the rate table | Transport planner |
| Tender acceptance window | Unanswered tenders roll to the next carrier | Transport planner |
| Freight audit | Carrier invoice matched to the calculation | Audit result |
| Proof of delivery | POD captured for every stop | Carrier |

## KPIs that show it works
| KPI | What it measures | Data source |
|---|---|---|
| On-time delivery to store | Stops delivered in the window | Tracking events |
| Tender acceptance rate | Tenders accepted first time | Tender responses |
| Cost per unit delivered | Freight cost per unit | Freight cost and volume |
| Trailer utilisation | Cube used per load | Load plans |

## Today and target
### Today
- Routes fixed by day of week, loads half full
- Freight invoices paid without audit
### Target
- Loads built from real volumes each day
- Every freight invoice matched to its calculation
