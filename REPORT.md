
# MINI COURIER PLANNER
## Design and Analysis of Algorithms – Capstone Project Report

## 1. Introduction

Mini Courier Planner is a Python-based application designed to improve parcel selection and courier delivery planning.

The system combines sorting, dynamic programming, graph algorithms, and route optimization to generate an efficient delivery plan.

## 2. Problem Statement

Courier services need to prioritize parcels according to delivery deadlines while ensuring that the total parcel weight does not exceed the vehicle's capacity.

They also need to determine efficient routes between delivery locations to reduce total travel distance.

This project addresses these problems by integrating multiple algorithms into one application.

## 3. Objectives

- Prioritize parcels based on delivery deadlines.
- Select valuable parcels within vehicle capacity.
- Find shortest paths between delivery locations.
- Generate an approximate optimized delivery route.
- Measure algorithm execution time.
- Compare performance for different input sizes.

## 4. System Configuration

- Programming Language: Python
- Data Storage: JSON files
- Vehicle Capacity: 20 kg
- Warehouse Location: W
- Test Dataset Sizes: 10, 50, 100, 200

## 5. Algorithms Implemented

### 5.1 Merge Sort

Used to sort parcels according to their delivery deadlines.

Time Complexity: O(n log n)

### 5.2 0/1 Knapsack

Used to select parcels while keeping the total weight within vehicle capacity.

Dynamic Programming is used to maximize the total selected parcel value.

Time Complexity: O(n × W), where W is the capacity.

### 5.3 Dijkstra's Algorithm

Used to calculate shortest distances between locations in the road network.

The implementation uses a priority queue.

Time Complexity: O((V + E) log V) with a binary heap and adjacency list.

### 5.4 Nearest Neighbor TSP

Used to generate an approximate delivery route by repeatedly visiting the nearest unvisited destination.

The route returns to the warehouse after visiting all selected destinations.

Time Complexity: O(k²) for k locations in the distance matrix.

## 6. Dataset Description

The project contains two JSON datasets.

### Parcels

Each parcel contains:

- Parcel ID
- Customer
- Destination
- Weight
- Value
- Delivery deadline
- Priority

### Locations

The location dataset contains:

- Warehouse
- Vehicle capacity
- Delivery locations
- Road connections
- Distances between locations

## 7. Implementation Results

### Parcel Prioritization

The parcels were sorted in the following order:

| Parcel ID | Deadline |
|---|---|
| P104 | 10:00 |
| P102 | 11:00 |
| P101 | 12:00 |
| P103 | 14:00 |
| P105 | 15:00 |

### Optimal Packing

| Parcel ID | Weight | Value |
|---|---:|---:|
| P104 | 6 kg | Rs. 1200 |
| P102 | 8 kg | Rs. 1500 |
| P101 | 5 kg | Rs. 1000 |
| **Total** | **19 kg** | **Rs. 3700** |

Vehicle Capacity: 20 kg

### Shortest Path Results

The shortest distances from warehouse W were:

| Destination | Distance |
|---|---:|
| W | 0 km |
| A | 4 km |
| B | 7 km |
| C | 9 km |
| D | 6 km |

### Optimized Delivery Route

W → A → B → D → W

Total Route Distance: 17 km

## 8. Performance Analysis

The algorithms were tested using four different dataset sizes.

| Dataset Size | Merge Sort (s) | Knapsack (s) | Dijkstra (s) | Nearest Neighbor TSP (s) |
|---:|---:|---:|---:|---:|
| 10 | 0.000018 | 0.000067 | 0.000029 | 0.000023 |
| 50 | 0.000090 | 0.000241 | 0.000176 | 0.000173 |
| 100 | 0.000167 | 0.000391 | 0.000454 | 0.000423 |
| 200 | 0.000230 | 0.000462 | 0.000805 | 0.001196 |

Execution times are measured in seconds and may vary between runs and systems.

The project generates separate runtime charts for all four algorithms.

## 9. Conclusion

The Mini Courier Planner successfully integrates four important algorithmic techniques into a single application.

It prioritizes parcels, selects packages within vehicle capacity, calculates shortest paths, and generates an approximate delivery route.

Performance testing was conducted at multiple dataset sizes, and runtime charts were generated to compare algorithm execution times.

The project demonstrates the practical application of Design and Analysis of Algorithms in courier delivery planning.

## 10. Future Scope

- Add a graphical user interface.
- Integrate real map and GPS data.
- Support multiple delivery vehicles.
- Include live traffic information.
- Add database storage.
- Improve route optimization for larger delivery networks.
