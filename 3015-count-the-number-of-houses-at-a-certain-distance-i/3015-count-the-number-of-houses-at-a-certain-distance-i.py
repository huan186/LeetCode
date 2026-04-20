class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
        x, y = min(x, y), max(x, y)
        res = [0] * n
        for i in range(1, n):
            for j in range(i + 1, n + 1):
                d = min(
                    j - i,
                    abs(i - x) + 1 + abs(j - y)
                )
                res[d - 1] += 2
        return res