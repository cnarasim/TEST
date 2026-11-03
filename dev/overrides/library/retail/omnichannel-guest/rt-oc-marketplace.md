---
id: rt-oc-marketplace
domain: Retail
l1: Omnichannel & Guest
l2: Marketplace sellers
summary: Third-party sellers on the site and app: vetting, catalog and content checks, seller orders and shipping, returns, payouts and performance.
systems: Marketplace platform, Seller portal, OMS, PIM, ERP finance
tags: marketplace, third-party seller, seller onboarding, drop ship, commission, payout, seller performance
order: 406
---
# Marketplace sellers

## What the marketplace covers
### Purpose
- Widen the range without owning the stock
- Keep every seller to our guest standard
### In scope
- Seller vetting, catalog, content and price
- Seller orders, shipping, returns, payouts
### Outcome
- New brands live fast, with no inventory risk
- Sellers measured and held to service levels

## Sellers ship, we keep the guest
Layout: swimlane handoffs
- Seller: Applies with the product range
- Marketplace team: Vets brand and product safety
- Seller: Lists items in the portal
- Marketplace team: Content and price compliant?
- Marketplace team: If yes, publish to the site
- Seller: If no, fix and resubmit
- Seller: Ships orders to the guest
- Finance: Pays out, net of commission

## Systems and data for marketplace sellers
| Step | What the system does | Records it keeps |
|---|---|---|
| Seller setup | The marketplace platform holds terms and payout details | Seller account, commission rates |
| Catalog | Seller items mapped to our categories and checked | Seller offers, item content |
| Orders | The OMS splits seller lines and sends them to the seller | Seller order, ship-by date |
| Settlement | Sales, refunds and fees netted each payout cycle | Payout statement, ledger entries |

## Five records from contract to payout
Layout: retail document-flow
- Seller agreement: terms, fees, service levels (Marketplace team)
- Offer: item, price and stock (Seller)
- Seller order: what to ship, by when (OMS)
- Ship confirmation: carrier and tracking (Seller)
- Payout statement: sales less fees and refunds (Finance)

## Controls and exceptions
| Control | How it works | Owner |
|---|---|---|
| Seller vetting | Brand, safety and ingredient checks before listing | Marketplace team |
| Ship-by date | Seller orders not shipped by the date are canceled | Marketplace operations |
| Return policy | Sellers accept returns on our policy and window | Customer care |
| Payout reserve | A reserve held back against refunds and chargebacks | Finance |

## KPIs that show it works
| KPI | What it measures | Data source |
|---|---|---|
| On-time ship rate | Seller orders shipped by the ship-by date | Seller orders and tracking |
| Seller cancel rate | Lines the seller could not fill | Seller order status |
| Guest rating | Reviews and complaints per seller | Reviews, care contacts |
| Marketplace sales | Sales and commission by seller | Payout statements |

## Today and target
### Today
- Seller items keyed by hand into the item master
- Seller orders e-mailed, tracking keyed in
### Target
- Sellers self-serve in a portal, checked by rules
- Orders, tracking and payouts flow by integration
