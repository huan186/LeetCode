class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        s = sum(nums)
        count = Counter(nums)
        res = float('-inf')
        for a in count:
            b = s - 2 * a
            if b in count:
                if a != b or count[a] >= 2:
                    res = max(res, b)
        return res