class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        n = len(s)
        if n <= 2:
            return n
        for length in range(n, 2, -1):
            for start in range(n - length + 1):
                if sum(s[i] == s[i + 1] for i in range(start, start + length - 1)) <= 1:
                    return length
        return 2