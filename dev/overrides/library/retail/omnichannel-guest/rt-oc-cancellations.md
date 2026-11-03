---
id: rt-oc-cancellations
domain: Retail
l1: Omnichannel & Guest
l2: Order cancellations and changes
summary: Guest, care and system cancellations and order edits: what can change when, stopping the pick, payment reversal, refunds and reasons.
systems: OMS, WMS, Store fulfillment app, Payments, CRM
tags: order cancellation, cancel order, order change, edit order, authorization reversal, refund, cancel reasons
order: 408
---
# Order cancellations and changes

## What cancellations and changes cover
### Purpose
- Let guests fix an order while it can be fixed
- Never charge for what does not ship
### In scope
- Guest, care and system cancellations
- Address, delivery method and item changes
### Outcome
- Changes made before the pick, not after
- Every cancel with a reason and a clean refund

## The order's status sets what can change
Layout: swimlane handoffs
- Guest: Asks to cancel or change
- OMS: Checks the order status
- OMS: Released to fulfillment yet?
- OMS: If yes, request a pick stop
- OMS: If no, change or cancel at once
- DC: Stops the pick, restocks units
- Payments: Reverses the authorization
- Guest: Gets the confirmation

## Systems and data for cancellations
| Step | What the system does | Records it keeps |
|---|---|---|
| Request | The guest, care or a rule asks to cancel or edit | Cancel or change request, reason |
| Status check | The OMS allows it only before release or shipment | Order status, change window |
| Pick stop | A cancel message stops the DC or store pick | Pick cancel, units back in stock |
| Payment | The authorization is voided, or refunded if captured | Authorization reversal, refund |

## One cancel request, three outcomes
Layout: process diverge
- Request: guest, care or a system rule
- Not released: canceled at once, payment voided
- In picking: pick stopped, units restocked
- Shipped: carrier intercept or a return

## Controls and exceptions
| Control | How it works | Owner |
|---|---|---|
| Change window | Edits allowed only until the order is released | Ecommerce team |
| Reason codes | Every cancel tagged guest, stock, fraud or payment | Omnichannel operations |
| Pick stop confirmation | The DC confirms the stop before the refund | DC operations |
| Same-day reversal | Uncaptured payments released the same day | Payments team |

## KPIs that show it works
| KPI | What it measures | Data source |
|---|---|---|
| Cancel rate | Canceled orders as a share of all orders | OMS order status |
| Cancels by reason | Guest, stock, fraud and payment cancels | Cancel reason codes |
| Post-release cancels | Cancels after release to fulfillment | Cancel vs release times |
| Refund time | Cancel request to refund or reversal | Cancel and payment events |

## Today and target
### Today
- Care cancels by phone, the DC ships anyway
- Cancel reasons in free text, or missing
### Target
- Self-service edits until the order is released
- Pick stop confirmed before the refund
