class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        leftMax = nums[0]
        curMax = nums[0]
        pos = 0
        
        for i in range(1, len(nums)):
            curMax = max(curMax, nums[i])
            
            if nums[i] < leftMax:
                leftMax = curMax
                pos = i
        
        return pos + 1