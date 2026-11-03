---
id: sc-sp-import-flow
domain: Supply Chain
l1: Source & Procure
l2: Import and inbound logistics
summary: Imported product from factory to DC: booking, ocean freight, customs, drayage and receipt against the ASN.
systems: ERP purchasing, Transportation, Trade compliance, WMS
tags: import, ocean, customs, container, landed cost, ASN
order: 203
---
# Import and inbound logistics

## What import and inbound logistics covers
### Purpose
- Bring imported product in on time at known cost
- See every container from factory to DC
### In scope
- Booking, ocean freight, customs and drayage
- ASN, receipt and landed cost
### Outcome
- Containers received against the PO and ASN
- Duties and freight in the product cost

## Imports pass four hands before the DC
Layout: swimlane handoffs
- Vendor: Books the shipment and loads
- Freight forwarder: Sends ASN and shipping documents
- Customs broker: Files the entry
- Customs broker: Cleared on arrival?
- Customs broker: If yes, release to drayage
- Customs broker: If no, resolve the hold
- DC: Receives containers against the ASN

## The systems and data it runs on
| Step | What the system does | Records it keeps |
|---|---|---|
| Import order | The purchase order carries import terms and port | Purchase order |
| Advance ship notice | The forwarder sends what is on each container | ASN, bill of lading |
| Freight booking | The transport system books and tracks the container | Freight order, tracking events |
| Customs | The broker files the entry; duties are recorded | Customs entry, duty |
| Landed cost | Freight and duty are added to the product cost | Landed cost, vendor and carrier invoices |

## Imported product crosses four lanes to reach a store
Layout: retail import-flow

## Controls and exceptions
| Control | How it works | Owner |
|---|---|---|
| ASN required | No container is received without an ASN | DC receiving |
| Classification check | Every article has a tariff code before booking | Trade compliance |
| Landed cost accrual | Freight and duty accrued at receipt | Cost accounting |
| Demurrage watch | Containers near the free-time limit alert | Logistics planner |

## KPIs that show it works
| KPI | What it measures | Data source |
|---|---|---|
| Transit time vs plan | Days from ship to DC receipt | Tracking events vs planned dates |
| Customs hold rate | Entries held at the port | Customs entry status |
| Landed cost accuracy | Planned vs actual freight and duty | Planned vs invoiced freight and duty |
| Demurrage cost | Fees paid for late container return | Freight invoices |

## Today and target
### Today
- Container status from carrier websites and e-mail
- Freight and duty spread across products by hand
### Target
- One tracked freight order per container
- Landed cost planned on the PO and settled on invoice
