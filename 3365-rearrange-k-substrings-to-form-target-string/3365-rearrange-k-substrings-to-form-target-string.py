class Solution:
    def isPossibleToRearrange(self, s: str, t: str, k: int) -> bool:
        l = len(s) // k
        return (Counter(s[i:i + l] for i in range(0, len(s), l))
                == Counter(t[i:i + l] for i in range(0, len(t), l)))