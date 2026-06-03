import sys
sys.setrecursionlimit(10000000)
from collections import deque
data = sys.stdin.read().split()
index = 0
n,m = int(data[index]),int(data[index+1])
index += 2
adj = [[] for _ in range(n)]
for _ in range(m):
    a,b,c,d = int(data[index]),int(data[index+1]),int(data[index+2]),float(data[index+3])
    index += 4
    a -= 1
    b -= 1
    adj[a].append((b,c,d))
def tarjan_scc(n, adj):
    dfn = [-1] * n      # 搜索次序
    low = [-1] * n      # 最低链接值
    stack = []          # 辅助栈
    in_stack = [False] * n
    timer = 0
    sccs = []           # 存储最终结果
    def dfs(u):
        nonlocal timer
        dfn[u] = low[u] = timer
        timer += 1
        stack.append(u)
        in_stack[u] = True
        for v,w,s in adj[u]:
            if dfn[v] == -1: # 情况 A：邻居未访问
                dfs(v)
                low[u] = min(low[u], low[v])
            elif in_stack[v]: # 情况 B：邻居在栈中（回边）
                low[u] = min(low[u], dfn[v])
        # 判定强连通分量的根
        if low[u] == dfn[u]:
            current_scc = []
            while True:
                node = stack.pop()
                in_stack[node] = False
                current_scc.append(node)
                if node == u:
                    break
            sccs.append(current_scc)
    for i in range(n):
        if dfn[i] == -1:
            dfs(i)        
    return sccs
sccs = tarjan_scc(n,adj)
scc_id = [0] * n
cnt = len(sccs)
scc_mr = [0]*cnt
for i in range(len(sccs)):
    for node in sccs[i]:
        scc_id[node] = i
# 构建缩点后的 DAG & 计算出度
dag = [[] for _ in range(len(sccs))]
graph = [[0]*len(sccs) for _ in range(len(sccs))]
indegree = [0] * len(sccs)
edges = set()
for u in range(n):
    for v,w,s in adj[u]:
        a = scc_id[u]
        b = scc_id[v]
        if a == b:
            t = 0
            while w:
                t += w
                w = int(w * s+ 1e-8)
            scc_mr[a] += t
        if a != b :
            graph[a][b] = max(graph[a][b],w)
            if (a,b) not in edges:
                edges.add((a,b))
                dag[a].append(b)
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
start = scc_id[int(data[index])-1]
reach1 = [False] * len(sccs)
def dfs1(u):
    reach1[u] = True
    for v in dag[u]:
        if not reach1[v]:
            dfs1(v)
dfs1(start)
INF = -10**18
mn = [INF] * cnt
mn[start] = scc_mr[start]
for u in topo:
    if mn[u] == INF:
        continue
    if not reach1[u]:
        continue
    for v in dag[u]:
        if not reach1[v]:
            continue
        mn[v] = max(
            mn[v],
            scc_mr[v]+mn[u]+graph[u][v])
ans = 0
for i in range(cnt):
    if reach1[i] and  mn[i] != INF:
        ans = max(
            ans,
            mn[i]
        )
print(ans)