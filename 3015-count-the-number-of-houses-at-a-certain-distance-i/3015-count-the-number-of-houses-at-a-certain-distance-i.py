class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
        res = [0] * n
        for i in range(1, n):
            for j in range(i + 1, n + 1):
                d = min(
                    abs(i - j),
                    abs(i - x) + 1 + abs(j - y),
                    abs(i - y) + 1 + abs(j - x),
                )
                res[d - 1] += 2
        return res