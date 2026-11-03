---
id: pp-dl-design-review
domain: Programs and Projects
l1: Deliver
l2: Solution design review
summary: How a solution design is checked before build: what reviewers look at, the review steps, the three outcomes, readiness by area and common findings.
systems: Architecture repository, Requirements management tool, Collaboration site
tags: design review, solution design, design authority, functional design, technical design, sign-off, quality
order: 406
---
# Solution design review

## What the design review covers
### Purpose
- Catch design problems before they are built
- One approved design per process area
### In scope
- Process, solution, data and integration designs
- Security, controls and non-functional needs
### Outcome
- Approved designs, conditions closed
- Build starts on a stable baseline

## What reviewers check
| Area | Question | Reviewer |
|---|---|---|
| Process | Does it meet the signed-off requirements? | Process owner |
| Solution | Standard first, every extension justified? | Solution architect |
| Integration | Interfaces, volumes and error handling? | Integration lead |
| Data | Objects, owners and migration rules? | Data lead |
| Security and controls | Roles, approvals and audit trail? | Risk and controls lead |

## A design passes five steps
Layout: process chevrons
- Draft: written and traced to requirements
- Peer review: another designer checks it
- Walk-through: the business sees it end to end
- Design authority: approves or sets conditions
- Baseline: locked, changes via change control

## Three possible outcomes
### Approved
- Meets requirements and standards
- Build can start
### With conditions
- Small gaps, each with an owner and date
- Build starts, conditions tracked
### Rework
- Gaps in scope, risk or standards
- Back to the designer, new review date

## Designs approved by area
Layout: bullet
- Order to cash: 9 of 10
- Procure to pay: 7 of 9
- Record to report: 6 of 6
- Store operations: 4 of 8
> Notes: illustrative counts - designs approved against designs planned in each area.

## How the design authority decides
Layout: swimlane handoffs
- Designer: Submits design and trace list
- Reviewers: Check it against the checklist
- Design authority: Meets the standards?
- Design authority: If yes, approves and baselines it
- Designer: If no, reworks it by the date
- Project manager: Tracks conditions to closure

## Common findings to avoid
| Finding | Why it matters | Prevention |
|---|---|---|
| Unjustified extension | Cost to build and to upgrade | Fit-gap decision first |
| Interface errors not handled | Silent failures in production | Integration pattern checklist |
| Roles not defined | Access delays and control gaps | Role design in the same review |
| Volumes not stated | Slow at peak | Peak volumes in every design |
