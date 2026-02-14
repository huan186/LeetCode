class Solution:
    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        res = 1
        cnt = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                cnt = 1
            else:
                cnt += 1
            res += cnt
        return res