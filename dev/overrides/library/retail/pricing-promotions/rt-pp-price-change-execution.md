---
id: rt-pp-price-change-execution
domain: Retail
l1: Pricing & Promotions
l2: Price changes in store
summary: Store execution of price changes: batches released ahead of the date, labels and signs printed, set by the effective date and scan-audited.
systems: Pricing engine, POS, Store task app, Label printing, Handheld scanners
tags: price change, store execution, shelf labels, signs, price audit, re-ticket, electronic shelf labels
order: 206
---
# Price changes in store

## What price changes in store cover
### Purpose
- The shelf price matches the register, always
- Every change set by its effective date
### In scope
- Price batches, labels, signs and stickers
- Set, verify and remove on the right dates
### Outcome
- Price accuracy proven by scans
- Fewer price overrides at the register

## Pricing releases, stores set and scan
Layout: swimlane handoffs
- Pricing team: Releases the price batch
- POS: Loads the new prices overnight
- Store team: Prints labels and signs
- Store team: Sets them before opening
- Store team: Label matches the register?
- Store team: If yes, confirm the task
- Store team: If no, reprint and fix
- Store operations: Reviews compliance by store

## Systems and data for price changes
| Step | What the system does | Records it keeps |
|---|---|---|
| Price batch | Changes grouped by effective date and department | Price batch, effective date |
| POS update | New prices loaded to every register before opening | POS price file, load confirmation |
| Labels and signs | Labels print in shelf order, one task per batch | Label batch, store task |
| Verification | Handheld scans compare label and register price | Scan audit result |

## Five steps put a new price on the shelf
Layout: process vertical
- Release: the batch reaches stores [n] days ahead
- Load: the POS takes the new prices overnight
- Print: labels and signs print in shelf order
- Set: labels changed before the store opens
- Verify: a scan audit finds and fixes misses

## Controls and exceptions
| Control | How it works | Owner |
|---|---|---|
| Lead time | Batches reach stores [n] days before they take effect | Pricing team |
| Task deadline | Label tasks stay open until confirmed, then escalate | Store manager |
| Scan audit | A sample of labels scanned against the POS each week | Store operations |
| Sign take-down | Promotion signs removed when the offer ends | Store team |

## KPIs that show it works
| KPI | What it measures | Data source |
|---|---|---|
| Price accuracy | Labels that match the register price | Scan audits |
| Task completion | Price tasks done by the effective date | Store task app |
| Price overrides | Prices changed by hand at the register | POS overrides |
| Hours on pricing | Store hours spent on labels and signs | Task and labor data |

## Today and target
### Today
- Batches arrive late, labels set mid-day
- Price errors found by guests at the register
### Target
- Batches on time, labels set before opening
- Electronic shelf labels where prices change often
