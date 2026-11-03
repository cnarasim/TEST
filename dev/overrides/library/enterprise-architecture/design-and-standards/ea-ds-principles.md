---
id: ea-ds-principles
domain: Enterprise Architecture
l1: Design and Standards
l2: Architecture principles
summary: The few rules every technology decision is tested against, why each one matters, and how teams apply them or ask for a waiver.
systems: Architecture repository, Decision log
tags: architecture principles, guiding principles, standards, design authority, waiver, decision criteria
order: 601
---
# Architecture principles

## What architecture principles do
### Purpose
- One set of rules for every technology decision
- Faster decisions, fewer debates about taste
### In scope
- Business, data, application and technology rules
- How principles are applied and waived
### Outcome
- Designs that fit together and age well
- Exceptions made openly, with an end date

## Six principles every design must meet
Layout: hexagons
- Guest first: design from the guest and associate journey
- Reuse first: reuse, then buy, then build
- Data as an asset: one owner, one system of record
- Secure by design: least access, privacy built in
- Cloud ready: managed services where they fit
- Simple to run: monitored, documented, owned

## Each principle has a reason and a test
| Principle | Why it matters | Test in a design review |
|---|---|---|
| Guest first | Technology serves the journey | Which journey step gets better? |
| Reuse first | Fewer systems to run and pay for | What do we own that does this? |
| Data as an asset | One version of the truth | Who owns each data object? |
| Secure by design | Breaches cost trust and money | How is access limited and logged? |
| Simple to run | Support lasts longer than the build | Who runs it, and how is it watched? |

## Every design review applies them
Layout: swimlane handoffs
- Project team: Submits the design
- Design authority: Tests it against the principles
- Design authority: Every principle met?
- Design authority: If yes, approves the design
- Design authority: If no, reviews a waiver
- Project team: Logs decision and end date

## When a principle can be waived
| Rule | How it works | Owner |
|---|---|---|
| Written request | The gap, the reason and the risk | Project lead |
| Time limit | Every waiver has an end date | Design authority |
| Remediation plan | How and when the gap closes | Project lead |
| Quarterly review | Open waivers checked each quarter | Enterprise architecture |

## KPIs that show it works
| KPI | What it measures | Data source |
|---|---|---|
| Designs reviewed | Projects reviewed before build | Decision log |
| Overdue waivers | Waivers past their end date | Waiver register |
| Reuse rate | Needs met by systems we own | Decision log |
| Time to decision | Days from submission to decision | Decision log |

## Today and target
### Today
- Decisions made project by project
- Exceptions granted without an end date
### Target
- Six principles applied in every review
- Every waiver tracked and closed
