class Solution:
    def findLengthOfShortestSubarray(self, arr):
        n = len(arr)

        left = 0
        while left < n - 1 and arr[left] <= arr[left + 1]:
            left += 1

        if left == n - 1:
            return 0

        right = n - 1
        while right > 0 and arr[right] >= arr[right - 1]:
            right -= 1

        ans = min(n - left - 1, right)

        j = right
        for i in range(left + 1):
            while j < n and arr[j] < arr[i]:
                j += 1
            ans = min(ans, j - i - 1)

        return ans