---
id: to-so-problem
domain: Technology Operations
l1: Service Operations
l2: Problem management
summary: Removing the causes of repeat incidents: problem records, root cause analysis, known errors and workarounds, permanent fixes, controls and KPIs.
systems: Ticketing tool, Knowledge base, CMDB, Monitoring platform
tags: problem management, root cause analysis, known error, workaround, repeat incidents, trend analysis
order: 103
---
# Problem management

Incident management restores the service; problem management removes the cause so it does not come back.

## What problem management covers
### Purpose
- Remove the causes of repeat incidents
- Cut incident volume and outage time
### In scope
- After major incidents and repeat faults
- Trends found before they hurt guests
### Outcome
- Known errors with workarounds at the desk
- Permanent fixes delivered through change

## Problem owners find causes, change fixes
Layout: swimlane handoffs
- Service desk: Links repeat incidents
- Problem manager: Logs and ranks the problem
- Resolver team: Finds the root cause
- Problem manager: Permanent fix ready now?
- Resolver team: If yes, raises a change
- Problem manager: If no, publishes the workaround
- Change board: Approves the fix
- Problem manager: Closes when it holds

## Impact and frequency set the order of work
Layout: matrix
- Fix now: high impact, frequent
- Plan the fix: high impact, rare
- Work around: low impact, frequent - automate it
- Accept: low impact, rare - record it

## Systems and data for problem management
| Step | What the system does | Records it keeps |
|---|---|---|
| Trends | Incidents grouped by cause | Incident trend report |
| Log | Problem linked to its incidents | Problem record |
| Analyse | Evidence and five whys attached | Root cause analysis |
| Known error | Workaround published to the desk | Known error article |
| Fix | Change linked to the problem | Change record |

## Five steps from repeat incident to fix
Layout: process chevrons
- Detect: trends and repeats
- Log: problem record
- Analyse: root cause
- Work around: known error
- Fix: change, then close

## Controls and exceptions
| Control | How it works | Owner |
|---|---|---|
| Repeat trigger | [n] repeats open a problem | Problem manager |
| Major incident link | Every P1 gets a problem record | Incident manager |
| Fix through change | Permanent fixes go through change | Change manager |
| Known error review | Workarounds reviewed quarterly | Problem manager |
| Closure check | Close after [n] days, no repeat | Service owner |

## KPIs that show it works
| KPI | What it measures | Data source |
|---|---|---|
| Repeat incidents | Incidents with a known cause | Incident-problem links |
| Root cause found | Problems with a confirmed cause | Problem records |
| Known errors published | Workarounds the desk can use | Knowledge base |
| Incidents avoided | Fewer incidents after the fix | Incident trend by service |
| Problem age | Open problems over [n] days | Problem ageing report |

## Today and target
### Today
- The same incidents fixed again and again
- Root cause found only for big outages
### Target
- Trends reviewed every week, causes removed
- Known errors at the service desk on day one
