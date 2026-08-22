class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        coins.sort()

        x = []
        for c in coins:
            if all(c % p != 0 for p in x):
                x.append(c)

        n = len(x)
        
        def count(v):
            res = 0

            for mask in range(1, 1 << n):
                LCM = 1
                bits = 0

                for i in range(n):
                    if mask >> i & 1:
                        bits += 1
                        LCM = lcm(LCM, x[i])
                        if LCM > v:
                            break
                
                if LCM <= v:
                    if bits & 1:
                        res += v // LCM
                    else:
                        res -= v // LCM
                
            return res
        
        l, h = 0, x[0] * k
        while l < h:
            m = l + (h - l) // 2
            if count(m) >= k:
                h = m
            else:
                l = m + 1
        
        return l
                
            

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna