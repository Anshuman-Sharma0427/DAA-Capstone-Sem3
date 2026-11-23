
import json
from algorithms.knapsack import knapsack

# Load parcel data
with open("data/parcels.json", "r") as file:
    parcels = json.load(file)

# Vehicle capacity
capacity = 20

# Apply Knapsack
selected, total_weight, total_value, dp = knapsack(
    parcels, capacity
)

print("\n===== OPTIMAL PACKING PLAN =====")

for parcel in selected:
    print(
        parcel["id"],
        "| Weight:", parcel["weight"], "kg",
        "| Value: Rs.", parcel["value"]
    )

print("\nVehicle Capacity:", capacity, "kg")
print("Total Weight:", total_weight, "kg")
print("Total Value: Rs.", total_value)

print("\n===== DP TABLE =====")

print("Parcel/Capacity", *range(capacity + 1))

for i, row in enumerate(dp):
    print(i, *row)
