---
id: rt-pp-coupons
domain: Retail
l1: Pricing & Promotions
l2: Coupons and personalized offers
summary: Mass coupons and personalized member offers from setup to redemption: rules, exclusions, unique codes, POS and cart checks, measured lift.
systems: Promotion engine, CRM, Loyalty platform, POS, E-commerce cart
tags: coupon, offer, personalized offer, promo code, digital coupon, redemption, exclusions, holdout
order: 205
---
# Coupons and personalized offers

## What coupons and offers cover
### Purpose
- Drive trips with the right offer for each guest
- Spend offer money where it changes behavior
### In scope
- Mass coupons, codes and member offers
- Rules, exclusions, stacking, redemption
### Outcome
- Offers that work the same in store and online
- Lift measured against a control group

## Marketing targets, the register validates
Layout: swimlane handoffs
- Marketing: Defines the offer and audience
- Marketing: Loads offers to member accounts
- Guest: Shows the offer at checkout
- POS: Valid for this basket?
- POS: If yes, apply and mark used
- POS: If no, show the reason
- Analyst: Measures lift vs control

## Systems and data for coupons and offers
| Step | What the system does | Records it keeps |
|---|---|---|
| Offer setup | Discount, threshold, dates and exclusions set once | Offer record, exclusion list |
| Targeting | Segments built from member data, with a holdout | Audience, control group |
| Issue | Codes generated and offers loaded to accounts | Unique codes, member offers |
| Redemption | POS and cart validate and mark the code used | Redemption, discount by line |

## Offers turn data into measured lift
Layout: process io
- Input: Member purchase history
- Input: Offer budget and rules
- Input: Brand partner funding
- Target: Offer by segment, with a holdout
- Output: Redemptions by channel
- Output: Incremental sales and margin

## Controls and exceptions
| Control | How it works | Owner |
|---|---|---|
| Single-use codes | Each code works once, for one guest | Promotions team |
| Brand exclusions | Brands excluded by agreement are blocked | Merchant |
| Stacking rules | Which offers can combine, set in one rule | Pricing team |
| Offer budget | Redemption cost tracked against the budget | Finance |

## KPIs that show it works
| KPI | What it measures | Data source |
|---|---|---|
| Redemption rate | Offers used vs offers issued | Issue and redemption records |
| Incremental sales | Sales lift vs the holdout group | Test and control sales |
| Offer cost | Discount given as a share of sales | Discount by line |
| Code leakage | Codes used outside their audience | Redemptions vs audience |

## Today and target
### Today
- One mass coupon for every guest
- Shared codes spread on deal sites
### Target
- Member offers, unique codes, one rule set
- Every offer measured against a holdout
