class Solution:
    def minimumPushes(self, word: str) -> int:
        f = sorted(Counter(word).values(), reverse=True)
        return sum(f[i] * (i // 8 + 1) for i in range(len(f)))