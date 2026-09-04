class Solution:
    def maximumTotalSum(self, maximumHeight: List[int]) -> int:
        maximumHeight.sort(reverse=True)
        res = 0
        mh = inf
        for h in maximumHeight:
            if mh == 1:
                return -1
            if h >= mh:
                mh -= 1
            else:
                mh = h
            res += mh
        return res


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna