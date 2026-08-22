class Solution:
    def lastNonEmptyString(self, s: str) -> str:
        counts = Counter(s)
        m = max(counts.values())
        r = []
        for k, v in counts.items():
            if v == m:
                r.append([s.rindex(k), k])
        r.sort()
        return ''.join(map(lambda x: x[1], r))

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna