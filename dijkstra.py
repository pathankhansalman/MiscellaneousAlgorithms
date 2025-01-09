import heapq
from typing import Dict, Any

def dijkstra(graph: Dict[Any, Dict[Any, float]], start: Any) -> Dict[Any, float]:
    """
    Computes the shortest paths from start node to all other nodes in a weighted graph.
    Uses a priority queue (min-heap) for efficiency.
    """
    distances = {node: float('inf') for node in graph}
    distances[start] = 0.0
    pq = [(0.0, start)]
    while pq:
        dist, node = heapq.heappop(pq)
        if dist > distances[node]:
            continue
        for neighbor, weight in graph[node].items():
            new_dist = dist + weight
            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor))
    return distances

# Commit updates step 3 for robustness
