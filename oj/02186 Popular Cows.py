n,m = map(int,input().split())
import sys
sys.setrecursionlimit(100000)
from collections import defaultdict
adj = defaultdict(list)
for _ in range(m):
    i,j = map(int,input().split())
    i -= 1
    j -= 1
    adj[i].append(j)
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
# 2. 创建反向图
rev_adj = [[] for _ in range(n)]
for u in range(n):
    for v in adj[u]:
        rev_adj[v].append(u)
# 3. 反向 DFS，提取 SCC
visited = [False] * n
index = 0
scc = [0 for _ in range(n)]
count = [0 for _ in range(n)]
def dfs2(u,index):
    scc[u] = index
    count[index] += 1
    visited[u] = True
    for v in rev_adj[u]:
        if not visited[v]:
            dfs2(v,index)
while stack:
    u = stack.pop()
    if not visited[u]:
        dfs2(u,index)
        index += 1
chudu = [0 for _ in range(index)]
for i in range(n):
    for j in adj[i]:
        if scc[i] == scc[j]:
            continue
        else:
            chudu[scc[i]] += 1
total = 0
visit = 0
for i in range(index):
    if chudu[i] == 0:
        visit += 1
        total = count[i]
if visit == 1:
    print(total)
else:
    print(0)