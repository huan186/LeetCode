class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        x = [(sum(map(int, str(num))), num, i) for i, num in enumerate(nums)]
        arr = [i for _, _, i in sorted(x)]

        indices = {v: i for i, v in enumerate(arr)}

        res = 0
        for i in range(len(arr)):
            if arr[i] == i:
                continue

            j = indices[i]
            arr[i], arr[j] = arr[j], arr[i]
            indices[arr[i]] = i
            indices[arr[j]] = j
            res += 1

        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna