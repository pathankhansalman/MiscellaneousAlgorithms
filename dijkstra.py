import heapq
from typing import Dict, Any

def dijkstra(graph: Dict[Any, Dict[Any, float]], start: Any) -> Dict[Any, float]:
    distances = {node: float('inf') for node in graph}
    distances[start] = 0.0
    pq = [(0.0, start)]
    visited = set()
    while pq:
        dist, node = heapq.heappop(pq)
        if node in visited: continue
        visited.add(node)
        for neighbor, weight in graph[node].items():
            if neighbor in visited: continue
            new_dist = dist + weight
            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor))
    return distances

# Commit updates step 8 for robustness
