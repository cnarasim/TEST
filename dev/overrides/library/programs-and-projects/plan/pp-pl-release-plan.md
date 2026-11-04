---
id: pp-pl-release-plan
domain: Programs and Projects
l1: Plan
l2: Release plan
summary: How the scope is split into releases: the slicing rules, what each release delivers, the timeline, readiness criteria and how scope moves.
systems: Project plan, Work management tool, Product backlog
tags: release plan, releases, scope, MVP, phasing, roadmap, readiness
order: 205
---
# Release plan

## What the release plan covers
### Purpose
- Deliver value early, in safe steps
- One view of what ships when
### In scope
- Release goals, scope and dates
- Dependencies, freezes and readiness
### Outcome
- Every release has a goal, scope and owner
- Teams and the business plan the same dates

## How we slice the scope
Layout: hexagons
- Value first: the scope that pays back soonest
- End to end: a whole process, not half of one
- Risk early: the hardest integration first
- Peak aware: nothing lands in the holiday freeze
- Sized: fits the team's proven pace
- Reversible: can be switched off if it fails

## What each release delivers
| Release | Goal | Main scope | Ready by |
|---|---|---|---|
| Release 1 | Core flow in pilot stores | Store returns, refunds, daily report | [date] |
| Release 2 | Every store and ulta.com | Online returns, exchanges, fraud rules | [date] |
| Release 3 | Simpler and automated | Self-service returns, vendor claims | [date] |
> Notes: example scope for a returns program - replace with the project's own releases.

## Releases on one timeline
Layout: timeline quarters
- Release 1: Feb 2027 to Apr 2027 (Pilot stores)
- Release 2: May 2027 to Aug 2027 (All stores)
- Holiday freeze: Nov 1, 2027 (All)
- Release 3: Jan 2028 to Mar 2028 (Digital)
> Notes: example dates; replace them with the plan.

## Ready to release when
| Check | Ready when | Owner |
|---|---|---|
| Scope | Frozen [n] weeks before the release | Product owner |
| Testing | Regression and acceptance passed | Test lead |
| Business | Users trained, procedures updated | Business lead |
| Support | Runbooks shared, service desk briefed | Service owner |
| Decision | Go / no-go held and recorded | Release manager |

## How scope moves between releases
Layout: swimlane handoffs
- Product owner: Proposes moving an item
- Release manager: Checks capacity
- Release manager: Release goal still holds?
- Release manager: If yes, updates the release plan
- Steering committee: If no, decides on scope or date
- Product owner: Tells teams and the business

## What each release depends on
Layout: process converge
- Interfaces: built and tested with partner systems
- Data: items and open returns migrated
- Stores: devices and training in place
- Result: A release the business can run - on the planned date
