---
id: ea-pr-cloud-migration
domain: Enterprise Architecture
l1: Portfolio and Rationalisation
l2: Cloud migration assessment (6 Rs)
summary: Each application placed on one of six migration paths, the reasons, the waves and how the migration is run.
systems: Cloud platform, Application portfolio
tags: cloud migration, 6 Rs, rehost, replatform, refactor, retire, migration waves
order: 403
---
# Cloud migration assessment

## Six paths to the cloud
Layout: process list
- Rehost: move as is
- Replatform: small changes, managed services
- Refactor: rebuild for the cloud
- Repurchase: move to a cloud product
- Retire: switch it off
- Retain: keep where it is for now

## Each application's path
| Application | Path | Why | Wave |
|---|---|---|---|
| Application A | Rehost | Stable, end of hardware life | 1 |
| Application B | Replatform | Database to a managed service | 1 |
| Application C | Repurchase | A cloud product covers it | 2 |
| Application D | Refactor | Needs to scale at peak | 3 |
| Application E | Retire | Replaced by Application C | 2 |
| Application F | Retain | Tied to on-site equipment | - |

## Migration in waves
Layout: timeline quarters
- Wave 1: Jan 2027 – Apr 2027 (Infrastructure)
- Wave 2: May 2027 – Sep 2027 (Applications)
- Wave 3: Oct 2027 – Mar 2028 (Applications)
- Data centre exit: Jun 30, 2028 (Infrastructure)
> Notes: example dates; replace them with the plan.

## How each wave runs
Layout: process phases
- Assess: inventory; dependencies; cost (Weeks 1-4)
- Mobilise: landing zone; security; skills (Weeks 5-8)
- Migrate: move; test; cut over (Weeks 9-16)
- Optimise: right-size; automate; cost review (Weeks 17-20)
