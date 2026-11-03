---
id: rt-so-planogram
domain: Retail
l1: Store Operations
l2: Planogram and space changes
summary: Planogram and space changes from the space plan to a set store: store-specific planograms, reset kits, the reset window, photo compliance.
systems: Space planning, Assortment planning, Item master, Store task app, Store inventory
tags: planogram, POG, reset, space planning, fixture, compliance, shelf set
order: 305
---
# Planogram and space changes

## What planogram changes cover
### Purpose
- Put the right items in the right space
- Reset every store on time, as planned
### In scope
- Planograms by fixture and store cluster
- Reset kits, labels, set and photo check
### Outcome
- Stores that match the planogram
- Old items out, new items on the shelf

## Space plans it, stores set it
Layout: swimlane handoffs
- Merchant: Approves the new assortment
- Space planner: Builds planograms by cluster
- Supply chain: Ships the reset kits
- Store team: Sets the reset overnight
- Store team: Matches the planogram?
- Store team: If yes, upload photos and close
- Space planner: If no, approve or fix the variance

## Systems and data for planogram changes
| Step | What the system does | Records it keeps |
|---|---|---|
| Planogram | Items, facings and positions by fixture | Planogram, version, dates |
| Store fit | Each store gets the version that fits its fixtures | Store-to-planogram link |
| Reset task | A task with the planogram, labels and due date | Store task, label batch |
| Compliance | Photos and sign-off uploaded by section | Section photos, sign-off |

## Six steps from space plan to set store
Layout: process arrow
- Plan: space and facings by cluster
- Publish: planograms to stores
- Ship: new items and reset kits
- Pull: discontinued items first
- Set: during the reset window
- Prove: photos and sign-off

## Controls and exceptions
| Control | How it works | Owner |
|---|---|---|
| Version control | One live planogram per fixture and store | Space planning |
| Reset window | Resets set and confirmed by the due date | Store operations |
| Item readiness | New items set up and shipped before the reset | Merchandising |
| Photo review | A sample of photos checked against the plan | Visual merchandising |

## KPIs that show it works
| KPI | What it measures | Data source |
|---|---|---|
| Planogram compliance | Sections that match the plan | Photo reviews, audits |
| Resets by due date | Resets confirmed on time | Store task app |
| Sales per linear foot | Sales against shelf space | Sales and space data |
| Gaps after reset | Empty facings in the first weeks | Store gap scans |

## Today and target
### Today
- Paper planograms, one version for all stores
- No proof the reset matches the plan
### Target
- Store-specific planograms on the store app
- Photo proof reviewed for every reset
