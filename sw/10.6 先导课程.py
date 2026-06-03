n,m = map(int,input().split())
from collections import defaultdict
import heapq
graph = defaultdict(list)
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
def has_cycle_karn(graph,n): # n是顶点数
    indegree = [0] * n
    num_visited = 0
    queue = []
    mylist = []
    # 计算每个顶点的入度
    for u in graph:
        for v in graph[u]:
            indegree[v] += 1
    # 将入度为 0 的顶点加入队列
    mylist = []
    for u in range(n):
        if indegree[u] == 0:
            heapq.heappush(queue,u)
    # 执行拓扑排序
    while queue:
        u = heapq.heappop(queue)
        mylist.append(u)
        num_visited += 1
        for v in graph[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                heapq.heappush(queue,v)
    return mylist
mylist = has_cycle_karn(graph,n)
if len(mylist) != n:
    print("No")
    print(n-len(mylist))
else:
    print("Yes")
    print(*mylist)