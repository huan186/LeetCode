class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        n = len(arr) - 1
        min_diff = min(arr[i + 1] - arr[i] for i in range(n))
        return [[arr[i], arr[i + 1]] for i in range(n) if arr[i + 1] - arr[i] == min_diff]