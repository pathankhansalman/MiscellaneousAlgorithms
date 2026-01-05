# -*- coding: utf-8 -*-
"""
Created on Sat Jun 06 2026

@author: Antigravity
"""

import math
from typing import List, Tuple, Optional

def floyd_warshall(graph: List[List[float]]) -> Tuple[List[List[float]], List[List[Optional[int]]]]:
    """
    Computes all-pairs shortest paths using the Floyd-Warshall algorithm.
    
    Args:
        graph: A 2D adjacency matrix representing the graph. 
               graph[i][j] represents the weight of the directed edge from i to j.
               Use math.inf if there is no edge between i and j.
               Self-loops graph[i][i] should be initialized to 0.
               
    Returns:
        A tuple (dist, next_node) where:
        - dist: A 2D list representing the shortest distance between any pair of vertices.
        - next_node: A 2D list used for reconstructing paths. next_node[i][j] stores the 
                     next vertex on the shortest path from i to j. If no path exists, it is None.
                     
    Raises:
        ValueError: If a negative cycle is detected in the graph.
    """
    n = len(graph)
    
    # Initialize distance matrix and next node matrix for path reconstruction
    dist = [[graph[i][j] for j in range(n)] for i in range(n)]
    next_node = [[None for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if i != j and dist[i][j] != math.inf:
                next_node[i][j] = j

    # Core Floyd-Warshall DP step
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    next_node[i][j] = next_node[i][k]

    # Detect negative cycles: if dist[i][i] < 0, a negative cycle exists
    for i in range(n):
        if dist[i][i] < 0:
            raise ValueError("Graph contains a negative weight cycle.")
            
    return dist, next_node

def reconstruct_path(i: int, j: int, next_node: List[List[Optional[int]]]) -> List[int]:
    """
    Reconstructs the shortest path from vertex i to j using the next_node matrix.
    
    Args:
        i: Starting vertex.
        j: Target vertex.
        next_node: The next node pointer matrix returned by floyd_warshall.
        
    Returns:
        A list of vertices representing the path from i to j, or empty list if no path exists.
    """
    if next_node[i][j] is None:
        return []
    
    path = [i]
    while i != j:
        i = next_node[i][j]
        if i is None:
            return []
        path.append(i)
    return path

if __name__ == "__main__":
    # Test case: Directed graph with 4 vertices
    # Edge weights:
    # 0 -> 2 with weight -2
    # 2 -> 3 with weight 2
    # 3 -> 1 with weight -1
    # 1 -> 0 with weight 4
    # 1 -> 2 with weight 3
    INF = math.inf
    test_graph = [
        [0, INF, -2, INF],
        [4, 0, 3, INF],
        [INF, INF, 0, 2],
        [INF, -1, INF, 0]
    ]
    
    print("Running Floyd-Warshall algorithm test...")
    try:
        distances, paths = floyd_warshall(test_graph)
        
        print("\nDistance Matrix:")
        for r in distances:
            print([f"{x:4}" if x != INF else " INF" for x in r])
            
        print("\nShortest path reconstruction:")
        for u in range(len(test_graph)):
            for v in range(len(test_graph)):
                if u != v:
                    p = reconstruct_path(u, v, paths)
                    path_str = " -> ".join(map(str, p)) if p else "No Path"
                    print(f"Path {u} to {v}: {path_str} (Cost: {distances[u][v]})")
                    
    except ValueError as e:
        print(f"Error: {e}")
