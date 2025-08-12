class SegmentTree:
    """Segment Tree for efficient range queries and point updates."""
    def __init__(self, data: list):
        self.n = len(data)
        self.tree = [0] * (4 * self.n)
        if self.n > 0:
            self.build(data, 0, 0, self.n - 1)

    def build(self, data: list, node: int, start: int, end: int):
        if start == end:
            self.tree[node] = data[start]
            return
        mid = (start + end) // 2
        left_child = 2 * node + 1
        right_child = 2 * node + 2
        
        self.build(data, left_child, start, mid)
        self.build(data, right_child, mid + 1, end)
        
        self.tree[node] = self.tree[left_child] + self.tree[right_child]

    def update(self, idx: int, val: int):
        """Updates the value at index idx to val."""
        self._update(0, 0, self.n - 1, idx, val)

    def _update(self, node: int, start: int, end: int, idx: int, val: int):
        if start == end:
            self.tree[node] = val
            return
        mid = (start + end) // 2
        left_child = 2 * node + 1
        right_child = 2 * node + 2
        
        if start <= idx <= mid:
            self._update(left_child, start, mid, idx, val)
        else:
            self._update(right_child, mid + 1, end, idx, val)
            
        self.tree[node] = self.tree[left_child] + self.tree[right_child]

    def query(self, L: int, R: int) -> int:
        """Queries the sum of range [L, R]."""
        return self._query(0, 0, self.n - 1, L, R)

    def _query(self, node: int, start: int, end: int, L: int, R: int) -> int:
        if R < start or end < L:
            return 0
        if L <= start and end <= R:
            return self.tree[node]
            
        mid = (start + end) // 2
        left_sum = self._query(2 * node + 1, start, mid, L, R)
        right_sum = self._query(2 * node + 2, mid + 1, end, L, R)
        return left_sum + right_sum

if __name__ == "__main__":
    arr = [1, 3, 5, 7, 9, 11]
    st = SegmentTree(arr)
    print("Sum of values in range [1, 3]:", st.query(1, 3)) # 3 + 5 + 7 = 15
    st.update(1, 10) # arr becomes [1, 10, 5, 7, 9, 11]
    print("Sum of values in range [1, 3] after update:", st.query(1, 3)) # 10 + 5 + 7 = 22
