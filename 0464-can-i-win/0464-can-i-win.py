class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if desiredTotal <= maxChoosableInteger:
            return True

        if (maxChoosableInteger * (maxChoosableInteger + 1)) // 2 < desiredTotal:
            return False

        @lru_cache(None)
        def win(used, total):
            for num in range(maxChoosableInteger, 0, -1):
                mask = 1 << (num - 1)
                if used & mask:
                    continue
                if num >= total or not win(used | mask, total - num):
                    return True
            return False
        
        return win(0, desiredTotal)