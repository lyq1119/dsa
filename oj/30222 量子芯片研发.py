from collections import defaultdict, deque
n,m = map(int,input().split())
days = list(map(int,input().split()))
edges = []
for _ in range(m):
    a,b = map(int,input().split())
    edges.append((a,b,days[b-1]))
def critical_path(n, edges):
    # 建图
    graph = defaultdict(list)
    # 入度
    in_degree = [0] * n
    for u, v, w in edges:
        graph[u].append((v, w))
        in_degree[v] += 1
    # 拓扑排序 + 求 ve
    queue = deque([0])
    for i in range(1,n):
        if in_degree[i] == 0:
            graph[0].append((i,days[i-1]))
            in_degree[i] += 1
    topo_order = []
    # 最早发生时间
    ve = [0] * n
    while queue:
        u = queue.popleft()
        topo_order.append(u)
        for v, w in graph[u]:
            # 更新 ve
            ve[v] = max(ve[v], ve[u] + w)
            # 入度减1
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)
    if len(topo_order) != n:
        return -1
    return max(ve)
print(critical_path(n+1,edges))