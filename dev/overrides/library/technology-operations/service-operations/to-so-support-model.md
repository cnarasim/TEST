---
id: to-so-support-model
domain: Technology Operations
l1: Service Operations
l2: Support model: L1 to L3
summary: Who supports what: the tiers from service desk to engineering and suppliers, the handoffs, hours of cover, controls and KPIs.
systems: Ticketing tool, Knowledge base, Self-service portal, On-call scheduling, Remote support tool
tags: support model, L1 L2 L3, service desk, escalation, support tiers, shift left, knowledge
order: 105
---
# Support model: L1 to L3

One clear path for every store, DC and corporate user, with each fix made at the first tier that can make it.

## What the support model covers
### Purpose
- One clear path for every request and fault
- Fix issues at the first tier that can
### In scope
- Service desk, application, engineering tiers
- Stores, DCs, corporate teams, hours of cover
### Outcome
- Faster fixes with fewer handoffs
- Engineers free for change, not repeat calls

## Each tier has its own job and hours
| Tier | Who | What they handle | Cover |
|---|---|---|---|
| L1 | Service desk | How-to, access, known fixes | [hours] |
| L2 | Application support | Diagnosis, configuration, data fixes | [hours] |
| L3 | Engineering and product teams | Code and design faults | On-call |
| Suppliers | Software and hardware partners | Product defects under contract | Per contract |
> Notes: set the hours of cover for stores, DCs and corporate users separately; peak season may need longer cover.

## Tickets move up only with the evidence
Layout: swimlane handoffs
- User: Contacts the service desk
- Service desk: Logs and tries known fixes
- Service desk: Solved at first contact?
- Service desk: If yes, closes with the user
- Application support: If no, diagnoses the fault
- Engineering: Fixes code or design faults
- Service desk: Confirms the fix, closes

## Systems and data for the support model
| Step | What the system does | Records it keeps |
|---|---|---|
| Contact | Portal, chat and phone logged | Ticket, contact channel |
| Self-help | Articles answer common questions | Article views |
| Assign | Rules route to the right team | Assignment history |
| Escalate | Notes and evidence go with it | Work notes |
| Close | Resolution and category kept | Resolution code |

## Five steps to shift fixes left
Layout: process numbered
- Find: top repeat tickets at L2 and L3
- Write: an article or a script
- Train: the service desk on it
- Automate: self-service where safe
- Measure: tickets solved at L1

## Controls and exceptions
| Control | How it works | Owner |
|---|---|---|
| Escalation criteria | Evidence before moving up | Service desk lead |
| One owner | One owner per ticket, end to end | Service desk |
| Bounce limit | [n] reassignments go to a lead | Support manager |
| Out of hours | P1 and P2 page on-call | On-call lead |
| Supplier contacts | Terms and contacts on file | Supplier manager |

## KPIs that show it works
| KPI | What it measures | Data source |
|---|---|---|
| First contact resolution | Solved at L1, first contact | Ticket history |
| Escalation rate | Tickets moved to L2 or L3 | Assignment history |
| Reassignments | Team changes per ticket | Assignment log |
| Time to resolve by tier | Average time at each tier | Ticket time stamps |
| User satisfaction | Rating after closure | Closure survey |

## Today and target
### Today
- Tickets bounce between teams, no owner
- Engineers answer how-to questions
### Target
- Clear entry criteria for every tier
- Most tickets solved at first contact
