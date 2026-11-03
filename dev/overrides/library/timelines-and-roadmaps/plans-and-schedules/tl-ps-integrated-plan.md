---
id: tl-ps-integrated-plan
domain: Timelines and Roadmaps
l1: Plans and Schedules
l2: Integrated program plan
summary: One plan for every workstream of a program: lanes by team, the milestones that tie them together, status and the critical path.
systems: Project plan, Portfolio tool
tags: integrated plan, program plan, workstreams, milestones, critical path, dependencies, status
order: 208
---
# Integrated program plan

## Workstreams in one plan
Layout: timeline lanes
- Process design: Jan 2027 to Apr 2027 (Business)
- Build and configure: Mar 2027 to Aug 2027 (Technology)
- Data migration: Apr 2027 to Oct 2027 (Data)
- Testing: Jul 2027 to Oct 2027 (Quality)
- Training and change: Aug 2027 to Nov 2027 (Change)
- Go-live: Nov 8, 2027 (Program)
> Notes: example dates; one line per workstream with its owning team in brackets.

## Milestones that tie the lanes together
Layout: timeline template-milestones
- Design signed off: Apr 30, 2027 (Business)
- Build complete: Aug 31, 2027 (Technology)
- Final data load rehearsed: Oct 15, 2027 (Data)
- Go / no-go decision: Nov 1, 2027 (Steering committee)
> Notes: example dates; each milestone has one owner and a date that the dependent lanes plan around.

## Status by workstream
Layout: timeline status-roadmap
- Process design: Jan 2027 to Apr 2027 (Business) done
- Build and configure: Mar 2027 to Aug 2027 (Technology) on track
- Data migration: Apr 2027 to Oct 2027 (Data) at risk
- Testing: Jul 2027 to Oct 2027 (Quality) on track

## The critical path decides the date
Layout: process chevrons
- Design: signed off before build starts
- Build: complete before system test
- Data: clean loads before user testing
- Test: exit criteria met
- Go-live: after the go / no-go decision

## Dependencies between workstreams
| Dependency | Needed by | Owner |
|---|---|---|
| Signed process design | Build and configure | Business lead |
| Test environments ready | Testing | Technology lead |
| Clean data loads | User acceptance testing | Data lead |
| Trained super users | Go-live | Change lead |

## How the plan is kept current
| Rule | How it works | Owner |
|---|---|---|
| Weekly update | Each lead updates dates and status | Workstream leads |
| Baseline kept | Changes shown against the baseline | Program office |
| Change control | Milestone moves need approval | Steering committee |
| One version | Only the program office publishes | Program office |
