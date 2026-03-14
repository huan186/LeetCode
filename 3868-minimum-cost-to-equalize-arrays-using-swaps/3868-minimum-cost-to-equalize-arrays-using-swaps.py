class Solution:
    def minCost(self, nums1: list[int], nums2: list[int]) -> int:
        f1, f2 = Counter(nums1), Counter(nums2)
        f1.subtract(f2)
        res = 0
        for f in f1.values():
            if f % 2 == 1:
                return -1
            if f > 0:
                res += f // 2
        return res