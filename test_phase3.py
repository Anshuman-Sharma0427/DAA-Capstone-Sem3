
import json
from algorithms.dijkstra import dijkstra
from algorithms.tsp import nearest_neighbor_tsp
from algorithms.sorting import merge_sort
from algorithms.knapsack import knapsack

# Load data
with open("data/parcels.json", "r") as file:
    parcels = json.load(file)

with open("data/locations.json", "r") as file:
    data = json.load(file)

# Phase 2: Sort and select parcels
sorted_parcels = merge_sort(parcels)

selected, total_weight, total_value, dp = knapsack(
    sorted_parcels, data["vehicle_capacity"]
)

# Get unique destinations of selected parcels
destinations = sorted(
    set(p["destination"] for p in selected)
)

# Build graph
graph = {node: {} for node in data["locations"]}

for source, destination, distance in data["roads"]:
    graph[source][destination] = distance
    graph[destination][source] = distance

# Calculate shortest distances from each required location
required_locations = ["W"] + destinations
distance_matrix = {}

for start in required_locations:
    distances, _ = dijkstra(graph, start)
    distance_matrix[start] = {
        location: distances[location]
        for location in required_locations
    }

# Generate route
route, total_distance = nearest_neighbor_tsp(
    distance_matrix, "W"
)

print("\n========== SELECTED DELIVERY PARCELS ==========")

for p in selected:
    print(p["id"], "->", p["destination"])

print("\n========== OPTIMIZED DELIVERY ROUTE ==========")
print("Route:", " -> ".join(route))
print("Total Distance:", total_distance, "km")
