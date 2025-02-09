from typing import List, Tuple

def bellman_ford(graph: List[Tuple[int, int, float]], num_vertices: int, start: int) -> List[float]:
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

# Commit updates step 3 for robustness
