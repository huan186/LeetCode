class Solution:
    def maximumCoins(self, coins: List[List[int]], k: int) -> int:
        coins.sort()
        res = 0
        left, total_coins = 0, 0
        for start, end, coin in coins:
            while end - coins[left][1] >= k:
                total_coins -= (coins[left][1] - coins[left][0] + 1) * coins[left][2]
                left += 1
            total_coins += (end - start + 1) * coin
            bags_skipped = max(end - k + 1 - coins[left][0], 0)
            res = max(res, total_coins - bags_skipped * coins[left][2])
        right, total_coins = len(coins) - 1, 0
        for start, end, coin in coins[::-1]:
            while coins[right][0] - start >= k:
                total_coins -= (coins[right][1] - coins[right][0] + 1) * coins[right][2]
                right -= 1
            total_coins += (end - start + 1) * coin
            bags_skipped = max(coins[right][1] - start - k + 1, 0)
            res = max(res, total_coins - bags_skipped * coins[right][2])
        return res