class Solution:
    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        i, n = 0, len(nums)
        res = 0
        while i < n:
            j = i
            while j + 1 < n and nums[j + 1] != nums[j]:
                j += 1
            l = j - i + 1
            res += l * (l + 1) // 2
            i = j + 1
        return res