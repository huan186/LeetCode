class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        dp = [0] * (n + 1)
        ans = 0
        for i in range(m):
            nxt = [0] * (n + 1)
            for j in range(n):
                if nums1[i] == nums2[j]:
                    nxt[j + 1] = dp[j] + 1
                    ans = max(ans, nxt[j + 1])
            dp = nxt
        return ans