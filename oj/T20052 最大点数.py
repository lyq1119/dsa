import copy
m,n,p = map(int,input().split())
board = []
for _ in range(m):
    board.append(list(map(int,input().split())))
def left(board):
    m = len(board)
    n = len(board[0])
    while True:
        c = False
        for i in range(m):
            for j in range(n-1, 0, -1):
                if board[i][j] > 0 and board[i][j-1] == 0:
                    # 交换位置，实现数字左移
                    board[i][j], board[i][j-1] = 0, board[i][j]
                    c = True
        if not c:
            break
    # 相同数字合并
    for i in range(m):
        for j in range(n-1):
            if board[i][j] == board[i][j+1]:
                board[i][j] *= 2
                board[i][j+1] = 0
    # 合并后再次左移，填补合并产生的空位
    while True:
        c = False
        for i in range(m):
            for j in range(n-1, 0, -1):
                if board[i][j] > 0 and board[i][j-1] == 0:
                    board[i][j], board[i][j-1] = 0, board[i][j]
                    c = True
        if not c:
            break
    return board
def rotatel(board):
    m = len(board)
    n = len(board[0])
    return [[board[j][n-1-i] for j in range(m)] for i in range(n)]
def operate(l,board):
    for _ in range(l):
        board = rotatel(board)
    board = left(board)
    for _ in range(3*l):
        board = rotatel(board)
    return board
totalmax = 0
def dfs(board,t):
    totalmax = 0
    for row in board:
        totalmax = max(totalmax,max(row))
    if t == p:
        return totalmax
    for l in range(4):
        board1 = copy.deepcopy(board)
        board1 = operate(l,board1)
        if board1 == board:
            continue
        for row in board1:
            totalmax = max(totalmax,max(row))
        totalmax = max(totalmax,dfs(copy.deepcopy(board1),t+1))
    return totalmax
print(dfs(board,0))