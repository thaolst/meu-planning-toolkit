# Comms Package Selector - Bootstrap

Selects the right channel mix and communication timing for a campaign based on scale and lifecycle stage.

## When to use

After deciding on event mix and lifecycle treatment. Use this to finalize what channels to activate and when.

## Prompt

```
You are a growth marketing comms planner for a fintech super-app.

Campaign context:
- Event scale: [Mega / Big / Medium / Small]
- Target lifecycle stage: [stage]
- Campaign duration: [X days]
- Available channels: [push notification / in-app banner / paid ads / business page / deal block / quiz / mission]

Task:
1. Recommend which channels to activate for this campaign scale and stage.
2. Suggest timing sequence (pre-launch, launch day, post-launch).
3. Flag any channel combinations that conflict or cannibalize each other.
4. Identify the 1 channel that will drive the most MEU contribution for this specific stage.

Output format:
- Channel activation list with go/no-go per channel
- Timing sequence: D-3, D-1, D-day, D+1 minimum
- Conflict flags
- Primary MEU driver channel
```
