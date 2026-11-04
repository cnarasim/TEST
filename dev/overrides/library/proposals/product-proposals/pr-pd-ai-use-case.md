---
id: pr-pd-ai-use-case
domain: Proposals
l1: Product Proposals
l2: AI use case proposal
summary: Proposing an AI use case: the problem, what the AI does and what people still decide, the data, the value, the guardrails, the pilot and the ask.
systems: AI platform, Data platform, PIM, Workflow tool
tags: AI use case, generative AI, machine learning, human in the loop, responsible AI, AI pilot, proposal
workbook: benefits
order: 107
---
# AI use case proposal

## The problem we want AI to solve
### The problem
- New items wait [n] days for site content
- Editors rewrite brand copy by hand
### Who it affects
- Guests looking for new launches
- The content team and brand partners
### Why now
- Launch volume keeps growing
- Item and brand data is already in the PIM

## AI drafts, people approve every word
Layout: swimlane handoffs
- Brand partner: Sends item data and images
- AI service: Drafts the description and attributes
- Content editor: Draft accurate and on brand?
- Content editor: If yes, approve and publish
- Content editor: If no, edit or reject the draft
- Product team: Tunes the prompts from feedback

## The data it needs is mostly ours already
| Data | Where it comes from | Ready |
|---|---|---|
| Item attributes | PIM | Yes |
| Brand copy and claims | Brand partner files | Partly |
| Style guide | Content team | Yes |
| Claims rules | Legal and regulatory | No |
> Notes: no guest personal data is used to draft or to train.

## How we will measure the value
| Benefit | Measure | Baseline | Target | Actual |
|---|---|---|---|---|
| Faster launches | Days from item setup to live | [baseline] | [target] | [actual] |
| Less rework | Editor minutes per item | [baseline] | [target] | [actual] |
| Richer content | Items with complete attributes | [baseline] | [target] | [actual] |
| More sales | Conversion on new items | [baseline] | [target] | [actual] |

## Guardrails keep the risks small
| Risk | Guardrail | Owner |
|---|---|---|
| Wrong or invented claims | An editor approves every draft | Content lead |
| Off-brand tone | Style guide in every prompt, spot checks | Brand team |
| Our data used to train others | Contract bars training on our data | Legal |
| Unclear accountability | One named owner for the use case | Product owner |

## Prove it in one category, then scale
Layout: timeline phases
- Pilot one category: Jan 2027 to Mar 2027
- Read the results: Apr 2027 to Apr 2027
- Scale up: May 2027 to Aug 2027
> Notes: example dates; scale only if the pilot meets its targets.

## Approve a one-category pilot
- Decision: Approve a pilot in one category
- Ask: [amount] and part of two editors' time
- Next step: Data and legal review by [date]
