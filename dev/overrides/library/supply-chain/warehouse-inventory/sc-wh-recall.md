---
id: sc-wh-recall
domain: Supply Chain
l1: Warehouse & Inventory
l2: Product recall
summary: Taking a recalled or withdrawn product out of DCs, stores and online orders fast, telling guests, returning stock and reporting.
systems: ERP inventory, WMS, OMS, POS, Quality system
tags: recall, product withdrawal, stock lock, lot trace, quarantine, guest notification, regulator report
order: 415
---
# Product recall

## What a recall covers
### Purpose
- Unsafe product off shelves within hours
- Guests and regulators told what they need
### In scope
- Vendor and regulator recalls, withdrawals
- DCs, stores, online orders and past buyers
### Outcome
- Recalled stock located and locked fast
- A full record for the vendor and regulator

## A recall runs in five phases
Layout: process phases
- Notify: notice received and items confirmed (hour 0)
- Lock: stock blocked in every system (hour [n])
- Pull: stores and DCs remove stock (day 1)
- Return: stock to the vendor or destroyed (week 1)
- Close: counts reconciled and reported (week [n])

## Quality leads, every channel acts
Layout: swimlane handoffs
- Quality: Receives the recall notice
- Quality: Confirms items and lots
- Inventory control: Locks stock everywhere
- Store operations: Pulls stock from shelves
- Quality: Guests affected?
- Quality: If yes, guest care contacts them
- Quality: If no, closes after the count

## Who does what in a recall
| Task | Owner | Done when |
|---|---|---|
| Confirm items and lots | Quality | Lot list signed off |
| Lock stock | Inventory control | Blocked in ERP, WMS, OMS and POS |
| Pull from stores | Store operations | Every store confirms its count |
| Tell guests | Guest care | Affected guests contacted |
| Report | Quality | Vendor and regulator reports filed |

## KPIs that show it works
| KPI | What it measures | Data source |
|---|---|---|
| Time to lock | Hours from notice to block | Recall log |
| Stores confirmed | Stores that confirmed removal | Store task replies |
| Units recovered | Units pulled vs units on hand | Recall counts |
| Guests contacted | Affected guests reached | Guest care records |

## Today and target
### Today
- Recalls run by email and phone trees
- Stock sold online after the notice
### Target
- Stock blocked in every channel within hours
- A tested recall drill every [n] months
