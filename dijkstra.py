import heapq
import time
from typing import Dict, Any

class NegativeWeightException(Exception):
    pass

def dijkstra(graph: Dict[Any, Dict[Any, float]], start: Any) -> Dict[Any, float]:
    for node in graph:
        for neighbor, w in graph[node].items():
            if w < 0:
                raise NegativeWeightException('Dijkstra does not support negative weights')
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

# Commit updates step 6 for robustness
