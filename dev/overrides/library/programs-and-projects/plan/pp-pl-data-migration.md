---
id: pp-pl-data-migration
domain: Programs and Projects
l1: Plan
l2: Data migration plan
summary: How data moves from legacy systems to the new solution: scope, cleansing, mapping, trial loads, reconciliation, ownership and sign-off.
systems: Legacy systems, ERP, Data migration tool, Data quality tool
tags: data migration, data conversion, trial load, mock load, reconciliation, cleansing, data quality
order: 207
---
# Data migration plan

## What data migration covers
### Purpose
- Move only the data the business needs
- Clean, complete and reconciled at go-live
### In scope
- Master data, open items and balances
- Rules for the history kept in an archive
### Outcome
- Data the business owners sign off
- Legacy data archived, never lost

## Six steps from legacy to live
Layout: process chevrons
- Scope: objects, volumes, owners
- Cleanse: fix at the source, early
- Map: fields, values and rules
- Load: extract, transform, load
- Reconcile: counts, values, samples
- Sign off: the business owner accepts

## What moves and what stays
| Data | Moves | Stays in the archive |
|---|---|---|
| Items and vendors | Active items and vendors | Inactive for over [n] years |
| Guests and members | Active members and points | Lapsed accounts, per retention rules |
| Open transactions | Open orders, invoices, returns | Settled and closed items |
| Balances | Ledger and stock balances at cutover | Detailed history before cutover |
| Prices and promotions | Current and future prices | Expired promotions |

## Each trial load must pass
| Trial load | Purpose | Pass when |
|---|---|---|
| Trial load 1 | Mapping and load programs work | Every object loads, errors logged |
| Trial load 2 | Full volume and real timings | Errors under [n]%, timings known |
| Trial load 3 | Dress rehearsal of the cutover | Inside the window, fully reconciled |
| Production load | The go-live data | Business owners sign off |

## Trial loads on the timeline
Layout: timeline template-milestones
- Trial load 1: Apr 30, 2027 (Data)
- Trial load 2: Jun 30, 2027 (Data)
- Trial load 3: Aug 31, 2027 (Cutover)
- Production load: Oct 2, 2027 (Cutover)
> Notes: example dates; leave time after each trial load to fix and re-cleanse.

## How we reconcile
| Check | How | Owner |
|---|---|---|
| Record counts | Source against target, per object | Data lead |
| Financial balances | Ledger and stock values agree to the cent | Finance lead |
| Samples | Key users check records field by field | Business owners |
| Business test | Run a process on migrated data | Process owners |

## Who owns the data
| Activity | Data owner | Data lead | Migration team | Key users |
|---|---|---|---|---|
| Agree scope and rules | A | R | C | C |
| Cleanse at the source | A | C | I | R |
| Build and run the loads | I | A | R | I |
| Reconcile and sample | A | R | C | R |
| Sign off the data | A | C | I | C |
> Notes: R does the work, A owns the outcome, C is asked before, I is told after.

## Risks we manage early
| Risk | Mitigation | Owner |
|---|---|---|
| Poor source data | Cleansing starts in design, weekly scores | Data owners |
| Mapping keeps changing | Mapping frozen after trial load 2 | Data lead |
| Loads too slow for the window | Timed in every trial load | Migration team |
| History lost | Archive the business can search | Technology lead |
