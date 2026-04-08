class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        inc = [1] * n
        for i in range(1, n - 1):
            for j in range(i):
                if nums[j] < nums[i]:
                    inc[i] = max(inc[i], inc[j] + 1)
        dec = [1] * n
        for i in range(n - 2, 0, -1):
            for j in range(n - 1, i, -1):
                if nums[j] < nums[i]:
                    dec[i] = max(dec[i], dec[j] + 1)
        max_len = 0
        for i in range(1, n - 1):
            if inc[i] != 1 and dec[i] != 1:
                max_len = max(max_len, inc[i] + dec[i])
        return n - max_len + 1