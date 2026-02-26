from functools import lru_cache
class Solution:
    def solveSudoku(self, board) -> None:
        @lru_cache
        def neighbor(i,j):
            i1,j1 = 3*(i//3),3*(j//3)
            myset = {(i1,j1),(i1,j1+1),(i1,j1+2),(i1+1,j1),(i1+1,j1+1),(i1+1,j1+2),(i1+2,j1),
                     (i1+2,j1+1),(i1+2,j1+2)}
            return ({(i,t) for t in range(9)})|({(t,j) for t in range(9)})|myset-{(i,j)}
        vac = set()
        matrix = [[0 for _ in range(9)] for __ in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    vac.add((i,j))
        def findmin():
            i1,j1 = 10,10
            for i in range(9):
                for j in range(9):
                    if board[i][j] != ".":
                        continue
                    i1,j1 = i,j
                    if list(bin(matrix[i][j])[2:]).count('1') >= 5:
                        return i,j
            return i1,j1
        def update(i,j):
            myset = 0
            for i1,j1 in neighbor(i,j):
                if board[i1][j1] != ".":
                    myset = myset|(1<<int(board[i1][j1]))
            matrix[i][j] = myset
            if myset == 1022:
                return False
            return True
        def uplin(i,j):
            for i1,j1 in neighbor(i,j):
                if board[i1][j1] == ".":
                    if not update(i1,j1):
                        return False
            return True
        for i in range(9):
            for j in range(9):
                if (i,j) in vac:
                    update(i,j)
        i,j = findmin()
        def dfs(i,j):
            if i == 10:
                return True
            for s in range(1,10):
                t = (1<<s)|matrix[i][j]
                if t == matrix[i][j]:
                    continue
                board[i][j] = str(s)
                verdict = uplin(i,j)
                if not verdict:
                    board[i][j] = "."
                    uplin(i,j)
                    continue
                i1,j1 = findmin()
                if dfs(i1,j1):
                    return True
                board[i][j] = "."
                uplin(i,j)
            return False
        dfs(i,j)
        for row in board:
            print(*row)
Solution().solveSudoku([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]])
Solution().solveSudoku([[".",".",".",".",".",".",".",".","."],[".","9",".",".","1",".",".","3","."],[".",".","6",".","2",".","7",".","."],[".",".",".","3",".","4",".",".","."],["2","1",".",".",".",".",".","9","8"],[".",".",".",".",".",".",".",".","."],[".",".","2","5",".","6","4",".","."],[".","8",".",".",".",".",".","1","."],[".",".",".",".",".",".",".",".","."]])
Solution().solveSudoku([[".",".","3",".",".",".",".",".","."], ["4",".",".",".","8",".",".","3","6"], [".",".","8","3",".",".","1",".","."], [".","4",".",".","6",".",".","7","3"], [".",".",".","9",".",".",".","1","."], [".",".",".",".",".","2",".",".","."], [".",".","4",".","7",".",".","6","8"], ["6",".",".",".",".",".",".",".","."], ["7",".",".",".",".",".","5",".","."]])