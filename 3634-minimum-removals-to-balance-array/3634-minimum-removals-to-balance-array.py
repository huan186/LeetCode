class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        def b_search(i: int) -> int:
            target = k * nums[i]
            if target >= nums[-1]:
                return n - 1
            l, r = i, n - 1
            while l < r:
                m = (l + r + 1) // 2
                if nums[m] > target:
                    r = m - 1
                else:
                    l = m
            return l
        ans = n
        for i in range(n):
            ans = min(ans, i + n - b_search(i) - 1)
        return ans