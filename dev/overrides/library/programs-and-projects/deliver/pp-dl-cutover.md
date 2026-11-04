---
id: pp-dl-cutover
domain: Programs and Projects
l1: Deliver
l2: Cutover plan
summary: How the business moves to the new solution: phases, the runbook, go/no-go checkpoints, the command centre, rollback and communications.
systems: Cutover runbook, Project plan, Service desk
tags: cutover, go-live, runbook, data migration, rollback, command centre, deployment
workbook: cutover
order: 402
---
# Cutover plan

## Cutover in five phases
Layout: process phases
- Prepare: rehearsals; sign-offs (T-4 weeks)
- Freeze: changes and transactions (T-2 days)
- Migrate: load and reconcile data (T-1 day)
- Validate: business checks (T-0 morning)
- Go live: open for business (T-0)

## The runbook
| Step | Task | Owner | Start | Hours | Checkpoint |
|---|---|---|---|---|---|
| 1 | Freeze changes in the old system | Technology lead | Fri 18:00 | 1 | |
| 2 | Extract open orders and balances | Data lead | Fri 19:00 | 3 | |
| 3 | Load master data | Data lead | Fri 22:00 | 4 | |
| 4 | Reconcile master data | Business lead | Sat 02:00 | 2 | Go / no-go 1 |
| 5 | Load open transactions | Data lead | Sat 04:00 | 5 | |
| 6 | Reconcile balances | Finance lead | Sat 09:00 | 3 | Go / no-go 2 |
| 7 | Business validation | Business owners | Sat 12:00 | 4 | Go / no-go 3 |
| 8 | Open to users | Project manager | Sun 06:00 | 1 | |
> Notes: illustrative extract - the full runbook lives in the workbook, minute by minute.

## Go / no-go checkpoints
| Checkpoint | When | We go on if | Decides |
|---|---|---|---|
| Go / no-go 1 | Sat 04:00 | Master data reconciled, no critical gaps | Cutover lead |
| Go / no-go 2 | Sat 12:00 | Balances agree to the cent | Finance lead |
| Go / no-go 3 | Sat 16:00 | Business checks passed | Sponsor |

## Who is in the command centre
- Cutover lead: runs the runbook and the clock
- Technology: systems, interfaces, access
- Data: loads and reconciliations
- Business: validation and sign-off
- Service desk: user support from day one
- Communications: updates to the business

## If we must roll back
### Trigger
- A checkpoint fails and cannot be fixed in time
- Balances do not reconcile
### Steps
- Stop loads, restore the old system
- Reopen the old system to users
### Decision
- Sponsor decides at the checkpoint
- Last point to roll back: Sat 20:00

## Who hears what and when
| Audience | Message | When | Channel |
|---|---|---|---|
| All users | Freeze starts, what to do | Two days before | Email, huddles |
| Store managers | What changes on Monday | One day before | Leader call |
| Leadership | Status at every checkpoint | During cutover | Message channel |
| All users | We are live, where to get help | Go-live morning | Email, intranet |
