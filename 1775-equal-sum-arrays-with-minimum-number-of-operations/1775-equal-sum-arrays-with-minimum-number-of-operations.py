class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        diff = sum(nums1) - sum(nums2)
        if diff < 0:
            nums1, nums2 = nums2, nums1
            diff = -diff
        cnt = [0] * 6
        for num in nums1:
            cnt[num - 1] += 1
        for num in nums2:
            cnt[6 - num] += 1
        res = 0
        for gain in range(5, 0, -1):
            q = min(cnt[gain], (diff + gain - 1) // gain)
            res += q
            diff -= q * gain
            if diff <= 0:
                return res
        return -1