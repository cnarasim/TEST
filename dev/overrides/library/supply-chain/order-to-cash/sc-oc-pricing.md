---
id: sc-oc-pricing
domain: Supply Chain
l1: Order to Cash
l2: Pricing and discounts
summary: How a sales price is found: price records, discounts and surcharges, the search order and the price calculation.
systems: Pricing engine, ERP order management
tags: pricing, price records, discount, surcharge, price calculation, price list
order: 302
---
# Pricing and discounts

## What pricing and discounts covers
### Purpose
- Price every order line the same way, every time
- Keep price, discount and freight rules auditable
### In scope
- Price records, price elements, search order
- Price calculation, assignment and revenue accounts
### Outcome
- A net price and tax on every line
- Revenue, discounts and freight on the right accounts

## Pricing rules are set once, used on every order
Layout: swimlane handoffs
- Pricing analyst: Agrees the price and discount
- Pricing analyst: Maintains the price records
- Pricing analyst: Above the approval limit?
- Commercial lead: If yes, approve the change
- Pricing analyst: If no, activate the record
- Sales order: Determines price at entry
- Billing: Copies or re-prices on the invoice

## The systems and data it runs on
| Step | What the system does | Records it keeps |
|---|---|---|
| Price records | Prices, discounts and surcharges kept with validity dates | Price records |
| Price elements | Each element has a role: base price, discount, freight, tax | Price element definitions |
| Search order | The most specific record wins: customer-item, then group, then list | Search sequence |
| Price calculation | Elements are applied in order with subtotals and rules | Calculation steps, net price |
| Which calculation | Sales channel, order type and customer pick the calculation | Calculation assignment |
| Revenue posting | Revenue, discounts and freight post to their accounts | Account mapping, ledger postings |

## Five steps find the price on every line
Layout: process numbered
- Records: prices and discounts
- Search: most specific first
- Elements: price, discount, freight
- Calculate: steps and subtotals
- Assign: per channel and customer

## Controls and exceptions
| Control | How it works | Owner |
|---|---|---|
| Approval for price changes | Records beyond tolerance need a second approver | Commercial lead |
| Mandatory price | The base price is mandatory: no price, no order | Pricing analyst |
| Manual change limit | Manual overrides limited per price element | Pricing team |
| Validity dates | Every record has a start and end date | Pricing analyst |

## KPIs that show it works
| KPI | What it measures | Data source |
|---|---|---|
| Price accuracy | Invoice lines billed at the agreed price | Invoiced price vs price list |
| Manual price override rate | Lines with a hand-changed price | Manual price flag on the line |
| Pricing-related credits | Credit memos caused by wrong prices | Credit memo reasons |
| Price change lead time | Approved change to live record | Change log vs effective date |

## Today and target
### Today
- Prices and discounts kept in many overlapping records
- Manual price changes common at order entry
### Target
- One price list per customer group with a clear search order
- Manual changes rare, limited and approved
