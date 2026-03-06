class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        n = (num - 3) // 3
        if 3 * n + 3 != num:
            return []
        return [n, n + 1, n + 2]
        