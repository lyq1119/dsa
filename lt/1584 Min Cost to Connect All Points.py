import heapq
def distance(x,y,a,b):
    return abs(x-a)+abs(y-b)
class Solution:
    def minCostConnectPoints(self, points) -> int:
        n = len(points)
        visited = [False]*n
        total = 0
        pq = [(0,0)]
        while pq:
            weight,node = heapq.heappop(pq)
            if visited[node]:
                continue
            visited[node] = True
            total += weight
            for i in range(n):
                if visited[i]:
                    continue
                a,b = points[i]
                dis = distance(points[node][0],points[node][1],a,b)
                heapq.heappush(pq,(dis,i))
        return total
print(Solution().minCostConnectPoints([[0,0],[2,2],[3,10],[5,2],[7,0]]))