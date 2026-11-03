---
id: sc-tr-store-delivery
domain: Supply Chain
l1: Deliver
l2: Store delivery and routing
summary: Getting DC stock to stores on time: routes and delivery windows, loading in stop order, proof of delivery and the trip back.
systems: TMS, WMS, Route planning, Store systems
tags: store delivery, routing, delivery window, proof of delivery, load sequence, backhaul, fleet
order: 506
---
# Store delivery and routing

## What store delivery covers
### Purpose
- Stock on the shelf before guests arrive
- Full trucks on efficient routes
### In scope
- Routes, delivery days and windows
- Loading, proof of delivery and returns pickup
### Outcome
- On-time deliveries stores can plan around
- Lower cost per carton delivered

## The store replenishment path
Layout: retail store-replenishment

## Every stop is confirmed at the store
Layout: swimlane handoffs
- Transportation: Builds routes by store window
- DC shipping: Loads in reverse stop order
- Driver: Delivers in the store's window
- Store: Delivery complete and correct?
- Store: If yes, confirms receipt
- Store: If no, logs shorts or damage
- Transportation: Resolves the claim

## Rules for store deliveries
| Rule | Standard | Owner |
|---|---|---|
| Delivery window | Agreed per store, around trading hours | Transportation |
| Delivery days | Set by store volume | Supply planning |
| Load sequence | Last stop loaded first | DC shipping |
| Proof of delivery | Electronic sign-off at the store | Store team |
| Return trip | Totes, returns and damages back to the DC | Driver |

## KPIs that show it works
| KPI | What it measures | Data source |
|---|---|---|
| On time to window | Stops inside the agreed window | Route records |
| Cost per carton | Delivery cost per carton | Freight cost, cartons |
| Trailer fill | Space used on each trip | Load plans |
| Store exceptions | Shorts or damages per delivery | Proof of delivery |

## Today and target
### Today
- Windows missed, stores staff for no truck
- Shorts disputed with no proof
### Target
- Routes built to each store's window
- Every stop signed for electronically
