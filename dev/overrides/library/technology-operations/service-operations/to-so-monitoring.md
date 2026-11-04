---
id: to-so-monitoring
domain: Technology Operations
l1: Service Operations
l2: Monitoring and alerting
summary: How services and guest journeys are watched: what we monitor, alert routing to on-call, noise control, the controls and the KPIs.
systems: Monitoring platform, Log platform, On-call scheduling, Ticketing tool, Status page
tags: monitoring, alerting, observability, on-call, thresholds, synthetic monitoring, alert noise
order: 104
---
# Monitoring and alerting

Find failures before guests, stores and DCs do, and page the right person once, with what they need to act.

## What monitoring and alerting covers
### Purpose
- Find failures before guests and stores do
- Alert the right person once, with context
### In scope
- Infrastructure, applications, integrations
- Guest journeys: search, checkout, pickup
### Outcome
- Every critical service watched and owned
- Fewer, better alerts that lead to action

## Five layers watched, guest journey first
| Layer | What we watch | Example alert |
|---|---|---|
| Guest journeys | Synthetic search and checkout | Checkout test fails twice |
| Applications | Errors, response time, queues | Error rate over [target] |
| Integrations | Order and stock messages | Orders stuck [n] minutes |
| Infrastructure | Servers, storage, network, cloud | Disk over [n]% full |
| Stores and DCs | POS, scanners, store network | Store offline [n] minutes |

## Alerts page on-call, not everyone
Layout: swimlane handoffs
- Monitoring: Detects a threshold breach
- Monitoring: Pages on-call with context
- On-call engineer: Confirms the alert
- On-call engineer: Real impact on service?
- On-call engineer: If yes, opens an incident
- On-call engineer: If no, tunes the alert
- Service desk: Informs users and stores

## Systems and data for monitoring
| Step | What the system does | Records it keeps |
|---|---|---|
| Collect | Metrics, logs and traces gathered | Telemetry history |
| Detect | Rules and anomalies checked | Alert rules, alert log |
| Route | On-call rota picks who is paged | Rota, escalation policy |
| Record | Real alerts open incidents | Incident ticket |
| Inform | Status page shows service state | Status history |

## Alerts get better every week
Layout: process cycle
- Define: what healthy looks like
- Alert: on symptoms guests feel
- Respond: a runbook in every alert
- Review: noisy and missed alerts
- Tune: thresholds and owners

## Controls and exceptions
| Control | How it works | Owner |
|---|---|---|
| Service onboarding | No go-live without monitoring | Service owner |
| Runbook link | Every alert links its runbook | On-call lead |
| Weekly alert review | Noisy alerts tuned or removed | Monitoring lead |
| Maintenance windows | Planned work silences its alerts | Change manager |
| Escalation | Missed pages go to the next level | Incident manager |

## KPIs that show it works
| KPI | What it measures | Data source |
|---|---|---|
| Found by monitoring | Incidents alerted before a call | Incident source |
| Mean time to detect | Failure to first alert | Alert and ticket times |
| Actionable alerts | Alerts that led to an action | Alert outcomes |
| Pages per shift | Pages per on-call engineer | On-call scheduling |
| Monitoring coverage | Critical services with alerts | Service catalogue |

## Today and target
### Today
- Thousands of alerts, few acted on
- Guests report checkout errors first
### Target
- Alerts on what guests feel, with runbooks
- Every page actionable, every service owned
