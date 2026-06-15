# MEU Backward Planning

## The core logic

Start from the end:

```
MEU Target (FY)
  -> MEU Gap = Target - Current Base
  -> Gap by lifecycle stage (Acquisition / Activation / Retention / Resurrection)
  -> Campaign ladder per stage
  -> Event mix (Mega / Big / Medium / Small)
  -> Budget split
```

## Step 1 - Calculate MEU gap by stage

Before planning any campaign, know where your gap comes from.

| Stage | Definition | Typical contribution to MEU gap |
|---|---|---|
| Acquisition | Never transacted or lapsed 6m+ | High if pool is large |
| Activation | Registered but not yet engaged with core product | Medium |
| Retention | Active but frequency dropping | High if churn is rising |
| Resurrection | Lapsed 1-6 months | Medium, high ROI if segment is large |

Run `02-prompts/01-meu-gap-analysis/bootstrap.md` to get your breakdown.

## Step 2 - Match gap to campaign type

| Gap size | Campaign response |
|---|---|
| <5% below target | Optimize existing events - better deals, better comms timing |
| 5-15% below target | Add 1 repeated mechanic (weekly or daily frequency builder) |
| >15% below target | Mega event or new lifecycle segment needed |

## Step 3 - Build the event ladder

A full-year MEU plan needs all 4 layers running simultaneously:

- Mega/Big: 1-3 per year, traffic spikes, broad reach
- Medium: monthly repeated event
- Small: weekly repeated mechanic (weekend themes, category days)
- Always-on: lifecycle treatment by segment, never stops

## Opinionated defaults

- Never plan a Mega event without an always-on base. Spikes convert better when users already have the habit.
- Resurrection segment responds best to time-limited offers with a clear deadline.
- Activation segment needs a low-friction first transaction - minimize steps, maximize discount depth.
- Retention segment needs frequency mechanics (streaks, challenges, collect-to-redeem) more than discount depth.
