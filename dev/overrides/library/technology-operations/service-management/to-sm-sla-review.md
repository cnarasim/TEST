---
id: to-sm-sla-review
domain: Technology Operations
l1: Service Management
l2: Service level review
summary: Are we delivering what we promised: service levels against target, breaches and causes, the review flow, supplier results, controls and KPIs.
systems: Ticketing tool, Monitoring platform, Reporting, Contract register
tags: service level, SLA, SLO, service review, availability, breaches, supplier performance
workbook: actions
order: 303
---
# Service level review

Once a month, an honest look at what we promised, what we delivered and what we will change.

## What the service level review covers
### Purpose
- Check we deliver what we promised
- Agree actions where we do not
### In scope
- Availability, response, resolution, requests
- Supplier commitments and user experience
### Outcome
- An honest scorecard every month
- Actions and target changes agreed

## Service levels against target this month
| Service level | Target | Actual | Status |
|---|---|---|---|
| Checkout availability | [target] | [actual] | [status] |
| Store POS availability | [target] | [actual] | [status] |
| P1 restored in target | [target] | [actual] | [status] |
| Requests on time | [target] | [actual] | [status] |
| User satisfaction | [target] | [actual] | [status] |
> Notes: fill from the monthly scorecard; each service level has a written definition and its agreed exclusions.

## Every breach has a cause and an owner
| Breach | Cause | Action | Owner |
|---|---|---|---|
| Store POS availability | Regional network outage | Second network link | Network lead |
| P1 restore time | Supplier fix arrived late | Supplier escalation, credit | Supplier manager |
| Requests on time | Device stock ran out | Buffer stock of devices | Field services |
> Notes: illustrative breaches; list every breach of the month, its cause and the action that stops it repeating.

## The review agrees actions, not excuses
Layout: swimlane handoffs
- Service manager: Prepares the scorecard
- Service owner: Explains breaches and causes
- Business owner: Missed two months running?
- Service owner: If yes, presents an improvement plan
- Service owner: If no, watches next month
- Business owner: Agrees actions and targets
- Service manager: Tracks actions to closure

## Systems and data for service levels
| Step | What the system does | Records it keeps |
|---|---|---|
| Measure | Raw numbers from the tools | Availability, ticket times |
| Calculate | Rules and agreed exclusions | Service level results |
| Report | A scorecard per service | Monthly scorecard |
| Suppliers | Results against contract | Supplier scorecard |
| Act | Actions logged and tracked | Action log |

## Measure, review and improve every month
Layout: process cycle
- Measure: data from the tools
- Review: with business owners
- Improve: actions and plans
- Adjust: targets where needed

## Controls and exceptions
| Control | How it works | Owner |
|---|---|---|
| Written definitions | Every service level defined | Service manager |
| Data from tools | Numbers from systems, not by hand | Reporting analyst |
| Agreed exclusions | Planned downtime only if agreed | Service owner |
| Supplier credits | Breaches claimed under contract | Supplier manager |
| Target review | Targets reviewed every [n] months | Business owner |

## KPIs that show it works
| KPI | What it measures | Data source |
|---|---|---|
| Service levels met | Share at or above target | Monthly scorecard |
| Repeat breaches | Missed two months running | Scorecard history |
| Actions on time | Actions done by the due date | Action log |
| Credits claimed | Credits claimed vs due | Contract register |
| User satisfaction | Rating after tickets close | Closure survey |

## Today and target
### Today
- Green scorecards while users complain
- Numbers collected by hand each month
### Target
- Service levels that match what users feel
- Automated scorecard, time spent on actions
