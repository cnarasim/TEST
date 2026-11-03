---
id: ea-ds-resilience
domain: Enterprise Architecture
l1: Design and Standards
l2: Resilience and disaster recovery
summary: How systems stay up and recover: tiers with recovery targets, design rules for resilience, and regular recovery tests.
systems: Cloud platform, Backup service, Monitoring, POS, OMS, WMS, ERP
tags: resilience, disaster recovery, RTO, RPO, failover, backup, business continuity
order: 609
---
# Resilience and disaster recovery

## What resilience covers
### Purpose
- Selling and fulfilling continue when parts fail
- Recovery in a time the business agreed
### In scope
- Recovery tiers and targets
- Design rules, backups and recovery tests
### Outcome
- Shorter outages, no lost orders
- Proof that recovery works before we need it

## Tiers set the recovery targets
| Tier | Recovery time | Data loss allowed | Examples |
|---|---|---|---|
| 1 Selling and fulfilling | Under [n] hours | Under [n] minutes | POS, ecommerce, OMS, WMS |
| 2 Running the business | Within [n] hours | Up to [n] hours | ERP, planning |
| 3 Analysis and support | Within [n] days | Last daily backup | Reporting, collaboration |

## Six rules for resilient design
Layout: hexagons
- Redundant: no single point of failure
- Isolated: one failure does not spread
- Degrade gracefully: stores keep selling offline
- Backed up: copies kept apart and restore-tested
- Tested: failover drills every [n] months
- Observed: alerts before guests notice

## Recovery is tested, not assumed
Layout: swimlane handoffs
- Operations: Schedules the recovery test
- Application team: Fails over to recovery
- Application team: Recovered within target?
- Application team: If yes, records the result
- Application team: If no, logs a fix and date
- Risk and compliance: Reviews results quarterly

## KPIs that show it works
| KPI | What it measures | Data source |
|---|---|---|
| Tier 1 apps tested | Recovery tested in the last [n] months | Test records |
| Recovery time achieved | Actual vs target in tests | Test records |
| Restore success | Backups restored without error | Backup reports |
| Outage minutes | Tier 1 downtime each month | Incident records |

## Today and target
### Today
- Recovery plans written, rarely tested
- Single points of failure in key systems
### Target
- Every tier 1 system tested each year
- Stores and DCs keep working through failures
