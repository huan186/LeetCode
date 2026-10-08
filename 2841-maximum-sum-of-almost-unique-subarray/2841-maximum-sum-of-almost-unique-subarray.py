class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        c = Counter()
        u = 0
        res = s = 0
        for i, num in enumerate(nums):
            s += num
            if not c[num]:
                u += 1
            c[num] += 1
            if i >= k:
                p = nums[i - k]
                s -= p
                c[p] -= 1
                if c[p] == 0:
                    u -= 1
            if u >= m:
                res = max(res, s)
        return res




# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna