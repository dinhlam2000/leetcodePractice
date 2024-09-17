from collections import defaultdict
import heapq

def bestSumKStar(g_from, g_to, values, k):
    # Step 1: Construct the graph
    graph = defaultdict(set)

    for u, v in zip(g_from, g_to):
        graph[u].add(v)
        graph[v].add(u)

    # Step 2: Calculate k-star sums with optimized approach
    max_sum = float('-inf')

    # Iterate over each node
    for node in graph:
        # Get all neighbors' values
        neighbors = list(graph[node])
        neighbor_values = [values[n] for n in neighbors]

        # If there are no neighbors, consider only the node itself
        if not neighbor_values:
            max_sum = max(max_sum, values[node])
            continue

        # Use a max-heap to get the top k neighbors
        heapq.heapify(neighbor_values)
        current_sum = values[node]
        largest_neighbors_sum = current_sum

        # Aggregate contributions by keeping top k neighbors
        for i in range(min(len(neighbor_values), k)):
            largest_neighbors_sum += heapq.nlargest(i + 1, neighbor_values)[-1]
            max_sum = max(max_sum, largest_neighbors_sum)

    return max_sum

# Example usage
g_from = [0, 1, 1, 3, 3, 4]
g_to = [1, 2, 3, 4, 5, 1]
values = [-3, -2, -3, -4, -5, -6]
k = 3

print(bestSumKStar(g_from, g_to, values, k))  # Output should be the maximum k-star sum
