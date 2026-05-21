class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        res = 0
        seen = set()
        for x in arr1:
            while x:
                seen.add(x)
                x //= 10
        for x in arr2:
            while x:
                if x in seen:
                    res = max(res, len(str(x)))
                    break
                x //= 10
        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna