class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 1
        if n <= 3:
            return 2
        min_index = max_index = 0
        for i in range(1, n):
            if nums[i] > nums[max_index]:
                max_index = i
            elif nums[i] < nums[min_index]:
                min_index = i
        a, b = min(min_index, max_index), max(min_index, max_index)
        return min(a + 1 +  n - b, b + 1, n - a)