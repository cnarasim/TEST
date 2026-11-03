---
id: to-so-incident
domain: Technology Operations
l1: Service Operations
l2: Incident management
summary: Restoring service fast: how incidents are detected, logged, prioritised, escalated and resolved, with controls, KPIs and the target.
systems: Ticketing tool, Monitoring platform, CMDB, On-call scheduling, Status page
tags: incident management, incidents, priority, escalation, on-call, outage, ITSM
order: 101
---
# Incident management

Get service back for guests, stores and DCs fast, and keep everyone informed until it is.

## What incident management covers
### Purpose
- Restore normal service as fast as possible
- Limit the impact on guests, stores and DCs
### In scope
- Every unplanned outage or drop in quality
- Detection, priority, escalation and resolution
### Outcome
- Service restored within the agreed targets
- Users kept informed until the ticket closes

## The service desk logs, resolvers restore
Layout: swimlane handoffs
- User: Reports the issue
- Service desk: Logs and sets the priority
- Service desk: Known fix available?
- Service desk: If yes, applies the fix
- Resolver team: If no, diagnoses and restores
- Resolver team: Records the cause and fix
- Service desk: Confirms with the user, closes

## Priority sets the response clock
| Priority | Example | Respond | Restore |
|---|---|---|---|
| P1 Critical | Stores cannot sell or ulta.com is down | [n] minutes | [n] hours |
| P2 High | A key service is slow, no workaround | [n] minutes | [n] hours |
| P3 Medium | One store or team affected, workaround | [n] hours | [n] days |
| P4 Low | A question or a minor fault | [n] days | Next release |
> Notes: priority comes from impact and urgency, never from who calls; replace every [n] with the agreed service levels.

## Systems and data for incident management
| Step | What the system does | Records it keeps |
|---|---|---|
| Detect | Alerts open tickets automatically | Alert, event history |
| Log | Impact and urgency set priority | Incident ticket |
| Diagnose | CMDB shows the service and links | Configuration items |
| Inform | Status page shares what is known | Status updates |
| Resolve | Fix and cause code on the ticket | Resolution, restore time |

## Five steps from alert to closure
Layout: process chevrons
- Detect: alert or user report
- Log: ticket and priority
- Diagnose: impact and cause
- Restore: fix or workaround
- Close: user confirms

## Controls and exceptions
| Control | How it works | Owner |
|---|---|---|
| Priority matrix | Impact and urgency set priority | Service desk lead |
| Timed escalation | Slow pickup pages the next level | Incident manager |
| Major incident | P1 opens a bridge and status page | Incident manager |
| Closure check | User confirms before closure | Service desk |
| Post-incident review | Every P1 reviewed in [n] days | Problem manager |

## KPIs that show it works
| KPI | What it measures | Data source |
|---|---|---|
| Mean time to restore | Detection to service restored | Ticket time stamps |
| Response in target | Tickets picked up inside target | Service level clock |
| First contact resolution | Solved by the service desk alone | Assignment history |
| Found by monitoring | Alerted before a user calls | Ticket source |
| Reopened tickets | Reopened after closure | Ticket status history |

## Today and target
### Today
- Users find outages before monitoring does
- Escalation depends on who answers the phone
### Target
- Alerts open tickets before guests notice
- Timed escalation and one status page for all
