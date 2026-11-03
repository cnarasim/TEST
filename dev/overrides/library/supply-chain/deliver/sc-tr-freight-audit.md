---
id: sc-tr-freight-audit
domain: Supply Chain
l1: Deliver
l2: Freight audit and payment
summary: Checking every freight bill against the shipment and the contract rate before it is paid, disputing errors and allocating the cost.
systems: Freight audit system, TMS, ERP, Accounts payable
tags: freight audit, freight payment, carrier invoice, accessorials, fuel surcharge, EDI 210, overcharge
order: 504
---
# Freight audit and payment

## What freight audit covers
### Purpose
- Pay carriers what the contract says, on time
- Recover overcharges before they are paid
### In scope
- Truckload, less than truckload and parcel bills
- Disputes, payment and cost allocation
### Outcome
- Fewer overcharges and duplicate payments
- Freight cost by lane, DC and channel

## Five steps for every freight bill
Layout: process chevrons
- Receive: the bill by EDI 210 or portal
- Match: to the shipment and the contract rate
- Decide: approve, short-pay or dispute
- Pay: on the agreed terms
- Allocate: cost to lane, DC and channel

## The audit checks, people judge exceptions
Layout: swimlane handoffs
- Carrier: Sends the freight bill
- Audit system: Matches shipment and rate
- Audit system: Within the tolerance?
- Audit system: If yes, approves payment
- Audit system: If no, sends it for review
- Freight audit team: Disputes or approves
- Accounts payable: Pays the carrier

## Common billing errors
| Error | How the audit finds it | Result |
|---|---|---|
| Wrong rate | Bill vs contract rate | Short-paid to contract |
| Duplicate bill | Same shipment billed twice | Rejected |
| Accessorial not agreed | Charge not in the contract | Disputed with proof |
| Wrong weight or class | Bill vs shipped weight | Re-rated |
| Fuel surcharge wrong | Bill vs the published index | Corrected |

## KPIs that show it works
| KPI | What it measures | Data source |
|---|---|---|
| Bills paid on time | Payments within terms | Accounts payable |
| Overcharges recovered | Value corrected before payment | Audit results |
| Exception rate | Bills needing review | Audit system |
| Cost per unit shipped | Freight cost per unit | Freight cost allocation |

## Today and target
### Today
- Bills paid as received, errors found later
- Freight cost seen only as one total
### Target
- Every bill matched before it is paid
- Cost visible by lane, DC and channel
