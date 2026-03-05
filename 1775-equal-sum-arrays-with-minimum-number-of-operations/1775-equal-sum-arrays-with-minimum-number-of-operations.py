from typing import List

class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        if len(nums1) * 6 < len(nums2) or len(nums2) * 6 < len(nums1):
            return -1

        s1, s2 = sum(nums1), sum(nums2)

        if s1 < s2:
            nums1, nums2 = nums2, nums1
            s1, s2 = s2, s1

        diff = s1 - s2
        cnt = [0] * 6

        for x in nums1:
            cnt[x - 1] += 1

        for x in nums2:
            cnt[6 - x] += 1

        ans = 0

        for gain in range(5, 0, -1):
            while cnt[gain] and diff > 0:
                diff -= gain
                cnt[gain] -= 1
                ans += 1
                if diff <= 0:
                    return ans

        return -1