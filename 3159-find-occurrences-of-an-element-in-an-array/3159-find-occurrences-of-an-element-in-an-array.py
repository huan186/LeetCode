class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        occurrences = []
        for i, v in enumerate(nums):
            if v == x:
                occurrences.append(i)
        n = len(occurrences)
        res = []
        for q in queries:
            if q > n:
                res.append(-1)
            else:
                res.append(occurrences[q - 1])
        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna