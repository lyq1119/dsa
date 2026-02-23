import sys
data = sys.stdin.read().split()
case = int(data[0])
t = 1
for _ in range(case):
    m,n = int(data[t]),int(data[t+1])
    t += 2
    grid = []
    for __ in range(m):
        grid.append([int(data[j]) for j in range(t,t+n)])
        t += n
    visited = [[0]*n for s in range(m)]
    vectors = [(0,1),(0,-1),(-1,0),(1,0)]
    maximum = 0
    for i in range(m):
        for j in range(n):
            if visited[i][j] == 0 and grid[i][j] != 0:
                stack = [(i,j)]
                total = 0
                visited[i][j] = 1
                while stack:
                    i1,j1 = stack.pop()
                    total += grid[i1][j1]
                    for a,b in vectors:
                        if i1+a >= 0 and i1+a <= m-1 and j1+b >= 0 and j1+b <= n-1 and visited[i1+a][j1+b] == 0 and grid[i1+a][j1+b] != 0:
                            stack.append((i1+a,j1+b))
                            visited[i1+a][j1+b] = 1
                maximum = max(maximum,total)
    print(maximum)