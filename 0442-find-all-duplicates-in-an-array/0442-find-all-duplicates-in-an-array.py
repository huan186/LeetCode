class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        i, n = 0, len(nums)
        while i < n:
            j = nums[i] - 1
            if j == -1 or i == j:
                i += 1
            elif nums[j] == nums[i]:
                res.append(nums[i])
                nums[i] = 0
                i += 1
            else:
                nums[i], nums[j] = nums[j], nums[i]
        return res
