---
id: sc-sp-supplier-collaboration
domain: Supply Chain
l1: Source & Procure
l2: Supplier collaboration and scorecards
summary: Working with key vendors on one plan: shared forecasts, capacity commitments, order confirmations, scorecards and joint business reviews.
systems: Planning system, Vendor portal, ERP purchasing, BI dashboards
tags: supplier collaboration, CPFR, vendor scorecard, OTIF, capacity commitment, business review, shared forecast
order: 208
---
# Supplier collaboration and scorecards

## What supplier collaboration covers
### Purpose
- Vendors who plan from our forecast
- Problems found before they reach the shelf
### In scope
- Shared forecasts and capacity commitments
- Scorecards and quarterly business reviews
### Outcome
- Higher on-time, in-full deliveries
- Fewer emergency orders and expedites

## A shared plan runs in a monthly loop
Layout: process cycle
- Share: the item forecast for the next [n] weeks
- Commit: the vendor confirms capacity
- Order: POs confirmed in full, on time
- Measure: the scorecard every month
- Review: a joint business review each quarter

## We share the plan, vendors commit to it
Layout: swimlane handoffs
- Supply planning: Shares the forecast
- Vendor: Confirms capacity by item
- Supply planning: Capacity covers the plan?
- Supply planning: If yes, releases the POs
- Supply planning: If no, agrees options
- Vendor: Confirms each PO
- Merchandising: Reviews the scorecard

## What the vendor scorecard measures
| Measure | What it shows | Target |
|---|---|---|
| On time in full | POs delivered complete and on time | [target] |
| Fill rate | Units shipped vs ordered | [target] |
| ASN accuracy | ASNs that match the receipt | [target] |
| Lead time | Days from PO to receipt | [target] |
| Compliance | Shipments with no breach | [target] |

## Systems and data for collaboration
| Step | What the system does | Records it keeps |
|---|---|---|
| Forecast | Publishes the forecast to the portal | Shared forecast versions |
| Capacity | Captures the vendor's commitment | Committed quantities |
| Confirm | Reads PO acknowledgements | Confirmed lines and dates |
| Score | Calculates the monthly scorecard | Scorecard history |

## Today and target
### Today
- Vendors see our needs when the PO arrives
- Scorecards built by hand, shared rarely
### Target
- Forecasts shared, capacity confirmed early
- Monthly scorecards, quarterly joint reviews
