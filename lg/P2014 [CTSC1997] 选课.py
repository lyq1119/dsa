import sys
sys.setrecursionlimit(100000)

n, m = map(int, input().split())

score = [0] * (n + 1)
g = [[] for _ in range(n + 1)]

for i in range(1, n + 1):
    fa, s = map(int, input().split())
    score[i] = s
    g[fa].append(i)

m += 1

dp = [[0] * (m + 1) for _ in range(n + 1)]
sz = [0] * (n + 1)

def dfs(u):
    sz[u] = 1
    dp[u][1] = score[u]

    for v in g[u]:
        dfs(v)

        for j in range(sz[u], 0, -1):
            for k in range(1, sz[v] + 1):
                if j + k <= m:
                    dp[u][j + k] = max(
                        dp[u][j + k],
                        dp[u][j] + dp[v][k]
                    )

        sz[u] += sz[v]

dfs(0)

print(dp[0][m])