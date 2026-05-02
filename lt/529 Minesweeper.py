from typing import List
class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        m,n = len(board),len(board[0])
        a,b = click[0],click[1]
        def callei(i,j):
            total = 0
            if board[i][j] == "M":
                return total
            if i >= 1 and board[i-1][j] == "M":
                total += 1
            if i < m-1 and board[i+1][j] == "M":
                total += 1
            if j >= 1 and board[i][j-1] == "M":
                total += 1
            if j < n-1 and board[i][j+1] == "M":
                total += 1
            if i >= 1 and j >= 1 and board[i-1][j-1] == "M":
                total += 1
            if i >= 1 and j < n-1 and board[i-1][j+1] == "M":
                total += 1
            if i < m-1 and j >= 1 and board[i+1][j-1] == "M":
                total += 1
            if i < m-1 and j < n-1 and board[i+1][j+1] == "M":
                total += 1
            return total
        leiboard = [[callei(__,_) for _ in range(n)] for __ in range(m)]
        if board[a][b] == "M":
            board[a][b] = "X"
            return board
        from collections import deque
        queue = deque([(a,b)])
        vectors = [(1,0),(0,1),(-1,0),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]
        visited = {(a,b)}
        while queue:
            i,j = queue.popleft()
            if leiboard[i][j] == 0:
                board[i][j] = "B"
            else:
                board[i][j] = str(leiboard[i][j])
                continue
            for t,s in vectors:
                if (i+t,j+s) not in visited and i+t >= 0 and i+t <= m-1 and j+s >= 0 and j+s <= n-1 and board[i+t][j+s] != "M":
                    visited.add((i+t,j+s))
                    queue.append((i+t,j+s))
        return board
print(Solution().updateBoard( board = [["E","E","E","E","E"],["E","E","M","E","E"],["E","E","E","E","E"],["E","E","E","E","E"]], click = [3,0]))