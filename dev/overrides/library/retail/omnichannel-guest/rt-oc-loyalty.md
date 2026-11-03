---
id: rt-oc-loyalty
domain: Retail
l1: Omnichannel & Guest
l2: Loyalty points earn and redeem
summary: Members earn points on purchases and services in store and online and redeem them as discounts, with returns, expiry, tiers and the liability.
systems: Loyalty platform, POS, OMS, CRM, ERP finance
tags: loyalty, rewards, points, redeem, member, tier, points liability, breakage
order: 410
---
# Loyalty points earn and redeem

## What loyalty earn and redeem covers
### Purpose
- Reward members for every purchase, any channel
- Bring members back more often
### In scope
- Earn, bonus events, tiers and redemption
- Returns, expiry and the points liability
### Outcome
- The right points on every receipt and in the app
- A points liability finance can trust

## The register asks, the platform answers
Layout: swimlane handoffs
- Member: Shops in store or online
- POS: Identifies the member
- POS: Reward to redeem today?
- POS: If yes, apply it as a discount
- POS: If no, complete the sale
- Loyalty platform: Posts the points earned
- Finance: Books the points liability

## Systems and data for loyalty points
| Step | What the system does | Records it keeps |
|---|---|---|
| Enroll | Members join in store, online or in the app | Member profile, consent |
| Earn | POS and OMS send each sale to the loyalty platform | Points transaction, tier progress |
| Redeem | Points become a discount on the sale | Redemption, reward used |
| Returns and expiry | Returns take points back; unused points expire | Points reversal, expiry |

## Points bring members back
Layout: process cycle
- Shop: in store, online or in the salon
- Earn: points on each purchase
- Grow: bonus events and tier status
- Redeem: points off a later basket
- Come back: offers based on what they buy

## Controls and exceptions
| Control | How it works | Owner |
|---|---|---|
| Returns reverse points | Points earned on a returned item are taken back | Loyalty team |
| Real-time balance | Rewards checked against the balance at the register | POS support |
| Liability reconciliation | Platform points tied to the ledger each month | Finance |
| Fraud rules | Unusual earn or redeem patterns flagged | Loss prevention |

## KPIs that show it works
| KPI | What it measures | Data source |
|---|---|---|
| Member sales share | Member sales as a share of total sales | POS and OMS sales by member |
| Redemption rate | Points redeemed vs points issued | Loyalty transactions |
| Active members | Members who bought in the last 12 months | Member purchase history |
| Points liability | Value of points outstanding | Loyalty balances, ledger |

## Today and target
### Today
- Points post overnight, receipts show no balance
- Liability estimated once a year
### Target
- Live balance at the register and in the app
- Monthly liability tied to the ledger
