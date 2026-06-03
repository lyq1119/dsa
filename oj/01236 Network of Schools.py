n = int(input())
from collections import defaultdict
adj = {}
for i in range(n):
    mylist = list(map(int,input().split()))[:-1]
    adj[i] = [mylist[i]-1 for i in range(len(mylist))]
# 1. 正向 DFS，记录完成顺序
visited = [False] * n
stack = []
def dfs1(u):
    visited[u] = True
    for v in adj[u]:
        if not visited[v]:
            dfs1(v)
    stack.append(u)  # 回溯时压入栈
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
# 给每个点分配SCC编号
scc_id = [0] * n
for i in range(len(sccs)):
    for node in sccs[i]:
        scc_id[node] = i
# 构建缩点后的 DAG & 计算出度
dag = [[] for _ in range(len(sccs))]
in_degree = [0] * len(sccs)
out_degree = [0] * len(sccs)
edges = set()  # 防止重复建边
for u in range(n):
    for v in adj[u]:
        a = scc_id[u]
        b = scc_id[v]
        if a != b and (a, b) not in edges:
            edges.add((a, b))
            dag[a].append(b)
            in_degree[b] += 1
            out_degree[a] += 1
print(in_degree.count(0))
if len(sccs) == 1:
    print(0)
else:
    print(max(in_degree.count(0),out_degree.count(0)))
