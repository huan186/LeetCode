class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if desiredTotal <= maxChoosableInteger:
            return True

        if (maxChoosableInteger * (maxChoosableInteger + 1)) // 2 < desiredTotal:
            return False
        memo = {}
        def win(state):
            if state in memo:
                return memo[state]
            for num in range(maxChoosableInteger, 0, -1):
                mask = 1 << (num + 8)
                if state & mask:
                    continue
                if num >= (state & 511) or not win((state - num) | mask):
                    memo[state] = True
                    return True
            memo[state] = False
            return False
        
        return win(desiredTotal)