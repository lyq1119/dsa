import sys
from collections import deque
data = iter(sys.stdin.read().split())
n,m = int(next(data)),int(next(data))
matrix = []
for _ in range(n):
    matrix.append([int(next(data)) for __ in range(m)])
record = [[float("inf") for _ in range(m)] for __ in range(n)]
record[0][0] = 0
q = deque([(0,0)])
vectors = [(0,1),(1,0),(-1,0),(0,-1)]
while q:
    i,j = q.popleft()
    for a,b in vectors:
        if i+a < n and i+a >= 0 and j+b < m and j+b >= 0:
            if max(record[i][j],abs(matrix[i+a][j+b]-matrix[i][j])) < record[i+a][j+b]:
                record[i+a][j+b] = max(record[i][j],abs(matrix[i+a][j+b]-matrix[i][j]))
                q.append((i+a,j+b))
print(record[-1][-1])