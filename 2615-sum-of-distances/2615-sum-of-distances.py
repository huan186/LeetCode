class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        indices = defaultdict(list)
        for i, num in enumerate(nums):
            indices[num].append(i)
        n = len(nums)
        res = [0] * n
        for idx in indices.values():
            m = len(idx)
            d = sum(idx) - idx[0] * m
            res[idx[0]] = d
            for i in range(1, m):
                d += (2 * i - m) * (idx[i] - idx[i - 1])
                res[idx[i]] = d
        return res