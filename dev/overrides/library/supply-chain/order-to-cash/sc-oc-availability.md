---
id: sc-oc-availability
domain: Supply Chain
l1: Order to Cash
l2: Availability check and backorders
summary: Available-to-promise: product availability, allocation, supply protection and backorder processing for confirmed dates.
systems: ERP order management, Supply planning
tags: ATP, availability, backorder, product allocation, supply protection, confirmation
order: 303
---
# Availability check and backorders

## What this process covers
### Purpose
- Confirm only what can be delivered
- Share scarce stock by priority, not by who ordered first
### In scope
- Availability check, product allocation, supply protection
- Backorder processing and re-confirmation
### Outcome
- Confirmed dates the DC can keep
- Scarce stock goes to the most important orders

## Planners decide who gets scarce stock
Layout: swimlane handoffs
- Sales order: Requests quantity and date
- ATP check: Checks stock and receipts
- ATP check: Enough for the request?
- ATP check: If yes, confirm the date
- ATP check: If no, confirm partly or later
- Supply planner: Runs backorder processing
- Customer service: Tells customer the new date

## The systems and data it runs on
| Step | What the system does | Records it keeps |
|---|---|---|
| Availability check | Stock and confirmed receipts against the request | Check rules, confirmed date |
| Overview | One view of stock, receipts and demand by item | Availability overview |
| Allocation | Scarce supply shared by channel, region or customer | Allocation quotas |
| Supply protection | A share of stock held back for priority demand | Protected quantities |
| Backorder run | Open orders re-confirmed by priority rules | Backorder results |
| Re-confirm | Customers get the new confirmed dates | Updated order schedule |

## Five checks confirm a date the DC can keep
Layout: process chevrons
- Request: quantity and date
- Check: stock and receipts
- Allocate: by channel or customer
- Protect: reserved supply
- Re-plan: backorder run

## Controls and exceptions
| Control | How it works | Owner |
|---|---|---|
| Confirmation rule | Only stock and confirmed receipts count | Supply planner |
| Allocation priority | Customer and channel order set by policy | Commercial lead |
| Backorder review | A daily run re-confirms open orders | Supply planner |
| Manual override limit | Changed confirmations need a reason | Customer service |

## KPIs that show it works
| KPI | What it measures | Data source |
|---|---|---|
| Confirmed on request date | Lines confirmed for the asked date | Requested vs confirmed date |
| Confirmation stability | Dates that did not move after confirm | Confirmed date changes |
| Backorder value | Open unconfirmed order value | Backorder results |
| Delivered as confirmed | Deliveries shipped on the confirmed date | Goods issue vs confirmed date |

## Today and target
### Today
- First come, first served on scarce product
- Backorders re-confirmed by hand
### Target
- Allocation and supply protection by channel
- A nightly backorder run with clear win and lose rules
