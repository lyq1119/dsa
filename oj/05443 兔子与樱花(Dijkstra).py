from collections import defaultdict
import heapq
p = int(input())
for i in range(p):
    loc = input()
q = int(input())
linjiebiao = defaultdict(list)
for _ in range(q):
    loc1,loc2,dis = input().split()
    dis = int(dis)
    linjiebiao[loc1].append((loc2,dis))
    linjiebiao[loc2].append((loc1,dis))
def solve(loc1,loc2):
    dists = {loc1:0}
    prev = {loc1:None}
    heap = [(0,loc1)]
    visited = set()
    while heap:
        dis,loc = heapq.heappop(heap)
        visited.add(loc)
        if loc == loc2:
            break
        for loc3,dis3 in linjiebiao[loc]:
            if loc3 in visited:
                continue
            newdis = dis3+dis
            if newdis < dists.get(loc3,float("inf")):
                dists[loc3] = newdis
                prev[loc3] = (loc,dis3)
                heapq.heappush(heap,(newdis,loc3))
    cur = loc2
    result = [loc2]
    while prev[cur]:
        loc,dis = prev[cur]
        result.extend([f"({dis})",loc])
        cur = loc
    print("->".join(reversed(result)))
r = int(input())
for _ in range(r):
    loc1,loc2 = input().split()
    solve(loc1,loc2)