
import json

from algorithms.sorting import merge_sort
from algorithms.knapsack import knapsack
from algorithms.dijkstra import dijkstra, get_path
from algorithms.tsp import nearest_neighbor_tsp


def load_data():
    with open("data/parcels.json", "r") as file:
        parcels = json.load(file)

    with open("data/locations.json", "r") as file:
        locations = json.load(file)

    return parcels, locations


def build_graph(roads):
    graph = {}

    for source, destination, distance in roads:
        graph.setdefault(source, {})
        graph.setdefault(destination, {})

        graph[source][destination] = distance
        graph[destination][source] = distance

    return graph


def display_parcels():
    parcels, _ = load_data()

    print("\n========== ALL PARCELS ==========")

    for parcel in parcels:
        print(
            parcel["id"],
            "| Customer:", parcel["customer"],
            "| Destination:", parcel["destination"],
            "| Weight:", parcel["weight"], "kg",
            "| Value: Rs.", parcel["value"],
            "| Deadline:", parcel["deadline"],
            "| Priority:", parcel["priority"]
        )


def prioritize_parcels():
    parcels, _ = load_data()
    sorted_parcels = merge_sort(parcels)

    print("\n========== PARCEL PRIORITIZATION ==========")

    for parcel in sorted_parcels:
        print(
            parcel["id"],
            "| Deadline:", parcel["deadline"],
            "| Priority:", parcel["priority"]
        )


def packing_plan():
    parcels, locations = load_data()

    sorted_parcels = merge_sort(parcels)

    selected, total_weight, total_value, dp = knapsack(
        sorted_parcels,
        locations["vehicle_capacity"]
    )

    print("\n========== OPTIMAL PACKING PLAN ==========")

    if not selected:
        print("No parcels selected.")
        return

    for parcel in selected:
        print(
            parcel["id"],
            "| Destination:", parcel["destination"],
            "| Weight:", parcel["weight"], "kg",
            "| Value: Rs.", parcel["value"]
        )

    print("\nTotal Weight:", total_weight, "kg")
    print("Total Value: Rs.", total_value)
    print("Vehicle Capacity:", locations["vehicle_capacity"], "kg")


def shortest_paths():
    _, locations = load_data()

    graph = build_graph(locations["roads"])
    warehouse = locations["warehouse"]

    distances, previous = dijkstra(graph, warehouse)

    print("\n========== SHORTEST PATHS FROM WAREHOUSE ==========")

    for destination in graph:
        path = get_path(previous, warehouse, destination)

        print(
            warehouse, "->", destination,
            "| Path:", " -> ".join(path),
            "| Distance:", distances[destination], "km"
        )


def full_delivery_plan():
    parcels, locations = load_data()

    sorted_parcels = merge_sort(parcels)

    selected, total_weight, total_value, dp = knapsack(
        sorted_parcels,
        locations["vehicle_capacity"]
    )

    print("\n========== SELECTED DELIVERY PARCELS ==========")

    if not selected:
        print("No parcels selected. Delivery plan cannot be generated.")
        return

    destinations = sorted(set(
        parcel["destination"] for parcel in selected
    ))

    for parcel in selected:
        print(
            parcel["id"],
            "->", parcel["destination"],
            "|", parcel["weight"], "kg"
        )

    print("\nTotal Weight:", total_weight, "kg")
    print("Total Value: Rs.", total_value)

    graph = build_graph(locations["roads"])
    warehouse = locations["warehouse"]

    required_locations = [warehouse] + destinations

    distance_matrix = {}

    for location in required_locations:
        distances, previous = dijkstra(graph, location)
        distance_matrix[location] = {
            destination: distances[destination]
            for destination in required_locations
        }

    route, total_distance = nearest_neighbor_tsp(
        distance_matrix,
        warehouse
    )

    print("\n========== OPTIMIZED DELIVERY ROUTE ==========")
    print("Route:", " -> ".join(route))
    print("Total Distance:", total_distance, "km")


def performance_analysis():
    from utilities.performance import run_performance_tests

    print("\n========== PERFORMANCE ANALYSIS ==========")
    run_performance_tests()


def show_menu():
    while True:
        print("\n")
        print("=" * 45)
        print("       MINI COURIER PLANNER")
        print("=" * 45)
        print("1. Display All Parcels")
        print("2. Sort Parcels by Deadline")
        print("3. Generate Optimal Packing Plan")
        print("4. Find Shortest Paths")
        print("5. Generate Optimized Delivery Route")
        print("6. Run Complete Courier Plan")
        print("7. Run Performance Analysis")
        print("0. Exit")
        print("=" * 45)

        choice = input("Enter your choice: ").strip()

        try:
            if choice == "1":
                display_parcels()

            elif choice == "2":
                prioritize_parcels()

            elif choice == "3":
                packing_plan()

            elif choice == "4":
                shortest_paths()

            elif choice == "5":
                full_delivery_plan()

            elif choice == "6":
                full_delivery_plan()

            elif choice == "7":
                performance_analysis()

            elif choice == "0":
                print("\nThank you for using Mini Courier Planner!")
                break

            else:
                print("\nInvalid choice. Please enter a number from 0 to 7.")

        except (FileNotFoundError, KeyError, ValueError) as error:
            print("\nUnable to complete this operation:", error)


if __name__ == "__main__":
    show_menu()
