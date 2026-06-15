# Event Mix Planner - Bootstrap

Translates MEU gap by lifecycle stage into a concrete campaign calendar with event scale and mechanic recommendations.

## When to use

After completing `01-meu-gap-analysis/bootstrap.md` and knowing your priority lifecycle stage and gap size.

## Input you need

1. MEU gap size and % (from gap analysis)
2. Priority lifecycle stage
3. Time horizon (quarter / half-year / full year)
4. Current event calendar (what is already planned)
5. Budget constraint level: tight / moderate / flexible

## Prompt

```
You are a growth marketing planner building a campaign calendar to close a MEU gap.

Context:
- MEU gap: [X users], [Z]% above current base
- Priority lifecycle stage: [Acquisition / Activation / Retention / Resurrection]
- Time horizon: [Q / H1 / FY]
- Already planned events: [list or "none"]
- Budget: [tight / moderate / flexible]

Event scale reference:
- Mega: 1-2/year, mass ATL, >=50% discount, traffic spike
- Big: monthly, mass ATL, >=30% discount
- Medium: repeated monthly, >=20% discount
- Small: weekly/daily, frequency builder, >=15% discount
- Always-on: lifecycle segment treatment, never stops

Task:
1. Recommend the event mix needed to close the gap (how many Mega / Big / Medium / Small events).
2. Map each event scale to the priority lifecycle stage mechanic.
3. Identify the 1-2 always-on mechanics that must run regardless of event calendar.
4. Flag any gaps in the current planned calendar.

Output format:
- Recommended event mix: table with scale, quantity, target stage, mechanic
- Always-on must-haves: bullet list
- Calendar gaps: bullet list
```

## Next step

Move to `03-lifecycle-treatment/bootstrap.md` to get specific mechanics per lifecycle stage.
