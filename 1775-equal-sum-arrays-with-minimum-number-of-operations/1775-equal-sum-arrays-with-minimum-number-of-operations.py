class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        min_sum = max(m, n)
        max_sum = min(6 * m, 6 * n)
        if min_sum > max_sum:
            return -1
        diff = sum(nums1) - sum(nums2)
        if diff == 0:
            return 0
        if diff < 0:
            nums1, nums2 = nums2, nums1
            diff = -diff
        freq1 = Counter(nums1)
        freq2 = Counter(nums2)
        ans = 0
        
        for i in range(1, 6):
            q = min(freq2[i], (diff + 5 - i) // (6 - i))
            ans += q
            diff -= min(diff, q * (6 - i))
            j = 6 - i
            q = min(freq1[j + 1], (diff + j - 1) // j)
            ans += q
            diff -= min(diff, q * j)
        return ans