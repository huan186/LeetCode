class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        n = len(arr)
        f = n // 20
        return sum(arr[f : n - f]) / (n - 2 * f)