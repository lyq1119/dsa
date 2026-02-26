import heapq
n = int(input())
adj = [set() for _ in range(n)]
for _ in range(n-1):
    mylist = list(input().split())
    node1 = ord(mylist[0])-65
    m = int(mylist[1])
    for i in range(m):
        i += 1
        node2 = ord(mylist[2*i])-65
        weight = int(mylist[2*i+1])
        adj[node1].add((weight,node2))
        adj[node2].add((weight,node1))
def prim(n, adj):
    mst_weight = 0
    visited = [False] * n
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
                heapq.heappush(pq, (next_weight, v))                
    return mst_weight
print(prim(n,adj))