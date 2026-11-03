---
id: pp-dl-test-strategy
domain: Programs and Projects
l1: Deliver
l2: Test strategy and exit criteria
summary: How the solution is tested: the phases, who tests what, defect severity, progress and the criteria to exit each phase.
systems: Test management, Defect tracker
tags: testing, test strategy, user acceptance, defects, exit criteria, quality
workbook: tests
order: 401
---
# Test strategy and exit criteria

## Test phases
Layout: process phases
- Unit: each change on its own (Build)
- System: end-to-end in one solution (Aug)
- Integration: across systems and partners (Sep)
- Acceptance: business users, real scenarios (Oct)
- Dress rehearsal: the cutover itself (Oct)

## Who tests what
| Phase | Purpose | Who | Environment | Exit when |
|---|---|---|---|---|
| Unit | Each change works | Developers | Development | All unit tests pass |
| System | The solution works end to end | Test team | Test | No open critical defects |
| Integration | Systems talk to each other | Test team, partners | Integration test | Every interface passed |
| Acceptance | It works for the business | Business users | Pre-production | Business owners sign off |

## How severe is a defect
| Severity | What it means | Fix within |
|---|---|---|
| Critical | Stops a business process, no workaround | 1 day |
| High | Stops a process, workaround exists | 3 days |
| Medium | Wrong but not blocking | Before go-live |
| Low | Cosmetic | Next release |

## Progress
Layout: kpi cards
- Scenarios run: 412 of 520 (79%)
- Passed first time: 86% (target 85%)
- Open critical and high defects: 7 (target 0)
> Notes: illustrative figures from the test tracker.

## From defect to fix
Layout: swimlane handoffs
- Tester: Logs the defect with evidence
- Test lead: Sets severity and owner
- Developer: Fixes and deploys to test
- Tester: Retests the scenario
- Tester: Passes the retest?
- Tester: If yes, closes the defect
- Test lead: If no, reopens it for the developer

## Exit criteria for acceptance
| Criterion | Target | Actual | Status |
|---|---|---|---|
| Scenarios run | 100% | 79% | Not met |
| Scenarios passed | 95% | 86% | Not met |
| Open critical defects | 0 | 1 | Not met |
| Open high defects | Under 5, each with a workaround | 6 | Not met |
| Business sign-off | All owners | 3 of 5 | Not met |
