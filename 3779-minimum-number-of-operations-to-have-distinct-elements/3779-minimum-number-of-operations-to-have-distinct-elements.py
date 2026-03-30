class Solution:
    def minOperations(self, nums: List[int]) -> int:
        seen = set()
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] in seen:
                return (i + 3) // 3
            else:
                seen.add(nums[i])
        return 0