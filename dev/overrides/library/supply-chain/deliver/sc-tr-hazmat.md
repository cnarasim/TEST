---
id: sc-tr-hazmat
domain: Supply Chain
l1: Deliver
l2: Dangerous goods shipping
summary: Shipping regulated beauty items safely and legally: aerosols, nail polish, fragrance and battery tools, from classification to the parcel.
systems: PIM, ERP item master, WMS, Parcel shipping system
tags: hazmat, dangerous goods, aerosols, flammable, limited quantity, safety data sheet, ground only
order: 505
---
# Dangerous goods shipping

## What dangerous goods shipping covers
### Purpose
- Regulated items shipped safely and legally
- No fines, refused parcels or incidents
### In scope
- Classification from safety data sheets
- Packing, marks, routes and training
### Outcome
- Every regulated item flagged before it ships
- Parcels carriers accept the first time

## Many beauty items are regulated to ship
| Item type | Example | Why it is regulated |
|---|---|---|
| Aerosols | Hairspray, dry shampoo | Compressed gas, often flammable |
| Flammable liquids | Nail polish, fragrance, remover | Alcohol or solvent based |
| Lithium batteries | Cordless styling tools | Fire risk if damaged or shorted |
| Oxidizers | Some hair color developers | Can intensify a fire |
> Notes: a starting point, not a classification; confirm each item from its safety data sheet and the current carrier and transport rules.

## Five steps keep every shipment legal
Layout: process numbered
- Classify: each item from its safety data sheet
- Flag: hazard and limited-quantity status in the item master
- Pack: approved packaging and the right marks
- Route: ground only where air is not allowed
- Audit: sample packages and refresh training

## Compliance classifies, systems enforce it
Layout: swimlane handoffs
- Item setup: Requests the safety data sheet
- Product compliance: Classifies the item
- Product compliance: Regulated for transport?
- Product compliance: If yes, sets hazmat flags
- Product compliance: If no, clears the item
- DC packing: Packs and marks by the flag
- Shipping system: Blocks air for flagged items

## Controls and exceptions
| Control | How it works | Owner |
|---|---|---|
| Classify before launch | No item ships without a review | Product compliance |
| Air blocked by flag | Flagged items offered ground only | Shipping system |
| Marked packages | Limited quantity marks on cartons | DC packing |
| Trained staff | Training renewed every [n] years | Safety lead |

## KPIs that show it works
| KPI | What it measures | Data source |
|---|---|---|
| Classified at launch | New items reviewed before sale | Item setup records |
| Carrier refusals | Parcels refused for hazmat errors | Carrier exceptions |
| Incidents | Leaks, spills or fires in transit | Incident log |
| Training current | Staff with current certification | Training records |

## Today and target
### Today
- Items classified after the first refusal
- Flags kept in a spreadsheet
### Target
- Every item classified before it is sold
- Systems apply the rules on every parcel
