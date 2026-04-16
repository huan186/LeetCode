class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        indices = defaultdict(list)
        for i, num in enumerate(nums):
            indices[num].append(i)
        n = len(nums)
        def min_dist(a, b):
            return min(a - b, n - a + b) if a >= b else min(b - a, n + a - b)
        res = [-1] * len(queries)
        for i, q in enumerate(queries):
            num = nums[q]
            idx = indices[num]
            m = len(idx)
            if m <= 1:
                continue
            k = bisect.bisect_left(idx, q)
            res[i] = min(min_dist(q, idx[k - 1]), min_dist(q, idx[(k + 1) % m]))
        return res