---
id: sc-sp-vendor-compliance
domain: Supply Chain
l1: Source & Procure
l2: Vendor compliance and chargebacks
summary: The rules vendors ship to, how breaches are found at the DC, and how a chargeback is raised, disputed and settled fairly.
systems: WMS, ERP purchasing, Vendor portal, Accounts payable
tags: vendor compliance, chargeback, routing guide, ASN accuracy, labelling, dispute, scorecard
order: 205
---
# Vendor compliance and chargebacks

## What vendor compliance covers
### Purpose
- Shipments the DC can receive quickly
- Costs of non-compliance recovered fairly
### In scope
- Routing guide, labels, ASNs and appointments
- Chargebacks, disputes and vendor coaching
### Outcome
- Faster, cheaper receiving
- Vendors who know the rules and the score

## Five steps from rule to settlement
Layout: process chevrons
- Publish: the routing guide and charge schedule
- Detect: breaches logged at receipt with evidence
- Notify: the vendor sees the charge and proof
- Dispute: the vendor answers within [n] days
- Settle: deduct, waive or coach

## Evidence first, then the charge
Layout: swimlane handoffs
- DC receiving: Logs the breach with photos
- Vendor compliance: Checks evidence and rules
- Vendor compliance: Sends the charge notice
- Vendor: Disputes the charge?
- Vendor compliance: If yes, reviews the evidence
- Vendor compliance: If no, sends it to payables
- Accounts payable: Deducts from the next payment

## Common breaches and how they are found
| Breach | How it is found | Charge basis |
|---|---|---|
| ASN missing or late | Receipt with no matching ASN | Per shipment |
| Label or barcode wrong | Scan fails at receiving | Per carton |
| Missed appointment | Arrival vs booked slot | Per load |
| Overs, shorts, substitutes | Receipt vs ASN and PO | Per unit |
| Packing not to standard | Inspection at the dock | Per carton |

## Controls and exceptions
| Control | How it works | Owner |
|---|---|---|
| Proof on every charge | Photo or scan record attached | DC receiving |
| Agreed schedule | Charges only from the published list | Vendor compliance |
| Dispute window | Vendor has [n] days to respond | Vendor compliance |
| New vendor grace | Coaching period before charges | Merchandising |

## KPIs that show it works
| KPI | What it measures | Data source |
|---|---|---|
| Compliance rate | Shipments with no breach | Receiving records |
| ASN accuracy | ASNs that match the receipt | ASN vs receipt |
| Recovery rate | Charges collected vs raised | Payables deductions |
| Dispute rate | Charges disputed by vendors | Chargeback log |

## Today and target
### Today
- Charges raised without proof, often reversed
- Vendors learn the rules from deductions
### Target
- Every charge backed by evidence
- Vendor scorecards shared every month
