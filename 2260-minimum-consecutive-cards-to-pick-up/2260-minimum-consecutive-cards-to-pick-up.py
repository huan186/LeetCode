class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        seen = {}
        res = inf
        for i, c in enumerate(cards):
            if c in seen:
                res = min(res, i - seen[c] + 1)
            seen[c] = i
        return res if res != inf else -1