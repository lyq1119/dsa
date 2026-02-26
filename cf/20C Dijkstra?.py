import sys,heapq
data = iter(sys.stdin.read().split())
n = int(next(data))
m = int(next(data))
linjiebiao = [{} for _ in range(n)]
for _ in range(m):
    a,b,w = [int(next(data)) for _ in range(3)]
    a -= 1
    b -= 1
    linjiebiao[a][b] = min(w,linjiebiao[a].get(b,float("inf")))
    linjiebiao[b][a] = min(w,linjiebiao[b].get(a,float("inf")))
def dijkstra():
    heap = [(0,0)]
    visited = set()
    cur = [float("inf") for _ in range(n)]
    cur[0] = 0
    prev = {0:None}
    while heap:
        dist,i = heapq.heappop(heap)
        if i in visited:
            continue
        if i == n-1:
            result = []
            t = n-1
            while prev[t] == 0 or prev[t]:
                result.append(t+1)
                t = prev[t]
            result.append(1)
            return reversed(result)
        visited.add(i)
        for key,value in linjiebiao[i].items():
            if key in visited:
                continue
            newdist = value + dist
            if newdist < cur[key]:
                cur[key] = newdist
                heapq.heappush(heap,(newdist,key))
                prev[key] = i
    return [-1]
print(*dijkstra())