---
id: ea-as-new-application
domain: Enterprise Architecture
l1: Assess
l2: New application assessment
summary: A new application request from intake to recommendation: the need, reuse first, fit, risk, cost and the board decision.
systems: Demand intake, Application portfolio
tags: new application, intake, demand, triage, assessment, request
order: 101
---
# New application assessment

## What the request is
### Business need
- The problem the business wants solved
- Who asks for it and who sponsors it
### Scope and users
- Processes, locations and user groups
- Data the application will hold
### Expected value
- Benefits in money, time or risk
- How we will measure them

## How a request moves to a decision
Layout: swimlane handoffs
- Requester: Submits the sponsored need
- Enterprise architect: Looks for an existing capability
- Enterprise architect: Existing application covers it?
- Enterprise architect: If yes, reuse and extend it
- Enterprise architect: If no, assess new options
- Security: Reviews data and access risk
- Architecture board: Approves, conditions or declines

## What we assess
| Dimension | The question we answer | Evidence |
|---|---|---|
| Business fit | Does it solve the stated need? | Use cases, process walk-through |
| Functional fit | How much works as standard? | Fit-gap, demos |
| Technical fit | Does it match our architecture standards? | Architecture review |
| Integration and data | What must it connect to and own? | Interface and data inventory |
| Security and privacy | What data, which risks, which controls? | Security assessment |
| Operations and support | Who runs it and how well? | Support model, service levels |
| Cost | What does it cost over three years? | Total cost of ownership |
| Supplier | Will the supplier be here and keep investing? | Due diligence |

## Five steps from request to decision
Layout: process chevrons
- Intake: need, sponsor, urgency
- Triage: reuse, buy or build
- Assess: fit, risk and cost
- Review: architecture board
- Decide: approve with conditions

## Where a request lands
Layout: matrix
- Fast track: high value, low risk - light assessment
- Full assessment: high value, high risk - every dimension
- Reuse or defer: low value, low risk - an existing tool first
- Decline: low value, high risk - not worth the exposure

## The decision we ask for
- Decision: Approve the assessment approach and the dimensions above
- Ask: Name a business sponsor and an owner for every request
- Next step: Triage the open requests within two weeks
