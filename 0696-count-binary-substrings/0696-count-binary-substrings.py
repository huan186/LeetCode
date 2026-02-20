class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        res = 0
        prev = 0
        i, n = 0, len(s)
        while i < n:
            j = i + 1
            while j < n and s[j] == s[i]:
                j += 1
            curr = j - i
            res += min(curr, prev)
            prev = curr
            i = j
        return res