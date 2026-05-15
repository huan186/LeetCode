class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        c = 1
        res = []

        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1] + 1:
                c += 1
            else:
                c = 1

            if i >= k - 1:
                res.append(nums[i] if c >= k else -1)

        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna