class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        board = [[None] * 3 for _ in range(3)]
        p = 'A'
        for x, y in moves:
            board[x][y] = p
            p = 'A' if p == 'B' else 'B'
        def helper(x, y, dx, dy):
            return board[x][y] and board[x][y] == board[x + dx][y + dy] == board[x + 2 * dx][y + 2 * dy]
        if helper(0, 0, 0, 1) or helper(0, 0, 1, 1) or helper(0, 0, 1, 0):
            return board[0][0]
        if helper(0, 1, 1, 0):
            return board[0][1]
        if helper(0, 2, 1, -1) or helper(0, 2, 1, 0):
            return board[0][2]
        if helper(1, 0, 0, 1):
            return board[1][0]
        if helper(2, 0, 0, 1):
            return board[2][0]
        return 'Draw' if len(moves) == 9 else 'Pending'