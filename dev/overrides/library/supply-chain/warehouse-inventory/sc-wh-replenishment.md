---
id: sc-wh-replenishment
domain: Supply Chain
l1: Warehouse & Inventory
l2: Pick-face replenishment
summary: Keeping pick faces full from reserve storage: min and max levels, demand-based tasks before waves, top-offs and emergency moves.
systems: WMS, Labor management
tags: replenishment, pick face, min max, reserve, top-off, emergency replenishment, short pick
order: 408
---
# Pick-face replenishment

## What replenishment covers
### Purpose
- Every pick face has stock when pickers arrive
- Reserve stock moved before, not during, waves
### In scope
- Min and max levels by pick face
- Demand, top-off and emergency tasks
### Outcome
- Fewer short picks and waiting pickers
- Fewer emergency moves in peak hours

## The WMS triggers, drivers move the stock
Layout: swimlane handoffs
- WMS: Checks pick-face levels
- WMS: Below the minimum or the wave?
- WMS: If yes, creates a move task
- WMS: If no, checks again after the wave
- Reach driver: Moves cases from reserve
- Reach driver: Confirms the face is full
- Picker: Picks the wave in full

## Four ways to trigger a move
| Trigger | When it runs | Best for |
|---|---|---|
| Min and max | Face drops below its minimum | Steady sellers |
| Demand-based | Before a wave, from its pick lines | Fast movers |
| Top-off | Off-peak, to fill faces | All faces before peak |
| Emergency | A picker finds an empty face | Exceptions only |

## Systems and data for replenishment
| Step | What the system does | Records it keeps |
|---|---|---|
| Levels | Holds min, max and face size | Pick-face settings |
| Trigger | Creates tasks by rule | Move tasks, priority |
| Move | Directs the driver from reserve | Move confirmations |
| Review | Flags faces to resize | Short picks by face |

## Controls and exceptions
| Control | How it works | Owner |
|---|---|---|
| Face sizes reviewed | Monthly, from sales velocity | Inventory control |
| Tasks before waves | Moves due before the wave release | Shift lead |
| Emergency review | Every emergency move has a cause | DC operations |

## KPIs that show it works
| KPI | What it measures | Data source |
|---|---|---|
| Short picks from empty faces | Lines short with stock in reserve | Pick and stock records |
| Emergency moves | Moves raised by pickers | Move tasks |
| Moves on time | Moves done before the wave | Move tasks vs waves |
| Face fill | Faces above the minimum | Pick-face levels |

## Today and target
### Today
- Faces run empty mid-wave
- Drivers chase emergency moves all shift
### Target
- Faces filled before every wave
- Emergency moves rare and explained
