class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        states = {0: -1}
        st = 0
        res = 0
        for i, c in enumerate(s):
            if c in ('a', 'e', 'i', 'o', 'u'):
                st ^= 1 << (ord(c) - 97)
            if st in states:
                res = max(res, i - states[st])
            else:
                states[st] = i
        return res