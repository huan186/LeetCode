class Solution:
    def subsequenceSumAfterCapping(self, nums: List[int], k: int) -> List[bool]:
        n, m = len(nums), 4001
        freq = [0] * m
        for num in nums:
            freq[num] += 1
        res = []
        seen = [True] + [False] * k

        def is_possible():
            for s in range(k + 1):
                if seen[s] and (k - s) % x == 0 and (k - s) // x <= n:
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