import sys
from collections import deque
data = iter(sys.stdin.read().split())
n,m = int(next(data)),int(next(data))
graph = [[] for _ in range(n+m)]
indegree = [0] * (n+m)
for i in range(m):
    t = int(next(data))
    mylist = [int(next(data))-1 for _ in range(t)]
    myset = set(mylist)
    for j in range(mylist[0],mylist[-1]+1):
        if j not in myset:
            graph[j].append(n+i)
            indegree[n+i] += 1
        else:
            graph[n+i].append(j)
            indegree[j] += 1
def karn(graph): # n是顶点数
    result = []
    queue = deque()
    # 将入度为 0 的顶点加入队列
    for u in range(n+m):
        if indegree[u] == 0:
            if u < n:
                queue.append(u)
            else:
                for r in graph[u]:
                    indegree[r] -= 1
                    if indegree[r] == 0:
                        queue.append(r)
    count = 0
    # 执行拓扑排序
    while queue:
        count += 1
        for _ in range(len(queue)):
            u = queue.popleft()
            result.append(u)
            for v in graph[u]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    if v >= n: 
                        for r in graph[v]:
                            indegree[r] -= 1
                            if indegree[r] == 0:
                                queue.append(r)
                    else:
                        queue.append(v)
    return count
print(karn(graph))