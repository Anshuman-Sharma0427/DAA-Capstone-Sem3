
import pandas as pd
import matplotlib.pyplot as plt

# Read performance results
data = pd.read_csv("results/test_results.csv")

algorithms = [
    "Merge Sort",
    "Knapsack",
    "Dijkstra",
    "Nearest Neighbor TSP"
]

for algorithm in algorithms:
    plt.figure(figsize=(8, 5))

    plt.plot(
        data["Dataset Size"],
        data[algorithm],
        marker="o",
        label=algorithm
    )

    plt.xlabel("Dataset Size")
    plt.ylabel("Execution Time (seconds)")
    plt.title(f"{algorithm} Performance Analysis")
    plt.legend()
    plt.grid(True)

    filename = algorithm.lower().replace(" ", "_")
    plt.savefig(f"results/{filename}.png")
    plt.close()

print("Runtime charts generated successfully!")
