class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        c = 1
        for i in range(k - 3, -1, -1):
            if nums[i + 1] - nums[i] == 1:
                c += 1
            else:
                break
        n = len(nums)
        res = [-1] * (n - k + 1)
        for i in range(len(res)):
            if nums[i + k - 1] == nums[i + k - 2] + 1:
                c += 1
            else:
                c = 1
            if c >= k:
                res[i] = nums[i + k - 1]
        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna