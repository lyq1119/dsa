from collections import deque
import sys
input = sys.stdin.readline
n, k = map(int, input().split())
g = [[] for _ in range(n + 1)]
for _ in range(k):
    x, a, b = map(int, input().split())
    if x == 1:
        # a = b
        g[a].append((b, 0))
        g[b].append((a, 0))
    elif x == 2:
        # a < b
        if a == b:
            print(-1)
            sys.exit()
        g[a].append((b, 1))
    elif x == 3:
        # a >= b
        g[b].append((a, 0))
    elif x == 4:
        # a > b
        if a == b:
            print(-1)
            sys.exit()
        g[b].append((a, 1))
    elif x == 5:
        # a <= b
        g[a].append((b, 0))
# 超级源点 0
for i in range(1, n + 1):
    g[0].append((i, 1))
dist = [0] * (n + 1)
inq = [False] * (n + 1)
cnt = [0] * (n + 1)
q = deque([0])
inq[0] = True
while q:
    u = q.popleft()
    inq[u] = False
    for v, w in g[u]:
        if dist[v] < dist[u] + w:  # 最长路松弛
            dist[v] = dist[u] + w
            if not inq[v]:
                q.append(v)
                inq[v] = True
                cnt[v] += 1
                if cnt[v] > n:
                    print(-1)
                    sys.exit()
print(sum(dist[1:]))