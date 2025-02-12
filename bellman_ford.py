from typing import List, Tuple

def bellman_ford(graph: List[Tuple[int, int, float]], num_vertices: int, start: int) -> List[float]:
    """
    Bellman-Ford algorithm finds shortest paths from a single source vertex to all of the other vertices
    in a weighted directed graph. It handles graphs with negative weights and detects negative weight cycles.
    """
    distances = [float('inf')] * num_vertices
    distances[start] = 0.0
    for _ in range(num_vertices - 1):
        for u, v, w in graph:
            if distances[u] + w < distances[v]:
                distances[v] = distances[u] + w
    for u, v, w in graph:
        if distances[u] + w < distances[v]:
            raise ValueError("Graph contains a negative weight cycle")
    return distances

# Commit updates step 4 for robustness
