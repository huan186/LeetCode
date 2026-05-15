class Solution:
    def fillCups(self, amount: List[int]) -> int:
        amount.sort()
        s = sum(amount)
        if 2 * amount[-1] >= s:
            return amount[-1]
        return (s + 1) // 2
        


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna