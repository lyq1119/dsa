from collections import defaultdict, deque
def critical_path(n, edges):
    """
    n: 节点数
    edges: 边列表
           [(u, v, w), ...]
    """
    # 建图
    graph = defaultdict(list)
    # 入度
    in_degree = [0] * n
    for u, v, w in edges:
        graph[u].append((v, w))
        in_degree[v] += 1
    # 拓扑排序 + 求 ve
    queue = deque()
    for i in range(n):
        if in_degree[i] == 0:
            queue.append(i)
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

    # 逆拓扑求 vl
    # 初始化为终点最早时间
    vl = [ve[topo_order[-1]]] * n
    for u in reversed(topo_order):
        for v, w in graph[u]:
            # 更新 vl
            vl[u] = min(vl[u], vl[v] - w)
    return True, max(vl)
n,m = map(int,input().split())
edges = []
for _ in range(m):
    u,v,w = map(int,input().split())
    edges.append((u,v,w))
verdict = critical_path(n,edges)
if verdict:
    print("Yes")
    print(verdict[1])
else:
    print("No")