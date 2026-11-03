---
id: rt-so-damages
domain: Retail
l1: Store Operations
l2: Damages, testers and destroys
summary: Unsellable product handled by rule: damages and testers recorded with a reason, vendor credits claimed, units destroyed safely.
systems: Store inventory app, ERP inventory, ERP purchasing, Returns center
tags: damages, testers, destroy, RTV, damage allowance, write-off, hazardous waste, known shrink
order: 308
---
# Damages, testers and destroys

## What damages and testers cover
### Purpose
- Account for every unit that cannot be sold
- Recover the value brands owe us
### In scope
- Damages, testers and destroys by reason
- Vendor allowances, RTV and safe disposal
### Outcome
- Known shrink, recorded the same day
- Vendor credits claimed, waste disposed safely

## Reason codes decide where a unit goes
Layout: swimlane handoffs
- Store team: Finds a damaged or opened unit
- Store team: Scans it with a reason code
- Store team: Brand takes it back?
- Store team: If yes, hold for return to vendor
- Store team: If no, destroy by the waste rules
- Inventory control: Posts the write-off
- Finance: Claims the credit or allowance

## Systems and data for damages and testers
| Step | What the system does | Records it keeps |
|---|---|---|
| Record | The unit is scanned out with a reason code | Damage or tester entry |
| Tester | Tester units issued and expensed by brand | Tester issue, expense |
| Disposition | Brand terms decide RTV, allowance or destroy | Disposition, vendor terms |
| Write-off and claim | Stock written off and credit claimed from the brand | Write-off posting, vendor claim |

## One unsellable unit, four paths
Layout: process diverge
- Off sale: damaged, opened, expired or a tester
- Tester: opened for the counter, expensed
- Return to vendor: sealed, damaged in transit
- Allowance: destroyed, the brand pays a set rate
- Destroy: used or unsafe, disposed by the rules

## Controls and exceptions
| Control | How it works | Owner |
|---|---|---|
| Reason codes | Every unit leaves stock with a reason | Store manager |
| Tester limits | Testers per item capped by the planogram | Store operations |
| Witnessed destroys | Destroys logged and witnessed by a manager | Asset protection |
| Hazardous waste | Polish, aerosols and fragrance disposed by the rules | Environmental compliance |

## KPIs that show it works
| KPI | What it measures | Data source |
|---|---|---|
| Damage rate | Damaged units as a share of sales | Damage entries, sales |
| Tester cost | Tester expense by brand and store | Tester issues |
| Vendor recovery | Credits claimed vs credits due | Vendor claims, terms |
| Disposal compliance | Destroys logged with a witness and a manifest | Destroy logs, waste manifests |

## Today and target
### Today
- Damages thrown away without a scan
- Allowances and RTV credits left unclaimed
### Target
- Every unit scanned with a reason and a path
- Credits claimed monthly under brand terms
