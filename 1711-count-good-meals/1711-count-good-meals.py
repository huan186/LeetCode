class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        MOD = 10**9 + 7
        count = {}
        res = 0
        
        for x in deliciousness:
            for i in range(22):
                target = (1 << i) - x
                if target in count:
                    res += count[target]
            
            count[x] = count.get(x, 0) + 1
        
        return res % MOD
