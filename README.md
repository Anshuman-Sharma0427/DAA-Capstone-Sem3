
# Mini Courier Planner

## Project Overview

Mini Courier Planner is a Python-based courier delivery optimization system developed as a DAA (Design and Analysis of Algorithms) capstone project.

The application helps a courier service prioritize parcels, select packages according to vehicle capacity, calculate shortest paths, and generate an optimized delivery route.

## Features

1. Parcel prioritization using Merge Sort.
2. Optimal parcel selection using Dynamic Programming (0/1 Knapsack).
3. Shortest path calculation using Dijkstra's Algorithm.
4. Delivery route optimization using Nearest Neighbor TSP.
5. Performance analysis for different dataset sizes.
6. Runtime charts for all four algorithms.
7. Menu-driven command-line interface.

## Algorithms Used

| Algorithm | Application |
|---|---|
| Merge Sort | Sort parcels by delivery deadline |
| 0/1 Knapsack | Select parcels within vehicle capacity |
| Dijkstra | Calculate shortest paths between locations |
| Nearest Neighbor TSP | Generate an approximate delivery route |

## Technologies

- Python 3
- JSON
- Pandas
- Matplotlib

## Project Structure

```text
Mini-Courier-Planner/
│
├── algorithms/
│   ├── sorting.py
│   ├── knapsack.py
│   ├── dijkstra.py
│   └── tsp.py
│
├── data/
│   ├── parcels.json
│   └── locations.json
│
├── utilities/
│   └── performance.py
│
├── results/
│   ├── test_results.csv
│   ├── merge_sort.png
│   ├── knapsack.png
│   ├── dijkstra.png
│   └── nearest_neighbor_tsp.png
│
├── screenshots/
│
├── main.py
├── generate_chart.py
├── requirements.txt
├── design.md
├── flowchart.md
└── README.md
```

## Installation

Clone the repository:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

Navigate into the project folder:

```bash
cd Mini-Courier-Planner
```

Install dependencies:

```bash
python3 -m pip install -r requirements.txt
```

## Run the Application

```bash
python3 main.py
```

## Application Menu

1. Display All Parcels
2. Sort Parcels by Deadline
3. Generate Optimal Packing Plan
4. Find Shortest Paths
5. Generate Optimized Delivery Route
6. Run Complete Courier Plan
7. Run Performance Analysis
0. Exit

## Sample Results

Vehicle Capacity: 20 kg

Selected Parcels:

- P104: 6 kg
- P102: 8 kg
- P101: 5 kg

Total Selected Weight: 19 kg

Total Parcel Value: Rs. 3700

Optimized Delivery Route:

W -> A -> B -> D -> W

Total Route Distance: 17 km

## Performance Testing

The algorithms were tested with datasets containing:

- 10 records
- 50 records
- 100 records
- 200 records

Runtime results are saved in:

`results/test_results.csv`

Performance charts are saved in the `results` directory.

To regenerate the charts:

```bash
python3 generate_chart.py
```

## Project Objective

The objective of this project is to combine multiple DAA concepts into one practical courier planning application and analyze their execution performance.

## Author

B.Tech CSE (AI & ML)

DAA Capstone Project
