from collections import deque

n, m = map(int, input().split())
grid = []
for _ in range(n):
    grid.append(list(map(int, input().split())))

INF = float('inf')
dist = [[INF] * m for _ in range(n)]
dist[0][0] = 0

dirs = [(-1,0), (1,0), (0,-1), (0,1)]
q = deque()
q.append((0, 0))

while q:
    x, y = q.popleft()
    for dx, dy in dirs:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < n and 0 <= ny < m:
            new_max = max(dist[x][y], abs(grid[nx][ny] - grid[x][y]))
            if new_max < dist[nx][ny]:
                dist[nx][ny] = new_max
                q.append((nx, ny))

print(dist[n-1][m-1])