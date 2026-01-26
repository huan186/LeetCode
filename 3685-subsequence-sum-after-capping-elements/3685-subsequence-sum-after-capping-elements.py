class Solution:
    def subsequenceSumAfterCapping(self, nums: List[int], k: int) -> List[bool]:
        n, m = len(nums), max(nums) + 1
        freq = [0] * m
        for num in nums:
            freq[num] += 1
        res = []
        seen = [True] + [False] * k

        def is_possible():
            for r in range(0, min(k, n * x) + 1, x):
                if seen[k - r]:
                    return True
            return False

        for x in range(1, n + 1):
            while x < m and freq[x]:
                for num in range(k, x - 1, -1):
                    seen[num] |= seen[num - x]
                freq[x] -= 1
                n -= 1
            res.append(is_possible())
        return res