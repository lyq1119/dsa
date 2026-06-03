from collections import deque
n, m = map(int, input().split())
bad = [set() for _ in range(n + 1)]
edges = []
for _ in range(m):
    u, v,w = map(int, input().split())
    bad[u].add(v)
    bad[v].add(u)
    edges.append((u,v,w))
unvisited = set(range(1, n + 1))
cc = []
indexcc = {}
while unvisited:
    start = unvisited.pop()
    q = deque([start])
    mylist = []
    while q:
        u = q.popleft()
        mylist.append(u)
        indexcc[u] = len(cc)
        nxt = []
        for v in unvisited:
            if v not in bad[u]:
                nxt.append(v)
        for v in nxt:
            unvisited.remove(v)
            q.append(v)
    cc.append(mylist)
graph = [[float("inf")]*len(cc) for _ in range(len(cc))]
for u,v,w in edges:
    a,b = indexcc[u],indexcc[v]
    if a == b:
        continue
    else:
        graph[a][b] = min(graph[a][b],w)
        graph[b][a] = min(graph[b][a],w)
import heapq
def prim(n, adj):
    mst_weight = 0
    visited = [False] * n
    # pq 是优先队列，存储格式为 (weight, to_node)
    pq = [(0, 0)]  # 从顶点 0 开始，权重为 0
    nodes_count = 0
    while pq and nodes_count < n:
        weight, u = heapq.heappop(pq)   
        # 如果点已经访问过，跳过
        if visited[u]:
            continue            
        # 将点标记为已访问，并累加权重
        visited[u] = True
        mst_weight += weight
        nodes_count += 1       
        # 遍历当前点的所有邻居
        for v in range(len(cc)):
            w = adj[v][u]
            if not visited[v]:
                heapq.heappush(pq, (w, v))                
    # 如果加入的点数等于 n，说明生成了完整的树
    return mst_weight
print(prim(n,graph))