---
id: to-cr-dr-test
domain: Technology Operations
l1: Change and Release
l2: Disaster recovery test
summary: Proving we can recover: recovery tiers with RTO and RPO, test scenarios, the failover and failback flow, controls, KPIs and actions.
systems: Backup platform, Recovery site, Monitoring platform, Ticketing tool, Runbook repository
tags: disaster recovery, DR test, RTO, RPO, failover, backup, resilience, business continuity
workbook: actions
order: 203
---
# Disaster recovery test

Prove that critical services come back in time, with the data we need, before a real disaster tests it for us.

## What the disaster recovery test covers
### Purpose
- Prove critical services recover in time
- Find the gaps before a real disaster does
### In scope
- Failover, restore from backup, failback
- Systems, data, people, runbooks, suppliers
### Outcome
- Recovery times measured, not assumed
- A fix list with owners and dates

## Each tier has its own RTO and RPO
| Tier | Example services | RTO | RPO |
|---|---|---|---|
| Tier 1 | Checkout, POS, payments, orders | [n] hours | [n] minutes |
| Tier 2 | WMS, replenishment, loyalty | [n] hours | [n] minutes |
| Tier 3 | Reporting, planning, internal tools | [n] days | [n] hours |
> Notes: RTO is how long until the service is back; RPO is how much data, measured in time, we can afford to lose. Agree both with each business owner.

## Test the scenarios that really happen
### Site or region loss
- Data center or cloud region goes down
- Fail over to the recovery site
### Cyber attack
- Ransomware hits servers and backups
- Restore from isolated, immutable copies
### Data corruption
- A bad change or load corrupts data
- Restore to a point before the error

## The test proves failover, then failback
Layout: swimlane handoffs
- DR coordinator: Announces scope and window
- Infrastructure team: Fails over to recovery site
- Application teams: Restore and check applications
- Business testers: Confirm key processes work
- DR coordinator: RTO and RPO met?
- DR coordinator: If yes, signs off the result
- DR coordinator: If no, logs gaps and actions
- Infrastructure team: Fails back to production

## Systems and data for the DR test
| Step | What the system does | Records it keeps |
|---|---|---|
| Back up | Backups and replicas on schedule | Backup log, replica status |
| Fail over | Services started at recovery site | Runbook, time stamps |
| Restore | Data restored and checked | Restore log, data checks |
| Verify | Test scripts confirm service | Test results |
| Report | Times compared with targets | DR test report |

## Four phases from plan to proven recovery
Layout: process phases
- Plan: scope; scenarios; approvals (T-6 weeks)
- Prepare: runbooks; contacts; backups checked (T-2 weeks)
- Test: fail over; verify; fail back (Test day)
- Review: times; gaps; actions (T+1 week)

## Controls and exceptions
| Control | How it works | Owner |
|---|---|---|
| Annual test | Tier 1 tested at least yearly | Service owner |
| Restore testing | Restores tested, not just backups | Infrastructure lead |
| Runbook upkeep | Updated after changes and tests | Application owner |
| Test window freeze | No other changes during the test | Change manager |
| Stop criteria | Stop if production is at risk | DR coordinator |

## KPIs that show it works
| KPI | What it measures | Data source |
|---|---|---|
| RTO achieved | Recovery time vs target | DR test report |
| RPO achieved | Data lost vs target | Restore logs |
| Services tested | Tier 1 and 2 tested this year | DR test schedule |
| Actions closed | DR actions closed on time | Action log |
| Backup success | Backups that restore cleanly | Backup platform |

## Today and target
### Today
- Recovery plans on paper, rarely tested
- RTO and RPO assumed, never measured
### Target
- Every Tier 1 service tested every year
- Measured times, gaps fixed before peak
