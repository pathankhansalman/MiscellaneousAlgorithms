class FenwickTree:
    def __init__(self, arr: list):
        self.size = len(arr)
        self.tree = [0] + list(arr)
        for i in range(1, self.size + 1):
            parent = i + (i & -i)
            if parent <= self.size:
                self.tree[parent] += self.tree[i]
    def update(self, idx: int, val: int) -> None:
        while idx <= self.size:
            self.tree[idx] += val
            idx += idx & (-idx)
    def query(self, idx: int) -> int:
        total = 0
        while idx > 0:
            total += self.tree[idx]
            idx -= idx & (-idx)
        return total
    def range_query(self, l: int, r: int) -> int:
        return self.query(r) - self.query(l - 1)

# Commit updates step 9 for robustness
