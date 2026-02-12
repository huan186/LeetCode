class Solution:
    def longestBalanced(self, s: str) -> int:
        res = 0
        a = [ord(c) - ord('a') for c in s]
        n = len(s)

        def is_balanced(fr):
            t = 0
            for f in fr:
                if f != 0:
                    if t == 0:
                        t = f
                    elif t != f:
                        return False
            return True

        for i in range(n):
            freq = [0] * 26
            for j in range(i, n):
                freq[a[j]] += 1
                if is_balanced(freq):
                    res = max(res, j - i + 1)
        
        return res