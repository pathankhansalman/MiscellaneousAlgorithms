# Dijkstra's Algorithm implementation
# Time Complexity: O((V + E) log V) using Binary Heap
# Space Complexity: O(V) to store distances and priority queue
import heapq
from typing import Dict, Any

def dijkstra(graph: Dict[Any, Dict[Any, float]], start: Any) -> Dict[Any, float]:
    distances = {node: float('inf') for node in graph}
    distances[start] = 0.0
    pq = [(0.0, start)]
    while pq:
        dist, node = heapq.heappop(pq)
        if dist > distances[node]: continue
        for neighbor, weight in graph[node].items():
            new_dist = dist + weight
            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor))
    return distances

# Commit updates step 7 for robustness
