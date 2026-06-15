# Lifecycle Treatment - Bootstrap

Assigns campaign mechanics and deal structures to each lifecycle stage based on behavioral patterns and MEU contribution potential.

## When to use

After knowing your event mix. Use this to get specific on what to offer each segment - deal depth, mechanic type, communication angle.

## Lifecycle stage definitions

| Stage | Definition | MEU contribution logic |
|---|---|---|
| Acquisition | New users or lapsed 6m+ | Grows the base, high cost, lower CVR |
| Activation | Registered, first transaction not yet completed | High CVR potential, low cost |
| Retention | Active users, frequency at risk | Defend MEU, highest ROI |
| Resurrection | Lapsed 1-6 months | Re-engage before permanent churn |

## Prompt

```
You are a lifecycle marketing strategist for a fintech platform with loyalty mechanics (points, vouchers, challenges).

Context:
- Priority stage: [stage from gap analysis]
- Platform type: [super-app / digital wallet / fintech / e-commerce]
- Available mechanics: [voucher / loyalty points / challenge/streak / referral / push notification / email / in-app banner]
- Budget constraint: [tight / moderate / flexible]

For the priority stage, provide:
1. Recommended deal structure (discount depth, minimum spend, cap)
2. Best mechanic type for this stage and why
3. Communication angle (what message resonates at this stage)
4. Success metric to track (not just MEU - what leading indicator tells you it is working)
5. Opinionated default: one thing to never do at this stage

Then repeat for the remaining 3 stages, in order of MEU gap contribution.

Output format: one section per stage with the 5 points above.
```

## Example output

See `example-output.md` in this folder.
