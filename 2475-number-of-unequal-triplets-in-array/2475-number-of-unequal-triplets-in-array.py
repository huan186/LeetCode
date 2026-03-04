class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        counts = Counter(nums)
        s1, s2, s3 = 0, 0, 0
        for c in counts.values():
            s1 += c
            s2 += c ** 2
            s3 += c ** 3
        return (s1 ** 3 - 3 * s1 * s2 + 2 * s3) // 6