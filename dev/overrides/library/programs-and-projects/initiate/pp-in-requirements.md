---
id: pp-in-requirements
domain: Programs and Projects
l1: Initiate
l2: Business requirements and scope
summary: How business needs become a signed-off scope: sources, what a good requirement looks like, ranking, scope boundaries and scope control.
systems: Requirements management tool, Product backlog, Collaboration site
tags: requirements, scope, business requirements, MoSCoW, traceability, scope baseline, backlog
order: 105
---
# Business requirements and scope

## What requirements and scope cover
### Purpose
- Agree what the business needs before design
- One scope that every team plans against
### In scope
- Process, data, reporting and control needs
- What is in and out of the project
### Outcome
- A ranked, signed-off requirements baseline
- A scope statement under change control

## From need to signed-off scope
Layout: process chevrons
- Gather: workshops, interviews, today's process
- Write: one need per line, with a test
- Rank: must, should, could, won't
- Trace: to a process step and an objective
- Baseline: sign-off, then change control

## A good requirement passes six tests
Layout: hexagons
- Clear: one need, in plain words
- Testable: an acceptance criterion
- Traced: to a process step and an objective
- Owned: a named business owner
- Ranked: must, should or could
- Sized: effort agreed with the team

## Requirements come in five kinds
| Kind | Example | Owner |
|---|---|---|
| Business process | Stores refund an online order at the counter | Process owner |
| Data | Every item carries shade, size and brand | Data owner |
| Reporting | Daily sales by store, channel and brand | Business lead |
| Control and compliance | Price changes approved before they go live | Finance controller |
| Non-functional | Checkout answers within [n] seconds at peak | Solution architect |
> Notes: illustrative requirements - replace them with the project's own.

## Must-haves first: how we rank
| Priority | What it means | Test we apply |
|---|---|---|
| Must | No go-live without it | Law, safety or the business case fails |
| Should | Important, a workaround exists | Painful but possible to go live without |
| Could | Nice to have | Only if time and budget allow |
| Won't (this time) | Agreed out of this release | Parked in the backlog with a reason |

## Scope has clear edges
| Area | In scope | Out of scope |
|---|---|---|
| Processes | Store and online returns, refunds | Vendor returns and claims |
| Locations | All stores and DCs | Salon back bar |
| Systems | POS, OMS, ERP finance | Loyalty program changes |
| Data | Open returns and refunds | History older than [n] years |
> Notes: example scope for a returns project - replace with the project's own lines.

## How scope is controlled
Layout: swimlane handoffs
- Requester: Raises a need and reason
- Business analyst: Writes it, checks for duplicates
- Process owner: Ranks it against the baseline
- Project board: Inside the agreed scope?
- Project board: If yes, adds it to the backlog
- Steering committee: If no, decides it as a change

## Signed off when
| Criterion | Evidence | Signs off |
|---|---|---|
| Requirements ranked, owned | Backlog report | Process owners |
| Musts traced to process steps | Traceability matrix | Business analyst lead |
| Scope statement agreed | In and out list, assumptions | Sponsor |
| Open questions closed or dated | Decision log | Project manager |
