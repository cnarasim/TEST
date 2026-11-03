---
id: sc-oc-delivery
domain: Supply Chain
l1: Order to Cash
l2: Delivery and shipping
summary: Outbound deliveries from due list to goods issue: picking, packing, loading, shipping documents and carrier hand-off.
systems: ERP order management, WMS, Transportation
tags: outbound delivery, shipping, picking, goods issue, shipping confirmation, carrier
order: 305
---
# Delivery and shipping

## What delivery and shipping covers
### Purpose
- Ship what was promised, on the confirmed date
- Hand the carrier complete, labelled loads
### In scope
- Delivery creation, picking, packing, loading
- Goods issue, shipping documents, carrier hand-off
### Outcome
- Goods issued and stock reduced on time
- A delivery the customer can match to the order

## The DC ships, the carrier takes over at the door
Layout: swimlane handoffs
- Shipping planner: Creates deliveries from the due list
- DC picker: Picks the delivery
- DC packer: Packs and labels the cartons
- DC packer: Quantity matches the delivery?
- DC packer: If yes, stage for loading
- DC lead: If no, short-pick or re-pick
- DC loader: Loads and posts goods issue
- Carrier: Collects and sends tracking

## The systems and data it runs on
| Step | What the system does | Records it keeps |
|---|---|---|
| Create deliveries | Released orders due for shipping become deliveries | Outbound delivery |
| Warehouse work | The WMS waves, picks and packs the delivery | Warehouse tasks, cartons |
| Monitor | One list of deliveries by status and cut-off | Delivery status |
| Shipment | Deliveries are loaded on a planned shipment | Shipment, load |
| Goods issue | Stock leaves the books when the truck is loaded | Goods issue, ledger posting |

## Six steps take a delivery out of the DC
Layout: process chevrons
- Create: delivery from order
- Wave: release to the floor
- Pick: scan every carton
- Pack: label and manifest
- Load: by route and stop
- Issue: goods issue and ASN

## Controls and exceptions
| Control | How it works | Owner |
|---|---|---|
| Delivery block | Credit or quality blocks stop delivery creation | Customer service |
| Scan-to-pack | Every unit scanned before the carton closes | DC lead |
| Goods issue on load | Stock leaves only when the truck is loaded | DC lead |
| ASN to customer | An ASN goes out with every shipment | Integration team |

## KPIs that show it works
| KPI | What it measures | Data source |
|---|---|---|
| On-time ship | Deliveries issued on the planned date | Planned vs actual goods issue |
| Pick accuracy | Lines picked with no error | Pick exceptions |
| Order cycle time | Order to goods issue in hours | Order time vs goods issue time |
| OTIF to customer | On time and in full at the customer | Goods issue date, delivered quantity, proof of delivery |

## Today and target
### Today
- Deliveries created in batches twice a day
- Paper pick lists and manual carton labels
### Target
- Deliveries created as orders release
- RF picking, scan-to-pack and automatic labels
