from collections import deque
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
g = [[] for _ in range(n + 1)]
for _ in range(m):
    c, cp, y = map(int, input().split())
    # x_c - x_cp <= y
    # x_c <= x_cp + y
    # cp -> c, weight = y
    g[cp].append((c, y))
dist = [0] * (n + 1)
cnt = [1] * (n + 1)
inq = [True] * (n + 1)
q = deque(range(1, n + 1))
while q:
    u = q.popleft()
    inq[u] = False
    du = dist[u]
    for v, w in g[u]:
        if dist[v] > du + w:
            dist[v] = du + w
            if not inq[v]:
                q.append(v)
                inq[v] = True
                cnt[v] += 1
                if cnt[v] > n:
                    print("NO")
                    sys.exit()
print(*dist[1:])