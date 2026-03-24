class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        half = n // 2
        
        sumL = sum(int(c) for c in num[:half] if c != '?')
        sumR = sum(int(c) for c in num[half:] if c != '?')
        
        cntL = num[:half].count('?')
        cntR = num[half:].count('?')
        
        if (cntL + cntR) % 2 == 1:
            return True
        
        return sumL - sumR != (cntR - cntL) // 2 * 9