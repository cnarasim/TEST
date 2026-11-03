---
id: fi-rr-deferred-revenue
domain: Finance
l1: Record to Report
l2: Loyalty and gift card liability
summary: Liabilities for unredeemed loyalty points and gift cards: issue, redemption, breakage, unclaimed property and the monthly true-up.
systems: Loyalty platform, Gift card system, POS, ERP finance
tags: gift card, loyalty points, breakage, deferred revenue, contract liability, unclaimed property, escheat
order: 306
---
# Loyalty and gift card liability

## Points and gift cards are owed to guests
### Gift cards
- Cash in now, revenue when redeemed
- Unused balances: breakage or unclaimed property
### Loyalty points
- Part of each sale deferred to the points
- Revenue when points are redeemed or expire
### Breakage
- Value never redeemed, estimated from history
- Recognized in step with redemptions

## Guests redeem, accounting moves the value
Layout: swimlane handoffs
- Guest: Buys a gift card or earns points
- POS and loyalty: Record the issue and the balance
- Revenue accountant: Card or points redeemed?
- Revenue accountant: If yes, move the value to revenue
- Revenue accountant: If no, keep it in the liability
- Controller: Approves breakage and the true-up

## Systems and data for the liability
| Step | What the system does | Records it keeps |
|---|---|---|
| Issue | Cards activated, points earned | Card and points balances |
| Allocate | Sale price split to points | Points deferral |
| Redeem | Redemptions reduce the balance | Redemption transactions |
| Breakage | Unused value estimated | Breakage rates |
| Reconcile | Subledger agrees to the ledger | Liability reconciliation |

## Five steps from sale to redemption
Layout: process arrow
- Issue: card sold or points earned
- Defer: value held as a liability
- Redeem: revenue as value is used
- Estimate: breakage from history
- True up: balances, breakage, escheat
> Notes: breakage is recognized only where it is not owed to a state as unclaimed property; check the rules of each state.

## Controls keep the liability whole
| Control | How it works | Owner |
|---|---|---|
| Subledger reconciliation | Card and points balances agree to the ledger monthly | Revenue accounting |
| Breakage review | Rates reset from actual redemption history | Controller |
| Unclaimed property review | Dormant card balances checked against state rules | Tax |
| Card activation control | Cards hold no value until activated at a register | Loss prevention |

## KPIs show what we owe and why it moves
| KPI | What it measures | Data source |
|---|---|---|
| Liability balance | Unredeemed card and points value | Subledgers |
| Redemption rate | Value redeemed against value issued | Card and points history |
| Breakage rate | Value expected never to be redeemed | Breakage model |
| Reconciling differences | Subledger vs ledger differences | Monthly reconciliation |

## From yearly estimates to monthly true-ups
### Today
- Breakage booked once a year
- Points deferral built in spreadsheets
### Target
- Monthly breakage from redemption curves
- Deferral calculated from the points ledger
