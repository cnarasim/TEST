---
id: sc-tr-carrier-onboarding
domain: Supply Chain
l1: Deliver
l2: Carrier onboarding
summary: Adding a new carrier: qualification, contract and rates, system and EDI setup, test loads and the first scorecard.
systems: TMS, ERP vendor master, Freight audit system, EDI
tags: carrier onboarding, carrier qualification, insurance, rates, EDI 204, EDI 214, carrier scorecard
order: 507
---
# Carrier onboarding

## What carrier onboarding covers
### Purpose
- Only qualified carriers move our freight
- New carriers live without billing surprises
### In scope
- Insurance, authority and safety checks
- Rates, system setup, tests and scorecards
### Outcome
- Carriers live in weeks, not months
- Clean tracking and invoices from day one

## Five steps to the first load
Layout: process numbered
- Qualify: insurance, operating authority, safety record
- Contract: rates, surcharges and service levels
- Connect: tenders, tracking and invoices by EDI
- Test: trial loads, scans and a first invoice
- Go live: first awards and the monthly scorecard

## Compliance checks before any award
Layout: swimlane handoffs
- Transportation: Selects the carrier
- Compliance: Checks insurance and authority
- Compliance: Requirements met?
- Compliance: If yes, approves the carrier
- Compliance: If no, asks for the missing items
- Integration: Sets up and tests EDI
- Transportation: Awards the first loads

## Systems and data for onboarding
| Step | What the system does | Records it keeps |
|---|---|---|
| Qualify | Stores documents and expiry dates | Insurance, authority |
| Contract | Loads rates and surcharges | Rate tables |
| Connect | Tests EDI 204, 214 and 210 | Message test results |
| Pay | Sets the carrier up as a vendor | Vendor and bank details |
| Score | Tracks service each month | Carrier scorecard |

## KPIs that show it works
| KPI | What it measures | Data source |
|---|---|---|
| Days to onboard | Request to first load | Onboarding log |
| First-load success | Test loads with no exception | Test results |
| Tracking compliance | Loads with every scan event | EDI 214 events |
| Invoices auto-matched | Bills matched without review | Freight audit |

## Today and target
### Today
- Onboarding by email, documents lost
- Tracking and billing fixed after go-live
### Target
- One checklist and system for every carrier
- Tests passed before the first award
