class FenwickTree:
    def __init__(self, arr: list):
        self.size = len(arr)
        self.tree = [0] * (self.size + 1)
        for i, val in enumerate(arr):
            self.update(i + 1, val)
    def update(self, idx: int, val: int) -> None:
        if idx <= 0 or idx > self.size:
            raise IndexError('Index out of bounds')
        while idx <= self.size:
            self.tree[idx] += val
            idx += idx & (-idx)
    def query(self, idx: int) -> int:
        if idx < 0 or idx > self.size:
            raise IndexError('Index out of bounds')
        total = 0
        while idx > 0:
            total += self.tree[idx]
            idx -= idx & (-idx)
        return total
    def range_query(self, l: int, r: int) -> int:
        return self.query(r) - self.query(l - 1)

# Commit updates step 8 for robustness
