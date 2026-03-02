class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2_sorted = sorted((v, i) for i, v in enumerate(nums2))
        n = len(nums1)
        left, right = 0, n - 1
        res = [0] * n

        for v, i in reversed(nums2_sorted):
            if nums1[right] > v:
                res[i] = nums1[right]
                right -= 1
            else:
                res[i] = nums1[left]
                left += 1
        
        return res