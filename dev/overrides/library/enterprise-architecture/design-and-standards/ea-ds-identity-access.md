---
id: ea-ds-identity-access
domain: Enterprise Architecture
l1: Design and Standards
l2: Identity and access architecture
summary: One way to sign in and get access for associates, guests, partners and systems: single sign-on, multi-factor, roles and reviews.
systems: Identity platform, HR system, Privileged access tool, Secrets vault
tags: identity, access management, single sign-on, MFA, role-based access, joiner mover leaver, least privilege
order: 608
---
# Identity and access architecture

## What identity and access covers
### Purpose
- The right people get the right access, fast
- Access removed the day it is no longer needed
### In scope
- Associates, guests, partners and systems
- Sign-in, roles, reviews and secrets
### Outcome
- Fewer passwords and fewer breaches
- Audits passed without a scramble

## One identity platform for four groups
Layout: process diverge
- Identity platform: one way to sign in and get access
- Associates: single sign-on, multi-factor for admin
- Guests: one account across site, app and stores
- Partners: vendor and carrier portals
- Systems: service accounts with managed secrets

## Access standards
| Standard | Rule | Owner |
|---|---|---|
| Single sign-on | Every app signs in through the platform | Identity team |
| Multi-factor | Required for remote and admin access | Security |
| Least access | Roles grant only what the job needs | Application owner |
| Joiner, mover, leaver | Access follows the HR record | Identity team |
| Reviews | Access reviewed every [n] months | Application owner |

## Access follows the HR record
Layout: swimlane handoffs
- HR: Records the hire or the move
- Identity platform: Grants access by role
- Manager: Extra access needed?
- Manager: If yes, requests it with a reason
- Manager: If no, keeps the role access
- Application owner: Approves and reviews it

## KPIs that show it works
| KPI | What it measures | Data source |
|---|---|---|
| Apps on single sign-on | Share of apps on the platform | Identity platform |
| Multi-factor coverage | Accounts with multi-factor on | Identity platform |
| Leavers removed | Access removed within [n] hours | HR and access logs |
| Reviews on time | Access reviews closed by the due date | Review records |

## Today and target
### Today
- A login per app, removed by ticket
- Shared admin accounts on key systems
### Target
- One sign-in, access by role
- Every admin account named and multi-factor
