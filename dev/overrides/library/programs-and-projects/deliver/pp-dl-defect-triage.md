---
id: pp-dl-defect-triage
domain: Programs and Projects
l1: Deliver
l2: Defect triage
summary: How defects found in testing are sorted and fixed: severity and priority, triage decisions, the daily triage, fix targets, roles and the trends to watch.
systems: Test management tool, Defect tracker
tags: defect triage, defects, bugs, severity, priority, testing, defect management
order: 408
---
# Defect triage

## What defect triage covers
### Purpose
- Fix the defects that matter first
- One decision per defect, made fast
### In scope
- Every defect raised in testing
- Severity, priority, owner and target date
### Outcome
- No defect without an owner and a date
- A clear view of go-live risk

## Severity and priority are different
| Level | Severity: business impact | Priority: fix order |
|---|---|---|
| 1 | Process stops, no workaround | Fix now, it blocks testing |
| 2 | Process stops, a workaround exists | Fix in this test cycle |
| 3 | Wrong result, not blocking | Fix before go-live |
| 4 | Cosmetic | Next release |
> Notes: severity is set by the impact, priority by the business; a severity 3 can be priority 1 before a key date.

## Every defect gets a decision
Layout: process diverge
- New defect: logged with steps and evidence
- Fix: an owner and a target date
- Reject: a duplicate, or works as designed
- Change request: a new need, to change control
- Defer: a later release, with the risk accepted

## The daily triage
Layout: swimlane handoffs
- Tester: Logs the defect with evidence
- Triage lead: Checks completeness and duplicates
- Triage board: A real defect?
- Triage board: If yes, sets severity, priority, owner
- Triage lead: If no, rejects or reroutes it
- Developer: Fixes it for retest

## Defects at a glance
Layout: kpi cards
- Open defects: 64 down from 92
- Critical and high open: 7 against a target of 0
- Average age: 4.2 days against a target of 3
> Notes: illustrative figures from the test management tool.

## Fix targets by severity
| Severity | Respond within | Fix within | Escalate to |
|---|---|---|---|
| Critical | 2 hours | 1 day | Test manager and sponsor |
| High | 1 day | 3 days | Test manager |
| Medium | 2 days | This test cycle | Triage lead |
| Low | 5 days | Before go-live or later | None |

## Who is in triage
| Role | Brings | Decides |
|---|---|---|
| Triage lead | The defect list, age and trends | Agenda and follow-up |
| Test lead | Evidence and retest status | Severity |
| Development lead | Effort and fix options | Owner and target date |
| Business lead | Impact on the process | Priority |

## Watch the trend, not just the count
| Measure | What it tells us | Target |
|---|---|---|
| Open by severity | Go-live risk today | No critical open at exit |
| New against fixed | Whether we are getting ahead | Fixes outpace new defects |
| Reopen rate | Quality of the fixes | Under [n]% |
| Age of open defects | Speed of the team | Under [n] days |
