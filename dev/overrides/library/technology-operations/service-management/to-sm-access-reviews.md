---
id: to-sm-access-reviews
domain: Technology Operations
l1: Service Management
l2: Access requests and reviews
summary: Who can access what: joiners, movers and leavers, role requests and approvals, privileged access, periodic reviews, controls and KPIs.
systems: Identity provider, HR system, Ticketing tool, Privileged access vault, Access review tool
tags: access management, access review, joiner mover leaver, least privilege, segregation of duties, privileged access, SOX
order: 302
---
# Access requests and reviews

The right access for every associate, granted fast, removed on time and proven to auditors at any moment.

## What access requests and reviews cover
### Purpose
- The right access for each person, no more
- Prove it to auditors at any time
### In scope
- Joiners, movers, leavers and requests
- Privileged access and periodic reviews
### Outcome
- Access removed the day someone leaves
- Clean reviews, every finding closed

## Access follows the person's job
| Event | Trigger | What changes | Target |
|---|---|---|---|
| Joiner | HR records the hire | Starter roles created | Day one |
| Mover | HR records a new job | New role in, old role out | [n] days |
| Leaver | HR records the last day | All access disabled | Same day |
| Request | A person asks for more | Access added once approved | [n] days |

## Owners approve, the identity team applies
Layout: swimlane handoffs
- Requester: Requests a role
- Line manager: Approves the business need
- Identity team: Conflicts with existing access?
- Data owner: If yes, approves or rejects
- Identity team: If no, grants the role
- Identity team: Logs the evidence for audit

## Systems and data for access
| Step | What the system does | Records it keeps |
|---|---|---|
| Identity | HR feeds joiners and leavers | Identity record |
| Roles | Roles bundle a job's access | Role catalogue |
| Request | Workflow captures approvals | Access request, approval |
| Provision | Accounts set up or removed | Entitlement log |
| Review | Owners certify who has access | Review results |

## Reviews remove access, not just list it
Layout: process cycle
- Extract: who has what
- Certify: owners keep or remove
- Remove: revoked within [n] days
- Evidence: results kept for audit

## Controls and exceptions
| Control | How it works | Owner |
|---|---|---|
| Leaver removal | Disabled when HR ends the job | Identity team |
| Segregation of duties | Conflicting roles blocked | Risk owner |
| Privileged access | Checked out, time-limited, logged | Platform owner |
| Periodic review | Owners certify every [n] months | Application owner |
| Shared accounts | Named owner and vault, or none | Security team |

## KPIs that show it works
| KPI | What it measures | Data source |
|---|---|---|
| Leavers removed on time | Disabled by the last day | HR and identity data |
| Review completion | Certified by the due date | Review records |
| Access removed | Rights revoked in reviews | Review results |
| Orphan accounts | Accounts with no owner | Identity reconciliation |
| Time to grant | Request to working access | Request time stamps |

## Today and target
### Today
- Access copied from a colleague
- Reviews are spreadsheets once a year
### Target
- Role-based access fed by the HR system
- Quarterly reviews in one tool, evidence kept
