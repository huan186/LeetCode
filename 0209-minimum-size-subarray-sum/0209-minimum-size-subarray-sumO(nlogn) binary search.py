class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if target > sum(nums):
            return 0
        pref_sum = [0]
        ans = len(nums)
        for i, num in enumerate(nums):
            pref_sum.append(pref_sum[i] + num)
            j = bisect.bisect_right(pref_sum, pref_sum[-1] - target)
            if j > 0:
                ans = min(ans, i - j + 2)
        return ans