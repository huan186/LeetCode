class Solution:
    def maximumCoins(self, coins: List[List[int]], k: int) -> int:
        coins.sort()
        res = 0
        
        # Case 1:
        left = 0
        bags = 0
        total_coins = 0
        for start, end, coin in coins:
            while end - coins[left][1] >= k:
                b = coins[left][1] - coins[left][0] + 1
                bags -= b
                total_coins -= b * coins[left][2]
                left += 1
            b = end - start + 1
            bags += b
            total_coins += b * coin
            left_bags_skipped = max(end - k + 1 - coins[left][0], 0)
            res = max(res, total_coins - left_bags_skipped * coins[left][2])
            
        # Case 2:
        right = len(coins) - 1
        bags = 0
        total_coins = 0
        for start, end, coin in coins[::-1]:
            while coins[right][0] - start >= k:
                b = coins[right][1] - coins[right][0] + 1
                bags -= b
                total_coins -= b * coins[right][2]
                right -= 1
            b = end - start + 1
            bags += b
            total_coins += b * coin
            right_bags_skipped = max(coins[right][1] - start - k + 1, 0)
            res = max(res, total_coins - right_bags_skipped * coins[right][2])

        return res