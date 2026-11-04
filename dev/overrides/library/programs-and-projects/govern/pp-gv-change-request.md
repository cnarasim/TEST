---
id: pp-gv-change-request
domain: Programs and Projects
l1: Govern
l2: Change request
summary: A change to scope, time or cost: what changes and why, the impact, the options, how change control works and the decision.
systems: Change log, Project plan
tags: change request, change control, scope change, variation, impact assessment
order: 304
---
# Change request

## What changes and why
Layout: process list
- The request: what we are asked to add, remove or change (who asks for it)
- Why: the business reason (what happens if we do not)
- Urgency: when the decision is needed (what waiting costs)

## Impact on scope, time, cost and risk
| Dimension | Baseline | With the change | Difference |
|---|---|---|---|
| Scope | 42 requirements | 45 requirements | +3 |
| Go-live | Nov 9, 2027 | Nov 9, 2027 | None |
| Cost | $4.8M | $4.95M | +$150K |
| Risk | Medium | Medium | Testing window shorter |

## Options
Layout: process list
| Option | What it means | Cost | Time | Risk |
|---|---|---|---|---|
| Approve now | Build in this release | +$150K | None | Shorter testing |
| Next release | Build after go-live | +$120K | +3 months for the benefit | Low |
| Reject | Keep today's workaround | $0 | None | Manual effort stays |

## How change control works
Layout: swimlane handoffs
- Requester: Submits the change and reason
- Project manager: Logs it, asks for estimates
- Workstream lead: Estimates scope, time and cost
- Project manager: Within the board's tolerance?
- Project manager: If yes, the project board decides
- Steering committee: If no, decides the change
- Project manager: Updates plan and budget

## Recommendation
### Next release
- Benefit kept, testing protected
- Lower cost when built after go-live
### Approve now
- Benefit three months sooner
- Testing window five days shorter

## The decision
- Decision: Build the change in the next release
- Ask: Approve $120K in next year's budget
- Next step: Add to the release backlog
