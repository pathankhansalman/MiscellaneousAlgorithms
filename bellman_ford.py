from typing import List, Tuple

def bellman_ford(graph: List[Tuple[int, int, float]], num_vertices: int, start: int) -> List[float]:
    if num_vertices <= 0:
        return []
    distances = [float('inf')] * num_vertices
    distances[start] = 0.0
    for _ in range(num_vertices - 1):
        updated = False
        for u, v, w in graph:
            if distances[u] != float('inf') and distances[u] + w < distances[v]:
                distances[v] = distances[u] + w
                updated = True
        if not updated:
            break
    for u, v, w in graph:
        if distances[u] != float('inf') and distances[u] + w < distances[v]:
            raise ValueError("Graph contains negative weight cycle detectable via relaxation")
    return distances

# Commit updates step 8 for robustness
