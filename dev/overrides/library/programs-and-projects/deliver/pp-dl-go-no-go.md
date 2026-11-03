---
id: pp-dl-go-no-go
domain: Programs and Projects
l1: Deliver
l2: Go / no-go decision
summary: Is the business ready to go live: readiness by area, open items and workarounds, the risk of going or waiting, and the decision.
systems: Readiness checklist, Defect tracker, Cutover runbook
tags: go-live, go no-go, readiness, launch decision, cutover, deployment
order: 403
---
# Go / no-go decision

## Readiness by area
| Area | Criterion | Status | Owner |
|---|---|---|---|
| Solution | All critical defects closed | Ready | Technology lead |
| Data | Final trial load reconciled | Ready | Data lead |
| People | 95% of users trained | Ready with conditions | Change lead |
| Support | Service desk briefed, hypercare staffed | Ready | Support lead |
| Business | Owners signed off acceptance | Ready | Business owners |
| Cutover | Dress rehearsal on time | Ready | Cutover lead |

## Readiness in numbers
Layout: rings
- Users trained: 93%
- Scenarios passed: 97%
- Runbook rehearsed: 100%

## Open items and workarounds
| Item | Impact | Workaround | Fix by |
|---|---|---|---|
| Two reports not ready | Weekly sales report late | Manual extract for two weeks | Week 2 |
| Seven users not trained | Slower first days | Floor walkers, quick guides | Week 1 |

## Going against waiting
### Go now
- Benefits start on plan
- Open items have workarounds
- Peak season freeze avoided
### Wait four weeks
- Every item closed
- Go-live falls in the freeze - moves to January
- $0.3M more cost

## How we decide
Layout: swimlane handoffs
- Workstream lead: Confirms each criterion with evidence
- Project manager: Consolidates readiness and open items
- Steering committee: Every criterion met or managed?
- Steering committee: If yes, go
- Steering committee: If no, sets conditions or new date
- Project manager: Tells teams, starts the cutover

## The decision
- Decision: Go live on November 9 with the two workarounds
- Ask: Floor walkers in every region for week one
- Next step: Cutover starts Friday at 18:00
