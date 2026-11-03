---
id: rt-oc-social-commerce
domain: Retail
l1: Omnichannel & Guest
l2: Social commerce orders
summary: Orders placed in social apps and live shopping, brought into the OMS, fulfilled like web orders and settled with each platform.
systems: Social commerce integration, OMS, PIM, WMS, ERP finance
tags: social commerce, social shop, live shopping, creator, catalog feed, platform orders, settlement
order: 407
---
# Social commerce orders

## What social commerce orders cover
### Purpose
- Sell where guests discover beauty
- Fulfill social orders like any web order
### In scope
- Catalog feed with stock and price sync
- Order import, tracking, returns, settlement
### Outcome
- Social orders shipped inside platform rules
- Sales, fees and commissions reconciled

## The platform sells, our DC fulfills
Layout: swimlane handoffs
- Ecommerce team: Publishes the catalog feed
- Guest: Buys in the social app
- OMS: Imports the platform order
- OMS: Item still in stock?
- DC: If yes, pick and ship it
- OMS: If no, cancel and tell the platform
- OMS: Sends tracking to the platform

## Systems and data for social commerce
| Step | What the system does | Records it keeps |
|---|---|---|
| Catalog feed | Items, prices and stock sent to each platform | Feed file, listing status |
| Order import | Platform orders pulled into the OMS | Platform order ID, customer order |
| Fulfillment | The DC ships it like a web order | Shipment, tracking number |
| Settlement | The platform pays out net of its fees | Settlement report, fees, commissions |

## Every social channel lands in one OMS
Layout: process converge
- Shoppable posts: checkout in the app
- Live shopping: orders during the stream
- Creator shops: sales with commission
- Result: One order flow - same pick, pack and care

## Controls and exceptions
| Control | How it works | Owner |
|---|---|---|
| Stock buffer | Only stock above a buffer is offered on social | Ecommerce team |
| Platform deadlines | Tracking sent before each platform's deadline | Omnichannel operations |
| Price parity | Feed prices match the site; promotions end on time | Pricing team |
| Payout match | Platform payouts matched to orders and refunds | Finance |

## KPIs that show it works
| KPI | What it measures | Data source |
|---|---|---|
| Social sales | Orders and sales by platform and creator | Platform orders in the OMS |
| Shipped in window | Orders shipped inside the platform's window | Order and tracking times |
| Oversell rate | Orders canceled for no stock | Cancel reasons |
| Net margin | Sales less fees, commissions and freight | Settlement reports |

## Today and target
### Today
- Platform orders keyed into the OMS by hand
- Fees found only when the payout arrives
### Target
- Orders and tracking flow by integration
- Payouts reconciled line by line each cycle
