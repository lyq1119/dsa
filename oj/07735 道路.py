import sys
import heapq
data = iter(sys.stdin.read().split())
k = int(next(data))
n = int(next(data))
graph = [[] for _ in range(n)]
for _ in range(int(next(data))):
    a,b,c,d = int(next(data)),int(next(data)),int(next(data)),int(next(data))
    a -= 1
    b -= 1
    graph[a].append((b,c,d))
def dijkstra(graph, start):
    dist = [[float("inf")]*(k+1) for _ in range(n)]
    dist[start][0] = 0
    pq = [(0,0, start)]  
    while pq:
        current_dist,cost1, node = heapq.heappop(pq)
        for neighbor, weight,cost2 in graph[node]:
            newcost = cost1+cost2
            if  newcost > k:
                continue 
            new_dist = current_dist + weight
            if dist[neighbor][newcost] <= new_dist:
                continue
            dist[neighbor][newcost] = new_dist
            heapq.heappush(pq, (new_dist, newcost,neighbor))
    return min(dist[-1]) if min(dist[-1]) != float("inf") else -1
print(dijkstra(graph,0))