class Solution:
    def minCost(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        n = len(nums)

        closet = [0] * n
        closet[0] = 1
        closet[-1] = n - 2
        for i in range(1, n - 1):
            d = abs(nums[i] - nums[i - 1]) - abs(nums[i] - nums[i + 1])
            closet[i] = i - 1 if d <= 0 else i + 1

        pref = [0] * n
        suff = [0] * n

        for i in range(1, n):
            pref[i] = pref[i - 1] + (1 if closet[i - 1] == i else abs(nums[i] - nums[i - 1]))
            suff[n - i - 1] = suff[n - i] + (1 if closet[n - i] == n - i - 1 else abs(nums[n - i] - nums[n - i - 1]))
        
        res = []

        for l, r in queries:
            if l <= r:
                res.append(pref[r] - pref[l])
            else:
                res.append(suff[r] - suff[l])
        
        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna