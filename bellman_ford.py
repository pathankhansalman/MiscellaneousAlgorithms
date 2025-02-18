from typing import List, Tuple

def bellman_ford(graph: List[Tuple[int, int, float]], num_vertices: int, start: int) -> List[float]:
    distances = [float('inf')] * num_vertices
    distances[start] = 0.0
    # Relax vertices N-1 times
    for _ in range(num_vertices - 1):
        for u, v, w in graph:
            if distances[u] != float('inf') and distances[u] + w < distances[v]:
                distances[v] = distances[u] + w
    # Detect negative weight cycle
    for u, v, w in graph:
        if distances[u] != float('inf') and distances[u] + w < distances[v]:
            raise ValueError("Graph contains a negative weight cycle")
    return distances

# Commit updates step 6 for robustness
