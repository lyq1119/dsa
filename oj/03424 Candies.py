n,m = map(int,input().split())
edges = []
for _ in range(m):
    a,b,c = map(int,input().split())
    edges.append((a-1,b-1,c))
import heapq
def dijkstra(n, edges, start):
    graph = [[] for _ in range(n)]
    for u, v, w in edges:
        graph[u].append((v, w))
    dist = [float('inf')] * n
    dist[start] = 0
    pq = [(0, start)]  # (当前距离, 节点)
    while pq:
        current_dist, node = heapq.heappop(pq)
        # 如果当前距离不是最优的，跳过
        if current_dist > dist[node]:
            continue
        for neighbor, weight in graph[node]:
            new_dist = current_dist + weight
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor))
    return dist
t = dijkstra(n,edges,0)[-1]
print(t)