n,m = map(int,input().split())
matrix = [[0]*n for _ in range(n)]
count = [[0]*n for _ in range(n)]
for _ in range(m):
    t,s = map(int,input().split())
    matrix[t][s] = 1
    matrix[s][t] = 1
    count[t][t] += 1
    count[s][s] += 1
matrix1 = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        matrix1[i][j] = count[i][j] - matrix[i][j]
for row in matrix1:
    print(*row)