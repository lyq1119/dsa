from collections import deque, defaultdict
T = int(input())
def topological_sort(N,graph):
    indegree = [0 for _ in range(N)]
    result = 0
    queue = deque()
    # 计算每个顶点的入度
    for u in graph:
        for v in graph[u]:
            indegree[v] += 1
    # 将入度为 0 的顶点加入队列
    for u in range(N):
        if indegree[u] == 0:
            queue.append(u)
    # 执行拓扑排序
    while queue:
        u = queue.popleft()
        result += 1
        for v in graph[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                queue.append(v)
    return result != N
for _ in range(T):
    graph = defaultdict(list)
    N,M = map(int,input().split())
    for _ in range(M):
        x,y = map(int,input().split())
        x -= 1
        y -= 1
        graph[x].append(y)
    if topological_sort(N,graph):
        print("Yes")
    else:
        print("No")