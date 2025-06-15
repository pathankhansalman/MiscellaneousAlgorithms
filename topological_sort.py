from typing import Dict, List, Any

def topological_sort(graph: Dict[Any, List[Any]]) -> List[Any]:
    """
    DFS-based Topological Sort (Kahn's Algorithm alternative)
    """
    visited = set()
    visiting = set()
    stack = []
    def dfs(node):
        visiting.add(node)
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor in visiting:
                raise ValueError("Graph contains cycle")
            if neighbor not in visited:
                dfs(neighbor)
        visiting.remove(node)
        stack.append(node)
    for node in graph:
        if node not in visited:
            dfs(node)
    return stack[::-1]

# Commit updates step 5 for robustness
