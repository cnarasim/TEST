---
id: fi-pp-supplier-bank-changes
domain: Finance
l1: Procure to Pay
l2: Supplier bank detail changes
summary: Supplier bank account changes requested, verified by a call-back to a known contact, approved under dual control and monitored.
systems: Supplier portal, ERP supplier master, Workflow tool, Bank account validation
tags: vendor bank change, payment fraud, call-back, dual control, supplier master, e-mail fraud, impersonation
order: 105
---
# Supplier bank detail changes

## What supplier bank detail changes cover
### Purpose
- Pay suppliers only into accounts they own
- Stop payment fraud before money leaves
### In scope
- New supplier bank details and changes
- Verification, approval and payment monitoring
### Outcome
- Every change verified and approved
- No payment to an unverified account

## Every request is verified before approval
Layout: swimlane handoffs
- Supplier: Requests the change online
- Supplier master team: Calls the contact on file
- Supplier master team: Change confirmed by the supplier?
- Supplier master team: If yes, enter the new details
- Supplier master team: If no, refuse and report it
- Supplier master lead: Approves as a second person
- Treasury: Reviews the first payment

## Systems and data for bank detail changes
| Step | What the system does | Records it keeps |
|---|---|---|
| Request | Portal form, no change by e-mail | Change request, documents |
| Verify | Account owner and bank checked | Validation result, call log |
| Approve | A second person approves | Before and after values |
| Notify | Known contact told of the change | Supplier notification |
| Monitor | First payment to it is flagged | Payment review |

## Five checks before the details change
Layout: process numbered
- Request: from the supplier's portal account
- Call back: a contact already on file
- Validate: the account name matches the supplier
- Approve: a second person, never the requester
- Confirm: tell the supplier's known contact
> Notes: never use a phone number or e-mail address from the change request itself; fraudsters impersonate suppliers by e-mail.

## Controls that stop payment fraud
| Control | How it works | Owner |
|---|---|---|
| Independent call-back | Number on file, never one from the request | Supplier master team |
| Dual control | Entry and approval by different people | Supplier master lead |
| Segregation of duties | Supplier master users cannot post or pay invoices | IT security |
| Change report review | Every bank change reviewed before the payment run | AP manager |

## KPIs show changes are safe and fast
| KPI | What it measures | Data source |
|---|---|---|
| Changes with a call-back | Changes verified with a known contact | Change requests |
| Change cycle time | Days from request to change in effect | Request dates |
| Attempts stopped | Requests refused as suspicious | Refused requests |
| First payments reviewed | First payments to new accounts checked | Payment reviews |

## From e-mail requests to verified changes
### Today
- Bank changes accepted from e-mail
- One person enters and approves
### Target
- Portal requests and an independent call-back
- Dual control and a change report every run
