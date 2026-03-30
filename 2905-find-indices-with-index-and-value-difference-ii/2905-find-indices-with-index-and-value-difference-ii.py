class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        n = len(nums)
        min_indices = [0] * n
        max_indices = [0] * n
        for i in range(1, n):
            if nums[i] > nums[max_indices[i - 1]]:
                max_indices[i] = i
            else:
                max_indices[i] = max_indices[i - 1]
            if nums[i] < nums[min_indices[i - 1]]:
                min_indices[i] = i
            else:
                min_indices[i] = min_indices[i - 1]
        for i in range(indexDifference, n):
            j = i - indexDifference
            if abs(nums[max_indices[j]] - nums[i]) >= valueDifference:
                return [max_indices[j], i]
            if abs(nums[min_indices[j]] - nums[i]) >= valueDifference:
                return [min_indices[j], i]
        return [-1, -1]