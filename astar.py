import heapq
from typing import Dict, List, Any, Callable

def astar(graph: Dict[Any, Dict[Any, float]], start: Any, goal: Any, heuristic: Callable[[Any, Any], float]) -> List[Any]:
    pq = [(heuristic(start, goal), 0.0, start, [])]
    g_score = {start: 0.0}
    visited = set()
    while pq:
        f, g, current, path = heapq.heappop(pq)
        if current == goal:
            return path + [current]
        if current in visited:
            continue
        visited.add(current)
        for neighbor, cost in graph[current].items():
            tentative_g = g + cost
            if neighbor not in g_score or tentative_g < g_score[neighbor]:
                g_score[neighbor] = tentative_g
                f_score = tentative_g + heuristic(neighbor, goal)
                heapq.heappush(pq, (f_score, tentative_g, neighbor, path + [current]))
    return []

if __name__ == '__main__':
    # Manhattan distance helper
    def manhattan(node, target):
        return abs(node[0] - target[0]) + abs(node[1] - target[1])
    grid_graph = {
        (0, 0): {(0, 1): 1, (1, 0): 1},
        (0, 1): {(0, 0): 1, (1, 1): 1},
        (1, 0): {(0, 0): 1, (1, 1): 1},
        (1, 1): {(0, 1): 1, (1, 0): 1}
    }
    print(astar(grid_graph, (0, 0), (1, 1), manhattan))

# Commit updates step 6 for robustness
