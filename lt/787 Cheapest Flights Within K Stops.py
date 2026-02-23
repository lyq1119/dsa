class Solution:
    def findCheapestPrice(self, n: int, flights, src: int, dst: int, k: int) -> int:
        from collections import defaultdict
        linjiebiao = defaultdict(list)
        for loc1,loc2,price in flights:
            linjiebiao[loc1].append((loc2,price))
        dists = [float("inf") for _ in range(n)]
        dists[src] = 0
        queue = {src}
        for _ in range(k+1):
            newset = set()
            cun = {}
            while queue:
                loc = queue.pop()
                dis = dists[loc]
                for loc3,dis3 in linjiebiao[loc]:
                    newdis = dis3+dis
                    if newdis < dists[loc3]:
                        cun[loc3] = min(newdis,cun.get(loc3,float("inf")))
                        newset.add(loc3)
            for loc in newset:
                dists[loc] = cun[loc]
            queue = newset
        if dists[dst] != float("inf"):
            return dists[dst]
        return -1
print(Solution().findCheapestPrice(4,[[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]],0,3,1))
