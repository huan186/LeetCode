class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = len(nums) - 1
        seen = [False] * (n + 1)
        for num in nums:
            if num > n:
                return False
            if num == n or not seen[num]:
                seen[num] = True
            else:
                return False
        return all(seen[1:])

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna