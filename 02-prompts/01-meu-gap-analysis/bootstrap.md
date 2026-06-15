# MEU Gap Analysis - Bootstrap

Use this at the start of a planning cycle when you need to understand where your MEU gap is coming from before deciding on campaign mix.

## When to use

- Beginning of quarter or annual planning
- After a period of MEU underperformance
- Before proposing a new campaign to leadership

## Input you need

Before running this prompt, gather:

1. Current MEU base (last full month)
2. MEU target (quarter or full year)
3. MEU breakdown by lifecycle stage if available (Acquisition / Activation / Retention / Resurrection)
4. Last 3 months MEU trend (growing, flat, declining)
5. Top 3 campaigns running currently

## Prompt

```
You are a growth marketing strategist specializing in engagement metric planning for fintech and super-app platforms.

Context:
- Current MEU base: [X users]
- MEU target: [Y users] by [date]
- MEU gap: [Y - X users] ([Z]% above current base)
- Lifecycle breakdown (if known): Acquisition [%], Activation [%], Retention [%], Resurrection [%]
- Recent trend: [growing / flat / declining] over last 3 months
- Current active campaigns: [list top 3]

Task:
1. Diagnose where the MEU gap is most likely coming from based on the context above.
2. Identify which lifecycle stage has the highest gap-closing potential given the timeframe.
3. Flag any risk if the trend continues without intervention.
4. Recommend the minimum campaign interventions needed to close the gap - ordered by estimated impact.

Output format:
- Gap diagnosis: 2-3 sentences
- Priority lifecycle stage: 1 stage with rationale
- Risk flag: 1 sentence
- Recommended interventions: ranked list, max 5 items
```

## Example output

See `example-output.md` in this folder.

## Next step

After running this prompt, move to `02-event-mix-planner/bootstrap.md` with the priority lifecycle stage identified here.
