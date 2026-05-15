class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        def power(start):
            for i in range(start + 1, start + k):
                if nums[i] - nums[i - 1] != 1:
                    return -1
            return nums[start + k - 1]
        return [power(i) for i in range(0, len(nums) - k + 1)]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna