---
id: pp-gv-dependencies
domain: Programs and Projects
l1: Govern
l2: Dependency management
summary: How the project tracks what it needs from others: kinds of dependency, the register, key dates, the critical ones, how they are agreed and escalated.
systems: RAID log, Project plan
tags: dependencies, dependency register, interdependencies, critical path, escalation, RAID, cross-project
order: 306
---
# Dependency management

## What dependency management covers
### Purpose
- See early what we need from others
- Protect the dates other teams rely on
### In scope
- Between workstreams, projects and partners
- Deliverables, decisions, people, environments
### Outcome
- Every dependency agreed by both sides
- Late ones escalated before they bite

## Five kinds of dependency
| Kind | Example | Usually from |
|---|---|---|
| Deliverable | An interface built by another team | Other projects |
| Decision | Returns policy signed off | Business leaders |
| People | Key users released for testing | Line managers |
| Environment | Test system refreshed with data | Technology operations |
| Event | No change in the holiday freeze | The business calendar |

## The dependency register
| ID | We need | From | By | If it is late |
|---|---|---|---|---|
| D-01 | Single sign-on for new users | Identity team | Aug 1 | No access on day one |
| D-02 | Network upgrade in pilot stores | Store technology | Sep 15 | Pilot moves a month |
| D-03 | Daily price feed | Pricing team | Jul 15 | Prices keyed by hand |
| D-04 | Key users for acceptance testing | Store operations | Aug 30 | Testing slips |
> Notes: illustrative register - keep the full list in the RAID log.

## Key dates we depend on
Layout: timeline template-milestones
- Price feed: Jul 15, 2027 (Pricing team)
- Single sign-on: Aug 1, 2027 (Identity team)
- Store network: Sep 15, 2027 (Store technology)
- Holiday freeze: Nov 1, 2027 (Business calendar)
> Notes: example dates; a single date is the latest date we can accept.

## Three dependencies hold the go-live
Layout: process converge
- Network: stores can run the new devices
- Identity: every user can sign in
- Price feed: items and prices flow daily
- Result: Pilot stores ready - the go-live date holds

## How a dependency is agreed
Layout: swimlane handoffs
- Workstream lead: Names the need and date
- Project manager: Logs it, finds the provider
- Provider: Agrees a date and owner
- Project manager: On plan at weekly check?
- Project manager: If yes, keeps tracking it
- Steering committee: If no, decides on options

## Dependencies at a glance
Layout: kpi cards
- Dependencies tracked: 38 in the register
- Not yet agreed: 5 against a target of 0
- Slipping: 3 of them on the critical path
> Notes: illustrative figures from the RAID log.

## The weekly rhythm
Layout: process cycle
- Identify: new needs from every team
- Agree: provider, date, owner
- Track: weekly, with both sides
- Escalate: before the date is missed
