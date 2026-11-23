
import json
from algorithms.dijkstra import dijkstra, get_path

# Load location data
with open("data/locations.json", "r") as file:
    data = json.load(file)

# Build adjacency list
graph = {node: {} for node in data["locations"]}

for source, destination, distance in data["roads"]:
    graph[source][destination] = distance
    graph[destination][source] = distance

# Find shortest paths from warehouse
distances, previous = dijkstra(graph, "W")

print("\n========== DIJKSTRA SHORTEST PATHS ==========")

for destination in data["locations"]:
    path = get_path(previous, "W", destination)

    print(
        "W ->", destination,
        "| Distance:", distances[destination], "km",
        "| Path:", " -> ".join(path)
    )
