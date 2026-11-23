# Mini-Courier Planner

## 1. Project Overview
Mini-Courier Planner is a Python-based application designed to optimize parcel selection and courier delivery routes. It combines sorting, Dynamic Programming, graph algorithms and approximation techniques.

## 2. Problem Definition
The courier company has multiple parcels, a vehicle with limited carrying capacity and multiple customer delivery locations. The system must prioritize parcels, select the best combination of parcels and generate an efficient delivery route.

## 3. Parcel Attributes
Each parcel contains:
- Parcel ID
- Customer Name
- Destination
- Weight
- Parcel Value
- Delivery Deadline
- Priority

## 4. Vehicle Details
- Maximum Capacity: 20 kg
- Starting Location: Warehouse
- Ending Location: Warehouse

## 5. Algorithms Used

### Merge Sort
Used to sort parcels according to their delivery deadlines in ascending order.

### 0/1 Knapsack using Dynamic Programming
Used to select the combination of parcels that maximizes total parcel value without exceeding vehicle capacity.

### Dijkstra's Algorithm
Used to calculate shortest paths between the warehouse and customer locations.

### Nearest Neighbor TSP Approximation
Used to generate an approximate delivery route that visits all selected delivery locations and returns to the warehouse.

## 6. Graph Representation
The delivery network is represented as an undirected weighted graph using an adjacency list. Each edge represents a road, and its weight represents distance in kilometres.

## 7. Performance Analysis
The execution time of sorting, knapsack, Dijkstra and TSP algorithms will be measured using Python's time module. Different dataset sizes will be tested.

## 8. Expected Outcome
The application will display prioritized parcels, an optimized packing plan, shortest paths, delivery route, total route distance and algorithm execution times.