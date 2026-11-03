---
id: rt-oc-gift-cards
domain: Retail
l1: Omnichannel & Guest
l2: Gift card sale and redemption
summary: Physical and e-gift cards sold, activated and redeemed as tender in store and online, with balances, liability, breakage and fraud controls.
systems: Gift card platform, POS, OMS, Payments, ERP finance
tags: gift card, e-gift card, stored value, activation, redemption, breakage, gift card liability, unclaimed property
order: 411
---
# Gift card sale and redemption

## What the gift card process covers
### Purpose
- Sell gift cards in every channel
- Protect every balance from fraud
### In scope
- Sale, activation, redemption, balance checks
- Liability, breakage and unclaimed property
### Outcome
- Cards live the moment they are paid for
- A gift card liability that ties to the ledger

## Cards go live only when they are paid
Layout: swimlane handoffs
- Guest: Buys a gift card
- POS: Takes payment, then activates
- Gift card platform: Records the card balance
- Guest: Pays with the card later
- Gift card platform: Balance covers the sale?
- POS: If yes, approve the full amount
- POS: If no, split the tender
- Finance: Moves redeemed value to sales

## Systems and data for gift cards
| Step | What the system does | Records it keeps |
|---|---|---|
| Sale and activation | POS or site activates the card once it is paid | Card number, activation, value |
| Balance | The gift card platform holds each card's balance | Card balance, transaction history |
| Redemption | The card is a tender; partial use keeps the rest | Redemption, remaining balance |
| Accounting | Cards sold are a liability until redeemed | Gift card liability, breakage |

## A gift card's life in five steps
Layout: process numbered
- Sell: in store, online and at partner racks
- Activate: only after payment
- Redeem: as tender, in full or in part
- Track: balance and liability
- Close: breakage or unclaimed property

## Controls and exceptions
| Control | How it works | Owner |
|---|---|---|
| Activation on payment | Cards stay inactive until the sale is paid | POS team |
| PIN and velocity limits | PIN needed online; repeated balance checks blocked | Payments team |
| Tender restrictions | Gift cards cannot buy other gift cards | Loss prevention |
| Liability reconciliation | Platform balances tied to the ledger monthly | Finance |

## KPIs that show it works
| KPI | What it measures | Data source |
|---|---|---|
| Gift card sales | Cards sold by channel and season | POS and site sales |
| Redemption rate | Value redeemed vs value sold, by age | Gift card transactions |
| Fraud losses | Value lost to drained or stolen cards | Fraud cases |
| Liability accuracy | Platform balance vs ledger balance | Monthly reconciliation |

## Today and target
### Today
- Gift card liability tracked in a spreadsheet
- Fraud found when a guest's card is empty
### Target
- Daily platform-to-ledger reconciliation
- Fraud rules block draining before it happens
