class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        i, j, k = 0, len(nums) - 2, len(nums) - 1
        while i < j or i < k:
            if i % 2 == nums[i] % 2:
                i += 1
            elif i % 2:
                nums[i], nums[j] = nums[j], nums[i]
                j -= 2
            else:
                nums[i], nums[k] = nums[k], nums[i]
                k -= 2
        return nums