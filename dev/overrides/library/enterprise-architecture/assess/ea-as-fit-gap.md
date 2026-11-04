---
id: ea-as-fit-gap
domain: Enterprise Architecture
l1: Assess
l2: Fit-gap analysis
summary: How much of the need the standard solution meets, how each gap is closed, and the effort and risk of the gaps.
systems: Requirements management
tags: fit gap, requirements, gap analysis, standard, configuration, extension
order: 102
---
# Fit-gap analysis

## Requirements by fit
Layout: donut
- Standard: 62% of scope
- Configuration: 23% of scope
- Extension: 10% of scope
- Gap: 5% of scope
> Notes: illustrative shares - replace with the counts from the fit-gap workshops.

## Fit by requirement area
| Requirement area | Fit | How it is met | Effort |
|---|---|---|---|
| Order capture | Standard | Out of the box | Low |
| Pricing and discounts | Configuration | Price rules set up | Medium |
| Approvals | Configuration | Workflow configured | Medium |
| Reporting | Extension | Report built on the data model | Medium |
| Partner portal | Gap | Separate portal or workaround | High |

## Four ways to close a gap
Layout: process diverge
- Gap: a need the standard does not meet
- Change the process: adopt the standard way
- Configure: settings, rules, workflow
- Extend: a supported extension point
- Accept: a manual workaround for now

## Our fit-gap principles
### Adopt
- The standard process first
- Change the process before the product
### Adapt
- Configure, do not customise
- Every change has an owner
### Extend
- Only for what makes us different
- Through supported extension points

## Standard or extend
### Today
- Every local variation becomes a requirement
- Gaps closed with custom code
### Target
- Standard process unless it costs us customers
- Extensions approved by the design authority
