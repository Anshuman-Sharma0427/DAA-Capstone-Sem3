
def knapsack(parcels, capacity):
    n = len(parcels)

    # Create DP table
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Fill the DP table
    for i in range(1, n + 1):
        weight = parcels[i - 1]["weight"]
        value = parcels[i - 1]["value"]

        for w in range(capacity + 1):

            # Exclude the current parcel
            dp[i][w] = dp[i - 1][w]

            # Include the parcel if capacity allows
            if weight <= w:
                dp[i][w] = max(
                    dp[i][w],
                    value + dp[i - 1][w - weight]
                )

    # Reconstruct selected parcels
    selected = []
    w = capacity

    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected.append(parcels[i - 1])
            w -= parcels[i - 1]["weight"]

    selected.reverse()

    total_weight = sum(p["weight"] for p in selected)
    total_value = sum(p["value"] for p in selected)

    return selected, total_weight, total_value, dp
