class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        res = 0
        n = len(s)

        diff = [0] * (n + 1)
        for i in range(n):
            diff[i + 1] = diff[i] + (1 if s[i] in "aeiou" else -1)

        limit = 1
        i = 2

        while i * i <= k:
            if k % i == 0:
                c = 0
                while k % i == 0:
                    c += 1
                    k //= i
                limit *= i ** ((c + 1) // 2)
            i += 1

        if k > 1:
            limit *= k

        limit *= 2

        for i in range(limit):
            x = defaultdict(int)
            for j in range(i, n + 1, limit):
                res += x[diff[j]]
                x[diff[j]] += 1

        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna