class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        seen = set(nums)

        self.ans = None

        n = len(nums[0])

        def dfs(curr):
            if len(curr) == n:
                if curr not in seen:
                    self.ans = curr
                    return True
                return False
            dfs(curr + '0')
            dfs(curr + '1')
        
        dfs('')
        return self.ans