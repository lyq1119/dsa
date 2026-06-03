import sys
from collections import defaultdict
sys.setrecursionlimit(1000000)
n,m = map(int,input().split())
costs = list(map(int,input().split()))
adj = defaultdict(set)
for _ in range(m):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    adj[a].add(b)
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
kuai_costs = [0] * len(sccs)
for i in range(len(sccs)):
    for node in sccs[i]:
        scc_id[node] = i
        kuai_costs[i] += costs[node]
# 构建缩点后的 DAG & 计算出度
dag = [[] for _ in range(len(sccs))]
in_degree = [0] * len(sccs)
edges = set()  # 防止重复建边
for u in range(n):
    for v in adj[u]:
        a = scc_id[u]
        b = scc_id[v]
        if a != b and (a, b) not in edges:
            edges.add((a, b))
            dag[a].append(b)
            in_degree[b] += 1
n = len(sccs)
root = set()
for i in range(n):
    if in_degree[i] == 0:
        root.add(i)
maxnum = 0
for t in root:
    def dfs(i,total):
        global maxnum
        maxnum = max(maxnum,total)
        for j in dag[i]:
            dfs(j,total+kuai_costs[j])
    dfs(t,kuai_costs[t])
print(maxnum)
