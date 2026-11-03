---
id: ea-ds-integration-patterns
domain: Enterprise Architecture
l1: Design and Standards
l2: Integration patterns
summary: The approved ways systems connect (API, event, batch file, stream, EDI), when to use each, and the standards every interface meets.
systems: Integration platform, Event platform, EDI, ERP, OMS, WMS
tags: integration patterns, API, events, batch, EDI, idempotency, reconciliation
order: 604
---
# Integration patterns

## What integration standards cover
### Purpose
- A short list of approved ways to connect
- Interfaces that are safe to retry and easy to run
### In scope
- APIs, events, files, streams and EDI
- Monitoring, replay and reconciliation
### Outcome
- New interfaces built faster on one platform
- Failures found before users notice

## One need, four ways to connect
Layout: process diverge
- Need: two or more systems must share data
- API: ask and answer in real time
- Event: publish once, many systems react
- Batch file: large volumes on a schedule
- Stream: a continuous high-volume feed

## Pick the pattern by the need
| Need | Pattern | Example |
|---|---|---|
| An answer now, one caller | API | Price and stock check |
| Many systems react to a change | Event | Order shipped |
| Large volume on a schedule | Batch file | Nightly sales to finance |
| A continuous feed | Stream | Store sales to the data platform |
| Documents with partners | EDI | Purchase orders to vendors |

## Standards every interface meets
| Standard | Rule | Why |
|---|---|---|
| On the platform | No new point-to-point connections | One place to secure and watch |
| Safe to retry | A replay creates no duplicates | Recovery without clean-up |
| Versioned | Old versions kept [n] months | Consumers move on their schedule |
| Monitored | Every interface alerts on failure | Errors fixed before users call |
| Reconciled | Counts and totals checked daily | No silent data loss |

## A new interface follows one path
Layout: swimlane handoffs
- Project team: Describes the data and timing
- Integration team: Picks the pattern
- Integration team: An interface already fits?
- Integration team: If yes, reuses and extends it
- Integration team: If no, builds on the platform
- Operations: Monitors and alerts on failure

## KPIs that show it works
| KPI | What it measures | Data source |
|---|---|---|
| Interfaces on the platform | Share of all interfaces | Interface inventory |
| Point-to-point left | Old direct connections | Interface inventory |
| Failed messages | Errors per day | Integration monitoring |
| Time to build | Days for a new interface | Project records |

## Today and target
### Today
- Each project picks its own way to connect
- Failures found when reports look wrong
### Target
- Five approved patterns, one platform
- Every interface monitored and reconciled
