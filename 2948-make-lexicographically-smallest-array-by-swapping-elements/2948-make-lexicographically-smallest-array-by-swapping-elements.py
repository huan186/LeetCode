class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        x = [(v, i) for i, v in enumerate(nums)]
        x.sort()
        n = len(x)
        res = [0] * n
        i = 0
        while i < n:
            indices = [x[i][1]]
            values = [x[i][0]]
            j = i + 1
            while j < n and x[j][0] - x[j - 1][0] <= limit:
                indices.append(x[j][1])
                values.append(x[j][0])
                j += 1
            indices.sort()
            for idx, value in zip(indices, values):
                res[idx] = value
            i = j
        return res

            
