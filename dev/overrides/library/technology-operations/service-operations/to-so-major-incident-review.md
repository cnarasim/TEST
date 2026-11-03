---
id: to-so-major-incident-review
domain: Technology Operations
l1: Service Operations
l2: Major incident review
summary: After a major incident: the timeline, a blameless review of causes, actions with owners and dates, the controls and the KPIs.
systems: Ticketing tool, Monitoring platform, Status page, Collaboration tool
tags: major incident, post-incident review, postmortem, blameless review, root cause, lessons learned, actions
workbook: actions
order: 102
---
# Major incident review

Learn from every major incident without blame, so it cannot happen the same way again.

## What the major incident review covers
### Purpose
- Learn from every major incident, without blame
- Stop the same failure from happening again
### In scope
- Priority 1 incidents and serious near misses
- Timeline, impact, causes, response, actions
### Outcome
- Actions with an owner and a due date
- Lessons shared with every technology team

## From first alert to full recovery
| Time | What happened | Who acted |
|---|---|---|
| [time] | Checkout error alert fires | Monitoring |
| [time] | Major incident declared | Incident manager |
| [time] | Recent change found as the cause | Resolver team |
| [time] | Change rolled back, errors fall | Release team |
| [time] | Service stable, incident resolved | Service owner |
> Notes: illustrative timeline; take the times from the ticket, the alerts and the bridge log, in one time zone.

## The review looks for causes, not culprits
Layout: swimlane handoffs
- Incident manager: Books the review meeting
- Incident manager: Drafts the timeline and impact
- Resolver team: Adds causes and evidence
- Problem manager: Root cause confirmed?
- Problem manager: If yes, agrees actions and owners
- Problem manager: If no, opens a problem record
- Service owner: Approves and shares the review

## Systems and data for the review
| Step | What the system does | Records it keeps |
|---|---|---|
| Timeline | Ticket and alert times in order | Ticket history, alert log |
| Impact | Orders and users affected | Error and order logs |
| Communication | Status page updates kept | Status history |
| Causes | Changes linked to the incident | Change records |
| Actions | Actions tracked to closure | Action log |

## Five steps from incident to lessons
Layout: process chevrons
- Gather: timeline and data
- Analyse: causes, five whys
- Review: blameless meeting
- Act: owners and dates
- Share: lessons for all teams

## Actions that stop it happening again
| Action | Type | Owner | Due |
|---|---|---|---|
| Alert on checkout error rate | Detect | Monitoring lead | [date] |
| Automatic rollback on deploy | Prevent | Release manager | [date] |
| Update runbook and contacts | Respond | Service owner | [date] |
| Load test the payment service | Prevent | Performance lead | [date] |
> Notes: illustrative actions; each one names the gap it closes and stays open until the fix is proven.

## Controls and exceptions
| Control | How it works | Owner |
|---|---|---|
| Review deadline | Every P1 reviewed in [n] days | Incident manager |
| Blameless format | Facts and systems, never names | Problem manager |
| Action tracking | Each action has owner and date | Problem manager |
| Near misses | Serious near misses reviewed too | Service owner |
| Sign-off | Service owner approves the review | Head of operations |

## KPIs that show it works
| KPI | What it measures | Data source |
|---|---|---|
| Reviews on time | P1 reviews held in [n] days | Review records |
| Actions closed on time | Actions done by the due date | Action log |
| Repeat major incidents | P1s with a cause seen before | Incident-problem links |
| Time to detect | Failure to first alert | Alert and ticket times |
| Time to restore | First alert to recovery | Ticket time stamps |

## Today and target
### Today
- Reviews only after the worst outages
- Actions agreed, then lost in e-mail
### Target
- Every P1 reviewed within [n] working days
- Actions tracked in one place to closure
