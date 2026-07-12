class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        if not arr:
            return []
        n = len(arr)
        s = sorted((v, i) for i, v in enumerate(arr))
        res = [0] * n
        res[s[0][1]] = 1
        rank = 1
        for i in range(1, n):
            if s[i][0] != s[i - 1][0]:
                rank += 1
            res[s[i][1]] = rank
        return res


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna