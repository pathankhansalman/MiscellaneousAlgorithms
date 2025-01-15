import heapq
import time
from typing import Dict, Any

def dijkstra(graph: Dict[Any, Dict[Any, float]], start: Any) -> Dict[Any, float]:
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

if __name__ == '__main__':
    g = {'A': {'B': 1, 'C': 4}, 'B': {'C': 2, 'D': 6}, 'C': {'D': 3}, 'D': {}}
    t0 = time.perf_counter()
    res = dijkstra(g, 'A')
    t1 = time.perf_counter()
    print(f'Done in {t1-t0:.6f}s: {res}')

# Commit updates step 5 for robustness
