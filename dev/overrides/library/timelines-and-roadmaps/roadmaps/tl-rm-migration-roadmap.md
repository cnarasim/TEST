---
id: tl-rm-migration-roadmap
domain: Timelines and Roadmaps
l1: Roadmaps
l2: Migration roadmap
summary: Moving from old systems to new ones in waves: what moves when, the rehearsals and cutovers, parallel running and when the old system switches off.
systems: Project plan, Integration platform, Data migration tools
tags: migration roadmap, cutover, waves, decommission, data migration, parallel run, rehearsal
order: 106
---
# Migration roadmap

## Waves on the timeline
Layout: timeline quarters
- Wave 1 finance and procurement: Jan 2027 to Jun 2027 (Finance)
- Wave 2 inventory and DCs: Apr 2027 to Oct 2027 (Supply chain)
- Wave 3 stores and channels: Sep 2027 to Mar 2028 (Retail)
- Old system switched off: Jun 30, 2028 (Technology)
> Notes: example dates; nothing cuts over in the holiday freeze.

## What moves in each wave
| Wave | What moves | Why this order |
|---|---|---|
| 1 Finance and procurement | Ledgers, vendors, purchasing | Lowest guest impact |
| 2 Inventory and DCs | Stock, receiving, shipping | Needs finance live first |
| 3 Stores and channels | POS links, orders, returns | Needs inventory live first |

## Every wave runs the same cutover play
Layout: process phases
- Rehearse: two full dress rehearsals (T-6 weeks)
- Freeze: data and change freeze (T-1 week)
- Cut over: final load and checks (T-0)
- Hypercare: daily calls and fixes (Weeks 1-4)
- Switch off: old system read-only, then off (T+3 months)

## Go / no-go for each cutover
| Check | We go when | Decides |
|---|---|---|
| Rehearsals | Two clean runs inside the window | Cutover lead |
| Data | Counts and totals reconciled | Data lead |
| Business | Teams trained and signed off | Business lead |
| Support | Hypercare team and rota in place | Support lead |

## The old system switches off in steps
Layout: process chevrons
- Parallel: both run, results compared
- Read-only: old system for lookups only
- Archive: records kept for audit and tax
- Off: licences and hosting ended
