class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        min_idx = 0
        max_idx = 0
        
        for i in range(indexDifference, len(nums)):
            j = i - indexDifference

            if nums[j] < nums[min_idx]:
                min_idx = j
            if nums[j] > nums[max_idx]:
                max_idx = j
            
            if nums[max_idx] - nums[i] >= valueDifference:
                return [max_idx, i]
            if nums[i] - nums[min_idx] >= valueDifference:
                return [min_idx, i]
        
        return [-1, -1]