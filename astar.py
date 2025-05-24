import heapq
from typing import Dict, List, Any, Callable

def astar(graph: Dict[Any, Dict[Any, float]], start: Any, goal: Any, heuristic: Callable[[Any, Any], float]) -> List[Any]:
    if start not in graph or goal not in graph:
        return []
    pq = [(heuristic(start, goal), 0.0, start, [])]
    g_score = {start: 0.0}
    visited = set()
    while pq:
        f, g, current, path = heapq.heappop(pq)
        if current in visited: continue
        if current == goal:
            return path + [current]
        visited.add(current)
        for neighbor, cost in graph[current].items():
            tentative_g = g + cost
            if neighbor not in g_score or tentative_g < g_score[neighbor]:
                g_score[neighbor] = tentative_g
                f_score = tentative_g + heuristic(neighbor, goal)
                heapq.heappush(pq, (f_score, tentative_g, neighbor, path + [current]))
    return []

# Commit updates step 8 for robustness
