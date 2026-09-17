class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        inf = 10 ** 9
        def min_len(a):
            ml = [inf] * (n + 1)
            s = l = 0
            for r, v in enumerate(a):
                s += v

                while s > target:
                    s -= a[l]
                    l += 1

                if s == target:
                    ml[r + 1] = min(ml[r], r - l + 1)
                else:
                    ml[r + 1] = ml[r]

            return ml

        left = min_len(arr)
        right = min_len(arr[::-1])

        res = inf
        for i in range(1, n):
            res = min(res, left[i] + right[n - i])
        return -1 if res == inf else res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna