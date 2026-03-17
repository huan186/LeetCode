class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        s = sum(nums)
        count = Counter(nums)
        res = float('-inf')
        for b, f in count.items():
            if (s - b) % 2 != 0:
                continue
            a = (s - b) // 2
            if a == b and f >= 2 or a != b and a in count:
                res = max(res, b)
        return res