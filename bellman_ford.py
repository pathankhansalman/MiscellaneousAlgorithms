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

if __name__ == '__main__':
    edges = [(0, 1, -1), (0, 2, 4), (1, 2, 3), (1, 3, 2), (1, 4, 2), (3, 2, 5), (3, 1, 1), (4, 3, -3)]
    print(bellman_ford(edges, 5, 0))

# Commit updates step 5 for robustness
