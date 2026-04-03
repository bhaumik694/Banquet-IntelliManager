def compute_synergy(current_items, adj_items, gap_hours):
    cuisine_match = 0
    heavy_prep = 0
    total_prep = 0

    current_categories = set()
    adj_categories = set()

    for ci in current_items:
        total_prep += ci["prepTime"]

        if ci["prepTime"] >= 30:
            heavy_prep += 1

        current_categories.add(ci["category"])

        for ai in adj_items:
            if ci["cuisine"] == ai["cuisine"]:
                cuisine_match += 1
            adj_categories.add(ai["category"])

    common_categories = list(current_categories & adj_categories)

    cuisine_overlap_pct = (cuisine_match / len(current_items)) * 100

    score = (
        cuisine_overlap_pct * 0.4 +
        len(common_categories) * 5 +
        heavy_prep * 3 -
        gap_hours * 2
    )

    efficiency_gain = min(40, round(score * 1.5))

    return {
        "score": round(score),
        "metrics": {
            "cuisineOverlapPct": round(cuisine_overlap_pct),
            "heavyPrepItems": heavy_prep,
            "commonCategories": len(common_categories),
            "timeGapHours": round(gap_hours, 2),
            "efficiencyGain": efficiency_gain
        },
        "efficiencyGain": efficiency_gain
    }