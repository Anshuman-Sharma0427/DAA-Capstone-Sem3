import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import time
import csv
import random

from algorithms.sorting import merge_sort
from algorithms.knapsack import knapsack
from algorithms.dijkstra import dijkstra
from algorithms.tsp import nearest_neighbor_tsp


def measure_time(function, *args):
    start = time.perf_counter()
    result = function(*args)
    end = time.perf_counter()

    return result, end - start


def generate_parcels(n):
    parcels = []

    for i in range(n):
        hour = 8 + (i % 12)

        parcels.append({
            "id": f"P{i+1}",
            "customer": f"Customer{i+1}",
            "destination": "A",
            "weight": random.randint(1, 10),
            "value": random.randint(100, 2000),
            "deadline": f"{hour:02d}:{random.randint(0, 59):02d}",
            "priority": random.choice(["High", "Medium", "Low"])
        })

    return parcels


def generate_graph(n):
    graph = {
        f"L{i}": {} for i in range(n)
    }

    nodes = list(graph.keys())

    # Create a connected chain
    for i in range(n - 1):
        weight = random.randint(1, 10)
        graph[nodes[i]][nodes[i + 1]] = weight
        graph[nodes[i + 1]][nodes[i]] = weight

    # Add additional random connections
    for i in range(n):
        for j in range(i + 2, n):
            if random.random() < 0.3:
                weight = random.randint(1, 20)
                graph[nodes[i]][nodes[j]] = weight
                graph[nodes[j]][nodes[i]] = weight

    return graph


def run_performance_tests():
    sizes = [10, 50, 100, 200]
    results = []

    for size in sizes:
        parcels = generate_parcels(size)
        graph = generate_graph(size)

        _, sort_time = measure_time(merge_sort, parcels)

        _, knapsack_time = measure_time(
            knapsack, parcels, 20
        )

        start_node = "L0"

        _, dijkstra_time = measure_time(
            dijkstra, graph, start_node
        )

        distances = {}

        for node in graph:
            distances[node], _ = dijkstra(graph, node)

        _, tsp_time = measure_time(
            nearest_neighbor_tsp,
            distances,
            start_node
        )

        results.append([
            size,
            sort_time,
            knapsack_time,
            dijkstra_time,
            tsp_time
        ])

        print(f"\nDataset size: {size}")
        print(f"Sorting:   {sort_time:.6f} seconds")
        print(f"Knapsack:  {knapsack_time:.6f} seconds")
        print(f"Dijkstra:  {dijkstra_time:.6f} seconds")
        print(f"TSP:       {tsp_time:.6f} seconds")

    os.makedirs("results", exist_ok=True)

    with open("results/test_results.csv", "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow([
            "Dataset Size",
            "Merge Sort",
            "Knapsack",
            "Dijkstra",
            "Nearest Neighbor TSP"
        ])

        writer.writerows(results)

    print("\nPerformance results saved successfully!")


if __name__ == "__main__":
    run_performance_tests()
