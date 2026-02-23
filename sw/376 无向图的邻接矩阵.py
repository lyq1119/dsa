n,m = map(int,input().split())
matrix = [[0]*n for _ in range(n)]
for _ in range(m):
    t,s = map(int,input().split())
    matrix[t][s] = 1
for row in matrix:
    print(*row)