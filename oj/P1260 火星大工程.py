from collections import defaultdict,deque
n,m = map(int,input().split())
graph = defaultdict(set)
indegree = [0]*n
for _ in range(m):
    a,b,c = map(int,input().split())
    a -= 1
    b -= 1
    graph[a].add((b,c))
    indegree[b] += 1
ve = [0]*n
order = []
topo = deque()
for i in range(n):
    if indegree[i] == 0:
        topo.append(i)
        order.append(i)
while topo:
    u = topo.popleft()
    for v,w in graph[u]:
        if w+ve[u] > ve[v]:
            ve[v] = w+ve[u]
        indegree[v] -= 1
        if indegree[v] == 0:
            topo.append(v)
            order.append(v)
vl = [max(ve)]*n
for i in range(n-1,-1,-1):
    u = order[i]
    for v,w in graph[u]:
        if vl[v]-w < vl[u]:
            vl[u] = vl[v]-w
crpo = set()
for i in range(n):
    if ve[i] == vl[i]:
        crpo.add(i)
lu = []
for u in graph:
    if u in crpo:
        for v,w in graph[u]:
            if v in crpo and ve[u]+w == ve[v]:
                lu.append((u,v))
lu.sort()
print(max(ve))
for u,v in lu:
    print(u+1,v+1)