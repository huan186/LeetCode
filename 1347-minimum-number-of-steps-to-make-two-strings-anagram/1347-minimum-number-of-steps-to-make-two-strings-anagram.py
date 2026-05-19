class Solution:
    def minSteps(self, s: str, t: str) -> int:
        diff = defaultdict(int)
        for c in s:
            diff[c] += 1
        for c in t:
            diff[c] -= 1
        return sum(x for x in diff.values() if x > 0)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna