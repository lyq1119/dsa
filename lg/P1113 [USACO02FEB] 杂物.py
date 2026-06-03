from collections import defaultdict, deque
n = int(input())
edges = []
for _ in range(n):
    mylist = list(map(int,input().split()))
    u = mylist[0]
    w = mylist[1]
    for i in range(2,len(mylist)-1):
        v = mylist[i]
        edges.append((v,u,w))
    if len(mylist) == 3:
        edges.append((0,u,w))
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
    return max(ve)
print(critical_path(n+1,edges))