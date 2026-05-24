class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)
        @cache
        def max_jump(i):
            res = 1
            j = i - 1
            while j >= max(0, i - d) and arr[j] < arr[i]:
                res = max(res, max_jump(j) + 1)
                j -= 1
            j = i + 1
            while j < min(n, i + d + 1) and arr[j] < arr[i]:
                res = max(res, max_jump(j) + 1)
                j += 1
            return res
        return max(max_jump(i) for i in range(n))
 

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna