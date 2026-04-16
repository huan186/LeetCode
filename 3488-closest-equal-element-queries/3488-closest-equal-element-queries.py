class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:        
        n = len(nums)
        pos = defaultdict(list)

        for i, v in enumerate(nums):
            pos[v].append(i)

        ans = [-1] * n

        for v, idx in pos.items():
            m = len(idx)
            if m == 1:
                continue
            for i in range(m):
                left = idx[i - 1]
                right = idx[(i + 1) % m]
                cur = idx[i]
                d1 = abs(cur - left)
                d2 = abs(cur - right)
                ans[cur] = min(min(d1, n - d1), min(d2, n - d2))

        return [ans[q] for q in queries]