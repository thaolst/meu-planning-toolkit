#!/usr/bin/env python3
"""
MEU Calculator
Input: MEU target, current base, lifecycle breakdown
Output: campaign ladder with estimated MEU contribution per activity
"""

def calculate_meu_gap(target: int, current_base: int) -> dict:
    """Calculate MEU gap and classify severity."""
    gap = target - current_base
    gap_pct = gap / current_base if current_base > 0 else 0

    if gap_pct < 0.05:
        severity = "low"
        recommendation = "Optimize existing events - better deals or comms timing"
    elif gap_pct < 0.15:
        severity = "medium"
        recommendation = "Add 1 repeated mechanic (weekly or daily frequency builder)"
    else:
        severity = "high"
        recommendation = "Mega event or new lifecycle segment needed"

    return {
        "target": target,
        "current_base": current_base,
        "gap": gap,
        "gap_pct": round(gap_pct * 100, 1),
        "severity": severity,
        "recommendation": recommendation,
    }


def estimate_lifecycle_gap(gap: int, stage_weights: dict = None) -> dict:
    """
    Estimate gap distribution across lifecycle stages.
    stage_weights: dict with keys acquisition/activation/retention/resurrection
    Default weights based on typical fintech platform patterns.
    """
    if stage_weights is None:
        stage_weights = {
            "acquisition": 0.25,
            "activation": 0.20,
            "retention": 0.35,
            "resurrection": 0.20,
        }

    return {
        stage: round(gap * weight)
        for stage, weight in stage_weights.items()
    }


def recommend_campaign_ladder(gap_pct: float, priority_stage: str) -> list:
    """
    Recommend campaign ladder based on gap size and priority stage.
    Returns list of campaigns ordered by estimated MEU contribution.
    """
    campaigns = []

    if gap_pct > 15:
        campaigns.append({
            "scale": "Mega",
            "quantity": 1,
            "mechanic": "Hero placement + push notification + paid social",
            "target_stage": "All",
            "estimated_meu_contribution_pct": 30,
        })

    campaigns.append({
        "scale": "Big",
        "quantity": 4 if gap_pct > 10 else 2,
        "mechanic": "Featured placement + in-app banner",
        "target_stage": priority_stage,
        "estimated_meu_contribution_pct": 25,
    })

    campaigns.append({
        "scale": "Medium",
        "quantity": 12,
        "mechanic": "Monthly repeated event",
        "target_stage": "Retention",
        "estimated_meu_contribution_pct": 20,
    })

    campaigns.append({
        "scale": "Small",
        "quantity": 52,
        "mechanic": "Weekly frequency builder",
        "target_stage": "Activation + Retention",
        "estimated_meu_contribution_pct": 15,
    })

    campaigns.append({
        "scale": "Always-on",
        "quantity": 365,
        "mechanic": f"Lifecycle treatment for {priority_stage}",
        "target_stage": priority_stage,
        "estimated_meu_contribution_pct": 10,
    })

    return campaigns


def run(target: int, current_base: int, priority_stage: str = "retention",
        stage_weights: dict = None):
    """Main entry point."""
    gap_result = calculate_meu_gap(target, current_base)
    lifecycle_gaps = estimate_lifecycle_gap(gap_result["gap"], stage_weights)
    campaign_ladder = recommend_campaign_ladder(gap_result["gap_pct"], priority_stage)

    print("MEU Gap Analysis")
    print(f"  Target:       {target:,}")
    print(f"  Current base: {current_base:,}")
    print(f"  Gap:          {gap_result['gap']:,} users ({gap_result['gap_pct']}%)")
    print(f"  Severity:     {gap_result['severity'].upper()}")
    print(f"  Recommendation: {gap_result['recommendation']}")
    print()
    print("Gap by lifecycle stage (estimated):")
    for stage, users in lifecycle_gaps.items():
        print(f"  {stage.capitalize():15} {users:,} users")
    print()
    print("Recommended campaign ladder:")
    for c in campaign_ladder:
        print(f"  [{c['scale']:10}] x{c['quantity']:3}  {c['mechanic']}")
        print(f"             Target: {c['target_stage']} | Est. MEU contribution: {c['estimated_meu_contribution_pct']}%")

    return {
        "gap_analysis": gap_result,
        "lifecycle_gaps": lifecycle_gaps,
        "campaign_ladder": campaign_ladder,
    }


if __name__ == "__main__":
    # Example: fintech platform targeting 2M MEU, currently at 1.6M
    run(
        target=2_000_000,
        current_base=1_600_000,
        priority_stage="retention",
    )
