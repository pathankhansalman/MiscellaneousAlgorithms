class DisjointSetUnion:
    """
    Disjoint Set Union (DSU) or Union-Find data structure.
    Implements path compression and union-by-rank.
    """
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, i):
        """
        Finds the representative of the set containing i.
        Applies path compression.
        """
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        """
        Unites the set containing i and the set containing j.
        Returns True if a union occurred (they were in different sets), 
        and False otherwise.
        """
        root_i = self.find(i)
        root_j = self.find(j)
        
        if root_i != root_j:
            # Union by rank
            if self.rank[root_i] < self.rank[root_j]:
                self.parent[root_i] = root_j
            elif self.rank[root_i] > self.rank[root_j]:
                self.parent[root_j] = root_i
            else:
                self.parent[root_j] = root_i
                self.rank[root_i] += 1
            return True
        return False


def kruskal(num_vertices, edges):
    """
    Finds the Minimum Spanning Tree (MST) of a connected, undirected graph.
    
    Parameters:
    - num_vertices: The number of vertices in the graph (0 to num_vertices-1).
    - edges: A list of tuples (u, v, weight) representing undirected edges.
    
    Returns:
    - A tuple (mst_edges, total_weight) where mst_edges is the list of edges
      included in the MST, and total_weight is the sum of their weights.
    """
    # Sort edges in non-decreasing order of their weight
    sorted_edges = sorted(edges, key=lambda edge: edge[2])
    
    dsu = DisjointSetUnion(num_vertices)
    mst_edges = []
    total_weight = 0
    
    for u, v, weight in sorted_edges:
        # If u and v belong to different sets, add edge to MST
        if dsu.union(u, v):
            mst_edges.append((u, v, weight))
            total_weight += weight
            
            # Optimization: Stop early if we have included V-1 edges
            if len(mst_edges) == num_vertices - 1:
                break
                
    return mst_edges, total_weight


if __name__ == "__main__":
    print("Running Kruskal's MST tests...")
    
    # Test Case 1: Simple 4-vertex graph
    # Vertices: 0, 1, 2, 3
    # Edges: (0-1: 10), (0-2: 6), (0-3: 5), (1-3: 15), (2-3: 4)
    num_vertices1 = 4
    edges1 = [
        (0, 1, 10),
        (0, 2, 6),
        (0, 3, 5),
        (1, 3, 15),
        (2, 3, 4)
    ]
    mst1, weight1 = kruskal(num_vertices1, edges1)
    
    # Expected MST weight: 5 (0-3) + 4 (2-3) + 10 (0-1) = 19
    assert weight1 == 19, f"Expected weight 19, got {weight1}"
    assert len(mst1) == 3, f"Expected 3 edges, got {len(mst1)}"
    
    # Test Case 2: Disconnected graph components (not fully connected, should return spanning forest)
    num_vertices2 = 3
    edges2 = [
        (0, 1, 5)
    ]
    mst2, weight2 = kruskal(num_vertices2, edges2)
    assert weight2 == 5
    assert len(mst2) == 1
    
    # Test Case 3: Complete triangle graph
    num_vertices3 = 3
    edges3 = [
        (0, 1, 1),
        (1, 2, 2),
        (0, 2, 3)
    ]
    mst3, weight3 = kruskal(num_vertices3, edges3)
    assert weight3 == 3  # Should pick (0-1: 1) and (1-2: 2)
    
    print("All Kruskal's MST tests passed successfully!")
