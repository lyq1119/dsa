class Solution:
    def solveSudoku(self, board) -> None:
        hang,lie,kuai = [0 for _ in range(9)],[0 for _ in range(9)],[0 for _ in range(9)]
        vac = set()
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    vac.add((i,j))
        def update(i,j):
            num = 0
            num = num|hang[i]|lie[j]|kuai[3*(i//3)+(j//3)]
            return num
        def findmin():
            i1,j1 = 10,10
            maxnum = -1
            for i,j in vac:
                a = update(i,j)
                if a > maxnum:
                    i1,j1 = i,j
                    maxnum = a
            return i1,j1
        def uplin(i,j):
            a = int(board[i][j])
            hang[i] = hang[i]|(1<<a)
            lie[j] = lie[j]|(1<<a)
            kuai[3*(i//3)+(j//3)] = kuai[3*(i//3)+(j//3)]|(1<<a)
        def downlin(i,j):
            a = int(board[i][j])
            a = 1022-(1<<a)
            hang[i] = hang[i]&a
            lie[j] = lie[j]&a
            kuai[3*(i//3)+(j//3)] = kuai[3*(i//3)+(j//3)]&a
        for i in range(9):
            for j in range(9):
                if (i,j) not in vac:
                    uplin(i,j)
        i,j = findmin()
        def dfs(i,j):
            if i == 10:
                return True
            m = update(i,j)
            for s in range(1,10):
                t = (1<<s)|m
                if t == m:
                    continue
                board[i][j] = str(s)
                uplin(i,j)
                vac.discard((i,j))
                i1,j1 = findmin()  
                if dfs(i1,j1):
                    return True
                downlin(i,j)
                board[i][j] = "."
                vac.add((i,j))
            return False
        dfs(i,j)
        for row in board:
            print(*row)
Solution().solveSudoku([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]])
Solution().solveSudoku([[".",".",".",".",".",".",".",".","."],[".","9",".",".","1",".",".","3","."],[".",".","6",".","2",".","7",".","."],[".",".",".","3",".","4",".",".","."],["2","1",".",".",".",".",".","9","8"],[".",".",".",".",".",".",".",".","."],[".",".","2","5",".","6","4",".","."],[".","8",".",".",".",".",".","1","."],[".",".",".",".",".",".",".",".","."]])
Solution().solveSudoku([[".",".","3",".",".",".",".",".","."], ["4",".",".",".","8",".",".","3","6"], [".",".","8","3",".",".","1",".","."], [".","4",".",".","6",".",".","7","3"], [".",".",".","9",".",".",".","1","."], [".",".",".",".",".","2",".",".","."], [".",".","4",".","7",".",".","6","8"], ["6",".",".",".",".",".",".",".","."], ["7",".",".",".",".",".","5",".","."]])