---
id: ea-cs-proof-of-concept
domain: Enterprise Architecture
l1: Compare and Select
l2: Proof of concept evaluation
summary: What the proof of concept must prove, the success criteria and results, the phases and the go / no-go recommendation.
systems: Test environment
tags: proof of concept, POC, pilot, success criteria, go no-go, validation
order: 203
---
# Proof of concept evaluation

## What the proof of concept must prove
Layout: process list
- Objective: the riskiest assumptions, proven or disproven (in weeks, not months)
- Scope: three to five critical scenarios (real data, real users)
- Exit criteria: every success criterion met or explained (a clear go or no-go)

## Success criteria and results
| Success criterion | Target | Result | Met |
|---|---|---|---|
| Order entry time | Under [x] minutes | [result] | [yes / no] |
| Integration with the order system | Orders flow both ways | [result] | [yes / no] |
| Peak volume | [x] orders an hour | [result] | [yes / no] |
| User acceptance | [x] of 10 average rating | [result] | [yes / no] |
| Security controls | Single sign-on, roles | [result] | [yes / no] |

## Four phases in six weeks
Layout: process phases
- Prepare: scenarios; data; users (Week 1)
- Build: configure; connect (Weeks 2-3)
- Test: scenarios; volume (Weeks 4-5)
- Decide: results; go or no-go (Week 6)

## What we learned
### Went well
- Standard process fitted most scenarios
- Users adopted it quickly
### Needs work
- Peak volume needed tuning
- One interface needs a new pattern
### Actions
- Volume test again before contract
- Design the interface in the build

## Recommendation
- Decision: Go - proceed to contract and implementation
- Ask: Approve the implementation budget
- Next step: Mobilise the implementation team
