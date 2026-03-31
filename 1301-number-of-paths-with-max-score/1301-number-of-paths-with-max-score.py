class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        mod = 10 ** 9 + 7
        n = len(board)
        dp = [[0, 0] for _ in range(n)]  # [max_sum, ways]
        dp[0] = [0, 1]
        board[0] = '0' + board[0][1:]
        board[-1] = board[-1][:-1] + '0'
        for j in range(1, n):
            if board[0][j] != 'X':
                dp[j][0], dp[j][1] = dp[j - 1][0] + int(board[0][j]), dp[j - 1][1]
        for i in range(1, n):
            nxt = [[0, 0] for _ in range(n)]
            for j in range(n):
                if board[i][j] != 'X':
                    if board[i - 1][j] != 'X':
                        nxt[j][0], nxt[j][1] = dp[j][0] + int(board[i][j]), dp[j][1]
                    if j == 0:
                        continue
                    for s, w in (nxt[j - 1], dp[j - 1]):
                        if w == 0:
                            continue
                        ns = s + int(board[i][j])
                        if ns == nxt[j][0]:
                            nxt[j][1] = (nxt[j][1] + w) % mod
                        elif ns > nxt[j][0]:
                            nxt[j][0] = ns
                            nxt[j][1] = w
            dp = nxt
        return dp[-1]