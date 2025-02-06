def bellman_ford(graph, num_vertices, start):
    distances = [float('inf')] * num_vertices
    distances[start] = 0
    for _ in range(num_vertices - 1):
        for u, v, w in graph:
            if distances[u] + w < distances[v]:
                distances[v] = distances[u] + w
    return distances

# Commit updates step 2 for robustness
