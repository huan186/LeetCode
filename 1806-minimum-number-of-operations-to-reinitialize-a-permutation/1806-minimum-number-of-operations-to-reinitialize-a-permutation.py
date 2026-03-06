class Solution:
    def reinitializePermutation(self, n: int) -> int:
        mapping = {i: i // 2 + (n // 2 if i % 2 else 0) for i in range(n)}
        ops = 1
        i = mapping[1]
        while i != 1:
            i = mapping[i]
            ops += 1
        return ops