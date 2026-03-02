class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums1)
        nums1.sort(reverse=True)
        nums2 = [(nums2[i], i) for i in range(n)]
        nums2.sort(reverse=True)
        res = [0] * n
        i11, i12 = 0, n - 1
        for i2 in range(n):
            idx = nums2[i2][1]
            if nums1[i11] > nums2[i2][0]:
                res[idx] = nums1[i11]
                i11 += 1
            else:
                res[idx] = nums1[i12]
                i12 -= 1
        return res