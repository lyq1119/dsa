import sys
from collections import deque
sys.setrecursionlimit(10000)
n = int(input())
p = int(input())
costs = {}
for _ in range(p):
    a,b = map(int,input().split())
    costs[a-1] = b
q = int(input())
adj = [[] for _ in range(n)]
for _ in range(q):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    adj[a].append(b)
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
# 给每个点分配SCC编号
scc_id = [0] * n
for i in range(len(sccs)):
    for node in sccs[i]:
        scc_id[node] = i
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
zero_in = []
for i in range(len(sccs)):
    if in_degree[i] == 0:
        zero_in.append(i)
minsum = 0
for num in zero_in:
    total = float("inf")
    for t in sccs[num]:
        if t in costs:
            total = min(total,costs[t])
    if total != float("inf"):
        minsum += total
avai = set()
avail = set()
for i in costs:
    avai.add(scc_id[i])
for i in avai:
    q = deque()
    q.append(i)
    while q:
        t = q.popleft()
        avail.add(t)
        for s in dag[t]:
            if s not in avai:
                q.append(s)
unavai = []
for i in range(len(sccs)):
    if i not in avail:
        unavai.extend(sccs[i])
if len(unavai) != 0:
    print("NO")
    print(min(unavai)+1)
else:
    print("YES")
    print(minsum)

