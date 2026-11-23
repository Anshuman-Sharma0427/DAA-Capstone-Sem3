
import json
from algorithms.sorting import merge_sort

# Load parcel data
with open("data/parcels.json", "r") as file:
    parcels = json.load(file)

# Apply Merge Sort
sorted_parcels = merge_sort(parcels)

# Display result
print("\n===== PARCELS SORTED BY DEADLINE =====")

for parcel in sorted_parcels:
    print(
        parcel["id"],
        "| Deadline:", parcel["deadline"],
        "| Weight:", parcel["weight"], "kg"
    )
