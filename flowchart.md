
flowchart TD
    A([Start]) --> B[Load Parcel and Location Data]
    B --> C[Sort Parcels using Merge Sort]
    C --> D[Apply 0/1 Knapsack DP]
    D --> E[Select Parcels within Vehicle Capacity]
    E --> F[Extract Unique Delivery Locations]
    F --> G[Build Weighted Graph]
    G --> H[Apply Dijkstra for Shortest Paths]
    H --> I[Apply Nearest Neighbor TSP]
    I --> J[Calculate Total Route Distance]
    J --> K[Measure Algorithm Execution Times]
    K --> L[Display Packing Plan and Delivery Route]
    L --> M([End])
