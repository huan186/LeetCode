class Solution:
    def lexicographicallySmallestArray(self, nums, limit):
        n = len(nums)
        x = sorted((v, i) for i, v in enumerate(nums))
        res = [0] * n

        i = 0
        while i < n:
            j = i
            while j + 1 < n and x[j + 1][0] - x[j][0] <= limit:
                j += 1
            indices = sorted(idx for _, idx in x[i:j+1])
            for k, idx in enumerate(indices):
                res[idx] = x[i + k][0]
            i = j + 1

        return res