from copy import deepcopy
n,m = map(int,input().split())
matrix = []
for _ in range(n):
    matrix.append(list(map(int,input().split())))
matrix1 = deepcopy(matrix)
vectors = [(0,1),(1,0),(-1,0),(0,-1)]
visited = [[False]*m for _ in range(n)]
def dfs(i,j,state):
    if state:
        matrix1[i][j] = 0
    for a,b in vectors:
        u,v= i+a,j+b
        if u >= 0 and u <= n-1 and v >= 0 and v <= m-1 and not visited[u][v] and matrix[u][v] == 1:
            visited[u][v] = True
            dfs(u,v,state)
for i in range(m):
    if not visited[0][i] and matrix[0][i] == 1:
        visited[0][i] = True
        dfs(0,i,0)
    if not visited[-1][i] and matrix[-1][i] == 1:
        visited[-1][i] = True
        dfs(n-1,i,0)
for i in range(n):
    if not visited[i][0] and matrix[i][0] == 1:
        visited[i][0] = True
        dfs(i,0,0)
    if not visited[i][m-1] and matrix[i][m-1] == 1:
        visited[i][m-1] = True
        dfs(i,m-1,0)
for i in range(1,n-1):
    for j in range(1,m-1):
        if not visited[i][j] and matrix[i][j] == 1:
            dfs(i,j,1)
for row in matrix1:
    print(*row)