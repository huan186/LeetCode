class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort(reverse=True)
        i, j, n = 0, 1, len(nums)
        res = 1
        while i < n - 1:
            while j < n and k >= 0 and nums[i] - nums[j] <= k:
                k -= nums[i] - nums[j]
                j += 1
            cnt = j - i
            k += (cnt - 1) * (nums[i] - nums[i + 1])
            res = max(res, cnt)
            i += 1
            if j <= i:
                j = i + 1
        return res