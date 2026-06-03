import sys
from collections import deque
sys.setrecursionlimit(2000000)
n, m = map(int, input().split())
scores = list(map(int, input().split()))
adj = [[] for _ in range(n)]
rev_adj = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    adj[a].append(b)
    rev_adj[b].append(a)
# ---------- Kosaraju ----------
visited = [False] * n
stack = []
def dfs1(u):
    visited[u] = True
    for v in adj[u]:
        if not visited[v]:
            dfs1(v)
    stack.append(u)
for i in range(n):
    if not visited[i]:
        dfs1(i)
scc_id = [-1] * n
sccs = []
def dfs2(u, idx):
    scc_id[u] = idx
    sccs[idx].append(u)
    for v in rev_adj[u]:
        if scc_id[v] == -1:
            dfs2(v, idx)
while stack:
    u = stack.pop()
    if scc_id[u] == -1:
        sccs.append([])
        dfs2(u, len(sccs) - 1)
# ---------- SCC 权值 ----------
score = [0] * len(sccs)
maxsccs = [0] * len(sccs)
for i in range(len(sccs)):
    for node in sccs[i]:
        score[i] += scores[node]
        maxsccs[i] = max(maxsccs[i], scores[node])
# ---------- 缩点 DAG ----------
dag = [[] for _ in range(len(sccs))]
indeg = [0] * len(sccs)
edges = set()
for u in range(n):
    for v in adj[u]:
        a = scc_id[u]
        b = scc_id[v]
        if a != b and (a, b) not in edges:
            edges.add((a, b))
            dag[a].append(b)
            indeg[b] += 1
# ---------- DAG DP ----------
dp = score[:]          # 最大亮度和
maxnum = maxsccs[:]    # 对应路径上的最大单点亮度
q = deque()
for i in range(len(sccs)):
    if indeg[i] == 0:
        q.append(i)
while q:
    u = q.popleft()
    for v in dag[u]:
        cand_sum = dp[u] + score[v]
        cand_max = max(maxnum[u], maxsccs[v])
        if cand_sum > dp[v]:
            dp[v] = cand_sum
            maxnum[v] = cand_max
        elif cand_sum == dp[v]:
            if cand_max > maxnum[v]:
                maxnum[v] = cand_max
        indeg[v] -= 1
        if indeg[v] == 0:
            q.append(v)
ans_sum = 0
ans_max = 0
for i in range(len(sccs)):
    if dp[i] > ans_sum:
        ans_sum = dp[i]
        ans_max = maxnum[i]
    elif dp[i] == ans_sum:
        ans_max = max(ans_max, maxnum[i])
print(ans_sum, ans_max)