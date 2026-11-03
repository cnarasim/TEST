---
id: to-cr-change-enablement
domain: Technology Operations
l1: Change and Release
l2: Change enablement and approval board
summary: Changing production safely and fast: change types and risk levels, approvals and the change advisory board, freezes, controls and KPIs.
systems: Ticketing tool, CMDB, Change calendar, Release pipeline
tags: change enablement, change management, CAB, change advisory board, change risk, emergency change, change freeze
order: 201
---
# Change enablement and approval board

Approve each change in proportion to its risk, so low-risk changes flow and risky ones get the board's attention.

## What change enablement covers
### Purpose
- Change production safely and quickly
- Protect stores, DCs and ulta.com at peak
### In scope
- Standard, normal and emergency changes
- Risk, approval, scheduling and review
### Outcome
- Fewer failed and change-caused incidents
- Low-risk changes approved without a meeting

## Risk sets the route to approval
| Change type | When it applies | Who approves |
|---|---|---|
| Standard | Low risk, pre-approved recipe | Pre-approved, logged only |
| Normal, low risk | Small impact, easy rollback | Change manager or peer |
| Normal, high risk | Wide impact, hard to roll back | Change advisory board |
| Emergency | Needed now to restore service | Emergency board, reviewed after |

## The board reviews only risky changes
Layout: swimlane handoffs
- Requester: Raises the change with rollback
- Change manager: Assesses risk and conflicts
- Change manager: High risk?
- Change board: If yes, reviews and decides
- Change manager: If no, approves it
- Implementer: Deploys in the agreed window
- Implementer: Confirms success or rolls back

## Systems and data for change enablement
| Step | What the system does | Records it keeps |
|---|---|---|
| Request | Plan, test and rollback recorded | Change record |
| Assess | CMDB shows affected services | Impacted configuration items |
| Schedule | Calendar flags clashes, freezes | Change calendar |
| Approve | Approval by risk level | Approval history |
| Implement | Deployments linked to the change | Deployment log |

## Five steps from request to review
Layout: process chevrons
- Request: plan and rollback
- Assess: risk and impact
- Approve: by risk level
- Implement: in the window
- Review: success or lessons

## Controls and exceptions
| Control | How it works | Owner |
|---|---|---|
| Rollback plan | No approval without a rollback | Change manager |
| Peak freeze | Emergency changes only at peak | Change manager |
| Separation of duties | No one approves their own change | Service owner |
| Emergency review | Reviewed at the next board | Change board |
| Unrecorded changes | Deployments matched to records | Platform team |
> Notes: set the freeze dates from the peak calendar (holiday season, big launches and events).

## KPIs that show it works
| KPI | What it measures | Data source |
|---|---|---|
| Change success rate | Without incident or rollback | Change closure codes |
| Change-caused incidents | Incidents linked to a change | Incident-change links |
| Emergency change share | Emergency changes of all changes | Change records by type |
| Lead time for change | Request to production | Change and deploy times |
| Standard change share | Changes that skip the board | Change type report |

## Today and target
### Today
- Every change waits for the weekly board
- Rollback plans missing or never tested
### Target
- Low-risk changes pre-approved and automated
- The board spends its time on risky changes
