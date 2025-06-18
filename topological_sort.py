from typing import Dict, List, Any

def topological_sort(graph: Dict[Any, List[Any]]) -> List[Any]:
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

if __name__ == '__main__':
    g = {'A': ['B', 'C'], 'B': ['D'], 'C': ['D'], 'D': []}
    print(topological_sort(g))

# Commit updates step 6 for robustness
