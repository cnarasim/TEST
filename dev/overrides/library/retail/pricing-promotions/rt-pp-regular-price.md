---
id: rt-pp-regular-price
domain: Retail
l1: Pricing & Promotions
l2: Regular price management
summary: Retail prices calculated from cost and margin rules, approved, activated and sent to every register and label.
systems: Pricing engine, POS, ERP, Label printing
tags: retail price, sales price calculation, price change, POS download, labels, price record
order: 201
---
# Regular price management

## What regular price management covers
### Purpose
- Set the shelf price every store charges
- Change prices on one date, everywhere
### In scope
- Sales price calculation and approval
- Activation, POS download and labels
### Outcome
- The same price at the shelf, the register and online
- A margin that matches the plan

## Pricing proposes, merchants approve, stores re-ticket
Layout: swimlane handoffs
- Pricing analyst: Proposes the new retail price
- Pricing analyst: Checks margin and competition
- Merchant: Margin within the target?
- Merchant: If yes, approve the price
- Merchant: If no, send back for review
- POS team: Sends prices to the registers
- Store team: Changes the shelf labels

## The systems and data it runs on
| Step | What the system does | Records it keeps |
|---|---|---|
| Price calculation | Proposed price from cost and margin rules | Price proposal, margin |
| Price record | The approved price with its effective date | Price record by zone or store |
| Worklist | Pending changes reviewed in one list | Price change worklist |
| Send to POS | New prices sent to every register before the date | POS price file |
| Labels | Shelf labels printed by store | Label batch |

## Five steps take a price from proposal to shelf
Layout: process chevrons
- Propose: cost and margin rules
- Compare: competitor prices
- Approve: merchant sign-off
- Activate: valid-from date
- Download: POS and labels

## Controls and exceptions
| Control | How it works | Owner |
|---|---|---|
| Margin floor | Prices below the margin floor need approval | Merchant |
| Effective dating | Every change has a valid-from date | Pricing analyst |
| POS confirmation | Stores confirm the price file loaded | POS team |
| Price audit | Sample shelf-to-register checks each week | Store operations |

## KPIs that show it works
| KPI | What it measures | Data source |
|---|---|---|
| Price accuracy at register | Shelf price equals register price | Store price audits |
| Price change cycle time | Approval to live in every store | Approval vs register confirmation |
| Margin vs plan | Achieved margin rate against plan | Actual margin vs plan |
| Label compliance | Shelf labels changed on time | Store task completion |

## Today and target
### Today
- Price changes keyed by hand in several systems
- Shelf and register prices differ for days
### Target
- One price calculation feeding POS and online
- Prices and labels change on the same date
