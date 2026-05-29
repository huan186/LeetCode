class Solution:
    def countExcellentPairs(self, nums: List[int], k: int) -> int:
        arr = sorted(num.bit_count() for num in set(nums))
        res = 0
        n = len(arr)
        j = n - 1
        for i in range(n):
            while j >= 0 and arr[i] + arr[j] >= k:
                j -= 1
            res += n - j - 1
        return res


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna