class SegmentTree:
    def __init__(self, arr):
        self.arr = arr
        self.tree = [0] * (4 * len(arr))
        self.lazy = [0] * (4 * len(arr))
        self.build(1, 0, len(arr) - 1)

    def build(self, node, start, end):
        if start == end:
            self.tree[node] = self.arr[start]
        else:
            mid = (start + end) // 2
            self.build(2 * node, start, mid)
            self.build(2 * node + 1, mid + 1, end)
            self.tree[node] = min(self.tree[2 * node], self.tree[2 * node + 1])

    def update(self, node, start, end, left, right, value):
        if self.lazy[node] != 0:
            self.tree[node] += self.lazy[node]
            if start != end:
                self.lazy[2 * node] += self.lazy[node]
                self.lazy[2 * node + 1] += self.lazy[node]
            self.lazy[node] = 0

        if start > end or start > right or end < left:
            return

        if left <= start and end <= right:
            self.tree[node] += value
            if start != end:
                self.lazy[2 * node] += value
                self.lazy[2 * node + 1] += value
            return

        mid = (start + end) // 2
        self.update(2 * node, start, mid, left, right, value)
        self.update(2 * node + 1, mid + 1, end, left, right, value)
        self.tree[node] = min(self.tree[2 * node], self.tree[2 * node + 1])

    def query(self, node, start, end, left, right):
        if start > end or start > right or end < left:
            return float('inf')

        if self.lazy[node] != 0:
            self.tree[node] += self.lazy[node]
            if start != end:
                self.lazy[2 * node] += self.lazy[node]
                self.lazy[2 * node + 1] += self.lazy[node]
            self.lazy[node] = 0

        if left <= start and end <= right:
            return self.tree[node]

        mid = (start + end) // 2
        left_min = self.query(2 * node, start, mid, left, right)
        right_min = self.query(2 * node + 1, mid + 1, end, left, right)
        return min(left_min, right_min)


# Чтение входных данных
n, q = map(int, input().split())
arr = list(map(int, input().split()))

segment_tree = SegmentTree(arr)

for _ in range(q):
    query_type, l, r, x = input().split()
    l, r, x = int(l), int(r), int(x)
    if query_type == "?":
        result = segment_tree.query(1, 0, n - 1, l - 1, r - 1)
        print(result)
    else:
        segment_tree.update(1, 0, n - 1, l - 1, r - 1, x)

