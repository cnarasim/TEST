---
id: rt-so-store-receiving
domain: Retail
l1: Store Operations
l2: Store receiving and transfers
summary: Store deliveries checked in against the ASN, discrepancies claimed, store-to-store transfers sent and received.
systems: Store inventory app, ERP inventory, WMS
tags: store receiving, ASN, discrepancy, store transfer, damages
order: 301
---
# Store receiving and transfers

## What this process covers
### Purpose
- Put deliveries on the shelf the day they arrive
- Book exactly what the store received
### In scope
- DC and vendor deliveries, ASN check-in
- Discrepancies, damages and store transfers
### Outcome
- Store stock correct after every delivery
- Claims raised while the evidence is fresh

## Stores check in, the DC answers discrepancies
Layout: swimlane handoffs
- DC: Ships with an ASN
- Store team: Scans cartons at the door
- Store team: Cartons match the ASN?
- Store team: If yes, confirm the receipt
- Store team: If no, record the discrepancy
- Inventory control: Resolves the claim
- Store team: Fills the shelf

## The systems and data it runs on
| Step | What the system does | Records it keeps |
|---|---|---|
| Expected delivery | The DC ASN tells the store what is coming | Inbound delivery |
| Receive | Cartons scanned at the back door; receipt posted | Goods receipt |
| Discrepancy | Differences recorded with a reason | Receipt difference, claim |
| Store transfer | Stock moved between stores on a transfer order | Transfer order |
| Damages | Damaged units written off with a reason | Write-off posting |

## Five steps from back door to shelf
Layout: process chevrons
- Arrive: truck with ASN
- Scan: every carton
- Check: against the ASN
- Claim: differences and damages
- Fill: the shelf

## Controls and exceptions
| Control | How it works | Owner |
|---|---|---|
| Carton scan | Every carton scanned at the back door | Store team |
| Discrepancy window | Claims accepted only within 48 hours | Inventory control |
| Transfer approval | Store transfers above a value need approval | District manager |
| Damage reason codes | Every scrap posting carries a reason | Store manager |

## KPIs that show it works
| KPI | What it measures | Data source |
|---|---|---|
| Receipt to shelf time | Hours from delivery to shelf | Receipt and task times |
| Delivery accuracy | Deliveries with no discrepancy | Receipt differences |
| Open claims | Claims older than a week | Claims log |
| Store transfer volume | Units moved between stores | Transfer volume |

## Today and target
### Today
- Deliveries signed for without a carton count
- Discrepancies e-mailed to the DC
### Target
- Scan-based check-in against the ASN
- Claims raised and answered in the system
