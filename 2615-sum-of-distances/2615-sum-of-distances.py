class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        indices = defaultdict(list)
        for i, num in enumerate(nums):
            indices[num].append(i)
        n = len(nums)
        res = [0] * n
        for num, idx in indices.items():
            m = len(idx)
            d = sum(idx) - idx[0] * m
            for i in range(m - 1):
                res[idx[i]] = d
                d += (2 * i + 2 - m) * (idx[i + 1] - idx[i])
            res[idx[-1]] = d
        return res