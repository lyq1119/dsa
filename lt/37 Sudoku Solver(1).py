class Solution:
    def solveSudoku(self, board) -> None:
        vac = []
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    vac.append((i,j))
        vac1 = set(vac)
        m = len(vac)
        matrix = [[{} for _ in range(9)] for __ in range(9)]
        def neighbor(i,j):
            i1,j1 = 3*(i//3),3*(j//3)
            myset = {(i1,j1),(i1,j1+1),(i1,j1+2),(i1+1,j1),(i1+1,j1+1),(i1+1,j1+2),(i1+2,j1),
                     (i1+2,j1+1),(i1+2,j1+2)}
            return ({(i,t) for t in range(9)})|({(t,j) for t in range(9)})|myset-{(i,j)}
        def update(i,j):
            a = board[i][j]
            for i1,j1 in neighbor(i,j):
                if (i1,j1) not in vac1:
                    continue
                if a not in matrix[i1][j1]:
                    matrix[i1][j1][a] = 1
                else:
                    matrix[i1][j1][a] += 1
        def antidate(i,j):
            a = board[i][j]
            for i1,j1 in neighbor(i,j):
                if (i1,j1) not in vac1:
                    continue
                matrix[i1][j1][a] -= 1
                if matrix[i1][j1][a] == 0:
                    del matrix[i1][j1][a]
            board[i][j] = "."
        def dfs(t):
            if t >= m:
                return True
            i,j = vac[t]
            for s in range(1,10):
                if str(s) in matrix[i][j]:
                    continue
                board[i][j] = str(s)
                update(i,j)
                if dfs(t+1):
                    return True
                antidate(i,j)
            return False
        for i in range(9):
            for j in range(9):
                if (i,j) not in vac1:
                    update(i,j)
        dfs(0)
        for row in board:
            print(*row)
Solution().solveSudoku([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]])