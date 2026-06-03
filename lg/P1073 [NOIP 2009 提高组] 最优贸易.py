import sys
from collections import deque
data = sys.stdin.read().split()
n,m = int(data[0]),int(data[1])
index = 2
costs = [int(data[index+j]) for j in range(n)]
index += n
adj = [[] for _ in range(n)]
for _ in range(m):
    a,b,c = int(data[index]),int(data[index+1]),int(data[index+2])
    index += 3
    a -= 1
    b -= 1
    if c == 1:
        adj[a].append(b)
    else:
        adj[a].append(b)
        adj[b].append(a)
def kosaraju(n, adj):
    # 1. 正向 DFS，记录完成顺序
    visited = [False] * n
    stack = []
    def dfs1(u):
        visited[u] = True
        for v in adj[u]:
            if not visited[v]:
                dfs1(v)
        stack.append(u) # 回溯时压入栈
    for i in range(n):
        if not visited[i]:
            dfs1(i)
    # 2. 创建反向图
    rev_adj = [[] for _ in range(n)]
    for u in range(n):
        for v in adj[u]:
            rev_adj[v].append(u)
    # 3. 反向 DFS，提取 SCC
    visited = [False] * n
    sccs = []
    def dfs2(u, current_scc):
        visited[u] = True
        current_scc.append(u)
        for v in rev_adj[u]:
            if not visited[v]:
                dfs2(v, current_scc)
    while stack:
        u = stack.pop()
        if not visited[u]:
            current_scc = []
            dfs2(u, current_scc)
            sccs.append(current_scc)
    return sccs
sccs = kosaraju(n,adj)
scc_id = [0] * n
scc_min = [float("inf")]*(len(sccs))
scc_max = [-float("inf")]*(len(sccs))
for i in range(len(sccs)):
    for node in sccs[i]:
        scc_id[node] = i
        scc_min[i] = min(scc_min[i],costs[node])
        scc_max[i] = max(scc_max[i],costs[node])
# 构建缩点后的 DAG & 计算出度
dag = [[] for _ in range(len(sccs))]
rdag = [[] for _ in range(len(sccs))]
indegree = [0]*len(sccs)
edges = set()  # 防止重复建边
for u in range(n):
    for v in adj[u]:
        a = scc_id[u]
        b = scc_id[v]
        if a != b and (a, b) not in edges:
            edges.add((a, b))
            dag[a].append(b)
            rdag[b].append(a)
            indegree[b] += 1
q = deque()

deg = indegree[:]

for i in range(len(sccs)):
    if deg[i] == 0:
        q.append(i)

topo = []

while q:
    u = q.popleft()
    topo.append(u)

    for v in dag[u]:
        deg[v] -= 1

        if deg[v] == 0:
            q.append(v)
start = scc_id[0]
end = scc_id[n-1]
reach1 = [False] * len(sccs)
def dfs1(u):
    reach1[u] = True
    for v in dag[u]:
        if not reach1[v]:
            dfs1(v)
dfs1(start)
reach2 = [False] * len(sccs)
def dfs2(u):
    reach2[u] = True
    for v in rdag[u]:
        if not reach2[v]:
            dfs2(v)
dfs2(end)
q = deque()

deg = indegree[:]
for i in range(len(sccs)):
    if deg[i] == 0:
        q.append(i)
topo = []
while q:
    u = q.popleft()
    topo.append(u)
    for v in dag[u]:
        deg[v] -= 1
        if deg[v] == 0:
            q.append(v)
INF = 10**18
cnt = len(sccs)
mn = [INF] * cnt
mn[start] = scc_min[start]
for u in topo:
    if mn[u] == INF:
        continue
    if not (reach1[u] and reach2[u]):
        continue
    for v in dag[u]:
        if not (reach1[v] and reach2[v]):
            continue
        mn[v] = min(
            mn[v],
            min(mn[u], scc_min[v])
        )
ans = 0
for i in range(cnt):
    if reach1[i] and reach2[i] and mn[i] != INF:
        ans = max(
            ans,
            scc_max[i] - mn[i]
        )

print(ans)