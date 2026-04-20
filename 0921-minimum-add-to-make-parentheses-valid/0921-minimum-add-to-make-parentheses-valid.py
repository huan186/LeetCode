class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open_cnt = 0
        res = 0
        for c in s:
            if c == '(':
                open_cnt += 1
            elif open_cnt > 0:
                open_cnt -= 1
            else:
                res += 1
        return res + open_cnt