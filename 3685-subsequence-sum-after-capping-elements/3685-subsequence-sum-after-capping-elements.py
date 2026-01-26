class Solution:
    def subsequenceSumAfterCapping(self, nums: List[int], k: int) -> List[bool]:
        n = len(nums)
        nums.sort()
        res = []
        seen = [True] + [False] * k
        i = 0
        for x in range(1, n + 1):
            j = i
            while j < n and nums[j] <= x:
                for num in range(k, nums[j] - 1, -1):
                    seen[num] |= seen[num - nums[j]]
                j += 1
            for num in range(k + 1):
                if seen[num] and (k - num) % x == 0 and (k - num) // x <= n - j:
                    res.append(True)
                    break
            else:
                res.append(False)
            i = j
        return res