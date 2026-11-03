---
id: ea-ds-observability
domain: Enterprise Architecture
l1: Design and Standards
l2: Observability standards
summary: What every service must report (logs, metrics, traces), the service levels and alerts on top, and how alerts reach the right engineer.
systems: Monitoring platform, Logging platform, Ticketing tool, On-call tool
tags: observability, monitoring, logs, metrics, traces, SLO, alerting
order: 610
---
# Observability standards

## What observability covers
### Purpose
- Problems seen before guests feel them
- A fast path from alert to the cause
### In scope
- Logs, metrics, traces and business signals
- Service levels, alerts and runbooks
### Outcome
- Shorter incidents and fewer repeats
- Fewer alerts that nobody acts on

## Observability runs as a loop
Layout: process cycle
- Instrument: every service sends logs, metrics, traces
- Collect: one platform, one view
- Alert: on service levels, not on noise
- Respond: on-call engineer with a runbook
- Learn: tune alerts after every incident

## Three signals every service sends
| Signal | What it shows | Standard |
|---|---|---|
| Logs | What happened, in order | Structured, no personal data |
| Metrics | How much and how fast | Latency, errors, volume, saturation |
| Traces | Where a request spent its time | One trace ID across services |

## Standards for every service
| Standard | Rule | Owner |
|---|---|---|
| Service levels | Every tier 1 service has an objective | Service owner |
| Alerts that act | Each alert links to a runbook | Service owner |
| One transaction ID | Carried end to end | Engineering lead |
| Retention | Logs kept [n] days | Operations |
| Business signals | Orders per minute on the dashboard | Product owner |

## From alert to fix
Layout: swimlane handoffs
- Monitoring: Detects an objective breach
- On-call engineer: Acknowledges the alert
- On-call engineer: Guests affected?
- On-call engineer: If yes, opens a major incident
- On-call engineer: If no, fixes from the runbook
- Service owner: Tunes the alert afterwards

## KPIs that show it works
| KPI | What it measures | Data source |
|---|---|---|
| Services with objectives | Tier 1 services with a target | Monitoring platform |
| Time to detect | Start of impact to first alert | Incident records |
| Alerts with runbooks | Alerts that link to a fix | Alert catalog |
| Alert noise | Alerts per real incident | Monitoring platform |
