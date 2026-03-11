class Solution:
    def minimumIndex(self, capacity: list[int], itemSize: int) -> int:
        ans = -1
        prev = float('inf')
        for i, c in enumerate(capacity):
            if prev > c >= itemSize:
                ans = i
                prev = c
        return ans