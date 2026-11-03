---
id: rt-oc-customer-care
domain: Retail
l1: Omnichannel & Guest
l2: Where is my order and appeasements
summary: Order status contacts answered from one view of the order and carrier events, with clear rules for appeasements, reships and carrier claims.
systems: CRM, OMS, Carrier tracking, Loyalty platform, Payments
tags: WISMO, where is my order, customer care, appeasement, goodwill, reship, carrier claim, contact center
order: 409
---
# Where is my order and appeasements

## What WISMO and appeasements cover
### Purpose
- Answer "where is my order" before guests ask
- Make it right when an order goes wrong
### In scope
- Tracking, delay alerts and self-service
- Reships, refunds, points and carrier claims
### Outcome
- Fewer contacts per order
- Fair, consistent and affordable appeasements

## Care solves it on the first contact
Layout: swimlane handoffs
- Guest: Asks for the order status
- Care agent: Opens the order and tracking
- Care agent: Past the delivery promise?
- Care agent: If yes, reship or refund
- Care agent: If no, share tracking and ETA
- Care agent: Adds an appeasement by rule
- Logistics: Files the carrier claim

## Systems and data for order care
| Step | What the system does | Records it keeps |
|---|---|---|
| Proactive alerts | Shipped, delayed and delivered messages sent | Notification log |
| Order view | The agent sees order, payment and tracking together | Contact record, order history |
| Appeasement | Points, a coupon or a refund within the agent's limit | Appeasement, reason code |
| Reship or claim | A replacement order and a carrier claim raised | Reship order, carrier claim |

## Appeasements follow a simple matrix
Layout: matrix
- Make it right: Our miss, high impact - reship plus points
- Apologize: Our miss, low impact - points or a shipping refund
- Recover: Carrier miss, high impact - reship and file a claim
- Inform: Carrier miss, low impact - tracking and a new ETA
> Notes: an example policy - set the appeasement for each box, and the agent limits, to your own rules.

## Controls and exceptions
| Control | How it works | Owner |
|---|---|---|
| Agent limits | Appeasements above the agent's limit need a lead | Customer care lead |
| Repeat-claim check | Guests with frequent claims reviewed before payout | Loss prevention |
| Carrier claim window | Claims filed inside the carrier's deadline | Logistics |
| Reason codes | Every contact and appeasement carries a reason | Customer care |

## KPIs that show it works
| KPI | What it measures | Data source |
|---|---|---|
| WISMO contacts | Status contacts per 100 orders | Contacts by reason, orders |
| First-contact resolution | Contacts solved without a follow-up | Contact history |
| Appeasement cost | Value given per order and by reason | Appeasement records |
| Claim recovery | Carrier claim value recovered | Carrier claims |

## Today and target
### Today
- Agents check three screens to find a parcel
- Appeasements vary from agent to agent
### Target
- Delay alerts sent before the guest asks
- One order view, appeasements by rule
