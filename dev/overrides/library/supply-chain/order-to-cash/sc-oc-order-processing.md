---
id: sc-oc-order-processing
domain: Supply Chain
l1: Order to Cash
l2: Sales order processing
summary: Orders captured once, priced, checked for stock and credit and released to delivery in one connected order history.
systems: ERP order management, EDI, Customer portal
tags: sales order, order entry, B2B, EDI 850, incomplete orders, order management
order: 301
---
# Sales order processing

## What sales order processing covers
### Purpose
- Capture every order once, priced and checked
- Promise a date the supply chain can keep
### In scope
- Order entry, pricing, availability and credit
- Changes, blocks, rejections and release
### Outcome
- A clean order ready for delivery and billing
- One connected history from quote to cash

## Customer service owns the order from PO to release
Layout: swimlane handoffs
- Customer: Sends the order (EDI 850)
- Customer service: Creates the sales order
- Customer service: Price and stock confirmed?
- Customer service: If yes, confirm the delivery date
- Customer service: If no, offers substitute or new date
- Credit: Checks exposure against the limit
- Logistics: Releases the order to delivery

## The systems and data it runs on
| Step | What the system does | Records it keeps |
|---|---|---|
| Create the order | Orders arrive by EDI or portal, or are keyed by customer service | Sales order header, lines, schedule |
| Price the order | Price lists and discounts apply to every line | Price records, net price |
| Check availability | Stock and planned receipts give a confirmed date | Confirmed quantity and date |
| Check credit | Exposure is compared with the customer limit | Credit status, exposure |
| Fix incomplete orders | Missing ship-to, terms or route blocks the order | Incomplete order list |
| Release to delivery | Released orders become deliveries | Delivery, order history |

## Seven steps take a B2B order to cash
Layout: process arrow
- Receive: PO by EDI or portal
- Create: sales order
- Price: price list and discounts
- Promise: availability check
- Release: credit and delivery
- Ship: pick, pack, goods issue
- Bill: invoice and cash

## Controls and exceptions
| Control | How it works | Owner |
|---|---|---|
| Duplicate PO check | The same customer PO number warns at entry | Customer service |
| Completeness check | No delivery without ship-to, terms and route | Customer service |
| Credit block | Orders over the limit wait in a review queue | Credit |
| Price tolerance | Manual price changes beyond tolerance need approval | Pricing team |

## KPIs that show it works
| KPI | What it measures | Data source |
|---|---|---|
| Order entry cycle time | PO received to order saved | Order created vs EDI received time |
| Perfect order rate | Orders with no change, block or rejection | Order rejections and blocks |
| Confirmed on request date | Orders confirmed on the asked date | Confirmed vs requested date |
| Touchless order rate | Orders created by EDI with no edit | Order change history |

## Today and target
### Today
- Orders keyed from e-mail and PDF
- Price and credit blocks found after saving
### Target
- EDI and portal orders created without a touch
- Blocks resolved at entry from owner queues
