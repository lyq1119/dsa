import heapq
class Solution:
    def networkDelayTime(self, times, n: int, k: int) -> int:
        graph = [[None for _ in range(n)] for __ in range(n)]
        cur = [float("inf") for _ in range(n)]
        for i,j,w in times:
            graph[i-1][j-1] = w
        mylist = [(0,k-1)]
        while mylist:
            dist,node = heapq.heappop(mylist)
            if dist >= cur[node]:
                continue
            cur[node] = dist
            for i in range(n):
                if graph[node][i] or graph[node][i] == 0:
                    newdist = dist+graph[node][i]
                    if newdist < cur[i]:
                        heapq.heappush(mylist,(newdist,i))
        return max(cur)
print(Solution().networkDelayTime([[2,1,1],[2,3,1],[3,4,1]],4,2))
            