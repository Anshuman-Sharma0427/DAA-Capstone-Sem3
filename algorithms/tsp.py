
def nearest_neighbor_tsp(distance_matrix, start):
    unvisited = set(distance_matrix.keys())
    unvisited.remove(start)

    route = [start]
    total_distance = 0
    current = start

    while unvisited:
        next_city = min(
            unvisited,
            key=lambda city: distance_matrix[current][city]
        )

        total_distance += distance_matrix[current][next_city]

        route.append(next_city)
        unvisited.remove(next_city)
        current = next_city

    # Return to warehouse
    total_distance += distance_matrix[current][start]
    route.append(start)

    return route, total_distance
