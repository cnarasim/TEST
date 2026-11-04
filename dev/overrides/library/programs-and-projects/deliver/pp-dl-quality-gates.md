---
id: pp-dl-quality-gates
domain: Programs and Projects
l1: Deliver
l2: Quality gates
summary: The delivery gates from design to hypercare exit: what each gate checks, the evidence, who decides, the outcomes and the quality measures behind them.
systems: Test management tool, Project plan, Collaboration site
tags: quality gates, entry criteria, exit criteria, stage gates, quality assurance, sign-off, testing
order: 410
---
# Quality gates

## What quality gates cover
### Purpose
- Move on only when the work is ready
- Find problems while they are cheap to fix
### In scope
- Design, build, test, cutover, hypercare
- Entry and exit criteria with evidence
### Outcome
- A recorded decision at every gate
- Conditions tracked to closure

## Six gates from design to hypercare
Layout: process chevrons
- Design: designs approved
- Build: built and unit tested
- Test entry: environment and data ready
- Test exit: scenarios passed, defects fixed
- Cutover: rehearsed, business ready
- Hypercare exit: stable, handed over

## What each gate checks
| Gate | Exit criteria | Evidence | Decides |
|---|---|---|---|
| Design | Designs approved, gaps closed | Design sign-offs | Design authority |
| Build | Every item built and unit tested | Build tracker | Technology lead |
| Test exit | Scenarios passed, no critical defects | Test report | Business owners |
| Cutover | Rehearsal on time, sites ready | Readiness report | Steering committee |
| Hypercare exit | Stable for [n] weeks | Ticket trends | Service owner |

## A gate has three outcomes
Layout: process diverge
- Gate review: the evidence against the criteria
- Pass: move to the next stage
- Pass with conditions: move on, gaps dated
- Hold: fix first, then a new review

## Gates on the timeline
Layout: timeline template-milestones
- Design gate: Mar 31, 2027 (Design authority)
- Build gate: Jun 30, 2027 (Technology lead)
- Test exit gate: Sep 15, 2027 (Business owners)
- Cutover gate: Oct 29, 2027 (Steering committee)
> Notes: example dates; replace them with the baseline plan.

## How a gate review runs
Layout: swimlane handoffs
- Workstream lead: Sends evidence early
- Quality lead: Checks it against the criteria
- Gate board: Criteria met?
- Gate board: If yes, passes, conditions dated
- Sponsor: If no, decides waiver or hold
- Quality lead: Logs the decision

## Quality we measure at every gate
| Measure | Target | Source |
|---|---|---|
| Musts traced to tests | Every must | Test management tool |
| Test scenarios passed | [target]% | Test report |
| Critical defects open | None at exit | Defect tracker |
| Conditions closed on time | [target]% | Gate log |
