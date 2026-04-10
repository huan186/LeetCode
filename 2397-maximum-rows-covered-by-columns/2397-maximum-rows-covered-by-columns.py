class Solution:
    def maximumRows(self, matrix: List[List[int]], numSelect: int) -> int:
        nums = [int("".join(map(str, row)), 2) for row in matrix]

        for k in range(len(nums), -1, -1):
            for c in combinations(nums, k):
                if reduce(or_, c, 0).bit_count() <= numSelect:
                    return k

        return 0