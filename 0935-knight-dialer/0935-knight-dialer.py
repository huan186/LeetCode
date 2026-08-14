class Solution:
    def knightDialer(self, n: int) -> int:
        nxt = {
            0: [4, 6],
            1: [6, 8],
            2: [7, 9],
            3: [4, 8],
            4: [0, 3, 9],
            6: [0, 1, 7],
            7: [2, 6],
            8: [1, 3],
            9: [2, 4]
        }
        mod = 10 ** 9 + 7
        if n == 1:
            return 10
        cnt = [1] * 10
        for i in range(n - 1):
            nxt_cnt = [0] * 10
            for j in nxt:
                for k in nxt[j]:
                    nxt_cnt[k] = (nxt_cnt[k] + cnt[j]) % mod
            cnt = nxt_cnt
        return sum(cnt) % mod

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna