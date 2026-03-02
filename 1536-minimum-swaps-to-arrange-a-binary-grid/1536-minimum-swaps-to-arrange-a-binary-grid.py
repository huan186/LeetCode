class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        cnts = []
        for row in grid:
            cnt = 0
            for num in row[::-1]:
                if num == 1:
                    break
                cnt += 1
            cnts.append(cnt)
        n = len(grid)
        swap = 0
        for i in range(n):
            need = n - i - 1
            for j in range(i, n):
                if cnts[j] >= need:
                    swap += j - i
                    for k in range(j, i, -1):
                        cnts[k] = cnts[k - 1]
                    break
            else: return -1
        return swap