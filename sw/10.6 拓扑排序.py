from collections import defaultdict
import heapq
def topological_sort(graph,n): # n是顶点数
    indegree = [0] * n
    result = []
    queue = []
    # 计算每个顶点的入度
    for u in graph:
        for v in graph[u]:
            indegree[v] += 1
    # 将入度为 0 的顶点加入队列
    for u in range(n):
        if indegree[u] == 0:
            heapq.heappush(queue,u)
    # 执行拓扑排序
    while queue:
        u = heapq.heappop(queue)
        result.append(u)
        for v in graph[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                heapq.heappush(queue,v)
    return result
n,m = map(int,input().split())
graph = defaultdict(list)
for _ in range(m):
    u,v = map(int,input().split())
    graph[u].append(v)
print(*topological_sort(graph,n))