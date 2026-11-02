class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        m, n = len(nums), len(nums[0])
        for row in nums:
            row.sort()
        res = 0
        for j in range(n):
            col = []
            for i in range(m):
                col.append(nums[i][j])
            col.sort()
            res += col[-1]
        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna