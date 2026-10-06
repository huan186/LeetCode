class Solution:
    def maxTurbulenceSize(self, arr: list[int]) -> int:
        n = len(arr)
        if n <= 1:
            return n
        def compare(a, b):
            return 0 if a == b else (1 if a > b else -1)
        res = 1
        cnt = p = 0
        for i in range(1, n):
            d = compare(arr[i], arr[i - 1])
            if d == 0:
                p = 0
            else:
                if d + p == 0:
                    cnt += 1
                else:
                    cnt = 1
                res = max(res, cnt + 1)
                p = d
        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna