class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums[0])
        seen = set(nums)

        self.ans = None

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