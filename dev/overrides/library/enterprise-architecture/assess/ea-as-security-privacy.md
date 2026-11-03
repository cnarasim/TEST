---
id: ea-as-security-privacy
domain: Enterprise Architecture
l1: Assess
l2: Security, privacy and compliance review
summary: Data classification, the controls a solution must have, supplier assurance, privacy review and the residual risk decision.
systems: Security assessment, Identity and access, Privacy office
tags: security, privacy, compliance, data classification, third-party risk, controls
order: 104
---
# Security, privacy and compliance review

## How the review runs
Layout: swimlane handoffs
- Product owner: Completes the access questionnaire
- Security architect: Classifies the data
- Security architect: Sensitive or regulated data?
- Security architect: If yes, run the full assessment
- Security architect: If no, apply the standard controls
- Privacy office: Reviews personal data use
- Risk owner: Accepts the residual risk

## Controls we check
| Control area | What we check | Evidence |
|---|---|---|
| Identity and access | Single sign-on, multi-factor, roles, joiner-mover-leaver | Configuration review |
| Data protection | Encryption at rest and in transit, key ownership | Supplier documentation |
| Supplier assurance | Independent audit reports, penetration tests | Current reports |
| Logging and monitoring | Security events sent to our monitoring | Integration test |
| Privacy | Purpose, consent, retention, deletion | Privacy impact assessment |
| Resilience | Backup, recovery, incident response | Recovery test, contract terms |

## Risk by likelihood and impact
Layout: matrix
- Act now: likely and severe - fix before go-live
- Plan: unlikely but severe - mitigate on a date
- Watch: likely but minor - monitor
- Accept: unlikely and minor - record and accept

## Five steps to a security decision
Layout: process chevrons
- Classify: the data
- Assess: controls and supplier
- Fix: gaps before go-live
- Accept: residual risk, signed
- Review: every year

## The decision
- Decision: Approve go-live with the conditions in the risk register
- Ask: The risk owner signs the residual risk
- Next step: Re-assess at contract renewal
