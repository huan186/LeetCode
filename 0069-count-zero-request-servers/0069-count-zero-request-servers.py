class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        logs.sort(key=lambda p: p[1])
        qs = sorted((q, i) for i, q in enumerate(queries))

        count = defaultdict(int)
        left = right = 0
        res = [0] * len(queries)

        for q, i in qs:
            while right < len(logs) and logs[right][1] <= q:
                count[logs[right][0]] += 1
                right += 1

            while left < right and logs[left][1] < q - x:
                s = logs[left][0]
                count[s] -= 1
                if count[s] == 0:
                    del count[s]
                left += 1

            res[i] = n - len(count)

        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna