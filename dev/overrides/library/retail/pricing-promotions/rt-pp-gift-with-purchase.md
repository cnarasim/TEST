---
id: rt-pp-gift-with-purchase
domain: Retail
l1: Pricing & Promotions
l2: Gift with purchase and samples
summary: Brand-funded gifts and free samples tied to a qualifying purchase: offer rules, gift items and stock, POS and cart triggers, sell-out.
systems: Promotion engine, POS, E-commerce cart, ERP inventory, WMS
tags: GWP, gift with purchase, free gift, samples, deluxe samples, while supplies last, vendor funded
order: 204
---
# Gift with purchase and samples

## What gifts and samples cover
### Purpose
- Reward a qualifying basket with a free gift
- Let guests try new products through samples
### In scope
- Offer rules, gift items and gift stock
- POS and cart triggers, returns, samples
### Outcome
- The gift in the bag whenever the guest qualifies
- Offers that end cleanly when gifts run out

## Brands fund the gift, rules add it
Layout: swimlane handoffs
- Brand partner: Funds and ships the gifts
- Merchant: Sets the offer and threshold
- POS: Basket meets the threshold?
- POS: If yes, add the gift at zero
- POS: If no, show the amount to qualify
- Store team: Bags the gift
- Merchant: Ends the offer at sell-out

## Systems and data for gifts and samples
| Step | What the system does | Records it keeps |
|---|---|---|
| Gift item | Each gift is a non-sellable item with its own barcode | Gift item, zero retail price |
| Offer rule | Brand, threshold, dates and gift held in one rule | Promotion, qualifying rules |
| Trigger | POS and cart add the gift when the basket qualifies | Sale line at zero, offer applied |
| Gift stock | Gift units received, allocated and counted like stock | Gift inventory by location |

## Three things must line up for a gift
Layout: process converge
- Offer rule: brand, threshold and dates
- Gift stock: in the store or the DC
- Qualifying basket: the guest's purchase
- Result: Gift added - free, tracked and funded

## Controls and exceptions
| Control | How it works | Owner |
|---|---|---|
| Gift stock check | The offer ends online when gift stock runs out | Ecommerce team |
| Returns rule | A return below the threshold takes back the gift | Store operations |
| Brand recap | Gifts given are reported back to the brand | Merchant |
| Sample limits | Samples per order capped by cart rules | Promotions team |

## KPIs that show it works
| KPI | What it measures | Data source |
|---|---|---|
| Offer lift | Brand sales during the offer vs baseline | Sales by brand and week |
| Gift sell-out timing | Days the gift lasted vs days planned | Gift stock by day |
| Gift accuracy | Qualifying baskets that got the gift | POS and order lines |
| Sample conversion | Full-size buys after a sample | Member purchase history |

## Today and target
### Today
- Gifts handed out by hand, stock not tracked
- Online offers run after the gifts are gone
### Target
- Every gift an item, counted like stock
- Offers end automatically at sell-out
