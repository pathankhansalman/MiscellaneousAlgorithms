class FenwickTree:
    def __init__(self, size: int):
        self.size = size
        self.tree = [0] * (size + 1)
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

if __name__ == '__main__':
    ft = FenwickTree(5)
    ft.update(1, 3)
    ft.update(3, 5)
    print(ft.range_query(1, 3)) # Should be 8

# Commit updates step 5 for robustness
