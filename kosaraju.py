# -*- coding: utf-8 -*-
"""
Created on Sat Jun 06 2026

@author: Antigravity
"""

from typing import List, Dict, Set

def get_transpose(graph: Dict[int, List[int]], num_vertices: int) -> Dict[int, List[int]]:
    """
    Creates the transpose of a directed graph (reverses all edges).
    """
    transposed = {i: [] for i in range(num_vertices)}
    for u in graph:
        for v in graph[u]:
            transposed[v].append(u)
    return transposed

def fill_order(u: int, graph: Dict[int, List[int]], visited: Set[int], stack: List[int]) -> None:
    """
    Fills the stack with vertices ordered by their finishing times in DFS.
    """
    visited.add(u)
    for neighbor in graph.get(u, []):
        if neighbor not in visited:
            fill_order(neighbor, graph, visited, stack)
    stack.append(u)

def dfs_collect(u: int, transposed_graph: Dict[int, List[int]], visited: Set[int], component: List[int]) -> None:
    """
    Runs DFS on the transposed graph to collect all reachable vertices in the component.
    """
    visited.add(u)
    component.append(u)
    for neighbor in transposed_graph.get(u, []):
        if neighbor not in visited:
            dfs_collect(neighbor, transposed_graph, visited, component)

def kosaraju_scc(graph: Dict[int, List[int]], num_vertices: int) -> List[List[int]]:
    """
    Finds Strongly Connected Components (SCCs) of a directed graph using Kosaraju's algorithm.
    
    Args:
        graph: Adjacency list representation of the directed graph (keys are vertex indices).
        num_vertices: The number of vertices in the graph.
        
    Returns:
        A list of lists, where each inner list represents a Strongly Connected Component.
    """
    # Step 1: Order vertices by finishing time
    stack: List[int] = []
    visited: Set[int] = set()
    
    for i in range(num_vertices):
        if i not in visited:
            fill_order(i, graph, visited, stack)
            
    # Step 2: Transpose the graph
    transposed = get_transpose(graph, num_vertices)
    
    # Step 3: Process all vertices in order defined by stack
    visited.clear()
    sccs: List[List[int]] = []
    
    while stack:
        u = stack.pop()
        if u not in visited:
            component: List[int] = []
            dfs_collect(u, transposed, visited, component)
            sccs.append(component)
            
    return sccs

if __name__ == "__main__":
    # Test Graph:
    # 5 vertices (0 to 4)
    # Edges:
    # 1 -> 0
    # 0 -> 2
    # 2 -> 1
    # 0 -> 3
    # 3 -> 4
    num_v = 5
    test_graph = {
        0: [2, 3],
        1: [0],
        2: [1],
        3: [4],
        4: []
    }
    
    print("Running Kosaraju's SCC algorithm test...")
    components = kosaraju_scc(test_graph, num_v)
    print("Strongly Connected Components found:")
    for idx, scc in enumerate(components):
        print(f"Component {idx + 1}: {scc}")
