---
id: da-dg-privacy-impact
domain: Data and AI
l1: Data Governance
l2: Privacy impact assessment
summary: Checking a new use of personal data before it starts: what data, why, who sees it, the risks, the controls and the decision.
systems: Privacy management tool, Data catalog, Consent platform
tags: privacy impact assessment, personal data, consent, data minimization, privacy by design, guest data
order: 104
---
# Privacy impact assessment

## What a privacy assessment covers
### Purpose
- Guest and associate data used fairly and lawfully
- Privacy risks found before launch, not after
### In scope
- New uses of personal data and new vendors
- Purpose, consent, access, retention and transfers
### Outcome
- Projects launch with the right controls
- A record of each decision for regulators

## Five questions for every new use
Layout: process numbered
- What: which personal data, and how sensitive
- Why: the purpose, and is the data needed for it
- Who: which teams and vendors see it
- How long: retention and deletion
- What could go wrong: the risks and their controls

## Common risks and their controls
| Risk | Control | Owner |
|---|---|---|
| More data than needed | Collect only what the purpose needs | Project lead |
| Use beyond consent | Check consent before each use | Marketing |
| Vendor access | Contract terms and security review | Procurement |
| Kept too long | Deletion after the retention period | Data owner |
| Re-identification | Aggregate or mask in analytics | Data platform team |

## The privacy team decides with the owner
Layout: swimlane handoffs
- Project team: Completes the assessment
- Privacy team: Reviews data, purpose, risks
- Privacy team: High risk left after controls?
- Privacy team: If yes, escalates to legal
- Privacy team: If no, approves with conditions
- Project team: Puts the controls in place

## KPIs that show it works
| KPI | What it measures | Data source |
|---|---|---|
| Assessed before launch | Projects assessed before go-live | Privacy tool |
| Time to decision | Days from submission to decision | Privacy tool |
| Open conditions | Agreed controls not yet in place | Privacy tool |
| Guest requests on time | Access and deletion requests met | Request log |

## Today and target
### Today
- Privacy reviewed late, if at all
- Decisions in email threads
### Target
- Every new use assessed before build
- One record of decisions and controls
