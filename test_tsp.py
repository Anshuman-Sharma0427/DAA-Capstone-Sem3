
import json
from algorithms.dijkstra import dijkstra
from algorithms.tsp import nearest_neighbor_tsp

# Load location data
with open("data/locations.json", "r") as file:
    data = json.load(file)

# Build graph
graph = {node: {} for node in data["locations"]}

for source, destination, distance in data["roads"]:
    graph[source][destination] = distance
    graph[destination][source] = distance

# Calculate all-pairs shortest distances using Dijkstra
distance_matrix = {}

for start in data["locations"]:
    distances, _ = dijkstra(graph, start)
    distance_matrix[start] = distances

# Generate delivery route
route, total_distance = nearest_neighbor_tsp(
    distance_matrix, "W"
)

print("\n========== DELIVERY ROUTE ==========")
print("Route:", " -> ".join(route))
print("Total Route Distance:", total_distance, "km")
