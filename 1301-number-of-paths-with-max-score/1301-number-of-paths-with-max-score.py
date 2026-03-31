class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        mod = 10 ** 9 + 7
        n = len(board)

        board[0] = '0' + board[0][1:]
        board[-1] = board[-1][:-1] + '0'
        
        dp = [[0, 0] for _ in range(n + 1)]  # [max_sum, ways]
        dp[1] = [0, 1]
        for j in range(1, n):
            if board[0][j] != 'X':
                dp[j + 1][0] = dp[j][0] + int(board[0][j])
                dp[j + 1][1] = dp[j][1]
        for i in range(1, n):
            nxt = [[0, 0] for _ in range(n + 1)]
            for j in range(n):
                if board[i][j] != 'X':
                    for s, w in (nxt[j], dp[j], dp[j + 1]):
                        if w == 0:
                            continue
                        ns = s + int(board[i][j])
                        if ns == nxt[j + 1][0]:
                            nxt[j + 1][1] = (nxt[j + 1][1] + w) % mod
                        elif ns > nxt[j + 1][0]:
                            nxt[j + 1][0] = ns
                            nxt[j + 1][1] = w
            dp = nxt
        return dp[-1]