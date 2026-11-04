---
id: pp-gv-raid
domain: Programs and Projects
l1: Govern
l2: Risks, issues and escalations
summary: The project RAID review: how risks are scored, the top risks and open issues with owners, dependencies and the escalation path.
systems: RAID log, Project plan
tags: RAID, risk register, issues log, dependencies, escalation, heat map, risk management
workbook: raid
order: 303
---
# Risks, issues and escalations

## How we score a risk
Layout: matrix
- Act now: likely and high impact - mitigate this week, report to steering
- Plan: unlikely but high impact - a contingency ready
- Watch: likely but low impact - the owner tracks it
- Accept: unlikely and low impact - review monthly

## Top risks
| ID | Risk | Likelihood | Impact | Mitigation | Owner |
|---|---|---|---|---|---|
| R-04 | Key users not available for testing | Medium | High | Backfill agreed with managers | Business lead |
| R-07 | Data quality delays migration | High | High | Cleansing now, three trial loads | Data lead |
| R-09 | Supplier release slips | Medium | Medium | Milestone payments tied to dates | Vendor manager |
| R-11 | Change freeze moves earlier | Low | High | Agree the window with operations | Project manager |

## Open issues
### I-02 Two interfaces late (high)
- Extra developer, daily check
- Technology lead, by next Friday
### I-05 Test environment unstable (medium)
- Fix plan with infrastructure
- Technology lead, this week

## Dependencies
| ID | We need | From | By | Status |
|---|---|---|---|---|
| D-01 | Single sign-on for new users | Identity team | Aug 1 | On track |
| D-03 | Store hardware refresh | Store technology | Oct 1 | At risk |

## How we escalate
Layout: swimlane handoffs
- Owner: Updates the item every week
- Project manager: Reviews the log weekly
- Project manager: Can the board resolve it?
- Project manager: If yes, agrees action and date
- Steering committee: If no, decides on options and funding
- Owner: Acts and closes the item

## The weekly rhythm
Layout: process cycle
- Identify: new items from every team
- Assess: likelihood and impact
- Act: owner, action, date
- Review: weekly board, monthly steering
