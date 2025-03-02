# -*- coding: utf-8 -*-
"""
Created on Tue May 19 23:08:11 2026

@author: patha
"""

class HeldKarpOptimizer:
    def __init__(self, distance_matrix: list[list[int]]):
        self.matrix = distance_matrix
        self.n = len(distance_matrix)
        # DP table: memo[mask][u] stores min cost to visit subset 'mask' ending at node 'u'
        self.memo = {}

    def find_min_cost(self) -> int:
        # Start at node 0. The initial mask is (1 << 0) which is 1 (binary: 0001)
        return self._solve(1, 0)

    def _solve(self, mask: int, u: int) -> int:
        # Base Case: If all nodes have been visited (mask has all n bits set to 1)
        if mask == (1 << self.n) - 1:
            return self.matrix[u][0] if self.matrix[u][0] != 0 else float('inf')

        # Check memoization table to prevent redundant calculations
        if (mask, u) in self.memo:
            return self.memo[(mask, u)]

        min_cost = float('inf')

        # Try visiting all other unvisited nodes 'v'
        for v in range(self.n):
            # Check if node 'v' has NOT been visited yet using bitwise AND
            if not (mask & (1 << v)):
                # Transition: Mark node 'v' as visited using bitwise OR
                new_mask = mask | (1 << v)
                cost = self.matrix[u][v] + self._solve(new_mask, v)
                min_cost = min(min_cost, cost)

        self.memo[(mask, u)] = min_cost
        return min_cost

# Example Execution
if __name__ == "__main__":
    # A 4x4 network routing distance matrix
    network_graph = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]
    
    optimizer = HeldKarpOptimizer(network_graph)
    print(f"Optimal Network Routing Cost: {optimizer.find_min_cost()}") # Output: 80 (0->1->3->2->0)
