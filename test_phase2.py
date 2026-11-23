
import json
from algorithms.sorting import merge_sort
from algorithms.knapsack import knapsack

# Load parcels
with open("data/parcels.json", "r") as file:
    parcels = json.load(file)

capacity = 20

# Step 1: Sort parcels
sorted_parcels = merge_sort(parcels)

print("\n========== PARCEL PRIORITIZATION ==========")

for p in sorted_parcels:
    print(p["id"], "| Deadline:", p["deadline"])

# Step 2: Apply Knapsack
selected, total_weight, total_value, dp = knapsack(
    sorted_parcels, capacity
)

print("\n========== OPTIMAL PACKING PLAN ==========")

for p in selected:
    print(p["id"], "| Weight:", p["weight"], "kg",
          "| Value: Rs.", p["value"])

print("\nTotal Weight:", total_weight, "kg")
print("Total Value: Rs.", total_value)
print("Vehicle Capacity:", capacity, "kg")

print("\n========== PHASE 2 COMPLETED ==========")
