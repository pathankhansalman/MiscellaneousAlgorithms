import heapq

def astar(graph, start, goal, heuristic):
    pq = [(heuristic(start, goal), 0, start, [])]
    g_score = {start: 0}
    visited = set()
    while pq:
        f, g, current, path = heapq.heappop(pq)
        if current == goal: return path + [current]
        if current in visited: continue
        visited.add(current)
        for neighbor, cost in graph[current].items():
            tentative_g = g + cost
            if neighbor not in g_score or tentative_g < g_score[neighbor]:
                g_score[neighbor] = tentative_g
                f_score = tentative_g + heuristic(neighbor, goal)
                heapq.heappush(pq, (f_score, tentative_g, neighbor, path + [current]))

# Commit updates step 3 for robustness
