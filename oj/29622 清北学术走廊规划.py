import heapq
def prim(n,adj):
    mst_weight = 0
    visited = [False]*n
    pq = [(0,0)]
    nodes_count = 0
    while pq and nodes_count < n:
        weight, u = heapq.heappop(pq)
        if visited[u]:
            continue
        visited[u] = True
        mst_weight += weight
        nodes_count += 1
        for next_weight, v in adj[u]:
            if not visited[v]:
                heapq.heappush(pq,(next_weight,v))
    return mst_weight if nodes_count == n else -1

n,m = map(int,input().split())
adj = [[] for _ in range(n)]
for _ in range(m):
    u,v,w = map(int,input().split())
    u -= 1
    v -= 1
    adj[u].append((w,v))
    adj[v].append((w,u))
t = prim(n,adj)
if t == -1:
    print("orz")
else:
    print(t)