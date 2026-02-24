class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        up, down = 0, 0
        res = 0
        for i in range(len(arr) - 1):
            if arr[i] == arr[i + 1]:
                up = down = 0
            elif arr[i] > arr[i + 1]:
                if up:
                    down += 1
                    res = max(res, up + down + 1)
            else:
                if down:
                    up = 1
                else:
                    up += 1
                down = 0
        return res