import heapq

def astar(graph, start, goal, heuristic):
    pq = [(0 + heuristic(start, goal), 0, start, [])]
    visited = set()
    while pq:
        f, g, current, path = heapq.heappop(pq)
        if current == goal: return path + [current]
        if current in visited: continue
        visited.add(current)
        for neighbor, cost in graph[current].items():
            heapq.heappush(pq, (g + cost + heuristic(neighbor, goal), g + cost, neighbor, path + [current]))

# Commit updates step 2 for robustness
