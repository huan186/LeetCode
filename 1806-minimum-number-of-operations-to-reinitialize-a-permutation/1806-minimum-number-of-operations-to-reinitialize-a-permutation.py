class Solution:
    def reinitializePermutation(self, n: int) -> int:
        ops = 0
        i = 1
        while True:
            i = i // 2 + (n // 2 if i % 2 else 0)
            ops += 1
            if i == 1:
                return ops