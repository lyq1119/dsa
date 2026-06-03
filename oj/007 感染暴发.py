from collections import deque

# 读取网格行列
m, n = map(int, input().split())
grid = []
q = deque()
# 四个方向：上下左右
dirs = [(-1,0), (1,0), (0,-1), (0,1)]

# 读入网格，记录初始感染点
for i in range(m):
    s = input().strip()
    row = []
    for j in range(n):
        val = int(s[j])
        row.append(val)
        if val == 1:
            q.append((i, j))
    grid.append(row)

k = int(input())

# 模拟 k 天传播
for _ in range(k):
    # 当天初始感染数量，只遍历当前这一层
    size = len(q)
    for __ in range(size):
        x, y = q.popleft()
        for dx, dy in dirs:
            nx = x + dx
            ny = y + dy
            # 边界合法且未感染
            if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 0:
                grid[nx][ny] = 1
                q.append((nx, ny))

# 统计总感染人数
cnt = 0
for row in grid:
    cnt += sum(row)
print(cnt)