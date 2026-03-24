class Solution:
    def minimumPushes(self, word: str) -> int:
        count = Counter(word)
        if len(count) <= 8:
            return len(word)
        f = list(count.values())
        f.sort(reverse=True)
        return sum(f[i] * (i // 8 + 1) for i in range(len(f)))