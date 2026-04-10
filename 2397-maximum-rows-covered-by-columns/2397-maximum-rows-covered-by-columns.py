class Solution:
    def maximumRows(self, matrix: List[List[int]], numSelect: int) -> int:
        nums = [int("".join(map(str, row)), 2) for row in matrix]
        res = 0
        for comb in combinations(range(len(matrix[0])), numSelect):
            mask = sum(1 << c for c in comb)
            res = max(res, sum(num == num & mask for num in nums))
        return res