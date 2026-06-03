import sys
sys.setrecursionlimit(1000000)
from collections import defaultdict
n,m = map(int,input().split())
edge = set() # 非零边
adj = defaultdict(list)
for _ in range(m):
    u,v,w = map(int,input().split())
    u -= 1
    v -= 1
    edge.add((u,v))
    edge.add((v,u))
    adj[u].append((v,w))
    adj[v].append((u,w))
visited = [False] * n
sccs = []
for i in range(n):
    if not visited[i]:
        cur = []
        def dfs(i):
            if visited[i]:
                return
            cur.append(i)
            visited[i] = True
            for j in range(n):
                if j == i:
                    continue
                if (i,j) in edge:
                    continue
                dfs(j)
        dfs(i)
        sccs.append(cur)
# 给每个点分配SCC编号
scc_id = [0] * n
for i in range(len(sccs)):
    for node in sccs[i]:
        scc_id[node] = i
# 构建缩点后的 DAG & 计算出度
dag = [[float("inf")]*len(sccs) for _ in range(len(sccs))]
for u in range(n):
    for v,w in adj[u]:
        a = scc_id[u]
        b = scc_id[v]
        if a != b:
            dag[a][b] = min(dag[a][b],w)
            dag[b][a] = min(dag[b][a],w)
edges = []
for a in range(len(sccs)):
    for b in range(len(sccs)):
        if dag[a][b] != float("inf"):
            edges.append((dag[a][b],a,b))
def find(parent, i):
    if parent[i] != i:
        parent[i] = find(parent, parent[i])  # 路径压缩
    return parent[i]
def union(parent, i, j):
    root_i = find(parent, i)
    root_j = find(parent, j)
    if root_i != root_j:
        parent[root_i] = root_j
        return True
    return False
def kruskal(n, edges):
    # 按权重从小到大排序
    edges.sort()
    # 初始化 parent 数组（代替类的 self.parent）
    parent = list(range(n))
    mst_weight = 0
    mst_edges = []
    for weight, u, v in edges:
        if union(parent, u, v):
            mst_weight += weight
            mst_edges.append((u, v, weight))
            # 凑够 n-1 条边提前结束
            if len(mst_edges) == n - 1:
                break       
    return mst_weight
print(kruskal(len(sccs),edges))