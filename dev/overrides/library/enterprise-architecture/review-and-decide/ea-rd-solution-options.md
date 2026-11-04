---
id: ea-rd-solution-options
domain: Enterprise Architecture
l1: Review and Decide
l2: Solution options review
summary: The problem, the options considered, how they compare on the criteria, the recommended option and its roadmap.
systems: Architecture repository
tags: solution options, option analysis, recommendation, options appraisal, solution review
order: 301
---
# Solution options review

## The problem and the decision we need
### Problem
- What is broken or missing today
- Who it hurts and how much
### Constraints
- Budget, dates, standards, skills
- What we must not change
### Decision needed
- Which option to take forward
- By when, and who decides

## Options considered
Layout: process list
| Option | What it is | Benefits | Risks | Cost |
|---|---|---|---|---|
| Do nothing | Keep today's solution | No spend | Problem grows | Low |
| Enhance | Extend the current application | Fast, familiar | Technical debt | Medium |
| Replace | A new standard product | Modern, supported | Change effort | High |
| Hybrid | New product for the core, keep the rest | Phased risk | Two systems for a while | Medium |

## Options against the criteria
| Criterion | Do nothing | Enhance | Replace | Hybrid |
|---|---|---|---|---|
| Meets the need | Weak | Medium | Strong | Strong |
| Time to value | Strong | Strong | Weak | Medium |
| Cost over five years | Medium | Medium | Medium | Medium |
| Delivery risk | Strong | Medium | Weak | Medium |
| Strategic fit | Weak | Weak | Strong | Strong |

## Recommended option
### Option A: Hybrid
- Replace the core in two waves
- Keep stable modules until their renewal
### Option B: Replace
- Faster to the end state
- Higher change risk in one go

## Roadmap for the recommended option
Layout: timeline quarters
- Design and contract: Jan 2027 – Mar 2027 (Programme)
- Wave 1 build, test: Apr 2027 – Aug 2027 (Delivery)
- Wave 1 live: Sep 6, 2027 (Delivery)
- Wave 2 build, test: Oct 2027 – Feb 2028 (Delivery)
- Retire the old core: Mar 31, 2028 (Programme)
> Notes: example dates; replace them with the plan.

## The decision
- Decision: Take the hybrid option forward
- Ask: Approve design and contract funding
- Next step: Architecture board review next month
