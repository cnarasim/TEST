---
id: fi-rr-revenue-recognition
domain: Finance
l1: Record to Report
l2: Revenue recognition across channels
summary: When and how much revenue to book for stores, ship to home, pickup, salon services, loyalty points, gift cards and returns.
systems: POS, Order management system, Loyalty platform, ERP finance
tags: revenue recognition, ASC 606, performance obligation, returns reserve, ship to home, buy online pick up, loyalty deferral
order: 305
---
# Revenue recognition across channels

## What revenue recognition covers
### Purpose
- Book revenue when the guest gets control
- One rule for every channel and tender
### In scope
- Stores, ship to home, pickup and salon services
- Loyalty points, gift cards and returns
### Outcome
- Revenue in the right period and amount
- Deferrals and reserves that hold up in audit

## Channels sell, accounting decides when
Layout: swimlane handoffs
- Channels: Record sales, tenders and points
- Revenue accountant: Goods or service delivered?
- Revenue accountant: If yes, recognize the revenue
- Revenue accountant: If no, defer until it is delivered
- Revenue accountant: Allocates value to points earned
- Controller: Reviews the returns reserve

## Each channel has its own revenue moment
| Sale | When revenue is booked | How it is measured |
|---|---|---|
| Store purchase | At checkout | Price less discounts |
| Ship to home | When control passes, per terms | Price plus shipping fees |
| Buy online, pick up | When the guest picks up | Price less order discounts |
| Salon service | When the service is done | Service price |
| Loyalty points | When points are redeemed or expire | Allocated standalone value |
> Notes: sales tax is never revenue. Gift cards are revenue only when redeemed, or as breakage; see the loyalty and gift card liability template.

## Five steps set the amount and the timing
Layout: process numbered
- Contract: the order or the receipt
- Obligations: goods, services and points
- Price: net of discounts and expected returns
- Allocate: by standalone selling price
- Recognize: as each obligation is met
> Notes: the five steps of ASC 606 (IFRS 15 is the same model).

## Systems and data for revenue recognition
| Step | What the system does | Records it keeps |
|---|---|---|
| Sales capture | POS and orders post sales | Sales and tender lines |
| Fulfilment events | Shipment and pickup release revenue | Shipment and pickup dates |
| Loyalty | Points earned and redeemed | Points ledger |
| Deferral | Unearned revenue held | Deferred revenue balance |
| Returns reserve | Expected returns estimated | Refund liability, return asset |

## Controls keep revenue in the right period
| Control | How it works | Owner |
|---|---|---|
| Period-end cut-off | Orders in transit at month end checked | Revenue accounting |
| Returns reserve review | Reserve trued up to actual return rates | Controller |
| Points value review | Standalone value and redemption rates reviewed | Revenue accounting |
| Revenue policy | One documented policy for every channel | Technical accounting |

## KPIs show revenue is right and on time
| KPI | What it measures | Data source |
|---|---|---|
| Cut-off errors | Sales booked in the wrong period | Cut-off tests |
| Reserve accuracy | Returns reserve vs actual returns | Returns and reserve |
| Deferred revenue | Revenue received, not yet earned | Deferral accounts |
| Manual revenue entries | Revenue journals keyed by hand | Journal source |

## From spreadsheets to rules in the ledger
### Today
- Deferrals calculated in spreadsheets
- Returns reserve set once a year
### Target
- Deferrals from order and loyalty data
- Returns reserve updated every month
