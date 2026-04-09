class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        threshold = int(n ** 0.5)

        mod = 10 ** 9 + 7

        kdict = defaultdict(list)

        for l, r, k, v in queries:
            if k >= threshold:
                for idx in range(l, r + 1, k):
                    nums[idx] = (nums[idx] * v) % mod
            else:
                kdict[k].append((l, r, v))

        diff = [1] * (threshold + n)
        for k, x in kdict.items():
            diff[:] = [1] * len(diff)
            for l, r, v in x:
                R = ((r - l) // k + 1) * k + l
                diff[l] = diff[l] * v % mod
                diff[R] = diff[R] * pow(v, mod - 2, mod) % mod
            for i in range(k, n):
                diff[i] = diff[i] * diff[i - k] % mod
            
            for i in range(n):
                nums[i] = nums[i] * diff[i] % mod

        res = 0
        for num in nums:
            res ^= num
        return res