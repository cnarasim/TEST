---
id: sc-wh-inbound
domain: Supply Chain
l1: Warehouse & Inventory
l2: Inbound to DC (receiving and putaway)
summary: Vendor freight into the DC: dock appointment, ASN, unload, receive, quality and putaway to storage.
systems: WMS, Yard management, ERP, EDI
tags: receiving, putaway, ASN, dock, WMS, goods receipt
order: 401
---
# Inbound to DC (receiving and putaway)

## What this process covers
### Purpose
- Get vendor freight available to sell quickly
- Receive exactly what the vendor shipped
### In scope
- Appointments, ASN, unloading and receipt
- Quality checks, labelling and putaway
### Outcome
- Stock available within hours of arrival
- Differences found at the door, not in the aisle

## Receiving turns trailers into stock
Layout: swimlane handoffs
- Vendor: Sends ASN, books a dock
- Yard: Checks the trailer in
- Receiver: Unloads and scans cartons
- Receiver: Matches the ASN?
- Receiver: If yes, post goods receipt
- Inventory control: If no, record the difference
- Putaway: Moves pallets to storage

## The systems and data it runs on
| Step | What the system does | Records it keeps |
|---|---|---|
| Advance ship notice | The vendor ASN creates the expected receipt | Inbound delivery |
| Yard and door | Appointments, check-in and door assignment | Appointment, trailer, door |
| Unload and receive | Cartons scanned at the door; receipt posted | Receipt, warehouse tasks |
| Putaway | The WMS directs each pallet to a bin | Putaway tasks, bin stock |
| Monitor | Open receipts and dock-to-stock time | Inbound status |

## Six steps bring vendor freight into the DC
Layout: retail inbound-to-dc

## Controls and exceptions
| Control | How it works | Owner |
|---|---|---|
| ASN before arrival | Trailers without an ASN wait in the yard | Yard lead |
| Blind receiving | Receivers count without seeing the expected quantity | DC lead |
| Over-receipt tolerance | Receipts above PO tolerance are blocked | Inventory control |
| Putaway confirmation | Every putaway task scanned to the bin | DC lead |

## KPIs that show it works
| KPI | What it measures | Data source |
|---|---|---|
| Dock-to-stock time | Trailer arrival to stock available | Trailer check-in vs putaway confirmed |
| ASN accuracy | ASNs that match what arrived | Receipt differences |
| Receipts per labour hour | Cartons received per hour | Tasks and labour hours |
| Putaway accuracy | Pallets found in the bin scanned | Count results |

## Today and target
### Today
- Paper receiving against printed POs
- Differences found days later in the aisle
### Target
- Scan-based receiving against the ASN
- Differences claimed with the vendor the same day
