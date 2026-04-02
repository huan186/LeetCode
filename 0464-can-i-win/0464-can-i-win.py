class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if (maxChoosableInteger * (maxChoosableInteger + 1)) // 2 < desiredTotal:
            return False

        memo = {}

        def win(used, total):
            if (used, total) in memo:
                return memo[(used, total)]
            for num in range(maxChoosableInteger, 0, -1):
                mask = 1 << (num - 1)
                if used & mask:
                    continue
                if num >= total or not win(used | mask, total - num):
                    memo[(used, total)] = True
                    return True
            memo[(used, total)] = False
            return False
        
        return win(0, desiredTotal)