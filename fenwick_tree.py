class FenwickTree:
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (size + 1)
        
    def update(self, idx, val):
        while idx <= self.size:
            self.tree[idx] += val
            idx += idx & (-idx)
            
    def query(self, idx):
        total = 0
        while idx > 0:
            total += self.tree[idx]
            idx -= idx & (-idx)
        return total

# Commit updates step 2 for robustness
