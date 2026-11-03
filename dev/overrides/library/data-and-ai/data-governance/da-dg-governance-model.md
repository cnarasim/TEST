---
id: da-dg-governance-model
domain: Data and AI
l1: Data Governance
l2: Data governance model
summary: Who decides what about data: owners, stewards and the council, the policies they keep, and how a data issue is raised and resolved.
systems: Data catalog, Data quality tool, Ticketing tool
tags: data governance, data owner, data steward, data council, data policy, accountability, operating model
order: 101
---
# Data governance model

## What data governance covers
### Purpose
- Clear owners for every important data set
- Decisions about data made once, by the right people
### In scope
- Roles, policies, standards and the council
- Issues, definitions and access decisions
### Outcome
- Data people trust and can find
- Fewer disputes about whose number is right

## Three roles carry the model
Layout: pyramid
- Data council: sets policy, settles disputes
- Data owners: accountable for a domain's data
- Data stewards: keep definitions and quality day to day

## Who decides what
| Decision | Decided by | Advised by |
|---|---|---|
| Data policy and standards | Data council | Enterprise architecture |
| Definitions in a domain | Data owner | Data stewards |
| Access to sensitive data | Data owner | Privacy and security |
| Quality rules and targets | Data steward | Data users |
| Disputes between domains | Data council | Data owners |

## Issues go to the owner, then the council
Layout: swimlane handoffs
- Data user: Raises a data issue
- Data steward: Triages and finds the cause
- Data steward: Fix inside one domain?
- Data steward: If yes, fixes with the owner
- Data steward: If no, takes it to the council
- Data council: Decides and records it

## Policies every domain follows
| Policy | What it requires | Owner |
|---|---|---|
| Ownership | A named owner for each data set | Data council |
| Definitions | Business terms in the catalog | Data stewards |
| Quality | Rules and targets for key data | Data owners |
| Access | Sensitive data by approval only | Data owners |
| Retention | Kept only as long as needed | Data council |

## KPIs that show it works
| KPI | What it measures | Data source |
|---|---|---|
| Data sets with owners | Key data sets with a named owner | Data catalog |
| Terms defined | Business terms with an agreed meaning | Data catalog |
| Issues resolved | Issues closed within [n] days | Issue log |
| Quality score | Key data passing its rules | Data quality tool |

## Today and target
### Today
- Nobody owns the data everyone uses
- The same term means three things
### Target
- Every key data set owned and defined
- Disputes settled once, then recorded
