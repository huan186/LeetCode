class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)

        if n == 2 and s[0] > s[1]:
            return -1

        if list(s) == sorted(s):
            return 0

        mn = min(s)
        mx = max(s)

        freq = Counter(s)

        if s[0] == mx and s[-1] == mn and freq[mx] == 1 and freq[mn] == 1:
            return 3

        if s[0] == mn or s[-1] == mx:
            return 1

        return 2